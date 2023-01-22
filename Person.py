class person:

def __str__(self):
    return f'{self.name} (hp:{self.hp},' \
           f' damage:{self.damage},' \
           f' defence: {self.defence})'

def Action(self):
    self.mood = self.mood + 15
    self.hp = self.hp = 3
