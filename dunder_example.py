class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says woof!"

    def __add__(self, other):
        return f"{self.speak()} {other}"

    def __bool__(self):
        print(f"Sad {self.name} says woof!")
        return False

    def __repr__(self):
        return f"Dog({self.name})"


dog = Dog("Rex")

print(dog + 4)
print(dog + Dog("Fido"))
print(not dog)
