"""

"""

from abc import ABC, abstractclassmethod

class BaseBench(ABC):
    """
    """
    
    @abstractclassmethod
    def prepare(self):
        pass

    @abstractclassmethod
    def build_circuits(self):
        pass

    @abstractclassmethod
    def run(self):
        pass

    @abstractclassmethod
    def get_results(self):
        pass

    @abstractclassmethod
    def analyze(self):
        pass