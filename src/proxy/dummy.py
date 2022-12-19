import random
import threading
from contextlib import contextmanager
from time import sleep
from typing import Generator, Optional, Union

from src.ip_utils import generate_random_ip, get_ip_country
from src.proxy.base import BaseProxy


class DummyDynamicProxyServer:
    """Dummy proxy server that updates its configuration.
    For imitating a proxy configuration change by a user.

    Args:
        update_interval (float, optional): the interval at which the proxy ip and country is updated.
    """

    def __init__(self, update_interval: Optional[float] = None) -> None:
        self.update_interval = update_interval

        self._ip = None
        self._country = None
        self.update()

        self._busy = False
        self._thread = threading.Thread(target=self._update_loop)

    @property
    def ip(self) -> str:
        return self._ip

    @property
    def country(self) -> Union[str, None]:
        return self._country

    def update(self) -> None:
        """Generate a new proxy ip address and update the country."""
        self._ip = generate_random_ip()
        self._country = get_ip_country(self._ip)

    def _update_loop(self) -> None:
        while True:
            if not self._busy:
                break
            self.update()
            sleep(self.update_interval)

    def start_updating(self) -> None:
        if self.update_interval and self.update_interval > 0:
            self._busy = True
            self._thread.start()

    def stop_updating(self) -> None:
        if self._busy:
            self._busy = False
            self._thread.join()

    @contextmanager
    def updating(self) -> Generator[None, None, None]:
        self.start_updating()
        yield
        self.stop_updating()


class DummyProxy(BaseProxy):
    """Dummy proxy for testing.

    Args:
        update_interval (float, optional): the interval at which the proxy ip and country is updated.
    """

    def __init__(self, name: str, update_interval: Optional[float] = None) -> None:
        self._name = name
        self._proxy_server = DummyDynamicProxyServer(update_interval=update_interval)
        self._state = random.choice([True, False])

    @property
    def name(self) -> str:
        return self._name

    @property
    def state(self) -> bool:
        return self._state

    @state.setter
    def state(self, new_state: bool) -> None:
        self._state = new_state

    @property
    def ip(self) -> str:
        return self._proxy_server.ip

    @property
    def country(self) -> Union[str, None]:
        return self._proxy_server.country

    def start_updating(self) -> None:
        self._proxy_server.start_updating()

    def stop_updating(self) -> None:
        self._proxy_server.stop_updating()

    @contextmanager
    def updating(self) -> Generator[None, None, None]:
        self.start_updating()
        yield
        self.stop_updating()
