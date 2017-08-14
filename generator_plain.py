from time import sleep

class ExpensiveComputer:
    def __iter__(self):
        self.last_val = 1
        return self
    def __next__(self):
        rv = self.last_val
        sleep(1)
        self.last_val += 1
        if(self.last_val >= 10):
            raise StopIteration()
        return rv

for x in ExpensiveComputer():
    print(x)