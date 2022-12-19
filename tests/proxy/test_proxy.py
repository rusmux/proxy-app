"""Tests for all proxies that are a subclass of :class:`src.proxy.Proxy`."""

import pytest

from src.proxy import DummyProxy, HTTPProxy, HTTPSProxy, Proxy

NoneType = type(None)


@pytest.mark.parametrize(
    ("proxy_class", "args"),
    [
        (DummyProxy, {"name": "Dummy"}),
        (HTTPProxy, {}),
        (HTTPSProxy, {}),
    ],
)
class TestProxy:
    @pytest.fixture
    def proxy(self, proxy_class: type, args: dict):
        return proxy_class(**args)

    def test_name(self, proxy: Proxy):
        assert isinstance(proxy.name, str)

    def test_state_getter(self, proxy: Proxy):
        assert isinstance(proxy.state, bool)

    @pytest.mark.parametrize("new_state", [True, False])
    def test_state_setter(self, proxy: Proxy, new_state: bool):
        proxy.state = new_state
        assert proxy.state == new_state

    def test_ip(self, proxy: Proxy):
        assert isinstance(proxy.ip, (str, NoneType))

    def test_country(self, proxy: Proxy):
        assert isinstance(proxy.country, (str, NoneType))
