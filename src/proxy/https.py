import re
import subprocess
from abc import ABC
from typing import Union

from src.ip_utils import get_ip_country
from src.proxy.base import BaseProxy


class BaseHTTPProxy(BaseProxy, ABC):
    """Base class for HTTP and HTTPS proxies."""

    _state_pattern = re.compile(r"Enabled: (Yes\b|No\b)")
    _ip_pattern = re.compile("Server: (.*)")
    _state_get_map = {"Yes": True, "No": False}
    _state_set_map = {True: "on", False: "off"}

    def __init__(self, secure: bool) -> None:
        self._secure = "secure" if secure else ""
        self._name = "HTTPS" if secure else "HTTP"

    @property
    def name(self) -> str:
        return self._name

    def get_proxy_info(self) -> str:
        proxy_info = subprocess.run(
            ["networksetup", f"-get{self._secure}webproxy", "Wi-Fi"], capture_output=True, text=True
        )
        return proxy_info.stdout

    @property
    def state(self) -> bool:
        proxy_info = self.get_proxy_info()
        state = re.search(self._state_pattern, proxy_info).group(1)
        return self._state_get_map[state]

    @state.setter
    def state(self, new_state: bool) -> None:
        new_state = self._state_set_map[new_state]
        subprocess.run(["networksetup", f"-set{self._secure}webproxystate", "Wi-Fi", new_state], check=True)

    @property
    def ip(self) -> Union[str, None]:
        proxy_info = self.get_proxy_info()
        ip = re.search(self._ip_pattern, proxy_info).group(1)
        if ip == "":
            return None
        return ip

    @property
    def country(self) -> Union[str, None]:
        return get_ip_country(self.ip)


class HTTPProxy(BaseHTTPProxy):
    """HTTP proxy."""

    def __init__(self) -> None:
        super().__init__(secure=False)


class HTTPSProxy(BaseHTTPProxy):
    """HTTPS proxy."""

    def __init__(self) -> None:
        super().__init__(secure=True)
