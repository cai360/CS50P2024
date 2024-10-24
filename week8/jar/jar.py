class Jar:
    def __init__(self, capacity=12):
        #call the line 29
        self.capacity = capacity
        #call line 36
        self.size = 0

    # return n🍪 in the cookie jar
    def __str__(self):
        return "🍪" * self.size

    #to add cookie and is it exceed capacity return valueerror
    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("deposit faild")
        self.size = self.size + n

    # to remove cookies
    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("deposit faild")
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity  < 1:
            raise ValueError("capacity error")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Size Error")
        self._size = size


def main():
    jar = Jar(20)
    jar.deposit(12)
    jar.withdraw(3)
    print(jar)



if __name__ == "__main__":
    main()
