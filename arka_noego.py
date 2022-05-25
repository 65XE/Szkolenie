class Dog:
    def speak(self):
        print("Dog sais : Hau, hau!")


class Cat:
    def speak(self):
        print("Cat sais : Miauuu!")


class Snake:
    def speak(self):
        print("Snake sais : Sssss...!")


class Cow:
    def speak(self):
        print("Cow sais : Muuu!")


class Bee:
    def speak(self):
        print("Bee sais : Bzzzzz..!")


if __name__ == '__main__':
    print("Arka Noego!")

    arka = [Dog(), Cat(), Snake(), Cow(), Bee()]
    arka[0].speak()
    arka[1].speak()
    arka[2].speak()
    arka[3].speak()