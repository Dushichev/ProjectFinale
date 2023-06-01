from abc import ABC, abstractmethod


class Animals(ABC):
        
    @abstractmethod
    def print_name_animal():
        pass
    
    @abstractmethod
    def add_animal_skill():
        pass