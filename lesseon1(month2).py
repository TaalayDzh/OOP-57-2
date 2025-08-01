class Hero:
    def __init__(self, name, lvl, hp):
        self.name_1 = name
        self.lvl_1 = lvl
        self.hp_1 = hp

    def action(self):
        print(f'{self.name_1} base action!!')

kirito = Hero("Kirito", 100, 1000)

print(kirito.hp_1)
kirito.action()


