class RemoteControl():
    def __init__(self):
        self.channels = ["HBO","cnn","abc","espn"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration

        return self.channels[self.index]
##an iterator object consists of __iter__ and __next__ methods

r = RemoteControl()
itr=iter(r) ## returns an iterator for the object
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))