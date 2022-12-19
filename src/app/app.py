"""Menu bar app to enable and disable proxy."""

from pathlib import Path
from typing import List

import rumps

from src.app.proxy_item import ProxyItem
from src.proxy import Proxy

project_dir = Path(__file__).parents[2]


class ProxyApp(rumps.App):
    """Rumps app to enable and disable proxy from the menu bar."""

    def __init__(self, proxies: List[Proxy]):
        super().__init__(name="Proxy")

        self.title = " Proxy"
        self.icon = str(project_dir / "icons" / "icon.png")
        self.quit_button = None

        self.proxies = proxies
        self.menu = self.setup_menu()

    def setup_menu(self) -> List[rumps.MenuItem]:
        menu = []

        for proxy in self.proxies:
            proxy_item = ProxyItem(proxy)
            menu.extend(proxy_item.menu)
        menu.append(rumps.MenuItem("Quit"))

        return menu

    @rumps.clicked("Quit")
    def quit(self, _sender: rumps.MenuItem) -> None:
        for proxy in self.proxies:
            proxy.state = False
        rumps.quit_application()
