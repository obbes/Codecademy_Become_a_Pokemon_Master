#Codecademy 'Become A Pokemon Master'
# my strategy for creating the game
# future implmentation to be move types, more pokemon types
# A subclass for each pokemon or each pokemon family tree to allow for evolution
# pokemon stats that will be in the pokemon subclasses for each kind.  

class pokemon:
    def __init__(self, name, _type, level, maxhp, currhp, ko, exp):
        self.name = name
        self._type = _type
        self.level = level
        self.maxhp = maxhp
        self.currhp = currhp
        self.ko = ko
        self.exp = exp
        #self.moves = moves

    def lose_health(self, dmg):
        if dmg >= self.currhp:
            self.ko = True
            self.currhp = 0
            print(self.name + " fainted!")
        else:
            self.currhp = self.currhp - dmg
            print(self.name + " has " + str(self.currhp) + " remaining!")

    def gain_health(self, heal):
        if self.currhp == self.maxhp:
            print(self.name + " is already at full health!")
        else:
            if ((self.currhp + heal) >= self.maxhp):
                self.currhp = self.maxhp
                print(self.name + " was healed to full!")
            elif self.ko is True:
                print(self.name + " is knocked out and cannot be healed")
            else:
                self.currhp = self.currhp + heal
                print('healed ' + self.name + ' to ' + str(self.currhp) + ' health!')

    def attack(self, opponent, dmg):
        if self.ko is True:
            print(self.name + ' is knocked out, choose new pokemon!')
        else:
            print(self.name + ' attacks ' + opponent.name + '!')
            if self._type == 'Fire':
                if opponent._type == 'Grass':
                    dmg = dmg * 2
                    opponent.lose_health(dmg)
                elif opponent._type == 'Water':
                    dmg = dmg * .5
                    opponent.lose_health(dmg)
                else:
                    opponent.lose_health(dmg)
            if self._type == 'Water':
                if opponent._type == 'Fire':
                    dmg = dmg * 2
                    opponent.lose_health(dmg)
                elif opponent._type == 'Grass':
                    dmg = dmg * .5
                    opponent.lose_health(dmg)
                else:
                    opponent.lose_health(dmg)
            if self._type == 'Grass':
                if opponent._type == 'Water':
                    dmg = dmg * 2
                    opponent.lose_health(dmg)
                elif opponent._type == 'Fire':
                    dmg = dmg * .5
                    opponent.lose_health(dmg)
                else:
                    opponent.lose_health(dmg)
    
    def gain_exp(self, amount):
        self.exp = self.exp + amount
        print(self.name + ' has gained ' + str(amount) + ' exp')
        if self.exp >= 1.0:
            self.level = self.level + 1
            print(self.name + ' leveled to ' + str(self.level))
            self.exp = self.exp - 1
        else:
            self.exp = self.exp + amount

Charmander = pokemon('Charmander', 'Fire', 5, 30, 30, False, 0.00)
Bulbasaur = pokemon('Bulbasaur', 'Grass', 5, 30, 30, False, 0.00)
Squirtle = pokemon('Squirtle', 'Water', 5, 30, 30, False, 0.00)
Char2 = pokemon('Charmander', 'Fire', 5, 30, 30, False, 0.00)


class Trainer:
    def __init__(self, pokemons, name, active_pokemon, potions):
        self.name = name
        self.pokemons = pokemons
        self.active_pokemon = pokemons[active_pokemon]
        self.potions = potions

    def use_potion(self, active_pokemon):
        if self.potions >= 1:
            active_pokemon.gain_health(15)
            self.potions = self.potions - 1
            print(self.name + ' uses a potion on ' + active_pokemon.name)
        if self.potions == 0:
            print(self.name + " does not have any more potions")

    def attack_(self, opponent, dmg):
        self.active_pokemon.attack(opponent.active_pokemon, dmg)
        if opponent.active_pokemon.ko is True:
            difference = self.active_pokemon.level - opponent.active_pokemon.level
            if difference > 0:
                if difference > 25:
                    self.active_pokemon.gain_exp(.75)
                elif difference > 10:
                    self.active_pokemon.gain_exp(.5)
                elif difference > 5:
                    self.active_pokemon.gain_exp(.25)
                else:
                    self.active_pokemon.gain_exp(.15)
            if difference == 0:
                self.active_pokemon.gain_exp(.1)
            if difference < 0:
                if difference < 25:
                    self.active_pokemon.gain_exp(.01)
                elif difference < 10:
                    self.active_pokemon.gain_exp(.02)
                elif difference < 5:
                    self.active_pokemon.gain_exp(.05)
                else:
                    self.active_pokemon.gain_exp(.07)

    def switch(self, new_pokemon):
        if new_pokemon < 0 or new_pokemon > 6:
            print('pokemon entry invalid')
        elif self.pokemons[new_pokemon].ko:
            print(self.pokemons[new_pokemon].name + ' is fainted and cannot be selected')
        else:
            self.active_pokemon = self.pokemons[new_pokemon]
            print(self.name + ' switched pokemon to ' + self.active_pokemon.name)

Me = Trainer([pokemon('ChaChaCharmander', 'Fire', 5, 30, 30, False, 0.00), pokemon('Toortle', 'Water', 5, 30, 30, False, 0.00)], 'Obbes', 0, 2)
Gary = Trainer([pokemon('Squirtle', 'Water', 5, 20, 20, False, 0.00), pokemon('Bulbasaur', 'Grass', 5, 50, 50, False, 0.95), pokemon('Faintman', 'Fire', 100, 12000, 0, True, 0.00)], 'Gary', 0, 2)

Me.attack_(Gary, 10)
Gary.switch(1)
Me.switch(1)
Gary.attack_(Me, 25)
print(Gary.active_pokemon.exp)