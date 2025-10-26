# Ice Age Eras - Multiplayer Integration

## 🌍 **Era System Overview**

The Ice Age expansion introduces three new eras that integrate our factions into Wesnoth's multiplayer system, providing different levels of faction variety for different play preferences.

## 🏔️ **Available Eras**

### **1. Default + Ice Age Era** 
**Era ID:** `era_default_plus_ice_age`  
**Name:** "Default + Ice Age"

**Description:** The standard Wesnoth experience enhanced with arctic factions

**Available Factions:**
- ✅ **Rebels** (Elves) - Forest specialists
- ✅ **Loyalists** (Humans) - Balanced faction  
- ✅ **Northerners** (Orcs) - Mountain barbarians
- ✅ **Undead** - Dark necromancy
- ✅ **Knalgans** (Dwarves) - Underground warriors
- ✅ **Drakes** - Desert reptilian faction
- ❄️ **Frost Clans** - Arctic human survivors with 4+ level progression
- 🧊 **Ice Dwellers** - Mystical ice elementals with magical powers

**Strategic Balance:**
- 8 total factions provide extensive variety
- Ice Age factions complement existing terrain preferences
- Frost Clans fill heavy cavalry/late-game power niche
- Ice Dwellers add unique magical specialist role

### **2. Default + Dunefolk + Ice Age Era**
**Era ID:** `era_default_plus_dunefolk_plus_ice_age`  
**Name:** "Default + Dunefolk + Ice Age"

**Description:** Maximum faction variety including desert and arctic specialists

**Available Factions:**
- ✅ **All Default Factions** (6 factions as above)
- 🏜️ **Dunefolk** - Desert faction with unique mechanics
- ❄️ **Frost Clans** - Arctic survivors
- 🧊 **Ice Dwellers** - Ice elementals

**Strategic Balance:**
- 9 total factions for ultimate multiplayer variety
- Full spectrum from desert (Dunefolk/Drakes) to arctic (Ice Age) specialists
- Complete terrain coverage: forest, plains, underground, desert, ice, water
- Maximum tactical diversity for complex multiplayer games

### **3. Pure Ice Age Era**
**Era ID:** `era_ice_age_only`  
**Name:** "Ice Age"

**Description:** Thematic arctic-only battles in the eternal winter

**Available Factions:**
- ❄️ **Frost Clans** - Hardy northern survivors
- 🧊 **Ice Dwellers** - Mystical ice beings

**Strategic Balance:**
- 2 factions for focused, thematic gameplay
- Perfect for Ice Age campaigns or themed matches
- Emphasizes faction-specific mechanics and interactions
- Ideal for showcasing unique Ice Age features

## ⚔️ **Faction Recruitment Lists**

### **Frost Clans Recruitment**
**Starting Units:**
- **Frost Warrior** - Solaris-Noctis melee infantry (Level 1 → Warlord Level 4)
- **Frost Scout** - Twilight ranged archer (Level 1 → Pathfinder Level 4)  
- **Pack Rider** - Twilight snow dog cavalry (Level 1 → Blizzard Lord Level 4)
- **Bear Rider** - Solaris-Noctis heavy cavalry (Level 1 → Primal Champion Level 4)

**Random Leaders:**
- **Frost Chieftain** - Standard Level 3 leader
- **Frost Warlord** - Elite Level 4 infantry leader
- **Ancient Bear Lord** - Level 3 mounted leader
- **Primal Bear Champion** - Ultimate Level 4 mounted leader

### **Ice Dwellers Recruitment** (Planned)
**Starting Units:**
- **Ice Elemental** - Pure ice magical creature
- **Frost Wraith** - Ghostly ice spirit
- **Ice Beast** - Primal ice creature

**Random Leaders:**
- **Frost Lord** - Elemental commander
- **Ice Sovereign** - Elite magical leader  
- **Primal Ice Spirit** - Ultimate ice being

## 🎮 **Multiplayer Integration Features**

### **Terrain Preferences**
**Frost Clans:**
- **Liked Terrain:** `Ai` (Ice), `Aa` (Frozen), `Ms` (Snowy Mountains), `Gs` (Grass)
- **Strategy:** Defensive ice fortress with forest mobility
- **Weakness:** Poor performance in deserts and swamps

**Ice Dwellers:**
- **Liked Terrain:** `Ai` (Ice), `Aa` (Frozen), `Ms` (Snowy Mountains)
- **Strategy:** Pure ice control with magical superiority
- **Weakness:** Limited to cold terrain environments

### **AI Behavior Profiles**

**Frost Clans AI:**
- **Aggression:** 0.5 (Moderate - balanced offense/defense)
- **Caution:** 0.25 (Low - willing to take calculated risks)
- **Village Value:** 1.0 (Standard - values territorial control)
- **Leader Value:** 3.0 (High - protects commanders well)

**Ice Dwellers AI:**
- **Aggression:** 0.3 (Low - defensive magical faction)
- **Caution:** 0.4 (Moderate - careful with valuable magical units)
- **Village Value:** 0.8 (Lower - less dependent on villages)
- **Leader Value:** 4.0 (Very High - magical leaders are critical)

### **Flag Integration**
**Custom Faction Flags:**
- `flags/frost-clans-flag.png` - Frost Clans banner
- `flags/ice-dwellers-flag.png` - Ice Dwellers mystical symbol

## 🔧 **Technical Implementation**

### **Era Loading System**
**File:** `eras.cfg`
- Defines all three eras with complete faction lists
- Integrates seamlessly with Wesnoth's era selection system
- Loaded automatically via `_main.cfg` integration

**WML Structure:**
```wml
[era]
    id=era_name
    name= _ "Display Name"
    description= _ "Era description"
    
    [multiplayer_side]
        id=faction_id
        name= _ "Faction Name"
        type=recruit_list
        leader=default_leader
        random_leader=leader_options
        terrain_liked=preferred_terrains
        recruit=recruit_list
        flag=flag_image
    [/multiplayer_side]
[/era]
```

### **Faction Integration**
**Files Updated:**
- `_main.cfg` - Added era loading
- `factions/frost_clans.cfg` - Updated recruitment to Pack Rider
- `eras.cfg` - Complete era definitions

### **Compatibility**
- ✅ **Wesnoth 1.18** - Full compatibility with current version
- ✅ **Multiplayer** - Ready for online and local multiplayer games
- ✅ **Campaign Integration** - Eras available for custom scenarios
- ✅ **AI Support** - Custom AI profiles for balanced computer opponents

## 🎯 **Usage Recommendations**

### **For New Players**
**Recommended:** `era_default_plus_ice_age`
- Familiar default factions plus exciting new Ice Age options
- Good balance of complexity and variety
- Easy to learn Ice Age mechanics alongside known factions

### **For Veterans**
**Recommended:** `era_default_plus_dunefolk_plus_ice_age`  
- Maximum strategic variety with 9 factions
- Complex terrain and alignment interactions
- Ultimate test of faction mastery

### **For Thematic Games**
**Recommended:** `era_ice_age_only`
- Pure Ice Age experience
- Focus on unique faction mechanics
- Perfect for Ice Age campaigns and themed matches

## 🎲 **Strategic Implications**

### **Meta-Game Impact**
**Frost Clans Role:**
- **Late-Game Powerhouse:** Higher XP requirements balanced by elite Level 4 units
- **Time Management:** Dual alignment system rewards tactical timing
- **Heavy Cavalry Specialists:** Unique bear-mounted and snow dog cavalry

**Ice Dwellers Role:**
- **Magical Specialists:** Pure elemental damage and ice manipulation  
- **Terrain Control:** Ice creation and frozen battlefield dominance
- **Support/Control:** Magical utilities and battlefield control

### **Counter-Play Dynamics**
**Against Frost Clans:**
- **Early Pressure:** Exploit their slower early-game development
- **Fire Damage:** Target their cold-adapted weaknesses
- **Terrain Denial:** Force fights away from ice/forest terrain

**Against Ice Dwellers:**
- **Anti-Magic:** Use units with magical resistance
- **Mobility:** Outmaneuver their slower elemental units
- **Disruption:** Prevent their magical setup and terrain control

This era system provides Ice Age factions with complete integration into Wesnoth's multiplayer ecosystem while maintaining the unique 4+ level progression and alignment mechanics that make them distinctive.