# Fire Units for Ice Age Factions

## 🔥 **Design Philosophy**

Adding fire creatures to both ice factions creates compelling gameplay dynamics and thematic depth:

- **Thematic Tension**: Represents the eternal struggle between ice and fire, cold and warmth
- **Strategic Balance**: Provides counter-units to enemy ice abilities and pure ice strategies  
- **Narrative Richness**: Fire creatures can be allies, enemies, or neutral parties in different campaigns
- **Gameplay Variety**: Creates interesting tactical decisions about when to use fire vs ice units

---

## 🧊 **Ice Dwellers Fire Units** (2 Units)

### **🔥 Flame Wraith** ⭐
**Type**: Magical Fire Spirit  
**Theme**: Corrupted fire spirit bound to ice magic  
**Rarity**: Uncommon (Level 1)

**Lore**: Once pure fire elementals, these beings were corrupted by ancient ice magic and now serve the Ice Dwellers. They retain their fire powers but are bound by frost, creating internal conflict that makes them both powerful and unpredictable.

**Game Statistics**:
- **Level**: 1  
- **HP**: 26
- **Movement**: 6 (fly)
- **Cost**: 18
- **Alignment**: Noctis (strong during night, weak during day - represents corruption by ice)
- **Advances to**: Greater Flame Wraith

**Attacks**:
- **Fire Touch** (Melee): 7 fire damage × 3 attacks, magical
- **Burning Wail** (Ranged): 5 fire damage × 4 attacks, magical

**Resistances**: 
- Fire: -50% (weak to own element due to corruption)
- Cold: +20% (ice binding provides some protection)
- Physical: +50% (spectral nature)

**Special Abilities**:
- **Spectral**: Can pass through enemy units
- **Fire Aura**: Adjacent ice terrain melts after 2 turns
- **Corrupted Magic**: 10% chance attacks backfire and damage self

**Suggested Sprite**: Modified wraith with flickering flames instead of dark energy

---

### **🌋 Molten Guardian** ⭐
**Type**: Elite Fire Construct  
**Theme**: Ancient fire guardian enslaved by ice magic  
**Rarity**: Rare (Level 2)

**Lore**: Powerful constructs of living magma and stone, these guardians once protected ancient fire temples. Ice Dweller mages have learned to bind them with frost chains, forcing them to serve while causing them constant pain—making them extremely dangerous in combat.

**Game Statistics**:
- **Level**: 2
- **HP**: 48  
- **Movement**: 4
- **Cost**: 32
- **Alignment**: Twilight (balanced between fire and ice binding, strongest at transition times)
- **Advances to**: null (AMLA)

**Attacks**:
- **Molten Slam** (Melee): 12 fire damage × 2 attacks, slows target
- **Lava Burst** (Ranged): 8 fire damage × 3 attacks, area effect (hits adjacent hexes)

**Resistances**:
- Fire: +70% 
- Cold: -30% (vulnerable to ice binding)
- Physical: +40% (stone construction)

**Special Abilities**:
- **Molten Trail**: Leaves fire terrain that damages non-fire units (2 fire damage/turn)
- **Frost Chains**: Ice Dweller units within 2 hexes gain +10% accuracy (magical coordination)
- **Berserker Rage**: +25% damage when below 50% HP (pain from ice binding)

**Suggested Sprite**: Fire elemental with visible ice chains/crystals binding it

---

## ❄️ **Frost Clans Units** (3 Units: 2 Fire + 1 Ice Beast)

### **🔥 Flame Keeper**
**Type**: Human Fire Priest  
**Theme**: Tribal guardian of the sacred flame  
**Rarity**: Common (Level 1)

**Lore**: Every Frost Clan settlement maintains a sacred flame that must never be extinguished—it represents hope, warmth, and survival in the endless winter. Flame Keepers are the priests who tend these fires and have learned to channel their power in battle.

**Game Statistics**:
- **Level**: 1
- **HP**: 30
- **Movement**: 5  
- **Cost**: 16
- **Alignment**: Solaris-Noctis (draws power from sacred flames, strongest during day/night extremes)
- **Advances to**: Fire Shaman

**Attacks**:
- **Sacred Staff** (Melee): 6 impact damage × 2 attacks
- **Flame Bolt** (Ranged): 7 fire damage × 3 attacks, magical

**Resistances**:
- Fire: +20%
- Cold: +10% (accustomed to temperature extremes)

**Special Abilities**:
- **Sacred Flame**: Can create "warm hex" that heals fire-resistant units +3 HP/turn
- **Light Bearer**: Allied units within 2 hexes immune to fear effects
- **Fire Blessing**: Can grant one ally per battle +20% fire resistance for 3 turns

**Suggested Sprite**: Human priest with flaming staff, warm clothing with fire motifs

---

### **🐺 Fire Wolf** 
**Type**: Magical Beast  
**Theme**: Wolf spirit infused with flame magic  
**Rarity**: Uncommon (Level 1)

**Lore**: Rare wolves that have been touched by ancient fire magic, possibly from proximity to dragon lairs or fire spirit domains. Frost Clans consider them sacred animals and have learned to bond with them, seeing them as symbols of fierce survival.

**Game Statistics**:
- **Level**: 1
- **HP**: 28
- **Movement**: 7
- **Cost**: 15  
- **Alignment**: Twilight (mystical beast active during dawn/dusk hunting hours)
- **Advances to**: Greater Fire Wolf

**Attacks**:
- **Fire Bite** (Melee): 8 fire damage × 2 attacks
- **Howl** (Ranged): 4 fire damage × 2 attacks, causes fear

**Resistances**:
- Fire: +40%
- Cold: 0% (balanced nature)

**Special Abilities**:
- **Pack Hunter**: +15% damage when adjacent to allied Frost Clan units
- **Flame Trail**: Movement through snow/ice terrain melts it temporarily
- **Loyal Bond**: If Flame Keeper is within 3 hexes, gains +1 movement and regeneration

**Suggested Sprite**: Wolf with glowing ember fur and flame-colored eyes

---

### **🐻 Bear Rider** ⭐ *[NEWLY IMPLEMENTED]*
**Type**: Human Heavy Cavalry  
**Theme**: Sacred bond between warrior and ice bear  
**Rarity**: Elite (Level 1)

**Lore**: The ultimate achievement in Frost Clans culture - a warrior who has earned the sacred bond with one of the great ice bears. These partnerships create legendary shock troops who embody the spirit of arctic survival and primal power.

**Game Statistics**:
- **Level**: 1
- **HP**: 42
- **Movement**: 4 (slow but powerful)
- **Cost**: 22
- **Alignment**: Neutral (represents balance between human and beast)
- **Advances to**: Dire Bear Rider

**Attacks**:
- **War Axe** (Melee): 11 blade damage × 2 attacks, charge special
- **Bear Claws** (Melee): 8 blade damage × 3 attacks

**Resistances**:
- Cold: +20% (adapted to frozen climate)
- Pierce: -20% (vulnerable to spears due to size)

**Special Abilities**:
- **Snow Camouflage**: Can hide in frozen terrain (invisible unless adjacent)
- **Terrain Master**: Excellent movement in ice and forest (1 MP cost)
- **Cannot Cross Deep Water**: Limited to shallow water crossings

**Suggested Sprite**: Warrior in fur armor mounted on massive ice bear

**Implementation Status**: ✅ **COMPLETED** - Fully implemented in WML with custom bear_mounted movement type

---

## ⚖️ **Balance Integration**

### **Existing Wesnoth Fire Units to Reference**
Based on Wesnoth's Drake faction, these units exist and can serve as statistical references:

1. **Drake Burner** - Fire-breathing flying unit (can reference for fire breath mechanics)
2. **Drake Fighter** - Melee fire unit (can reference for fire melee attacks)  
3. **Fire Elemental** - Pure fire magical unit (if it exists in core)
4. **Salamander** - Fire creature (if available in bestiary)

### **Fire Unit Integration Strategy**

**Recruitment Balance**:
- Fire units cost 10-15% more than equivalent ice units (representing rarity)
- Limited to 1-2 fire units per faction initially  
- Can be recruited from special buildings (Fire Shrine, Sacred Hearth)

**Campaign Integration**:
- **Early Campaigns**: Fire units are rare, expensive allies
- **Mid Campaigns**: Players can choose ice or fire strategies 
- **Late Campaigns**: Fire/ice balance becomes crucial for defeating final enemies

**Multiplayer Balance**:
- Fire units counter ice abilities but are vulnerable to cold attacks
- Create rock-paper-scissors dynamic: Fire > Ice > Physical > Fire

### **Counter-Play Matrix**

| **Fire Unit** | **Weak Against** | **Strong Against** | **Neutral** |
|---------------|------------------|-------------------|-------------|
| Flame Wraith | Cold magic, exorcism | Ice units, physical resistance | Other fire units |
| Molten Guardian | Ice/cold attacks, magic dispel | Physical attacks, ice terrain | Fire magic |
| Flame Keeper | Cold damage, anti-magic | Ice effects, fear effects | Physical combat |
| Fire Wolf | Ice attacks, ranged combat | Ice units, pack tactics | Solo combat |

---

## 🎮 **Implementation Priority**

### **Phase 1: Basic Implementation**
1. **Flame Keeper** - Essential for Frost Clans fire strategy
2. **Flame Wraith** - Core Ice Dwellers fire unit

### **Phase 2: Enhanced Experience**  
3. **Fire Wolf** - Adds tactical variety to Frost Clans
4. **Molten Guardian** - Elite option for Ice Dwellers

### **Phase 3: Advanced Features**
- Fire/ice terrain interactions
- Advanced fire abilities (Warm Aura, Fire Shield, etc.)
- Cross-faction fire unit recruitment in special scenarios

---

## 🔧 **Technical Implementation Notes**

### **Required WML Additions**
```
# New unit files needed:
units/frost_clans_fire.cfg    # Flame Keeper, Fire Wolf  
units/ice_dwellers_fire.cfg   # Flame Wraith, Molten Guardian

# Updated faction files:
factions/frost_clans.cfg      # Add fire unit recruitment
factions/ice_dwellers.cfg     # Add fire unit recruitment
```

### **Art Assets Needed**
- 4 new unit sprites (or adaptations of existing fire units)
- Fire effect animations
- Unit portraits for key characters
- Fire terrain effects (warm hexes, molten trails)

### **Campaign Integration**
- Update scenarios to include fire unit recruitment options
- Add fire vs ice tactical scenarios  
- Create story elements explaining fire unit presence
- Design special maps with fire/ice terrain interactions

This design adds strategic depth while maintaining thematic coherence—fire units represent hope, survival tools, and the eternal struggle against the endless winter, rather than breaking the ice age theme.