#!/usr/bin/env python3
"""
Cave Adventure - A Text-Based Adventure Game
Inspired by classic games like Zork
"""

class Room:
    """Represents a room in the adventure game"""
    def __init__(self, name, description, exits=None, items=None):
        self.name = name
        self.description = description
        self.exits = exits if exits else {}
        self.items = items if items else []
    
    def describe(self):
        """Print the room description"""
        print(f"\n{self.name}")
        print("=" * len(self.name))
        print(self.description)
        
        if self.items:
            print(f"\nYou see: {', '.join(self.items)}")
        
        if self.exits:
            print(f"\nExits: {', '.join([f'{direction} to {room}' for direction, room in self.exits.items()])}")


class Game:
    """Main game class"""
    def __init__(self):
        self.current_room = None
        self.inventory = []
        self.rooms = {}
        self.running = True
        self.setup_rooms()
    
    def setup_rooms(self):
        """Initialize all game rooms"""
        # Room 1: Cave Entrance
        self.rooms['room1'] = Room(
            "Cave Entrance",
            "The cave entrance is damp and smells bad from the swallows that inhabit the entrance.",
            {"north": "Room 2"}
        )
        
        # Room 2: Dark Room with Dagger
        self.rooms['room2'] = Room(
            "Dark Room",
            "You are in a dark room. The walls are cold and slick with moisture.",
            {"east": "Room 3", "south": "Room 1"},
            ["shiny dagger"]
        )
        
        # Room 3: Bright Room with Sign
        self.rooms['room3'] = Room(
            "Bright Room",
            "A bright room illuminated by an unknown source. A sign on the wall reads:\n"
            "\"If you forget to get it pick go back and get it before heading east, go North if you're done with this\"",
            {"west": "Room 2", "north": "Room 4", "east": "Room 5"}
        )
        
        # Room 4: Poison Gas Trap
        self.rooms['room4'] = Room(
            "Trapped Room",
            "This room appears empty...",
            {}
        )
        
        # Room 5: Treasure Room
        self.rooms['room5'] = Room(
            "Treasure Room",
            "A man is standing in front of a treasure chest. He glares at you menacingly.\n"
            "He shouts: \"You can't have my gold! I'm going to kill you!\"",
            {}
        )
        
        self.current_room = self.rooms['room1']
    
    def move(self, direction):
        """Move to a different room"""
        direction = direction.lower()
        
        if direction in self.current_room.exits:
            next_room_name = self.current_room.exits[direction]
            next_room_key = next_room_name.lower().replace(" ", "")
            
            # Special handling for Room 4 (poison trap)
            if next_room_key == 'room4':
                print("\nAs you enter this room you hear a switch click...")
                print("Poisonous gas fills the room!")
                print("\n💀 YOU DIED 💀")
                print("\nGAME OVER")
                self.running = False
                return
            
            # Special handling for Room 5 (treasure room)
            if next_room_key == 'room5':
                self.current_room = self.rooms[next_room_key]
                self.current_room.describe()
                self.handle_treasure_room()
                return
            
            self.current_room = self.rooms[next_room_key]
            self.current_room.describe()
        else:
            print("You can't go that way!")
    
    def handle_treasure_room(self):
        """Handle the final confrontation in the treasure room"""
        if "shiny dagger" in self.inventory:
            print("\nYou quickly draw your shiny dagger and engage the man in combat!")
            print("With a swift strike, you defeat him!")
            print("\n🏆 You open the treasure chest and claim the gold! 🏆")
            print("\n✨ CONGRATULATIONS! YOU WIN! ✨")
        else:
            print("\nYou have no weapon to defend yourself!")
            print("The man attacks you with his sword!")
            print("\n💀 YOU DIED 💀")
            print("\nGAME OVER")
        
        self.running = False
    
    def take(self, item):
        """Pick up an item from the current room"""
        item = item.lower()
        
        # Check if item exists in current room
        for room_item in self.current_room.items:
            if item in room_item.lower():
                self.inventory.append(room_item)
                self.current_room.items.remove(room_item)
                print(f"You picked up the {room_item}.")
                return
        
        print(f"There is no {item} here.")
    
    def use(self, item):
        """Use an item from inventory"""
        item = item.lower()
        
        for inv_item in self.inventory:
            if item in inv_item.lower():
                print(f"You can't use the {inv_item} right now.")
                return
        
        print(f"You don't have a {item}.")
    
    def show_inventory(self):
        """Display the player's inventory"""
        if self.inventory:
            print(f"\nInventory: {', '.join(self.inventory)}")
        else:
            print("\nYour inventory is empty.")
    
    def show_help(self):
        """Display available commands"""
        print("\nAvailable commands:")
        print("  go <direction>    - Move in a direction (north, south, east, west)")
        print("  take <item>       - Pick up an item")
        print("  use <item>        - Use an item from your inventory")
        print("  inventory (i)     - Show your inventory")
        print("  look (l)          - Look around the current room")
        print("  help (h)          - Show this help message")
        print("  quit (q)          - Quit the game")
    
    def parse_command(self, command):
        """Parse and execute player commands"""
        parts = command.lower().strip().split()
        
        if not parts:
            return
        
        action = parts[0]
        
        if action in ['quit', 'q', 'exit']:
            print("Thanks for playing!")
            self.running = False
        
        elif action in ['help', 'h']:
            self.show_help()
        
        elif action in ['look', 'l']:
            self.current_room.describe()
        
        elif action in ['inventory', 'i']:
            self.show_inventory()
        
        elif action in ['go', 'move', 'walk']:
            if len(parts) > 1:
                self.move(parts[1])
            else:
                print("Go where? Specify a direction (north, south, east, west).")
        
        elif action in ['north', 'south', 'east', 'west', 'n', 's', 'e', 'w']:
            # Allow direct direction commands
            direction_map = {'n': 'north', 's': 'south', 'e': 'east', 'w': 'west'}
            direction = direction_map.get(action, action)
            self.move(direction)
        
        elif action in ['take', 'get', 'grab', 'pick']:
            if len(parts) > 1:
                item = ' '.join(parts[1:])
                self.take(item)
            else:
                print("Take what?")
        
        elif action in ['use']:
            if len(parts) > 1:
                item = ' '.join(parts[1:])
                self.use(item)
            else:
                print("Use what?")
        
        else:
            print("I don't understand that command. Type 'help' for available commands.")
    
    def play(self):
        """Main game loop"""
        print("=" * 60)
        print("  CAVE ADVENTURE")
        print("  A Text-Based Adventure Game")
        print("=" * 60)
        print("\nType 'help' for a list of commands.\n")
        
        self.current_room.describe()
        
        while self.running:
            try:
                command = input("\n> ").strip()
                if command:
                    self.parse_command(command)
            except KeyboardInterrupt:
                print("\n\nThanks for playing!")
                break
            except EOFError:
                print("\n\nThanks for playing!")
                break


def main():
    """Entry point for the game"""
    game = Game()
    game.play()


if __name__ == "__main__":
    main()
