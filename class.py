class Character:
    """Base class for all RPG characters.

    Attributes:
        _name (str): The name of the character.
        _health (float): The current health points of the character.
        _mana (float): The current mana points of the character.
        _action_speed (float): The speed determining turn order.
    """
    def __init__(self, name: str, health: float, mana: float, action_speed: float):
        """Initializes a Character instance.

        Args:
            name (str): The name of the character.
            health (float): Initial health points.
            mana (float): Initial mana points.
            action_speed (float): Initial action speed.
        """
        self._name = name
        self._health = health
        self._mana = mana
        self._action_speed = action_speed

    def get_damage(self) -> float:
        """Calculates the base damage of the character.

        Returns:
            float: The calculated damage value.
        """
        return 1.0


class Grunt(Character):
    """A combatant class focusing on Strength and Health.

    Attributes:
        __strength (float): The strength stat of the Grunt.
    """
    def __init__(self, name: str, health: float, mana: float, action_speed: float, strength: float):
        """Initializes a Grunt instance.

        Args:
            name (str): The name of the character.
            health (float): Initial health points.
            mana (float): Initial mana points.
            action_speed (float): Initial action speed.
            strength (float): The strength stat.
        """
        super().__init__(name, health, mana, action_speed)

        self.__strength = strength

    #* added simple get_damage
    def get_damage(self) -> float:
        """Calculates damage based on Strength and Health.

        Returns:
            float: Strength plus twice the health.
        """
        return float(self.__strength + 2 * self._health)
    

class Wizard(Character):
    """A combatant class focusing on Intelligence and Mana.

    Attributes:
        __intelligence (float): The intelligence stat of the Wizard.
    """
    def __init__(self, name: str, health: float, mana: float, action_speed: float, intelligence: float):
        """Initializes a Wizard instance.

        Args:
            name (str): The name of the character.
            health (float): Initial health points.
            mana (float): Initial mana points.
            action_speed (float): Initial action speed.
            intelligence (float): The intelligence stat.
        """
        super().__init__(name, health, mana, action_speed)

        self.__intelligence = intelligence

        #? maybe in the future wizard HP is 0.8 effective
        #? because I planned to include portion of MP as bonus damage

    #* int + mp damage
    def get_damage(self) -> float:
        """Calculates damage based on Intelligence and Mana.

        Returns:
            float: Intelligence plus twice the mana.
        """
        return float(self.__intelligence + 2 * self._mana)
    

class Ranger(Character):
    """A combatant class focusing on Finesse and Action Speed.

    Attributes:
        __finesse (float): The finesse stat of the Ranger.
    """
    def __init__(self, name: str, health: float, mana: float, action_speed: float, finesse: float):
        """Initializes a Ranger instance.

        Args:
            name (str): The name of the character.
            health (float): Initial health points.
            mana (float): Initial mana points.
            action_speed (float): Initial action speed.
            finesse (float): The finesse stat.
        """
        super().__init__(name, health, mana, action_speed)

        #* decided finesse sounds nicer instead of dexterity
        self.__finesse = finesse
    
    def get_damage(self) -> float:
        """Calculates damage based on Finesse and Action Speed.

        Returns:
            float: Finesse plus twice the action speed.
        """
        return float(self.__finesse + 2 * self._action_speed)
