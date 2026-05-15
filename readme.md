# PyCap FantasyRPG Battler

A text-based, turn-based RPG combat simulator built with Python. Create unique characters, manage their stats, and pit them against each other in strategic battles.

## 🎮 Features

- **Character Creation**: Create characters from three distinct classes: Grunt, Wizard, and Ranger.
- **Persistent Storage**: Characters are saved as `.json` files in the `characters/` directory, allowing you to build a roster that persists across sessions.
- **Dynamic Combat**: Initiative-based turn order, resource management (Mana), and class-specific damage scaling.
- **Character Management**: View, edit, or delete existing characters through an intuitive menu system.

## ⚔️ Character Classes

Each class scales its damage differently based on its primary and secondary stats:

| Class | Primary Stat | Damage Scaling Formula |
| :--- | :--- | :--- |
| **Grunt** | Strength (STR) | `STR + (0.15 * HP)` |
| **Wizard** | Intelligence (INT) | `INT + (0.7 * MP)` |
| **Ranger** | Finesse (FIN) | `FIN + (0.8 * Action Speed)` |

## 🛡️ Combat Mechanics

### Turn Order (Initiative)
At the start of every round, both combatants roll for initiative. A random number between 1 and the character's **Action Speed** is generated. The higher roll attacks first.

### Resource Management
- **Mana (MP)**: Every standard attack costs **4 MP**.
- **Struggle**: If a character is out of mana, they perform a "Struggle" move. This deals **70% of normal damage** but costs the attacker **4 HP**.
- **Counter-Attack**: After the first attacker finishes their turn, the second combatant performs a counter-attack (if still standing).

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/PyCap_FantasyRPG.git
   cd PyCap_FantasyRPG
   ```
2. Ensure the `characters/` directory exists:
   ```bash
   mkdir characters
   ```

### Running the Game
Start the main loop by running:
```bash
python main.py
```

## 📂 Project Structure

- `main.py`: Entry point for the application.
- `menu.py`: Main menu logic and navigation.
- `battle.py`: Combat loop, initiative, and damage calculation.
- `char_creation.py`: Character class selection and initialization.
- `job_class.py`: Class definitions and dictionary serialization.
- `helper_functions.py`: File I/O (JSON), input validation, and character management utilities.
- `characters/`: Directory where character data is stored.

## 📝 License
This project is open-source and available under the [MIT License](LICENSE).
