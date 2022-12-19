"""Test :class:`src.proxy.DummyProxy` class for updating its proxy configuration."""

from time import sleep

import pytest

from src.proxy import DummyProxy


@pytest.fixture
def dummy_proxy(request):
    return DummyProxy(name=request.param.get("name"), update_interval=request.param.get("update_interval"))


@pytest.mark.parametrize(
    ("dummy_proxy", "expected"),
    [
        ({"name": "Dummy HTTP", "update_interval": None}, "Dummy HTTP"),
        ({"name": "Dummy HTTPS", "update_interval": None}, "Dummy HTTPS"),
    ],
    indirect=["dummy_proxy"],
)
def test_name(dummy_proxy: DummyProxy, expected: str):
    assert dummy_proxy.name == expected


@pytest.mark.parametrize(
    ("dummy_proxy", "update_interval"),
    [
        ({"name": "Dummy", "update_interval": 0.1}, 0.1),
    ],
    indirect=["dummy_proxy"],
)
def test_update(dummy_proxy: DummyProxy, update_interval: float):
    """Test DummyProxy updates its proxy configuration."""
    with dummy_proxy.updating():
        current_ip = dummy_proxy.ip
        sleep(update_interval + 0.5)  # add lag time
        new_ip = dummy_proxy.ip
        assert new_ip != current_ip


@pytest.mark.parametrize(
    "dummy_proxy",
    [
        {"name": "Dummy", "update_interval": None},
        {"name": "Dummy", "update_interval": -1},
    ],
    indirect=True,
)
def test_static(dummy_proxy: DummyProxy):
    """Test DummyProxy ip is static when `update_interval` is negative or None."""
    with dummy_proxy.updating():
        current_ip = dummy_proxy.ip
        sleep(0.5)
        new_ip = dummy_proxy.ip
        assert new_ip == current_ip
