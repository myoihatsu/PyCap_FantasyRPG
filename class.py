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

    #* added simple get_damage
    def get_damage(self):
        return self.__strength
    

class Wizard(Character):
    def __init__(self, name, health, mana, action_speed,intelligence):
        super().__init__(name, health, mana, action_speed)

        self.__intelligence = intelligence

        #? maybe in the future wizard HP is 0.8 effective
        #? because I planned to include portion of MP as bonus damage

    #* int + mp damage
    def get_damage(self):
        return self.__intelligence + 0.2 * self._mana