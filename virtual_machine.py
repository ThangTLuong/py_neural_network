class Virtual_Machine():
  def __init__(self) -> None:
    self._is_running: bool = False
  
  def start(self) -> None:
    self._is_running = True
    
    while self._is_running:
      user_input = input('>>> ')
      
      if user_input == 'goodbye':
        print('Good bye...')
        break
      
      print(user_input)

def main(args=None):
  vm = Virtual_Machine()
  
  vm.start()