from dotenv import dotenv_values


class Environment():
  def __init__(self) -> None:
    self._env_vars = dotenv_values('../.env')

  def get_path(self, key: str) -> str:
    return self._env_vars[key]

def main(args=None):
  env = Environment()
  print(env.get_path('MEMORY'))

if __name__ == '__main__':
  main()