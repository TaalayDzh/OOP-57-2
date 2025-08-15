class Hero:

    def __init__ (self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action (self):
        return "base action"

class HeroWarrior(Hero):
    def __init__(self, name, lvl, hp, rage=0):
        super().__init__(name, lvl, hp)
        self.rage = rage
    def action(self):
        return "Герой готов к атаке!"

    def attack(self):
        if self.rage >= 100:
            self.rage = 0
            return "Мощная атака!"

        else:
            self.rage += 25
            return "обычная атака"


class HeroMage(Hero):

    def __init__ (self, name, lvl, hp, spell_book):
        super().__init__(name, lvl, hp)
        self.spell_book = spell_book

    def action(self):
        return "base action"

    def show_spells(self):
        result = "Доступные заклинания:\n"
        for spell in self.spell_book:
            result += f"- {spell}\n"
        return result

mage = HeroMage(name="Gendalf", hp=90, lvl=3, spell_book=["Fireball", "Teleport"])
warrior = HeroWarrior(name="Aragorn", lvl=5, hp=110)
hero = Hero(name="Frodo", lvl=2, hp=50)

print(mage.action())
print(mage.show_spells())
print(warrior.action())
print(warrior.attack())
print(warrior.attack())
print(hero.action())