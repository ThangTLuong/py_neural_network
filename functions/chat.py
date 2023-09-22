from difflib import get_close_matches as gcm
from typing import Any
import sys

sys.path.append('../')
from functions import Functions

class Chat(Functions):
  def __init__(self) -> None:
    pass
  
  def execute(self, *data) -> Any | None:
    pass
  
  def find_best_match(self, user_question: str, questions: list[str]) -> str | None:
    matches: list = gcm(user_question, questions, n = 1, cutoff=0.6)
    return matches[0] if matches else None
  
  def get_answer_for_question(question: str, memory: dict) -> str | None:
    pass
  
def main(args=None):
  chat = Chat()
  
if __name__ == '__main__':
  main()