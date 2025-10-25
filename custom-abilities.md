# Ice Age - Custom Abilities Reference

## Overview

This document defines all custom abilities created for the Ice Age expansion, providing unique tactical options and thematic depth to both the Frost Clans and Ice Dwellers factions.

---

## 🧊 **Ice Dwellers Abilities**

### **❄️ Glacial Aura** ⭐ *SIGNATURE ABILITY*
**Type**: Passive Environmental Ability  
**Theme**: Gradual ice formation and territorial control  
**Rarity**: Epic (Level 3+ units only)

**Description**: The unit's ancient connection to winter itself allows them to gradually freeze surrounding waters, reshaping the battlefield to their advantage. This is the Ice Dwellers' most iconic and strategically powerful ability.

**Mechanics**:
- **Activation**: Unit must remain stationary for 1 full turn (no movement, no attacks)
- **Effect Range** (Progressive scaling):
  - **Level 1 Units**: 2-tile radius (basic ice magic)
  - **Level 2 Units**: 3-tile radius (developing power)
  - **Level 3+ Units**: 5-tile radius (mastery)
- **Transformation Process**:
  - Turn 1: Unit remains still → Aura charges (visual effect begins)
  - Turn 2: Water tiles show "freezing" animation → 50% frozen, units that step into that tile will break the ice and fall.
  - Turn 3: Complete transformation → Water becomes traversable ice
- **Duration**: Permanent until scenario end or specific destruction
- **Ice Properties**: 
  - +20% movement for Ice Dwellers units
  - -10% movement for fire-based units
  - Can be shattered by fire attacks (reverts to water) and by Warm Aura.
  - Reveals any hidden unit, even on land if stationed close to a tile with a hidden unit, the hidden unit will be found
- **Cancellation**: Any unit action stops the charging process

**Strategic Impact**:
- **Tactical Control**: Creates new pathways and blocks enemy routes
- **Territorial Advantage**: Establishes "ice domain" areas
- **Risk/Reward**: Powerful but requires vulnerable positioning
- **Late Game Power**: Becomes increasingly dominant with higher level units

**Balance Considerations**:
- **Counterplay**: Fire magic and certain attacks can destroy created ice
- **Positioning Risk**: Unit must remain stationary and vulnerable
- **Resource Cost**: Should be on expensive, high-level units only

**Suggested Units**: Frost Lord, Ancient Ice Elemental, Glacier Shaper (new unit)

---

### **🌨️ Freeze Attack**
**Type**: Special Attack Ability  
**Theme**: Temporary movement impairment  

**Description**: Target enemy unit becomes frozen, reducing movement capability for the next turn.

**Mechanics**:
- **Trigger**: On successful melee or ranged attack
- **Effect**: Target loses 50% movement points next turn
- **Duration**: 1 turn only
- **Resistance**: Units with fire resistance have 25% chance to avoid effect
- **Stacking**: Multiple freeze effects do not stack

**Strategic Impact**:
- Disrupts enemy positioning and retreat options
- Enables follow-up attacks by allied units
- Particularly effective against fast-moving enemies

**Suggested Units**: Ice Elemental, Frost Wraith, Glacial Guard

---

### **🩸 Vampire Aura** ⭐ *SIGNATURE ABILITY*
**Type**: Passive Environmental Enhancement Ability  
**Theme**: Ancient blood magic and life force manipulation  
**Rarity**: Epic (Level 3+ dark mages only)
**Faction**: **Ice Dwellers** (Exclusive - Dark magic specialists)

**Description**: Drawing upon forbidden knowledge from the darkest depths of winter magic, the unit emanates an unholy aura that enhances nearby melee fighters with vampiric properties. This represents the corruption aspect of ice magic, where the endless hunger of winter transforms warriors into creatures that feed on their enemies' life force.

**Mechanics**:
- **Activation Process** (Similar to Glacial Aura):
  - **Turn 1**: Unit must remain stationary (no movement, no attacks) → Aura begins charging
  - **Turn 2**: Dark energy builds → Visual crimson mist effect around unit
  - **Turn 3**: Full activation → Vampire Aura spreads to affect nearby allies
- **Effect Range** (Progressive scaling like Glacial Aura):
  - **Level 3 Units**: 2-tile radius (basic dark magic)
  - **Level 4 Units**: 3-tile radius (growing power)
  - **Level 5+ Units**: 4-tile radius (mastery of blood magic)
- **Target Units**: **Only melee units** within range (ranged units unaffected)
- **Enhancement Effects**:
  - **Life Drain**: Melee attacks heal attacker for 25% of damage dealt
  - **Blood Thirst**: +10% accuracy on melee attacks
  - **Vampiric Strength**: +15% melee damage
  - **Death Empowerment**: Killing an enemy with melee grants +1 movement for 2 turns
- **Duration**: Permanent until scenario end or aura caster dies/moves
- **Vulnerability**: 
  - Holy/light magic dispels aura entirely
  - Fire attacks reduce aura range by 1 tile per hit on caster
  - Undead units gain double benefits but become uncontrollable for 1 turn after kills
- **Cancellation**: Any unit action by caster stops the charging process

**Strategic Impact**:
- **Melee Superiority**: Transforms melee units into self-sustaining fighters
- **Aggressive Positioning**: Encourages front-line engagement over defensive tactics
- **Risk/Reward**: Powerful enhancement but requires vulnerable 3-turn setup
- **Formation Fighting**: Rewards keeping melee units clustered around aura caster
- **Late Game Dominance**: High-level casters create devastating melee death squads

**Balance Considerations**:
- **Setup Vulnerability**: 3-turn activation makes caster extremely vulnerable
- **Melee Limitation**: Only affects melee units, leaving ranged units unenhanced
- **Holy Counter**: Light magic completely negates the aura
- **Positioning Risk**: Caster must stay stationary and exposed to maintain effect
- **Moral Corruption**: Enhanced units may suffer morale penalties vs holy units

**Faction Thematic Integration**:
- Represents the darker, more desperate side of Ice Dweller magic
- Shows the corruption that extreme cold and isolation can bring
- Creates internal faction tension between "pure" ice magic and blood magic
- Reflects the theme of survival at any cost during the endless winter

**Suggested Units**:
- **Frost Necromancer** - Level 3 dark mage, basic 2-tile aura
- **Blood Ice Shaman** - Level 4 corrupted spellcaster, 3-tile range
- **Vampire Lord of Winter** - Level 5 legendary unit, 4-tile aura + additional dark abilities
- **Ancient Death Caller** - Special recruitment, aura affects undead allies as well

**Visual & Audio Design**:
- **Charging Phase**: Dark red energy swirling around caster, getting more intense each turn
- **Active Aura**: Crimson mist emanating outward, affected melee units gain red-tinted weapons
- **Life Drain Effect**: Red energy streams from victims to attackers during combat
- **Audio**: Low, ominous humming during charging, satisfied whispers when life is drained

**Advanced Tactical Considerations**:
- **Undead Synergy**: Works exceptionally well with undead melee units (skeleton warriors, etc.)
- **Formation Strategy**: Best used with heavy infantry formations and berserkers
- **Counter-Strategy**: Enemies will prioritize disrupting the 3-turn setup phase
- **Scenario Integration**: Particularly powerful in prolonged siege battles or survival scenarios

---

### **❄️ Winter's Blessing** ⭐ *SIGNATURE ABILITY*
**Type**: Area Support Active Ability  
**Theme**: Divine protection of winter spirits  
**Rarity**: Rare (Spiritual leader units only)
**Faction**: **Ice Dwellers** (Primary), **Frost Clans** (Limited access)

**Description**: Drawing upon the ancient pact between their people and the winter spirits, the unit channels protective magic that grants ongoing healing and enhanced focus to nearby allies. This blessing represents the spiritual core of ice-dweller society and their connection to the eternal winter.

**Mechanics**:
- **Activation**: Active ability with 2-8 turn random cooldown (average 5 turns)
- **Range**: 2-tile radius around caster
- **Target**: All allied units within range (including self)
- **Duration Management**:
  - **Base Duration**: 3-8 blessing turns applied randomly per cast
  - **Maximum Stack**: 8 blessing turns per unit
  - **Proximity Bonus**: Units remaining within 1 tile of blessing caster gain +1 blessing turn each round (up to max)
  - **Separation Penalty**: Units moving >3 tiles away lose remaining blessing turns
- **Blessing Effects (Per Turn)**:
  - **Healing**: +2 HP regeneration
  - **Accuracy**: +5% attack accuracy  
  - **Morale**: Immunity to fear and routing effects
  - **Spiritual Protection**: +10% resistance to dark magic/undead attacks
- **Special Interactions**:
  - **Poison Cure**: Removes poison effect but consumes 4 blessing turns
  - **Curse Resistance**: Blessing turns protect against curses (1 turn consumed per curse blocked)
  - **Dispel Vulnerability**: Fire-based dispel magic removes all blessing turns

**Strategic Impact**:
- **Formation Fighting**: Rewards keeping blessed units near the blessing caster
- **Sustained Engagements**: Makes prolonged battles more favorable
- **Support Role**: Creates valuable high-priority support units
- **Tactical Positioning**: Players must balance staying near caster vs tactical positioning
- **Resource Management**: Limited uses require careful timing

**Balance Considerations**:
- **Range Limitation**: Must stay relatively close to maintain full benefits
- **Random Cooldown**: Prevents predictable ability cycling
- **Fire Vulnerability**: Clear counterplay through dispel magic
- **High-Value Target**: Blessing casters become priority targets for enemies
- **Formation Requirement**: Breaking formation reduces effectiveness

**Faction Assignment & Suggested Units**:

**Ice Dwellers** (Primary Users):
- **Winter Priestess** - Level 2 support caster, 4-tile blessing range
- **Frost Oracle** - Level 3 spiritual leader, enhanced blessing duration
- **Ancient Shrine Keeper** - Level 4 temple guardian, can bless twice per battle
- **Glacial Hierophant** - Legendary unit, blessing affects all allied units on map

**Frost Clans** (Limited Access):
- **Clan Spiritcaller** - Level 3 rare unit, shorter blessing duration but stronger proximity bonus  
- **Elder Shaman** - Level 4 tribal leader, blessing grants +1 movement instead of accuracy
- **Ancestor Speaker** - Special recruitment, blessing also grants +10% experience gain

**Visual & Audio Design**:
- **Casting Animation**: Ethereal snowflakes and soft blue light emanating from caster
- **Blessed Units**: Subtle aurora-like shimmer around affected units
- **Audio**: Gentle wind chimes and whispered blessings in ancient tongue
- **Proximity Indicator**: Glowing connection lines between caster and nearby blessed units

**Advanced Tactical Considerations**:
- **Blessing Chains**: Multiple blessing casters can overlap effects but not duration
- **Formation Tactics**: Best used with defensive formations or slow-moving heavy units
- **Priority Targeting**: Enemies will focus fire on blessing casters
- **Scenario Integration**: Particularly powerful in siege defense or survival scenarios


### **🌪️ Blizzard Call** ⭐ *SIGNATURE ABILITY*
**Type**: Area Effect Active Ability  
**Theme**: Weather manipulation and battlefield control  
**Rarity**: Epic (High-level spellcasters only)

**Description**: The unit summons a localized blizzard that affects a large area, providing tactical advantages to ice units while hindering enemies.

**Mechanics**:
- **Activation**: Active ability, 2-turn cooldown
- **Range**: 4-tile radius centered on target location (not unit)
- **Effect Duration**: 3 turns
- **Area Effects**:
  - **Visibility**: Reduced to 2 tiles for all units in area
  - **Movement**: -1 movement point for non-ice units
  - **Accuracy**: -15% ranged attack accuracy
  - **Ice Unit Bonuses**: +10% damage, +5% accuracy for ice units
- **Casting Requirements**: Unit must not have moved this turn
- **Mana Cost**: High (if using mana system) or scenario limitation

**Strategic Impact**:
- **Area Denial**: Makes zones dangerous for enemy advancement
- **Tactical Support**: Enhances allied ice units in the storm
- **Vision Control**: Limits enemy reconnaissance and targeting
- **Positioning Tool**: Forces enemy repositioning or tactical adaptation

**Balance Considerations**:
- **Limited Uses**: Once or twice per scenario maximum
- **Self-Affecting**: Caster also experiences reduced visibility
- **Counterplay**: Fire magic can dispel early or reduce effects

**Suggested Units**: Frost Archmagus, Storm Caller, Winter Shaman

---

### **🧊 Ice Shield**
**Type**: Defensive Active Ability  
**Theme**: Crystalline barrier protection  
**Rarity**: Common (Available to multiple unit types)

**Description**: Unit creates a protective ice barrier that absorbs incoming damage and provides temporary defensive bonuses.

**Mechanics**:
- **Activation**: Manual ability, once per battle
- **Duration**: 4 turns or until shield is depleted
- **Shield Points**: 15-25 HP equivalent (varies by unit level)
- **Effects While Active**:
  - Absorbs damage before affecting unit HP
  - +10% resistance to physical attacks
  - -20% resistance to fire attacks (vulnerability)
  - Visual: Shimmering ice crystal overlay
  - Inmune to poison and curse attacks.
  - **Depletion**: Shield breaks when damage absorbed exceeds limit
  - **Fire Weakness**: Fire damage counts as 2x against shield points

**Strategic Impact**:
- **Engagement Tool**: Enables aggressive positioning
- **Resource Management**: Players must time activation carefully
- **Risk/Reward**: Strong vs physical, weak vs fire
- **Visual Feedback**: Clear indication of defensive state

**Suggested Units**: Ice Guardian, Glacial Defender, Frost Knight

---

### **❄️ Frostbite**
**Type**: Damage Over Time Ability  
**Theme**: Persistent cold damage  

**Description**: Inflicts ongoing cold damage that weakens enemies over multiple turns.

**Mechanics**:
- **Trigger**: On successful attack with cold damage
- **Effect**: Target takes 3-5 cold damage at start of each turn
- **Duration**: 3 turns or until healed
- **Healing**: Regeneration, healing abilities, or fire damage removes effect
- **Resistance**: Fire-resistant units take half duration
- Defense precision reduced 10%

**Strategic Impact**:
- Weakens enemies for future engagements
- Forces opponents to seek healing or retreat
- Synergizes with hit-and-run tactics

**Suggested Units**: Frost Archer, Ice Stalker, Winter Wolf

---

### **🛡️ Ice Armor**
**Type**: Defensive Ability  
**Theme**: Crystalline protective barrier  

**Description**: Unit gains temporary defensive bonus by forming protective ice crystals around itself.

**Mechanics**:
- **Activation**: Manual ability, usable once per scenario
- **Effect**: +20% resistance to physical attacks for 4 turns
- **Visual**: Unit gains shimmering ice crystal overlay
- **Vulnerability**: Fire attacks deal +25% damage while active
- **Cooldown**: Cannot be used again in same scenario or until the unit levels up.

**Strategic Impact**:
- Enables aggressive positioning in dangerous situations
- Trades fire vulnerability for physical protection
- Tactical timing becomes crucial for maximum effectiveness

**Suggested Units**: Frost Champion, Glacial Warrior, Ice Guardian

---

## ⚔️ **Frost Clans Abilities**

### **🏔️ Arctic Survival**
**Type**: Terrain-Based Passive  
**Theme**: Adaptation to harsh winter conditions  

**Description**: Frost Clan units gain bonuses when fighting in their natural cold environment.

**Mechanics**:
- **Trigger**: Unit positioned on snow, ice, or frozen terrain
- **Effects**:
  - +10% damage bonus on cold terrain
  - +5% accuracy bonus on ice/snow
  - Cold resistance increases by 10%
  - Regeneration +2 HP per turn on snow tiles
- **Duration**: Continuous while on appropriate terrain

**Strategic Impact**:
- Encourages territorial control of winter terrain
- Makes Frost Clans stronger defenders of their homeland
- Creates terrain-based tactical decisions

**Suggested Units**: All Frost Clan units (faction-wide ability)

---

### **🐺 Pack Tactics**
**Type**: Cooperative Combat Ability  
**Theme**: Coordinated hunting and warfare  

**Description**: Units fight more effectively when positioned near allied units, reflecting their tribal cooperation.

**Mechanics**:
- **Trigger**: Unit has 2+ allied units within 2 tiles
- **Effects**:
  - +15% damage when flanking enemies with allies
  - +10% accuracy when attacking same target as ally
  - Shared experience: 25% of XP gained goes to nearby allies
- **Range**: 2-tile radius for ally detection

**Strategic Impact**:
- Rewards keeping units together in formations
- Encourages coordinated attacks on priority targets
- Balances against spreading forces too thin

**Suggested Units**: Frost Warrior, Clan Hunter, Frost Champion

---

### **🔥 Last Stand**
**Type**: Desperate Combat Ability  
**Theme**: Fighting fiercely when cornered  

**Description**: When severely wounded, Frost Clan units fight with desperate fury.

**Mechanics**:
- **Trigger**: Unit drops below 25% health
- **Effects**:
  - +30% damage output
  - +20% accuracy
  - Immune to fear and routing effects
  - Cannot retreat from combat
- **Duration**: Until healed above 25% or unit dies

**Strategic Impact**:
- Makes wounded units dangerous rather than just vulnerable
- Creates dramatic comeback potential in battles
- Adds risk/reward to focusing fire on single targets

**Suggested Units**: Frost Berserker, Clan Chieftain, Veteran units

---

### **🏹 Hunter's Mark** ⭐ *SIGNATURE ABILITY*
**Type**: Target Designation Active Ability  
**Theme**: Tribal hunting expertise and coordination  
**Rarity**: Rare (Specialized hunter units)

**Description**: Drawing on generations of hunting experience, the unit marks a target for coordinated attack, making it vulnerable to the entire clan's assault.

**Mechanics**:
- **Activation**: Active ability targeting enemy unit within 4 tiles
- **Duration**: 3 turns or until target dies
- **Effects on Marked Target**:
  - -10% dodge chance against all Frost Clan attacks
  - +15% damage from all Frost Clan ranged attacks
  - +5% critical hit chance for Frost Clan units
  - Marked target visible through fog of war
- **Limitations**: Only one mark active per Hunter unit
- **Visual**: Target gains distinctive hunter's mark overlay

**Strategic Impact**:
- **Focus Fire**: Encourages concentrated attacks on priority targets
- **Intelligence**: Provides reconnaissance through mark visibility
- **Coordination**: Rewards tactical cooperation between clan units
- **Threat Prioritization**: Players must decide which enemy to mark

**Balance Considerations**:
- **Range Limitation**: Must get relatively close to mark targets
- **Single Target**: Can't mark multiple enemies simultaneously
- **Counterplay**: Healing or certain abilities can remove marks

**Suggested Units**: Clan Hunter, Frost Tracker, Elite Scout

---

### **🔥 Survival Instinct**
**Type**: Adaptive Passive Ability  
**Theme**: Hardy northern resilience and adaptation  
**Rarity**: Common (Frost Clan racial trait)

**Description**: Years of surviving in harsh conditions have taught the Frost Clans to adapt quickly to threats and recover from injuries more effectively.

**Mechanics**:
- **Trigger**: Automatic when unit takes damage
- **Adaptation System**:
  - After taking fire damage: +10% fire resistance for 2 turns
  - After taking cold damage: +15% cold resistance for 2 turns
  - After taking physical damage: +5% dodge for 2 turns
  - After taking magical damage: +10% magic resistance for 2 turns
- **Stacking**: Multiple damage types can trigger multiple adaptations
- **Cooldown**: Each adaptation type has 3-turn cooldown
- **Healing Bonus**: +2 HP regeneration per turn when below 50% health

**Strategic Impact**:
- **Survivability**: Makes Frost Clan units increasingly durable in prolonged fights
- **Adaptation Reward**: Benefits from diverse enemy damage types
- **Tactical Consideration**: Enemies must consider adaptation when choosing attacks
- **Endurance Fighting**: Supports Frost Clan's defensive nature

**Suggested Units**: All Frost Clan units (faction-wide passive)

---

### **⚡ Berserker Fury**
**Type**: Escalating Combat Ability  
**Theme**: Northern warrior battle rage  
**Rarity**: Uncommon (Warrior specialists)

**Description**: As battle intensifies, the warrior enters a state of controlled fury, becoming increasingly dangerous but also more reckless.

**Mechanics**:
- **Trigger**: Each kill or assist increases fury level (Max: 3 stacks)
- **Fury Effects per Stack**:
  - +20% damage output
  - +10% attack speed (extra attack chance)
  - -5% accuracy (growing recklessness)
  - -10% defense (abandoning caution)
- **Duration**: Fury stacks persist until end of scenario or unit dies
- **Cooling Down**: Losing 25% HP removes one fury stack
- **Visual**: Increasingly intense red aura with more stacks

**Strategic Impact**:
- **Snowball Potential**: Successful warriors become increasingly powerful
- **Risk Management**: High damage but increasing vulnerability
- **Positioning Critical**: Furious units become glass cannons
- **Tactical Trade-offs**: Power vs survivability decisions

**Balance Considerations**:
- **Fragility Increase**: Easier to kill as fury grows
- **Accuracy Penalty**: May miss crucial attacks when furious
- **Stack Loss**: Damage taken can reduce effectiveness

**Suggested Units**: Frost Berserker, Clan Warrior, Battle-Scarred Veteran

---


## 🌍 **Environmental Abilities**

### **🌨️ Weather Mastery** (Potential Future Implementation)
**Type**: Map-Wide Effect  
**Theme**: Control over winter weather patterns  

**Description**: Certain powerful units can influence weather conditions across the battlefield.

**Mechanics**:
- **Activation**: Powerful spellcaster units only
- **Effects**: Change weather to blizzard, clear, or fog
- **Duration**: 5-8 turns depending on unit level
- **Impact**: Affects visibility, movement, and damage types

**Suggested Units**: Frost King, Ancient Ice Lord, Weather Shaman

---

### **❄️ Terrain Transformation** (Advanced Feature)
**Type**: Permanent Map Alteration  
**Theme**: Reshaping the battlefield  

**Description**: Extremely powerful units can permanently alter terrain types.

**Mechanics**:
- **Requirements**: Level 4+ units, specific spell abilities
- **Effects**: Convert grass→snow, shallow water→ice, etc.
- **Limitations**: 1-2 tiles per scenario maximum
- **Strategy**: Creates permanent tactical advantages

**Suggested Units**: Archlich of Winter, Primordial Ice Elemental

---

## 🎯 **Ability Design Philosophy**

### **Faction Identity Matrix**

| **Ice Dwellers** | **Frost Clans** |
|------------------|------------------|
| **Theme**: Ancient magic, environmental control | **Theme**: Survival, adaptation, cooperation |
| **Playstyle**: Territorial, defensive, powerful | **Playstyle**: Mobile, aggressive, coordinated |
| **Signature**: Glacial Aura (terrain control) | **Signature**: Hunter's Mark (coordination) |
| **Secondary**: Blizzard Call, Ice Shield | **Secondary**: Survival Instinct, Berserker Fury |
| **Weakness**: Fire magic, mobility requirements | **Weakness**: Individual unit power, magic resistance |

### **Ability Complexity Tiers**

#### **🟢 Tier 1 - Simple Abilities** (Easy to understand and use)
- **Freeze Attack**: Basic debuff on hit
- **Arctic Survival**: Passive terrain bonuses
- **Survival Instinct**: Automatic damage adaptation
- **Ice Shield**: Simple active defense

#### **🟡 Tier 2 - Moderate Abilities** (Require tactical thinking)
- **Frostbite**: Damage over time management
- **Pack Tactics**: Positioning coordination
- **Hunter's Mark**: Target prioritization
- **Ice Armor**: Timing and risk assessment
- **Winter's Blessing**: Formation management and support timing

#### **🔴 Tier 3 - Complex Abilities** (Advanced strategic depth)
- **Glacial Aura**: Multi-turn setup and positioning
- **Vampire Aura**: Multi-turn setup with formation management and risk assessment
- **Blizzard Call**: Area control and timing
- **Berserker Fury**: Risk/reward escalation
- **Last Stand**: Desperate tactical decisions

### **Counterplay Design**

| **Ability** | **Primary Counter** | **Secondary Counter** | **Situational Counter** |
|-------------|---------------------|----------------------|------------------------|
| Glacial Aura | Fire attacks break ice | Force movement/repositioning | Fast cavalry raids |
| Vampire Aura | Holy/light magic dispel | Interrupt 3-turn setup | Ranged unit focus fire |
| Winter's Blessing | Fire-based dispel magic | Kill the blessing caster | Force unit separation |
| Freeze Attack | Fire resistance | High mobility units | Regeneration abilities |
| Hunter's Mark | Kill the Hunter | Stealth/invisibility | Healing removes marks |
| Blizzard Call | Fire magic dispel | Wait it out | Underground movement |
| Ice Shield | Fire damage (2x effect) | Sustained damage | Piercing attacks |
| Berserker Fury | Focus fire on furious units | Defensive positioning | Patience (let them burn out) |

## 🔧 **Implementation Guidelines**

### **Balance Considerations**
- **Power Budget**: Each faction should have roughly equal total power, distributed differently
- **Counterplay**: Every ability must have at least 2 viable counters
- **Complexity Scaling**: Simple abilities on common units, complex abilities on rare units
- **Thematic Coherence**: All abilities must reinforce faction identity and campaign themes
- **Interactive Design**: Abilities should create interesting decisions for both players

### **Visual Design**
- Glacial Aura: Spreading crystalline effect from unit outward
- Freeze: Target unit gains blue-tinted overlay with ice crystals
- Frostbite: Periodic blue damage numbers with snowflake particles
- Ice Armor: Shimmering ice shell around unit model

### **Audio Cues**
- Glacial Aura: Subtle crackling ice sound when activating
- Freeze: Sharp ice formation sound on successful hit
- Frostbite: Periodic cold wind whistle while active
- Arctic Survival: Ambient wind sounds on snow terrain

### **Coding Priority**
1. **High Priority**: Glacial Aura, Freeze Attack, Arctic Survival
2. **Medium Priority**: Frostbite, Pack Tactics, Ice Armor  
3. **Low Priority**: Last Stand, Weather effects
4. **Future Features**: Terrain Transformation, advanced weather

---

## 📚 **Lore Integration**

Each ability draws from the established ice mythology:
- **Glacial Aura**: Reflects the slow, inevitable spread of ice age
- **Freeze/Frostbite**: Echoes Norse concepts of binding winter
- **Arctic Survival**: Represents human adaptation to Fimbulwinter
- **Pack Tactics**: Mirrors clan-based survival strategies
- **Ice Armor**: Channels protective magic of ice spirits

These abilities create a cohesive mechanical and thematic experience that reinforces the campaign's core themes of survival, adaptation, and the power of winter magic.

---

## 🌟 **Supporting Abilities**

### **🧊 Cold Walking** *(Passive - Tier 1)*

**Who Gets It**: Ice Dweller scouts, some Frost Clan rangers

**Mechanics**:
- Move through frozen water hexes with no movement penalty
- Cannot slip on ice terrain (immune to ice-based movement debuffs)
- +10% dodge chance on snow/ice terrain

**Strategic Impact**: 
- Enhanced mobility on transformed terrain created by Glacial Aura
- Natural synergy with ice-creating abilities
- Provides tactical flanking routes others cannot use

**Balance Notes**: 
- Limited to specific terrain types
- Defensive bonus is modest
- Requires ice terrain to be fully effective

---

### **🔥 Thermal Sense** *(Passive - Tier 1)*

**Who Gets It**: Frost Clan hunters, Ice Dweller seers

**Mechanics**:
- Detect warm-blooded units (not undead/mechanical) within 2 hexes even in darkness
- See through Blizzard Call weather effects with no vision penalty  
- +20% accuracy against fire-based units (heat signature targeting)

**Strategic Impact**:
- Counter to stealth and weather-based concealment
- Enhanced coordination in blizzard conditions
- Natural advantage against fire mages

**Balance Notes**:
- Limited range keeps it from being overpowered
- Only works on living units
- Accuracy bonus is situational

---

### **❄️ Permafrost** *(Active - Tier 2)*

**Who Gets It**: Ice Dweller shamans, high-level frost mages

**Mechanics**:
- **Activation**: Usable once per battle, requires 2 turns to activate
- **Effect**: Target 3x3 area becomes "frozen solid" for 5 turns
- **Frozen Solid**: Units cannot move into or out of affected hexes
- **Duration**: Effect can be dispelled by fire magic or wait timer

**Strategic Impact**:
- Creates temporary chokepoints and barriers
- Defensive positioning tool
- Area denial for key objectives

**Balance Notes**:
- Long cooldown prevents spam
- Fire magic provides reliable counter
- Limited to specific tactical situations

---

### **🌨️ Snow Blindness** *(Active - Tier 2)*

**Who Gets It**: Frost Clan weather-workers, Ice Dweller wind-callers

**Mechanics**:
- **Target**: Enemy unit within 4 hexes
- **Effect**: Target loses 50% accuracy and 30% dodge for 3 turns
- **Visual**: Unit appears "dazed" with swirling snow effects
- **Resistance**: Fire resistance reduces duration by 1 turn

**Strategic Impact**:
- Debuff powerful enemy units
- Setup for coordinated attacks
- Disrupts enemy archer/mage formations

**Balance Notes**:
- Single target keeps it balanced
- Moderate duration
- Clear visual indicator for counterplay

---

### **🏔️ Avalanche** *(Active - Tier 3)*

**Who Gets It**: Only the strongest Frost Clan berserkers and Ice Dweller titans

**Mechanics**:
- **Requirements**: Must be adjacent to mountain or hill hex
- **Activation**: Usable once per scenario, requires unit to be stationary for 1 turn
- **Effect**: Creates a 5-hex line of debris that deals damage and blocks movement
- **Damage**: 15-25 impact damage to units caught in the slide
- **Duration**: Debris blocks movement for remainder of battle

**Strategic Impact**:
- Terrain reshaping for permanent battlefield control
- High-impact ability with scenario-changing potential
- Ultimate expression of environmental mastery

**Balance Notes**:
- Extremely limited usage (once per scenario)
- Requires specific terrain positioning
- High-tier units only (rare and expensive)

---

### **🌊 Ice Flow** *(Active - Tier 2)*

**Who Gets It**: Ice Dweller water-shapers, advanced Frost Clan shamans

**Mechanics**:
- **Target**: Any water hex within 3 hexes
- **Effect**: Creates a 1-hex wide "ice bridge" connecting two points
- **Duration**: Bridge lasts 8 turns or until destroyed by fire damage
- **Capacity**: Can support up to 3 units crossing simultaneously

**Strategic Impact**:
- Tactical mobility across water barriers
- Enables surprise flanking maneuvers  
- Creates new strategic options on water-heavy maps

**Balance Notes**:
- Limited range prevents easy map crossing
- Vulnerable to fire attacks
- Capacity limit prevents mass movement

---

## 🌍 **Environmental Interactions**

### **Terrain Transformation Priority**
1. **Fire Magic** > Ice effects (fire melts ice, removes frozen status)
2. **Avalanche** > All other terrain (permanent debris placement)
3. **Glacial Aura** > Normal terrain (slow ice spreading)
4. **Permafrost** > Movement (temporary blocking)
5. **Ice Flow** > Water (temporary bridging)

### **Weather System Integration**
- **Blizzard Active**: All ice abilities gain +1 range
- **Fire Weather**: All ice abilities have -1 range, +1 turn activation time
- **Normal Weather**: All abilities work as designed

### **Synergy Chains**
- **Glacial Aura** → **Cold Walking** → Enhanced mobility advantage
- **Blizzard Call** → **Snow Blindness** → Coordinated area control
- **Hunter's Mark** → **Thermal Sense** → Perfect tracking combination
- **Ice Shield** → **Permafrost** → Defensive fortress strategy

---

## 📊 **Complete Ability Summary**

### **Ice Dwellers** (16 Total Abilities)
**Signature**: Glacial Aura (Tier 3), Vampire Aura (Tier 3), Winter's Blessing (Tier 2), Blizzard Call (Tier 3), Ice Shield (Tier 2)
**Supporting**: Freeze Attack (Tier 1), Frostbite (Tier 2), Arctic Survival (Tier 1), Ice Armor (Tier 2), Cold Walking (Tier 1), Thermal Sense (Tier 1), Permafrost (Tier 2), Avalanche (Tier 3), Ice Flow (Tier 2)

### **Frost Clans** (12 Total Abilities)  
**Signature**: Hunter's Mark (Tier 2), Survival Instinct (Tier 2), Berserker Fury (Tier 3)
**Supporting**: Pack Tactics (Tier 2), Last Stand (Tier 3), Arctic Survival (Tier 1), Cold Walking (Tier 1), Thermal Sense (Tier 1), Snow Blindness (Tier 2), Avalanche (Tier 3), Ice Flow (Tier 2)

### **Complexity Distribution**
- **Tier 1 (Simple)**: 4 abilities - Easy to learn and use
- **Tier 2 (Moderate)**: 9 abilities - Require tactical thinking  
- **Tier 3 (Complex)**: 7 abilities - Advanced strategic depth

This comprehensive ability system provides both factions with unique identity, tactical depth, and meaningful strategic choices while maintaining balance and clear counterplay options.