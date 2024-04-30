class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("woof, my name is " + self.name)

def main():
    fido = Dog("fido", 13)
    fido.bark()

    fifi = Dog("fifi", 1)
    fifi.bark()
    fido.bark()

if __name__ == "__main__":
    main()