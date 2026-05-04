class Character:
    def __init__(self,name,health,mana,action_speed):
        self._name = name
        self._health = health
        self._mana = mana
        self._action_speed = action_speed

    def __str__(self):
        pass

    def get_damage(self):
        pass

    def to_dict(self):
        pass

    
class Grunt(Character):
    def __init__(self, name, health, mana, action_speed,strength):
        super().__init__(name, health, mana, action_speed)

        self.__strength = strength

    #* added simple get_damage
    def get_damage(self):
        return self.__strength + 2 * self._health
    
    #* convert to dict to be saved in json
    def to_dict(self):
        return {
            "name" : self._name,
            "job_class" : "Grunt",
            "health" : self._health,
            "mana" : self._mana,
            "action_speed" : self._action_speed,
            "strength" : self.__strength
        }


class Wizard(Character):
    def __init__(self, name, health, mana, action_speed,intelligence):
        super().__init__(name, health, mana, action_speed)

        self.__intelligence = intelligence

        #? maybe in the future wizard HP is 0.8 effective
        #? because I planned to include portion of MP as bonus damage

    #* int + mp damage
    def get_damage(self):
        return self.__intelligence + 2 * self._mana
    
    def to_dict(self):
        return {
            "name" : self._name,
            "job_class" : "Wizard",
            "health" : self._health,
            "mana" : self._mana,
            "action_speed" : self._action_speed,
            "intelligence" : self.__intelligence
        }


class Ranger(Character):
    def __init__(self, name, health, mana, action_speed, finesse):
        super().__init__(name, health, mana, action_speed)

        #* decided finesse sounds nicer instead of dexterity
        self.__finesse = finesse
    
    def get_damage(self):
        return self.__finesse + 2 * self._action_speed
    
    def to_dict(self):
        return {
            "name" : self._name,
            "job_class" : "Ranger",
            "health" : self._health,
            "mana" : self._mana,
            "action_speed" : self._action_speed,
            "finesse" : self.__finesse
        }