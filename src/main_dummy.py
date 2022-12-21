"""App launch script with all proxies overriden with :class:`src.proxy.DummyProxy`."""

from dependency_injector.wiring import Provide, inject

from src.app import ProxyApp
from src.containers import Container, DummyContainer


@inject
def main(proxy_app: ProxyApp = Provide[Container.proxy_app]) -> None:
    proxy_app.run()


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    dummy_container = DummyContainer()
    for provider_name, provider in container.providers.items():
        if "_proxy" in provider_name:
            proxy_name = provider_name.replace("_proxy", "").upper()
            provider.override(dummy_container.dummy_proxy(f"Dummy {proxy_name}", update_interval=3))

    main()
