from abc import ABC, abstractmethod

class ApproximationStrategy(ABC):
  
  @abstractmethod
  def approximate(self):
    pass