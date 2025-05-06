class SeasonNotFoundError(Exception):
  def __init__(self, message: str):
    self.message = message

class InvalidMonthError(Exception):
  def __init__(self, message: str):
    self.message = message