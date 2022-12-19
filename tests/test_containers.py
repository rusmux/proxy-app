import pytest

from src.app import ProxyApp
from src.containers import Container, DummyContainer
from src.proxy import DummyProxy, HTTPProxy, HTTPSProxy


def test_dummy_proxy():
    dummy_proxy = DummyContainer().dummy_proxy(name="Dummy", update_interval=1)
    assert isinstance(dummy_proxy, DummyProxy)


class TestContainer:
    @pytest.fixture
    def container(self):
        return Container()

    def test_http_proxy(self, container: Container):
        http_proxy = container.http_proxy()
        assert isinstance(http_proxy, HTTPProxy)

    def test_https_proxy(self, container: Container):
        https_proxy = container.https_proxy()
        assert isinstance(https_proxy, HTTPSProxy)

    def test_proxy_app(self, container: Container):
        proxy_app = container.proxy_app()
        assert isinstance(proxy_app, ProxyApp)
