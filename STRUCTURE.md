# Ice Age Add-on Structure

## Overview
This Battle for Wesnoth add-on provides 2 new factions and 4 interconnected campaigns.

## File Structure

```
wesnoth.iceage/
├── _main.cfg              # Main entry point for the add-on
├── _server.pbl            # Server metadata for add-on
├── README.md              # User documentation
├── STRUCTURE.md           # This file
│
├── factions/              # Faction definitions
│   ├── _main.cfg
│   ├── frost_clans.cfg    # Frost Clans faction
│   └── ice_dwellers.cfg   # Ice Dwellers faction
│
├── units/                 # Unit type definitions
│   ├── _main.cfg
│   ├── frost_clans.cfg    # 7 Frost Clans units
│   └── ice_dwellers.cfg   # 8 Ice Dwellers units
│
└── campaigns/             # Campaign definitions
    ├── _main.cfg
    │
    ├── the_frozen_wastes/           # Campaign 1
    │   ├── _main.cfg
    │   ├── maps/
    │   │   └── 01_The_Long_Winter.map
    │   └── scenarios/
    │       ├── _main.cfg
    │       ├── 01_The_Long_Winter.cfg
    │       ├── 02_Frozen_Scouts.cfg
    │       ├── 03_The_Ice_Caverns.cfg
    │       ├── 04_Blizzard_Pass.cfg
    │       └── 05_The_Last_Stand.cfg
    │
    ├── rise_of_the_frost_king/      # Campaign 2
    │   ├── _main.cfg
    │   ├── maps/
    │   │   └── 01_The_Ice_Throne.map
    │   └── scenarios/
    │       ├── _main.cfg
    │       ├── 01_The_Ice_Throne.cfg
    │       ├── 02_Alliance_of_Ice.cfg
    │       ├── 03_The_Frozen_Army.cfg
    │       └── 04_Heart_of_Winter.cfg
    │
    ├── the_ice_dwellers_pact/       # Campaign 3
    │   ├── _main.cfg
    │   ├── maps/
    │   │   └── 01_Awakening.map
    │   └── scenarios/
    │       ├── _main.cfg
    │       ├── 01_Awakening.cfg
    │       ├── 02_The_Mortal_Tribes.cfg
    │       ├── 03_Servants_of_Winter.cfg
    │       └── 04_The_Choice.cfg
    │
    └── the_great_thaw/              # Campaign 4
        ├── _main.cfg
        ├── maps/
        │   └── 01_Seeds_of_Spring.map
        └── scenarios/
            ├── _main.cfg
            ├── 01_Seeds_of_Spring.cfg
            ├── 02_The_Melting.cfg
            ├── 03_Balance_Restored.cfg
            └── 04_New_Beginning.cfg
```

## Content Summary

### Factions (2)
1. **Frost Clans** - Hardy northern warriors
2. **Ice Dwellers** - Mystical ice beings

### Unit Types (15)
- **Frost Clans (7):** Frost Warrior, Frost Champion, Frost Chieftain, Frost Scout, Frost Ranger, Frost Rider, Frost Knight
- **Ice Dwellers (8):** Ice Elemental, Greater Ice Elemental, Frost Lord, Frost Wraith, Frost Banshee, Ice Beast, Frost Behemoth, (plus Frost Lord leader variant)

### Campaigns (4)
1. **The Frozen Wastes** - 5 scenarios (Easy difficulty)
2. **Rise of the Frost King** - 4 scenarios (Normal difficulty)
3. **The Ice Dwellers' Pact** - 4 scenarios (Normal difficulty)
4. **The Great Thaw** - 4 scenarios (Hard difficulty)

**Total:** 17 scenarios

## Technical Details

- **WML Version:** Compatible with Wesnoth 1.14+
- **Textdomain:** wesnoth-Ice_Age
- **Add-on Type:** campaign_mp_scenario (campaigns + multiplayer factions)
- **File Format:** All .cfg files use UTF-8 encoding
- **Map Format:** Standard Wesnoth .map format

## Validation Status

✓ All WML files have matching open/close tags
✓ All required _main.cfg files present
✓ Campaign progression properly linked
✓ Unit advancement trees defined
✓ All scenarios have victory/defeat conditions

## Notes

- Maps are simple placeholder maps using standard terrain codes (Aa, Gs, Gg, Ai)
- Unit graphics reference standard Wesnoth sprites
- All text strings are marked for translation with _ prefix
- Factions can be used in both campaigns and multiplayer
