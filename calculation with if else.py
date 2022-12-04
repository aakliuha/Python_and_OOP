class Operation:

    @classmethod
    def validator(cls, num):
        return type(num) == int

    def add(self, num: int) -> int:
        self.num = num
        if not self.validator(num):
            raise TypeError('Should be int type')
        return self.num + 10

    def minus(self, num: int) -> int:
        self.num = num
        if not self.validator(num):
            raise TypeError('Should be int type')
        return self.num - 2

    def divide(self, num: int) -> int:
        self.num = num
        if not self.validator(num):
            raise TypeError('Should be int type')
        return self.num / self.num

    def multiple(self, num: int) -> int:
        self.num = num
        if not self.validator(num):
            raise TypeError('Should be int type')
        return self.num * self.num

    def processOperation(self, operator: str, num: int) -> int:
        if operator == '+':
            return self.add(num)
        elif operator == '-':
            return self.minus(num)
        elif operator == '/':
            return int(self.divide(num))
        elif operator == '*':
            return self.multiple(num)

p = Operation()
print(p.processOperation('/', 10))