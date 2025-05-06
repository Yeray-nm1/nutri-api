class ProductNotFoundError(Exception):
  def __init__(self, message: str):
    self.message = message

class InvalidProductInputError(Exception):
  def __init__(self, message: str):
    self.message = message