"""Containers with proxies and application for dependency injection."""

from dependency_injector import containers, providers

from src.app.app import ProxyApp
from src.proxy import DummyProxy, HTTPProxy, HTTPSProxy


class DummyContainer(containers.DeclarativeContainer):
    dummy_proxy = providers.Factory(DummyProxy)


class Container(containers.DeclarativeContainer):
    http_proxy = providers.Singleton(HTTPProxy)
    https_proxy = providers.Singleton(HTTPSProxy)

    proxy_app = providers.Singleton(
        ProxyApp,
        proxies=providers.List(
            http_proxy,
            https_proxy,
        ),
    )
