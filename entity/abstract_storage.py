from abc import ABC, abstractmethod


class AbstractStorage(ABC):

    @property
    @abstractmethod
    def _capacity(self):
        pass

    @abstractmethod
    def add(self, title, quantity):
        pass

    @abstractmethod
    def remove(self, title, quantity):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass
