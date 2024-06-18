# Only allow key presses if the buttons are not locked
def lockerWrapper(func):
  def checkIfLocked(controller, *args, **kwargs):
    if not controller.locked:
      func(controller, *args, **kwargs)
  return checkIfLocked
