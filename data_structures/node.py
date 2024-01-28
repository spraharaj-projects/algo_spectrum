from abc import ABC, abstractmethod
from typing import Any


class Node(ABC):
    """
    Abstract base class for nodes in various data structures.
    """
    def __init__(self, data: Any):
        """
        Initializes a node with the given data.

        :param Any data: The data to be stored in the node.
        """
        self.data = data

    @abstractmethod
    def __str__(self) -> str:
        """
        Abstract method to return the string representation of the node's data.
        Returns:
            str: string value of the node.
        """
        pass
