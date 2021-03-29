class A:
    def _init_(self):
        self.a=1
        self._b=1
    def getY(self):
        return self._b
obj=A()
obj.a=45
print(obj.a)
