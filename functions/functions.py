from abc import ABC, abstractmethod
from typing import Any

class Functions(ABC):
  def __init__(self) -> None:
    pass
  
  @abstractmethod
  def execute(self, *data) -> Any | None:
    pass