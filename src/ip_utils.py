import os
import random
import socket
import struct
from functools import lru_cache
from typing import Union

import requests


def generate_random_ip() -> str:
    int32_mask = 0xFFFFFFFF
    return socket.inet_ntoa(struct.pack(">I", random.randint(1, int32_mask)))


def get_ip() -> Union[str, None]:
    """Get the current ip address.
    Does not use proxy.

    Returns:
        str or None: current ip address.
    """
    ip = None

    api = "https://ipinfo.io"
    ipinfo_token = os.environ.get("IPINFO_TOKEN")
    token_query = f"?token={ipinfo_token}" if ipinfo_token else ""
    url = "/".join([api, "ip"]) + token_query

    with requests.Session() as session:
        session.trust_env = False

        try:
            response = session.get(url)
        except requests.exceptions.RequestException:
            pass
        else:
            if response.ok:
                ip = response.text.strip()

    return ip


@lru_cache(maxsize=None)
def get_ip_country(ip: Union[str, None]) -> Union[str, None]:
    """Get the country of an ip address.
    If the provided ip is ``None``, ``None`` is returned.

    Args:
        ip (str or None): ip address to get the country of.

    Returns:
        str or None: country of the ip address.
    """

    if ip is None:
        return None

    country = None

    api = "https://ipinfo.io"
    ipinfo_token = os.environ.get("IPINFO_TOKEN")
    token_query = f"?token={ipinfo_token}" if ipinfo_token else ""
    url = "/".join([api, ip, "country"]) + token_query

    with requests.Session() as session:
        session.trust_env = False

        try:
            response = session.get(url)
        except requests.exceptions.RequestException:
            pass
        else:
            if response.ok:
                country = response.text.strip()

    return country
