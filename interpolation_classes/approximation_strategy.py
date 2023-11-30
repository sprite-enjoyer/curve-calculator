from abc import ABC, abstractmethod

class ApproximationStrategy(ABC):
  
  @abstractmethod
  def approximate(self, x_arr, y_arr):
    pass

  @abstractmethod
  def draw(self):
    pass