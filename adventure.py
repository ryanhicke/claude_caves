#!/usr/bin/env python3
"""
Cave Adventure - A Text-Based Adventure Game
Inspired by classic games like Zork

Enhanced version with expanded cave system and descriptive room names
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
            print(f"\nExits: {', '.join(self.exits.keys())}")


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
        
        # ===== ORIGINAL 5 ROOMS (Enhanced) =====
        
        # Room 1: Cave Entrance -> The Swallow's Nest
        self.rooms['swallows_nest'] = Room(
            "The Swallow's Nest",
            "The cave entrance is damp and smells bad from the swallows that inhabit the entrance. "
            "Their nests cling to the rocky ceiling above, and the sound of chirping echoes through "
            "the passage. Bird droppings coat the ground, and you step carefully to avoid them. "
            "A cold draft flows from deeper within the cave.",
            {"north": "the_arsenal", "east": "echoing_chamber", "west": "crystal_pool"}
        )
        
        # Room 2: Dark Room with Dagger -> The Arsenal
        self.rooms['the_arsenal'] = Room(
            "The Arsenal",
            "You are in a dark room. The walls are cold and slick with moisture. As your eyes adjust, "
            "you notice ancient weapon racks along the walls, most of them empty and rusted with age. "
            "This must have been an armory long ago, perhaps used by those who once defended the cave. "
            "Broken shields and shattered sword fragments litter the corners.",
            {"east": "warning_chamber", "south": "swallows_nest", "west": "forgotten_shrine"},
            ["shiny dagger"]
        )
        
        # Room 3: Bright Room with Sign -> The Warning Chamber
        self.rooms['warning_chamber'] = Room(
            "The Warning Chamber",
            "A bright room illuminated by an unknown source - the light seems to emanate from the very "
            "walls themselves, casting no shadows. A weathered wooden sign has been driven into the "
            "ground in the center of the room. It reads:\n\n"
            "  \"If you forget to get it pick go back and get it before heading east,\n"
            "   go North if you're done with this\"\n\n"
            "The message is stained with what looks like old blood. The atmosphere feels ominous.",
            {"west": "the_arsenal", "north": "death_trap", "east": "guardians_lair", "south": "underground_river"}
        )
        
        # Room 4: Poison Gas Trap -> The Death Trap
        self.rooms['death_trap'] = Room(
            "The Death Trap",
            "This room appears empty and unremarkable...",
            {}
        )
        
        # Room 5: Treasure Room -> The Guardian's Lair
        self.rooms['guardians_lair'] = Room(
            "The Guardian's Lair",
            "A man dressed in ancient armor stands before a massive iron-bound treasure chest. "
            "His armor is worn but still imposing, and a wicked-looking sword hangs at his side. "
            "The chest behind him glimmers with the promise of gold. His eyes narrow as you enter, "
            "and his hand moves to his weapon.\n\n"
            "He shouts: \"You can't have my gold! I'm going to kill you!\"",
            {}
        )
        
        # ===== NEW ADDITIONAL ROOMS =====
        
        # The Crystal Pool
        self.rooms['crystal_pool'] = Room(
            "The Crystal Pool",
            "A serene underground pool glows with an ethereal blue light. Crystal formations around "
            "the water's edge refract the light into dancing patterns on the cave walls. The water "
            "is perfectly still and impossibly clear - you can see ancient coins scattered across "
            "the bottom, likely offerings from long ago. The air here feels peaceful, almost sacred.",
            {"east": "swallows_nest", "north": "mushroom_grove"}
        )
        
        # The Mushroom Grove
        self.rooms['mushroom_grove'] = Room(
            "The Mushroom Grove",
            "Bioluminescent mushrooms of various sizes cover every surface - the floor, walls, even "
            "parts of the ceiling. They cast an eerie green glow throughout the chamber. Some fungi "
            "are as tall as your knee, others barely the size of your thumb. The air is thick with "
            "spores, making it slightly difficult to breathe. A faint humming sound emanates from "
            "the largest mushrooms.",
            {"south": "crystal_pool", "east": "forgotten_shrine", "north": "bat_colony"}
        )
        
        # The Forgotten Shrine
        self.rooms['forgotten_shrine'] = Room(
            "The Forgotten Shrine",
            "This chamber was clearly built with purpose. A stone altar stands in the center, covered "
            "with the remains of ancient offerings - dried flowers, rusted coins, and small carved "
            "figures. Strange symbols are carved into the walls, and a feeling of reverence still "
            "lingers in the air despite the passage of time.",
            {"west": "mushroom_grove", "east": "the_arsenal", "south": "fossil_gallery"}
        )
        
        # The Echoing Chamber
        self.rooms['echoing_chamber'] = Room(
            "The Echoing Chamber",
            "This vast chamber has incredible acoustics. Every footstep, every breath echoes back at "
            "you multiple times, creating an eerie chorus of sound. The ceiling is so high it "
            "disappears into darkness above. Strange wind currents whistle through unseen cracks, "
            "creating haunting moans and whistles.",
            {"west": "swallows_nest", "north": "stalactite_forest", "south": "fossil_gallery"}
        )
        
        # The Fossil Gallery
        self.rooms['fossil_gallery'] = Room(
            "The Fossil Gallery",
            "The walls here are embedded with countless fossils - ancient sea creatures frozen in "
            "stone for millions of years. Ammonites spiral in perfect geometric patterns, trilobites "
            "march across the rock face, and creatures you don't recognize stare out with empty eye "
            "sockets. This entire cave system must have once been underwater, an ancient seabed now "
            "lifted high into the mountains.",
            {"north": "echoing_chamber", "east": "forgotten_shrine"}
        )
        
        # The Stalactite Forest
        self.rooms['stalactite_forest'] = Room(
            "The Stalactite Forest",
            "Massive stalactites hang from the ceiling like stone icicles, some reaching almost to "
            "the floor to meet their stalagmite counterparts. You weave between these stone pillars "
            "carefully - some look sharp enough to impale. Water drips steadily from their points, "
            "each drop adding another microscopic layer of mineral deposits. The formations cast "
            "strange shadows in your light.",
            {"south": "echoing_chamber", "east": "bat_colony", "north": "collapsed_tunnel"}
        )
        
        # The Bat Colony
        self.rooms['bat_colony'] = Room(
            "The Bat Colony",
            "Hundreds - no, thousands - of bats hang from the ceiling, their tiny bodies clustered "
            "together in a writhing mass. They stir restlessly at your presence, and you hear the "
            "rustle of leathery wings and high-pitched chirping. The floor is thick with guano, and "
            "the smell is overwhelming. You try to move quietly to avoid disturbing them further.",
            {"south": "mushroom_grove", "west": "stalactite_forest"}
        )
        
        # The Collapsed Tunnel
        self.rooms['collapsed_tunnel'] = Room(
            "The Collapsed Tunnel",
            "This passage has partially caved in at some point in the distant past. Large boulders "
            "and rubble block what was once a wider corridor. You can see gaps between the rocks "
            "where you might be able to squeeze through, but it looks precarious. Dust still hangs "
            "in the air, disturbed by your arrival. You wonder what lies beyond the rubble... or "
            "what caused the collapse in the first place.",
            {"south": "stalactite_forest", "east": "underground_river"}
        )
        
        # The Underground River
        self.rooms['underground_river'] = Room(
            "The Underground River",
            "A dark river cuts through this chamber, its waters flowing swiftly and silently from "
            "somewhere deep within the mountain. The current looks treacherous, and you cannot see "
            "the bottom. Small blind fish occasionally break the surface. The sound of rushing water "
            "fills the chamber, and the air is cool and humid. Smooth stones line the bank where you "
            "stand.",
            {"north": "warning_chamber", "west": "collapsed_tunnel"}
        )
        
        # Set starting room
        self.current_room = self.rooms['swallows_nest']
    
    def move(self, direction):
        """Move to a different room"""
        direction = direction.lower()
        
        if direction in self.current_room.exits:
            next_room_key = self.current_room.exits[direction]
            
            # Special handling for The Death Trap (poison trap)
            if next_room_key == 'death_trap':
                print("\n" + "="*60)
                print("As you step into the room, you hear a faint *click* beneath your foot...")
                print("A hidden pressure plate!")
                print("\nWith a hiss, poisonous gas begins pouring from vents in the walls!")
                print("You try to run back, but the gas fills your lungs instantly.")
                print("Your vision blurs... the world spins... and then darkness.")
                print("="*60)
                print("\n💀 YOU DIED 💀")
                print("\nGAME OVER - You triggered the ancient trap")
                self.running = False
                return
            
            # Special handling for The Guardian's Lair (treasure room)
            if next_room_key == 'guardians_lair':
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
        print("\n" + "="*60)
        if "shiny dagger" in self.inventory:
            print("The guardian draws his sword and charges at you!")
            print("You quickly draw your shiny dagger and meet his attack!")
            print("\nThe combat is fierce but brief. Your dagger finds its mark,")
            print("and the guardian falls to his knees, then collapses.")
            print("\nYou approach the treasure chest and throw it open.")
            print("Gold coins, precious gems, and ancient artifacts spill out!")
            print("="*60)
            print("\n🏆 ✨ CONGRATULATIONS! YOU WIN! ✨ 🏆")
            print("\nYou have claimed the legendary treasure of the cave!")
        else:
            print("You have no weapon to defend yourself with!")
            print("The guardian draws his sword with a menacing grin.")
            print("\nYou try to dodge, but you're no match for a trained warrior.")
            print("His blade flashes in the dim light...")
            print("="*60)
            print("\n💀 YOU DIED 💀")
            print("\nGAME OVER - You were slain by the guardian")
        
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
        print("\n" + "="*60)
        print("AVAILABLE COMMANDS")
        print("="*60)
        print("  go <direction>    - Move in a direction (north, south, east, west)")
        print("  <direction>       - Shortcut: just type the direction (n, s, e, w)")
        print("  take <item>       - Pick up an item")
        print("  use <item>        - Use an item from your inventory")
        print("  inventory (i)     - Show your inventory")
        print("  look (l)          - Look around the current room")
        print("  map               - Show the map (if you have one)")
        print("  help (h)          - Show this help message")
        print("  quit (q)          - Quit the game")
        print("="*60)
    
    def show_map(self):
        """Display an ASCII map of the cave system"""
        print("\n" + "="*60)
        print("CAVE SYSTEM MAP")
        print("="*60)
        print("""
                    [The Collapsed]
                    [   Tunnel    ]
                          |
                        north
                          |
        [Bat Colony]--[Stalactite]
             |         [  Forest  ]
            west            |
             |            south
        [Mushroom]          |
        [  Grove  ]--[Echoing Chmb]--[Fossil]
             |              |         [Gallery]
           south          west           |
             |              |          north
        [Crystal]----[Swallow's]--[Forgotten]
        [  Pool ]    [   Nest  ]  [ Shrine  ]
                          |             |
                        north         east
                          |             |
                     [The Arsenal]------+
                          |
                        east
                          |
                    [Underground]
                    [   River   ]
                          |
                        north
                          |
                     [Warning Chmb]
                       /    |    \\
                    north  east  west
                     /      |      \\
              [Death    [Guardian's  
               Trap]     Lair - GOAL]
              (DANGER!)   
        """)
        print("="*60)
        print("Legend: Your goal is to reach the Guardian's Lair!")
        print("        Avoid the Death Trap at all costs!")
        print("="*60)
    
    def parse_command(self, command):
        """Parse and execute player commands"""
        parts = command.lower().strip().split()
        
        if not parts:
            return
        
        action = parts[0]
        
        if action in ['quit', 'q', 'exit']:
            print("\nThanks for playing Cave Adventure!")
            self.running = False
        
        elif action in ['help', 'h', '?']:
            self.show_help()
        
        elif action in ['map', 'm']:
            self.show_map()
        
        elif action in ['look', 'l']:
            self.current_room.describe()
        
        elif action in ['inventory', 'i', 'inv']:
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
        
        elif action in ['take', 'get', 'grab', 'pick', 'pickup']:
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
        print("\n" + "="*60)
        print("           ⚔️  CAVE ADVENTURE  ⚔️")
        print("        A Text-Based Adventure Game")
        print("="*60)
        print("\nYou stand before the entrance to a mysterious cave system.")
        print("Legends speak of treasure deep within, guarded by an ancient")
        print("warrior. Many have entered... few have returned.")
        print("\nType 'help' for commands or 'map' to see the cave layout.")
        print("="*60)
        
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
