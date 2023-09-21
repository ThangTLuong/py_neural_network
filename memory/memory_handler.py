from difflib import get_close_matches as gcm

from memory import Memory as mry


class Memory_Handler():
  def __init__(self, file_path: str | None = None) -> None:
    if file_path == None:
      file_path = './memory.json'

    self._memory: mry = mry('./memory.json')
    self._memory.load_memory()

  def __del__(self) -> None:
    self._memory.save_memory()


def main(args=None):
  mem: Memory_Handler = Memory_Handler()


if __name__ == '__main__':
  main()
