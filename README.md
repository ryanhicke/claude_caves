# Cave Adventure

A classic text-based adventure game inspired by Zork and other interactive fiction games from the early days of gaming.

## Description

Navigate through a mysterious cave system, collect items, and overcome challenges to win the treasure! This game features:

- 5 unique rooms to explore
- Items to collect and use
- Multiple endings based on your choices
- Simple text-based interface

## Game Story

You stand at the entrance of a mysterious cave. Rumor has it that treasure lies deep within, but many have entered and never returned. Will you be the one to claim the gold?

## Installation

### Requirements
- Python 3.6 or higher

### Setup

1. Clone this repository:
```bash
git clone <repository-url>
cd cave-adventure
```

2. Make the game executable (optional):
```bash
chmod +x adventure.py
```

## How to Play

Run the game with:
```bash
python3 adventure.py
```

Or if you made it executable:
```bash
./adventure.py
```

## Commands

- `go <direction>` or just `<direction>` - Move in a direction (north, south, east, west)
- `take <item>` - Pick up an item
- `use <item>` - Use an item from your inventory
- `inventory` or `i` - Show your inventory
- `look` or `l` - Look around the current room
- `help` or `h` - Show available commands
- `quit` or `q` - Quit the game

### Command Shortcuts
- `n`, `s`, `e`, `w` - Quick direction movement
- `i` - Inventory
- `l` - Look
- `h` - Help
- `q` - Quit

## Game Map

```
        [Room 4]
        (Trap!)
            |
         north
            |
[Room 1] - [Room 2] - [Room 3] - [Room 5]
 (Start)   (Dagger)    (Sign)   (Treasure)
```

## Tips

- Read room descriptions carefully
- Pay attention to signs and messages
- Some rooms may be dangerous
- You might need certain items to succeed

## Winning the Game

Your goal is to reach the treasure room and claim the gold. But beware - the treasure is guarded, and you'll need to be prepared for the final confrontation!

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to fork this project and add your own rooms, items, and challenges!

## Future Enhancements

Potential features to add:
- More rooms and complex puzzles
- Save/load game functionality
- More items and interactions
- Combat system
- Score tracking
- Multiple game paths and endings
