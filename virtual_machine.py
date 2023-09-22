import random
import pickle
import numpy as np
import nltk
from memory import Memory_Handler as mh

from keras.models import Sequential
from nltk.stem import WordNetLemmatizer
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

class Virtual_Machine():
  def __init__(self) -> None:
    self._ignore_letters: list[str] = ['?', '!', '.', ',']
    self._lemmatizer: WordNetLemmatizer = WordNetLemmatizer()
    self._words = []
    self._classes = []
    
    self._is_running: bool = False
  
  def start(self) -> None:
    self._is_running = True
    
    while self._is_running:
      user_input = input('>>> ')
      
      if user_input.lower() == 'goodbye':
        print('Good bye...')
        break
      
      print(user_input)

def main(args=None):
  vm = Virtual_Machine()
  
  vm.start()