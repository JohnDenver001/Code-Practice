class Character:
    def __init__(self, name, hp, atk, magic, level):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.magic = magic
        self.level = level

charOne = Character("JDA", 100, 50, 25, 1)
print(charOne.name)