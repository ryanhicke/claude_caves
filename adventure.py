#!/usr/bin/env python3
"""
Cave Adventure - A Text-Based Adventure Game
Inspired by classic games like Zork

Enhanced version with expanded cave system and descriptive room names
"""

import random

import random
import time

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
        self.player_hp = 10
        self.player_max_hp = 10
        self.guardian_hp = 20
        self.bat_hp = 5
        self.has_shield = False
        self.in_combat = False
        self.combat_enemy = None
        self.surprised_guardian = False
        self.bat_defeated = False
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
            "lingers in the air despite the passage of time. Something metallic glints behind the altar.",
            {"west": "mushroom_grove", "east": "the_arsenal", "south": "fossil_gallery"},
            ["ancient shield"]
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
            "what caused the collapse in the first place. Wait - is that a small opening near the floor?",
            {"south": "stalactite_forest", "east": "underground_river", "down": "hidden_tunnel"}
        )
        
        # Hidden Tunnel (secret path to Guardian's Lair)
        self.rooms['hidden_tunnel'] = Room(
            "The Hidden Tunnel",
            "You've squeezed through a narrow opening into a cramped, dark tunnel. The passage is barely "
            "wide enough to crawl through. As you move forward, you notice the tunnel slopes downward and "
            "curves to the right. You can hear faint sounds ahead - the echo of a voice, perhaps? The air "
            "feels different here, warmer. You realize this tunnel must lead somewhere important.",
            {"up": "collapsed_tunnel", "forward": "guardians_lair_back"}
        )
        
        # Guardian's Lair (back entrance)
        self.rooms['guardians_lair_back'] = Room(
            "The Guardian's Lair (Behind)",
            "You emerge from the hidden tunnel behind the massive treasure chest! The guardian stands "
            "on the other side, facing the main entrance. He hasn't noticed you yet - you have the element "
            "of surprise! You could attack now while his back is turned, or try to sneak around.",
            {"back": "hidden_tunnel"}
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
        
        # Don't allow movement during combat
        if self.in_combat:
            print("You can't move while in combat! Use 'retreat' to flee.")
            return
        
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
            
            # Special handling for Bat Colony (bat enemy)
            if next_room_key == 'bat_colony' and not self.bat_defeated:
                self.current_room = self.rooms[next_room_key]
                self.current_room.describe()
                print("\n" + "="*60)
                print("A large bat swoops down from the ceiling, screeching!")
                print("It's attacking you!")
                print("="*60)
                self.start_combat('bat')
                return
            
            # Special handling for The Guardian's Lair (treasure room from front)
            if next_room_key == 'guardians_lair':
                self.current_room = self.rooms[next_room_key]
                self.current_room.describe()
                self.start_combat('guardian', surprised=False)
                return
            
            # Special handling for Guardian's Lair from behind (surprise attack)
            if next_room_key == 'guardians_lair_back':
                self.current_room = self.rooms[next_room_key]
                self.current_room.describe()
                print("\nYou have the element of surprise! You can attack first.")
                self.surprised_guardian = True
                self.start_combat('guardian', surprised=True)
                return
            
            self.current_room = self.rooms[next_room_key]
            self.current_room.describe()
        else:
            print("You can't go that way!")
    
    def start_combat(self, enemy_type, surprised=False):
        """Initialize combat with an enemy"""
        self.in_combat = True
        self.combat_enemy = enemy_type
        
        if enemy_type == 'guardian' and not surprised:
            print("\n" + "="*60)
            print("COMBAT BEGINS!")
            print("="*60)
            self.show_combat_status()
        elif enemy_type == 'guardian' and surprised:
            print("\n" + "="*60)
            print("SURPRISE ATTACK!")
            print("="*60)
            print("You have the first strike! The guardian hasn't noticed you yet.")
            self.show_combat_status()
        elif enemy_type == 'bat':
            print("\nCOMBAT: Large Bat")
            self.show_combat_status()
    
    def show_combat_status(self):
        """Display current combat status"""
        print(f"\nYour HP: {self.player_hp}/{self.player_max_hp}")
        
        if self.combat_enemy == 'guardian':
            print(f"Guardian HP: {self.guardian_hp}/20")
        elif self.combat_enemy == 'bat':
            print(f"Bat HP: {self.bat_hp}/5")
        
        has_dagger = "shiny dagger" in self.inventory
        if has_dagger:
            print("Weapon equipped: Shiny Dagger")
        else:
            print("Weapon: Bare hands")
        
        if self.has_shield:
            print("Shield: Equipped")
        print()
    
    def attack(self, weapon=None):
        """Player attacks during combat"""
        if not self.in_combat:
            print("You're not in combat!")
            return
        
        # Determine damage
        if weapon and weapon.lower() in ['dagger', 'shiny dagger'] and "shiny dagger" in self.inventory:
            player_damage = random.randint(2, 16)
            print(f"🗡️  You strike with your shiny dagger!")
        else:
            player_damage = random.randint(1, 4)
            print(f"👊 You attack with your bare hands!")
        
        # Apply damage to enemy
        if self.combat_enemy == 'guardian':
            self.guardian_hp -= player_damage
            print(f"   You deal {player_damage} damage!")
            print(f"   Guardian HP: {max(0, self.guardian_hp)}/20")
            
            # Check if guardian is defeated
            if self.guardian_hp <= 0:
                self.win_game()
                return
            
            # Guardian counter-attacks (unless surprised on first turn)
            if self.surprised_guardian:
                print("\nThe guardian spins around, startled by your attack!")
                print("He draws his sword to defend himself!")
                self.surprised_guardian = False
            else:
                self.guardian_counterattack()
                
        elif self.combat_enemy == 'bat':
            self.bat_hp -= player_damage
            print(f"   You deal {player_damage} damage!")
            print(f"   Bat HP: {max(0, self.bat_hp)}/5")
            
            # Check if bat is defeated
            if self.bat_hp <= 0:
                print("\n" + "="*60)
                print("The bat screeches one last time and falls to the ground!")
                print("You notice something among the guano on the floor...")
                print("You found: bat guano")
                print("="*60)
                self.inventory.append("bat guano")
                self.bat_defeated = True
                self.in_combat = False
                self.combat_enemy = None
                return
            
            # Bat counter-attacks
            self.bat_counterattack()
    
    def guardian_counterattack(self):
        """Guardian attacks the player"""
        guardian_damage = random.randint(1, 8)
        print(f"\n⚔️  The Guardian strikes back with his sword!")
        print(f"   The Guardian deals {guardian_damage} damage!")
        self.player_hp -= guardian_damage
        print(f"   Your HP: {max(0, self.player_hp)}/{self.player_max_hp}")
        
        if self.player_hp <= 0:
            print("\n" + "="*60)
            print("💀 YOU DIED 💀")
            print("="*60)
            print("\nThe guardian's blade proves too much for you.")
            print("Your vision fades as you collapse to the cold stone floor...")
            print("\nGAME OVER - You were slain by the guardian")
            self.running = False
            self.in_combat = False
    
    def bat_counterattack(self):
        """Bat attacks the player"""
        bat_damage = random.randint(0, 3)
        if bat_damage == 0:
            print(f"\n🦇 The bat swoops at you but misses!")
        else:
            print(f"\n🦇 The bat scratches you with its claws!")
            print(f"   The bat deals {bat_damage} damage!")
            self.player_hp -= bat_damage
            print(f"   Your HP: {max(0, self.player_hp)}/{self.player_max_hp}")
        
        if self.player_hp <= 0:
            print("\n" + "="*60)
            print("💀 YOU DIED 💀")
            print("="*60)
            print("\nThe bat's relentless attacks have overwhelmed you.")
            print("\nGAME OVER - You were killed by a bat")
            self.running = False
            self.in_combat = False
    
    def retreat(self):
        """Flee from combat"""
        if not self.in_combat:
            print("You're not in combat!")
            return
        
        print("\n" + "="*60)
        print("You retreat from combat!")
        print("="*60)
        
        if self.combat_enemy == 'guardian':
            print("You flee from the Guardian's Lair!")
            print("The guardian doesn't pursue you beyond his chamber.")
            print("Your HP and the guardian's HP remain as they were.")
            # Move back to warning chamber
            self.current_room = self.rooms['warning_chamber']
        elif self.combat_enemy == 'bat':
            print("You flee from the bat!")
            print("It returns to roosting with the others.")
            print("Your HP and the bat's HP remain as they were.")
            # Move back to previous room (stalactite forest or mushroom grove)
            self.current_room = self.rooms['stalactite_forest']
        
        self.in_combat = False
        self.combat_enemy = None
        self.current_room.describe()
    
    def win_game(self):
        """Player wins the game"""
        print(f"   Guardian HP: 0/20")
        print("\n" + "="*60)
        print("⚔️  VICTORY! ⚔️")
        print("="*60)
        print("\nWith a final, decisive blow, the guardian staggers backward!")
        print("His sword clatters to the ground as he falls to his knees.")
        print("'You... you have bested me...' he gasps, then collapses.")
        print("\nYou approach the massive treasure chest and throw it open.")
        print("Gold coins, precious gems, and ancient artifacts spill out,")
        print("glittering in the dim light!")
        print("\n" + "="*60)
        print("🏆 ✨ CONGRATULATIONS! YOU WIN! ✨ 🏆")
        print("="*60)
        print(f"\nYou have claimed the legendary treasure of the cave!")
        print(f"Final HP: {self.player_hp}/{self.player_max_hp}")
        self.running = False
        self.in_combat = False
    
    def take(self, item):
        """Pick up an item from the current room"""
        item = item.lower()
        
        # Check if item exists in current room
        for room_item in self.current_room.items:
            if item in room_item.lower():
                self.inventory.append(room_item)
                self.current_room.items.remove(room_item)
                print(f"You picked up the {room_item}.")
                
                # Special handling for the shield
                if "shield" in room_item.lower():
                    self.has_shield = True
                    self.player_max_hp += 5
                    self.player_hp += 5
                    print("The ancient shield feels surprisingly light and well-balanced!")
                    print(f"Your maximum hit points increased to {self.player_max_hp}!")
                    print(f"Current HP: {self.player_hp}/{self.player_max_hp}")
                
                return
        
        print(f"There is no {item} here.")
    
    def use(self, item):
        """Use an item from inventory"""
        item = item.lower()
        
        for inv_item in self.inventory:
            if item in inv_item.lower():
                # Special handling for bat guano (healing item)
                if "guano" in inv_item.lower():
                    if self.player_hp >= self.player_max_hp:
                        print(f"You're already at full health ({self.player_hp}/{self.player_max_hp})!")
                        print("You decide not to use the guano right now.")
                        return
                    
                    print(f"You cautiously consume the bat guano...")
                    print("Despite the awful taste, you feel reinvigorated!")
                    heal_amount = self.player_max_hp - self.player_hp
                    self.player_hp = self.player_max_hp
                    print(f"You healed {heal_amount} HP!")
                    print(f"Current HP: {self.player_hp}/{self.player_max_hp}")
                    self.inventory.remove(inv_item)
                    return
                else:
                    print(f"You can't use the {inv_item} right now.")
                    return
        
        print(f"You don't have a {item}.")
    
    def show_inventory(self):
        """Display the player's inventory"""
        if self.inventory:
            print(f"\nInventory: {', '.join(self.inventory)}")
        else:
            print("\nYour inventory is empty.")
    
    def show_status(self):
        """Display player's current status"""
        print("\n" + "="*60)
        print("PLAYER STATUS")
        print("="*60)
        print(f"Hit Points: {self.player_hp}/{self.player_max_hp}")
        print(f"Shield Equipped: {'Yes' if self.has_shield else 'No'}")
        
        # Show weapon status
        if "shiny dagger" in self.inventory:
            print("Weapon: Shiny Dagger (2-16 damage)")
        else:
            print("Weapon: Bare hands (1-4 damage)")
        
        # Show inventory
        if self.inventory:
            print(f"Inventory: {', '.join(self.inventory)}")
        else:
            print("Inventory: Empty")
        print("="*60)
    
    def show_help(self):
        """Display available commands"""
        print("\n" + "="*60)
        print("AVAILABLE COMMANDS")
        print("="*60)
        print("MOVEMENT:")
        print("  go <direction>    - Move in a direction")
        print("  <direction>       - Shortcut: north/south/east/west/up/down/forward/back")
        print("                      or n/s/e/w/u/d/f/b")
        print("\nCOMBAT:")
        print("  attack            - Attack with bare hands")
        print("  attack <weapon>   - Attack with a specific weapon (e.g., 'attack dagger')")
        print("  retreat           - Flee from combat")
        print("\nITEMS:")
        print("  take <item>       - Pick up an item")
        print("  use <item>        - Use an item from your inventory")
        print("  inventory (i)     - Show your inventory")
        print("\nINFORMATION:")
        print("  status (st)       - Show your hit points and equipment")
        print("  look (l)          - Look around the current room")
        print("  map               - Show the cave map")
        print("  help (h)          - Show this help message")
        print("\nGAME:")
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
        
        elif action in ['status', 'st', 'stats']:
            self.show_status()
        
        elif action in ['go', 'move', 'walk']:
            if len(parts) > 1:
                self.move(parts[1])
            else:
                print("Go where? Specify a direction (north, south, east, west).")
        
        elif action in ['north', 'south', 'east', 'west', 'n', 's', 'e', 'w', 'down', 'd', 'up', 'u', 'forward', 'f', 'back', 'b']:
            # Allow direct direction commands
            direction_map = {
                'n': 'north', 's': 'south', 'e': 'east', 'w': 'west',
                'd': 'down', 'u': 'up', 'f': 'forward', 'b': 'back'
            }
            direction = direction_map.get(action, action)
            self.move(direction)
        
        elif action in ['attack', 'a', 'fight', 'strike', 'hit']:
            if len(parts) > 1 and parts[1] in ['with', 'using']:
                # Attack with specific weapon: "attack with dagger"
                if len(parts) > 2:
                    weapon = ' '.join(parts[2:])
                    self.attack(weapon)
                else:
                    print("Attack with what weapon?")
            elif len(parts) > 1:
                # Attack with weapon: "attack dagger"
                weapon = ' '.join(parts[1:])
                self.attack(weapon)
            else:
                # Just "attack" - use bare hands
                self.attack()
        
        elif action in ['retreat', 'flee', 'run', 'escape']:
            self.retreat()
        
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
