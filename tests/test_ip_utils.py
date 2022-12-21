"""Test functions from `src.utils`."""

import socket
from typing import Union

import pytest

from src.ip_utils import generate_random_ip, get_ip, get_ip_country


def test_generate_random_ip():
    for _ in range(100):
        assert socket.inet_aton(generate_random_ip())


def test_get_ip():
    assert socket.inet_aton(get_ip())


@pytest.mark.parametrize(
    ("ip", "expected"),
    [
        ("77.88.8.8", "RU"),  # Yandex DNS
        ("8.8.8.8", "US"),  # Google DNS
        ("0.0.0.0", None),
        (None, None),
        ("", None),
    ],
)
def test_get_ip_country(ip: Union[str, None], expected: Union[str, None]):
    assert get_ip_country(ip) == expected


def test_get_ip_country_cache():
    get_ip_country.cache_info()
