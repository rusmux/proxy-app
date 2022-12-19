from dependency_injector.wiring import inject, Provide

from src.app import ProxyApp
from src.containers import Container


@inject
def main(proxy_app: ProxyApp = Provide[Container.proxy_app]) -> None:
    proxy_app.run()


if __name__ == "__main__":
    app_container = Container()
    app_container.wire(modules=[__name__])
    main()
