from dotenv import dotenv_values


class Environment():
  def __init__(self) -> None:
    self._env_vars: dict[str, str | None] = dotenv_values('../.env')

  def get_path(self, key: str) -> str:
    return self._env_vars[key]
