# Ice Age Factions - Unit Overview

## Legend - Unit Status Icons

- **📝 Planned**: Only basic information in this file
- **⚙️ Configuration Files Created**: The configuration files were created and the unit is selectable or upgradable in the game
- **🎨 All Animation Images Added**: We successfully implemented the animation images
- **✅ Fully Implemented**: All images there, upgradable functions, attacks and weaknesses were manually tested by the user

## **❄️ All Units**

| **Unit Name** | **Faction** | **Level** | **HP** | **MP** | **Cost** | **Status** | **Design Document** |
|---|---|---|---|---|---|---|---|
| **Iceborn Warrior** | Frost Clans | 1 | 32 | 5 | 14 | 📝 | [Iceborn Warrior Line](unit-designs/iceborn-warrior-line-design.md) |
| Winterbane Champion | Frost Clans | 2 | 46 | 5 | 28 | 📝 | [Iceborn Warrior Line](unit-designs/iceborn-warrior-line-design.md) |
| Rimeguard Chieftain | Frost Clans | 3 | 52 | 5 | 60 | 📝 | [Iceborn Warrior Line](unit-designs/iceborn-warrior-line-design.md) |
| Glacial Warlord | Frost Clans | 4 | 68 | 6 | 90 | 📝 | [Iceborn Warrior Line](unit-designs/iceborn-warrior-line-design.md) |
| **Tundra Scout** | Frost Clans | 1 | 28 | 6 | 15 | 📝 | [Tundra Scout Line](unit-designs/tundra-scout-line-design.md) |
| Blizzard Ranger | Frost Clans | 2 | 38 | 6 | 32 | 📝 | [Tundra Scout Line](unit-designs/tundra-scout-line-design.md) |
| Avalanche Hunter | Frost Clans | 3 | 48 | 7 | 50 | 📝 | [Tundra Scout Line](unit-designs/tundra-scout-line-design.md) |
| Whiteout Pathfinder | Frost Clans | 4 | 58 | 8 | 75 | 📝 | [Tundra Scout Line](unit-designs/tundra-scout-line-design.md) |
| **Pack Rider** | Frost Clans | 1 | 34 | 7 | 18 | 📝 | [Pack Rider Line](unit-designs/pack-rider-line-design.md) |
| Wolf Ranger | Frost Clans | 2 | 48 | 8 | 38 | 📝 | [Pack Rider Line](unit-designs/pack-rider-line-design.md) |
| Storm Rider | Frost Clans | 3 | 62 | 9 | 60 | 📝 | [Pack Rider Line](unit-designs/pack-rider-line-design.md) |
| Blizzard Lord | Frost Clans | 4 | 78 | 10 | 85 | 📝 | [Pack Rider Line](unit-designs/pack-rider-line-design.md) |

| **Bear Rider** | Frost Clans | 1 | 42 | 4 | 22 | 📝 | [Bear Rider Line](unit-designs/bear-rider-design.md) |
| Dire Bear Rider | Frost Clans | 2 | 58 | 4 | 45 | 📝 | [Bear Rider Line](unit-designs/bear-rider-design.md) |
| Ancient Bear Lord | Frost Clans | 3 | 74 | 5 | 70 | 📝 | [Bear Rider Line](unit-designs/bear-rider-design.md) |
| Primal Bear Champion | Frost Clans | 4 | 92 | 5 | 100 | 📝 | [Bear Rider Line](unit-designs/bear-rider-design.md) |
| **Iceguard Spearman** | Frost Clans | 1 | ? | ? | ? | 📝 | *To Be Created* |
| **Winterheart Shaman** | Frost Clans | 1 | ? | ? | ? | 📝 | *To Be Created* |
| **Snowfall Trapper** | Frost Clans | 1 | ? | ? | ? | 📝 | *To Be Created* |
| **Crystalborn Elemental** | Ice Dwellers | 1 | ? | ? | ? | 📝 | *To Be Created* |
| **Glacial Wraith** | Ice Dwellers | 1 | ? | ? | ? | 📝 | *To Be Created* |
| **Permafrost Beast** | Ice Dwellers | 1 | ? | ? | ? | 📝 | *To Be Created* |
| **Shimmer Sprite** | Ice Dwellers | 1 | ? | ? | ? | 📝 | *To Be Created* |
| **Hoarfrost Mage** | Ice Dwellers | 1 | ? | ? | ? | 📝 | *To Be Created* |
| **Icewall Guardian** | Ice Dwellers | 1 | ? | ? | ? | 📝 | *To Be Created* |
| **Coldmist Stalker** | Ice Dwellers | 1 | ? | ? | ? | 📝 | *To Be Created* |

**Recruitable Units**: Bold units are Level 1 (recruitable)  
**Target**: 7 recruitable units per faction (DuneFolk parity)  
**Current Progress**: Frost Clans 4/7, Ice Dwellers 3/7

---

## 🔧 **Implementation Knowledge Base**

### **Common Errors & Solutions**

#### **❌ Units Not Loading in Multiplayer Era**
- **Error**: Drake units appear instead of custom Ice Age units in era selection
- **Root Cause**: Missing `[units][/units]` wrapper tags in era configuration
- **Solution**: Always wrap unit definitions with proper `[units]` and `[/units]` tags
- **File**: `eras/*.cfg`
- **Example Fix**:
  ```wml
  [era]
      [multiplayer_side]
          [ai]
              recruitment_pattern=fighter,archer,scout
          [/ai]
          [units]
              {~add-ons/wesnoth.iceage/units/frost_clans.cfg}
              {~add-ons/wesnoth.iceage/units/ice_dwellers.cfg}
          [/units]
      [/multiplayer_side]
  [/era]
  ```

#### **❌ Unit Images Not Loading**
- **Error**: Units appear with placeholder images or wrong sprites
- **Common Causes**: 
  - Incorrect image file paths in unit configuration
  - Missing image files in expected directories
  - Case sensitivity issues in file names
- **Prevention**: Always verify image paths match actual file locations

#### **❌ Unit Advancement Not Working**
- **Error**: Units cannot upgrade to next level
- **Common Causes**:
  - Incorrect `advances_to` references
  - Missing target unit definitions
  - Typos in unit IDs
- **Prevention**: Ensure all advancement chains are properly linked

#### **❌ Custom Abilities Not Functioning**
- **Error**: Special abilities like "snow_camouflage" not working
- **Common Causes**:
  - Abilities defined but not properly referenced in unit files
  - Missing ability implementation in `[abilities]` section
- **Prevention**: Always test abilities in-game after implementation

#### **❌ Faction Not Appearing in Game**
- **Error**: Faction doesn't show up in multiplayer or scenario selection
- **Common Causes**:
  - Missing faction registration in `_main.cfg`
  - Incorrect file inclusion paths
  - Syntax errors in configuration files
- **Prevention**: Verify all file includes and test faction loading

### **Testing Checklist for Each Unit**
1. **⚙️ Configuration Files Created**: Unit appears in unit list and can be recruited
2. **🎯 Combat Testing**: All attacks work correctly with proper damage/accuracy
3. **🚶 Movement Testing**: Unit moves correctly on different terrain types
4. **⬆️ Advancement Testing**: Unit can advance to next level (if applicable)
5. **🎨 Animation Testing**: All animations play correctly (attack, death, idle)
6. **🛡️ Resistance Testing**: Damage resistances work as intended
7. **⭐ Ability Testing**: Special abilities function properly
8. **🏆 Complete Integration**: Unit works seamlessly in multiplayer matches

### **File Organization Standards**
- **Unit Configs**: `units/[faction_name].cfg`
- **Faction Configs**: `factions/[faction_name].cfg` 
- **Era Configs**: `eras/[era_name].cfg`
- **Documentation**: `unit-designs/[unit-line-name].md`
- **Always backup files before major changes**: Create `.backup` copies

### **WML Syntax Reminders**
- Always close tags properly: `[tag]` must have `[/tag]`
- Use underscores in IDs: `frost_warrior` not `frost-warrior`
- File paths use forward slashes: `images/units/frost/warrior.png`
- Include files with proper syntax: `{~add-ons/wesnoth.iceage/file.cfg}`

