# Cave Adventure - Enhanced Edition

A classic text-based adventure game inspired by Zork and other interactive fiction games from the early days of gaming.

## Description

Navigate through a mysterious cave system with **13 interconnected rooms**, collect items, and overcome challenges to win the treasure! This enhanced edition features:

- 13 unique rooms with descriptive, thematic names
- Rich, atmospheric descriptions for each location
- Items to collect and use strategically
- Multiple endings based on your choices
- Deadly traps to avoid
- Simple text-based interface with quality-of-life features
- Built-in map command

## Game Story

You stand at the entrance of a mysterious cave. Rumor has it that treasure lies deep within, guarded by an ancient warrior who has defended it for centuries. Many have entered seeking fortune and glory... few have returned. 

Will you be brave enough to navigate the dangers and claim the legendary treasure?

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

### Movement
- `go <direction>` - Move in a direction (north, south, east, west)
- `<direction>` or `n/s/e/w` - Quick movement shortcut

### Interaction
- `take <item>` - Pick up an item
- `use <item>` - Use an item from your inventory
- `look` or `l` - Look around the current room

### Information
- `inventory` or `i` - Show your inventory
- `map` or `m` - Display the cave system map
- `help` or `h` - Show available commands

### Game Control
- `quit` or `q` - Quit the game

## The 13 Rooms

### Original Core Rooms (Enhanced)
1. **The Swallow's Nest** (Start) - The cave entrance, home to countless swallows
2. **The Arsenal** - An ancient armory with a valuable item
3. **The Warning Chamber** - A mysteriously lit room with an ominous message
4. **The Death Trap** - A deadly room with a poison gas trap (AVOID!)
5. **The Guardian's Lair** - The treasure room with its fierce protector (GOAL!)

### New Exploration Rooms
6. **The Crystal Pool** - A serene underground pool with glowing crystals
7. **The Mushroom Grove** - Bioluminescent fungi create an eerie atmosphere
8. **The Forgotten Shrine** - An ancient place of worship
9. **The Echoing Chamber** - A vast room with incredible acoustics
10. **The Fossil Gallery** - Prehistoric creatures frozen in stone
11. **The Stalactite Forest** - Massive mineral formations hang like stone icicles
12. **The Bat Colony** - Home to thousands of bats
13. **The Collapsed Tunnel** - A partially blocked passage
14. **The Underground River** - A dark, swift-flowing subterranean waterway

## Game Map

Use the `map` command in-game to see a detailed ASCII map, or refer to this simplified version:

```
                [Collapsed Tunnel]
                        |
        [Bat Colony]--[Stalactite Forest]
             |              |
        [Mushroom Grove]--[Echoing Chamber]--[Fossil Gallery]
             |              |                      |
        [Crystal Pool]--[Swallow's Nest]--[Forgotten Shrine]
                            |                      |
                       [The Arsenal]---------------+
                            |
                   [Underground River]
                            |
                    [Warning Chamber]
                       /    |    \
              [Death Trap] [Guardian's Lair]
```

## Tips for Success

- **Explore thoroughly** - Not all rooms contain items, but all contain atmosphere
- **Read carefully** - Room descriptions and signs contain important clues
- **Pay attention to warnings** - The Warning Chamber's sign is there for a reason
- **Avoid the Death Trap** - Going north from the Warning Chamber means certain death
- **You need a weapon** - The Guardian cannot be defeated with bare hands
- **Map it out** - Use the `map` command to understand the layout

## Winning Strategy

1. Start at The Swallow's Nest
2. Navigate to The Arsenal (north from start)
3. Take the shiny dagger
4. Find your way to The Warning Chamber
5. From Warning Chamber, go EAST to The Guardian's Lair (NOT north!)
6. Defeat the guardian with your dagger
7. Claim the treasure!

## Alternate Endings

### Victory
- Reach The Guardian's Lair with the dagger → Defeat the guardian → Win the treasure! 🏆

### Death by Combat
- Reach The Guardian's Lair without the dagger → The guardian kills you → Game Over 💀

### Death by Trap
- Enter The Death Trap from Warning Chamber → Poison gas kills you → Game Over 💀

## Features

- **Atmospheric Descriptions**: Each room has rich, detailed descriptions
- **Thematic Names**: Room names reflect their contents and character
- **Multiple Paths**: Explore various routes through the cave system
- **Hidden Dangers**: Not all threats are obvious
- **Quality of Life**: Built-in map, multiple command shortcuts, helpful prompts

## Technical Details

- Written in Python 3
- Object-oriented design with Room and Game classes
- Flexible command parsing system
- No external dependencies required
- Fully playable in terminal/command prompt

## Future Enhancements

Potential features for future versions:
- More items to collect and use
- Puzzle-solving mechanics
- Save/load game functionality
- Multiple difficulty levels
- Random item placement
- Achievement system
- Story expansions and side quests

## License

This project is released under the MIT License - see LICENSE file for details.

## Contributing

Feel free to fork this project and add your own rooms, items, puzzles, and challenges! 

Some ideas for contributions:
- Additional interconnected rooms
- More items and interactive objects
- Puzzles that require multiple items
- NPCs to interact with
- Alternative paths to victory
- Easter eggs and secrets

## Credits

Inspired by classic text adventure games like:
- Zork (Infocom)
- Adventure (Colossal Cave Adventure)
- Hitchhiker's Guide to the Galaxy

Created as a learning project and homage to the golden age of interactive fiction.
