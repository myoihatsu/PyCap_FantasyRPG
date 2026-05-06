class Character:
    def __init__(self,name,health,mana,action_speed):
        self._name = name
        self._health = health
        self._mana = mana
        self._action_speed = action_speed

    def __str__(self):
        pass

    def to_dict(self):
        pass

    
class Grunt(Character):
    def __init__(self, name, health, mana, action_speed,strength):
        super().__init__(name, health, mana, action_speed)

        self.__strength = strength
    
    #* convert to dict to be saved in json
    def to_dict(self):
        return {
            "name" : self._name,
            "job_class" : "Grunt",
            "health" : round(self._health, 2),
            "mana" : round(self._mana, 2),
            "action_speed" : round(self._action_speed, 2),
            "strength" : round(self.__strength, 2)
        }


class Wizard(Character):
    def __init__(self, name, health, mana, action_speed,intelligence):
        super().__init__(name, health, mana, action_speed)

        self.__intelligence = intelligence

        #? maybe in the future wizard HP is 0.8 effective
        #? because I planned to include portion of MP as bonus damage

    def to_dict(self):
        return {
            "name" : self._name,
            "job_class" : "Wizard",
            "health" : round(self._health, 2),
            "mana" : round(self._mana, 2),
            "action_speed" : round(self._action_speed, 2),
            "intelligence" : round(self.__intelligence, 2)
        }


class Ranger(Character):
    def __init__(self, name, health, mana, action_speed, finesse):
        super().__init__(name, health, mana, action_speed)

        #* decided finesse sounds nicer instead of dexterity
        self.__finesse = finesse
    
    def to_dict(self):
        return {
            "name" : self._name,
            "job_class" : "Ranger",
            "health" : round(self._health, 2),
            "mana" : round(self._mana, 2),
            "action_speed" : round(self._action_speed, 2),
            "finesse" : round(self.__finesse, 2)
        }