class Hero:
    def __init__(self,name,nickname,hp,damage):
        self.name = name
        self.nickname = nickname
        self.hp = hp
        self.damage = damage
    def heal(self):
       self.hp = self.hp + 100
    def duoble_damage(self):
        self.damage = self.damage * 2
    def greetings(self):
        return f'my name is {self.name}'
    def brand_phrase(self):
        return f'good will win'
    def __str__(self):
        return f'\nname: {self.name}\nnickname: {self.nickname}\n' \
               f'hp: {self.hp}\ndamage: {self.damage}'
max =Hero('Max','SuperMax',120,15)
print(max)
max.heal()
print(max)

victor =Hero('Victor','Tsoi_is_alive',135,10)
print(victor)
victor.duoble_damage()
print(victor)

kate =Hero('Kate','RATARETO',110,12)
print(kate)
print(kate.greetings())

vanessa =Hero('Vanessa','vanny',105,9)
print(vanessa)
print(vanessa.brand_phrase())
