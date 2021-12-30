from abc import abstractmethod, ABC


class IDataView(ABC):
    "A method for the Observer to implement"

    @staticmethod
    @abstractmethod
    def notify(data):
        "Receive notifications"

    @staticmethod
    @abstractmethod
    def draw(data):
        "Draw the view"

    @staticmethod
    @abstractmethod
    def delete():
        "a delete method to remove observer specific resources"
