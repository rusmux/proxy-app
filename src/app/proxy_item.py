"""Wrapper for :class:`src.proxy.Proxy` class to be used like :class:`rumps.MenuItem`."""

import os
import subprocess
from enum import Enum
from typing import List, Optional, Union

import rumps

from src.ip_utils import get_ip, get_ip_country
from src.proxy import Proxy


def open_proxy_settings() -> None:
    subprocess.run(["open", "x-apple.systempreferences:com.apple.preference.network?Proxies"])


class AlertResponse(int, Enum):
    OK = 1
    DISABLE = -1
    IGNORE = 0


class ProxyItem:
    """:class:`rumps.MenuItem`-like wrapper for :class:`src.proxy.Proxy`.

    Args:
        proxy (Proxy): proxy to wrap.
    """

    icons_dir = os.path.join(os.path.dirname(__file__), "icons")

    def __init__(self, proxy: Proxy) -> None:
        self.proxy = proxy
        self.ignore = False
        self.menu = self.setup_menu()

        rumps.Timer(callback=self.update_menu, interval=2).start()

    @property
    def ip(self) -> Union[str, None]:
        """Get the current visible ip address."""
        if self.proxy.state:
            return self.proxy.ip
        return get_ip()

    @property
    def country(self) -> Union[str, None]:
        """Get the country of the current visible ip address."""
        return get_ip_country(self.ip)

    def setup_menu(self) -> List[rumps.MenuItem]:
        return [
            rumps.MenuItem(self.proxy.name, callback=self.toggle),
            rumps.separator,
            rumps.MenuItem(f"IP: {self.ip}"),
            rumps.MenuItem(f"Country: {self.country}"),
        ]

    def toggle(self, _sender: Optional[rumps.MenuItem] = None) -> None:
        self.ignore = False
        self.proxy.state = not self.proxy.state

    def set_icon(self) -> None:
        icon = "green_dot.png" if self.proxy.state else "red_dot.png"
        icon = os.path.join(self.icons_dir, icon)
        if self.menu[0].icon != icon:
            self.menu[0].set_icon(icon_path=icon, dimensions=(15, 15))

    def update_menu(self, _sender: Optional[rumps.MenuItem] = None) -> None:
        if not self.ip or not self.country:
            self.alert()
        self.set_icon()
        self.menu[2].title = f"IP: {self.ip}"
        self.menu[3].title = f"Country: {self.country}"

    def alert(self) -> None:
        """Show an alert that the connection to the proxy server cannot be established."""
        if self.ignore:
            return

        if self.proxy.ip:
            alert_message = (
                f"Cannot establish connection with the proxy server on {self.proxy.ip}. Check your proxy settings."
            )
        else:
            alert_message = "Cannot establish connection with the proxy server. Check your proxy settings."

        alert_response = rumps.alert(
            title=f"{self.proxy.name} Proxy Error",
            message=alert_message,
            ok="Proxy Settings",
            cancel="Ignore",
            other="Disable",
        )

        if alert_response == AlertResponse.OK:
            self.ignore = True  # to suppress alert while proxy settings are opened
            open_proxy_settings()
        elif alert_response == AlertResponse.DISABLE:
            self.proxy.state = False
        else:
            self.ignore = True
