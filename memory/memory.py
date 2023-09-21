import json


class Memory():
  def __init__(self, file_path: str) -> None:
    self._memory: dict | None = None
    self._file_path: str = file_path

  def load_memory(self) -> None:
    with open(self._file_path, 'r') as file:
      data: dict = json.load(file)

    self._memory = data

  def save_memory(self) -> None:
    with open(self._file_path, 'w') as file:
      json.dump(self._memory, file, indent=2)


def main(args=None):
  mem = Memory('memory.json')
  mem.load_memory()
  mem.save_memory()
