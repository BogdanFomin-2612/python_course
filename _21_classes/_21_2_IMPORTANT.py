class Ork:
    def __init__(self, level: int) -> None:     #? Магический метод, определяет как будет себя вести обьект класса с разными конструкциями языка
        self.level = level                      #? SELF - куземпляр класса, который мы передаем в метод класса
        self.health_points = 100 * level
        self.attack_power = 100 * level

    def attack(self):
        print(f"Ork attacks with {self.attack_power} power")


    #? ДАНДЕР_МЕТОДЫ

    def __str__(self):
        return f"Ork (level: {self.level}), (hp: {self.health_points}), (attack: {self.attack_power})"

ork = Ork(level=2)
# print(ork.attack_power)

# ork.level += 1
# print(ork.level)



print(ork)