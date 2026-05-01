class Character:
    def __init__(self,name,health,mana,action_speed):
        self._name = name
        self._health = health
        self._mana = mana
        self._action_speed = action_speed

    def get_damage(self):
        return 1 

class Grunt(Character):
    def __init__(self, name, health, mana, action_speed,strength):
        super().__init__(name, health, mana, action_speed)
        self.__strength = strength

    def get_damage(self):
        return self.__strength