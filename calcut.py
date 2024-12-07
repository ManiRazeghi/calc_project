

class Calculator:

    def __init__(self, number1: int, number2: int) -> None:
        self.number1 = number1
        self.number2 = number2


    def add(self) -> int:
        return self.number1 + self.number2
    
    def minus(self, multiple_negative: bool = False) -> int:

        target = self.number1 - self.number2

        return target * -1 if multiple_negative else target