from abc import ABC, abstractmethod
from typing import NewType, Union


class BaseProxy(ABC):
    """Base class for all proxy protocols."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Get the name of the proxy protocol.

        Returns:
            str: name of the proxy protocol.
        """

    @property
    @abstractmethod
    def state(self) -> bool:
        """Get the current state of the proxy.

        Returns:
            bool: state of the proxy.
        """

    @state.setter
    @abstractmethod
    def state(self, new_state: bool) -> None:
        """Enable or disable the proxy.

        Args:
            new_state (bool): new state to set the proxy to.
        """

    @property
    @abstractmethod
    def ip(self) -> Union[str, None]:
        """Get the ip address of the configured proxy server.
        If the proxy server is not configured return None.

        Returns:
            str or None: ip address of the configured proxy server.
        """

    @property
    @abstractmethod
    def country(self) -> Union[str, None]:
        """Get the country of the configured proxy server.
        If the proxy server is not configured return None.

        Returns:
            str or None: country of the configured proxy server.
        """


# to use in typing hints
Proxy = NewType("Proxy", BaseProxy)
