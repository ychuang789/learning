"The ATM Notes Dispenser Interface"
from abc import ABCMeta, abstractmethod

class IDispenser(metaclass=ABCMeta):
    "Methods to implement"

    def __init__(self, domination: int):
        self.domination = domination

    @abstractmethod
    def next_successor(self,successor):
        """Set the next handler in the chain"""


    @abstractmethod
    def handle(self,amount):
        """Handle the event"""
