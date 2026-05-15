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
        self._name: str = name
        self._health: float = health
        self._mana: float = mana
        self._action_speed: float = action_speed

    def __str__(self) -> str:
        """Returns a string representation of the character."""
        return f"{self._name} (HP: {self._health}, MP: {self._mana})"

    def to_dict(self) -> dict:
        """Converts the character instance to a dictionary for serialization.

        Returns:
            dict: Character data.
        """
        pass

    
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

        self.__strength: float = strength
    
    #* convert to dict to be saved in json
    def to_dict(self) -> dict:
        """Converts the Grunt instance to a dictionary for serialization.

        Returns:
            dict: Grunt data including strength.
        """
        return {
            "name" : self._name,
            "job_class" : "Grunt",
            "health" : round(self._health, 2),
            "mana" : round(self._mana, 2),
            "action_speed" : round(self._action_speed, 2),
            "strength" : round(self.__strength, 2)
        }


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

        self.__intelligence: float = intelligence

        #? maybe in the future wizard HP is 0.8 effective
        #? because I planned to include portion of MP as bonus damage

    def to_dict(self) -> dict:
        """Converts the Wizard instance to a dictionary for serialization.

        Returns:
            dict: Wizard data including intelligence.
        """
        return {
            "name" : self._name,
            "job_class" : "Wizard",
            "health" : round(self._health, 2),
            "mana" : round(self._mana, 2),
            "action_speed" : round(self._action_speed, 2),
            "intelligence" : round(self.__intelligence, 2)
        }


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
        self.__finesse: float = finesse
    
    def to_dict(self) -> dict:
        """Converts the Ranger instance to a dictionary for serialization.

        Returns:
            dict: Ranger data including finesse.
        """
        return {
            "name" : self._name,
            "job_class" : "Ranger",
            "health" : round(self._health, 2),
            "mana" : round(self._mana, 2),
            "action_speed" : round(self._action_speed, 2),
            "finesse" : round(self.__finesse, 2)
        }
