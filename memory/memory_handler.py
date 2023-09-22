import sys

sys.path.append('../')
from memory import Memory as mry
from dependencies import Environment

class Memory_Handler():
  def __init__(self, file_path: str | None = None) -> None:
    self._env: Environment = Environment()

    if file_path == None:
      file_path = self._env.get_path('MEMORY')

    self._memory: mry = mry(file_path)
    self._memory.load_memory()

  def __del__(self) -> None:
    self._memory.save_memory()


def main(args=None):
  mem: Memory_Handler = Memory_Handler()

if __name__ == '__main__':
  main()
