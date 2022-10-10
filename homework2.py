from homewr1 import Hero

class AirHero(Hero):
    superability ='speed'
    fly = False
    def __init__(self,name,nickname,hp,damage,fly = False):
        super().__init__(name,nickname,hp,damage)
        self.fly = fly
    def brand_phrase(self):
        self.fly = True
        return f'\n{self.name} fly = {self.fly}\nfly in the True_phrase'
    def __gen_x(self):
        pass
    def __str__(self):
        return f'\nname: {self.name}\nnickname: {self.nickname}\n' \
               f'hp: {self.hp}\ndamage: {self.damage}\n' \
               f'hero type: air hero\nsuper ability: {AirHero.superability}'


class EarthHero(Hero):
    superability ='summon earth golem'
    fly = False
    def __init__(self,name,nickname,hp,damage,fly = False):
        super().__init__(name,nickname,hp,damage)
        self.fly = fly
    def brand_phrase(self):
        self.fly = True
        return f'\n{self.name}fly = {self.fly}\nfly in the True_phrase'
    def __gen_x(self):
        pass
    def __str__(self):
        return f'\nname: {self.name}\nnickname: {self.nickname}\n' \
               f'hp: {self.hp}\ndamage: {self.damage}\n' \
               f'hero type: earth hero\nsuper ability: {EarthHero.superability}'



class SpaceHero(Hero):
    superability ='protection against radiation, vacuum, ultraviolet'
    fly = False
    def __init__(self,name,nickname,hp,damage,fly = False):
        super().__init__(name,nickname,hp,damage)
        self.fly = fly
    def brand_phrase(self):
        self.fly = True
        return f'\n{self.name}fly = {self.fly}\nfly in the True_phrase'
    def __gen_x(self):
        pass
    def __str__(self):
        return f'\nname: {self.name}\nnickname: {self.nickname}\n' \
               f'hp: {self.hp}\ndamage: {self.damage}\n' \
               f'hero type: space hero\nsuper ability: {SpaceHero.superability}'



sabina =AirHero('Sabina','_shellkyy_',140,35)
print(sabina)
print(sabina.brand_phrase())

maksat =SpaceHero('Maksat','maksym',165,40)
print(maksat)

islam =EarthHero('Islam','_argus',155,35)
print(islam)