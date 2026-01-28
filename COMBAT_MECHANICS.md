# Combat Mechanics - Technical Details

## Overview
The final battle with the Guardian uses a turn-based combat system implemented in Python with random damage rolls.

## Combat Statistics

### Player Stats
- **Base Hit Points**: 10
- **With Ancient Shield**: 15 HP (+5 bonus applied when shield is picked up)
- **Bare Hands Damage**: random.randint(1, 4) per hit
- **Shiny Dagger Damage**: random.randint(2, 16) per hit

### Guardian Stats
- **Hit Points**: 20 (fixed)
- **Damage**: random.randint(1, 8) per hit
- **Always attacks first** each round

## Combat Flow

1. **Combat Initiation**: Triggered automatically when entering Guardian's Lair
2. **Status Display**: Shows initial HP, weapon, and shield status
3. **Round Loop**: Continues while both combatants have HP > 0
   - Guardian attacks first
   - Damage is calculated and applied
   - Check if player died
   - Player attacks second  
   - Damage is calculated and applied
   - Check if guardian died
   - Prompt user to press Enter for next round
4. **Victory/Defeat**: Appropriate ending message displayed

## Combat Round Example

```
------------------------------------------------------------
ROUND 1
------------------------------------------------------------

⚔️  The Guardian attacks with his sword!
   The Guardian deals 5 damage!
   Your HP: 10/15

🗡️  You strike with your shiny dagger!
   You deal 12 damage!
   Guardian HP: 8/20

[Press Enter to continue to next round...]
```

## Probability Analysis

### Average Damage Per Hit
- Guardian: (1+8)/2 = 4.5 damage
- Player (bare hands): (1+4)/2 = 2.5 damage
- Player (dagger): (2+16)/2 = 9 damage

### Expected Rounds to Victory

**With Dagger Only (10 HP)**:
- Guardian needs: 10/4.5 ≈ 2.2 hits to kill you
- You need: 20/9 ≈ 2.2 hits to kill guardian
- Guardian attacks first, so roughly 50/50 chance

**With Dagger + Shield (15 HP)**:
- Guardian needs: 15/4.5 ≈ 3.3 hits to kill you  
- You need: 20/9 ≈ 2.2 hits to kill guardian
- Much better odds - you can take 1 more hit than guardian

**Without Dagger (bare hands)**:
- You need: 20/2.5 = 8 hits to kill guardian
- Guardian needs: ~2-3 hits to kill you
- Nearly impossible to win

## Code Implementation

```python
# Combat loop structure
combat_round = 1
while self.player_hp > 0 and self.guardian_hp > 0:
    # Guardian attacks
    guardian_damage = random.randint(1, 8)
    self.player_hp -= guardian_damage
    
    if self.player_hp <= 0:
        # Player death
        return
    
    # Player attacks
    if has_dagger:
        player_damage = random.randint(2, 16)
    else:
        player_damage = random.randint(1, 4)
    
    self.guardian_hp -= player_damage
    
    if self.guardian_hp <= 0:
        # Victory
        return
    
    combat_round += 1
    input("\n[Press Enter to continue...]")
```

## Items and Their Effects

### Shiny Dagger
- **Location**: The Arsenal
- **Effect**: Changes damage from 1-4 to 2-16
- **Impact**: ~3.6x damage increase (average)
- **Essential**: Yes - nearly impossible to win without it

### Ancient Shield  
- **Location**: The Forgotten Shrine
- **Effect**: +5 maximum HP (10 → 15) and immediate heal to new max
- **Impact**: Can take 1 more hit from guardian on average
- **Essential**: No, but highly recommended

## Balance Notes

The combat system is intentionally:
- **Simple**: Easy to understand
- **Luck-based**: RNG adds replayability
- **Strategic**: Rewards exploration and preparation
- **Forgiving with prep**: Both items make victory likely
- **Punishing without prep**: No items = almost certain death

The guardian attacking first balances the player's higher max damage range with the dagger.

## Design Philosophy

1. **Exploration is rewarded**: Finding both items significantly improves your odds
2. **Risk vs Reward**: Players can try with just one item if they're brave
3. **Not guaranteed**: Even with both items, bad RNG can lead to defeat
4. **Replayable**: Random damage means each fight is different
5. **Clear feedback**: Damage numbers and HP shown each round
