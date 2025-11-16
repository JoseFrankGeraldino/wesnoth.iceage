# Campaign Scenario Reference

## Campaign Files Structure

### Main Campaign Configuration
- **File**: `campaigns/rise_of_the_frost_king/_main.cfg`
- **Purpose**: Defines campaign metadata, first scenario, and imports all scenarios
- **Key Fields**:
  - `id`: Campaign identifier
  - `first_scenario`: Entry point (01_The_Ice_Throne)
  - Binary path setup for resource loading

### Scenarios Main Include File
- **File**: `campaigns/rise_of_the_frost_king/scenarios/_main.cfg`
- **Purpose**: Includes all 15 scenario configuration files
- **Format**: Each scenario referenced with `{~path/to/scenario.cfg}`

---

## Expected Scenario Files

### File Naming Convention: `##_Scenario_Name.cfg`

All files should be placed in: `campaigns/rise_of_the_frost_king/scenarios/`

| Scenario # | Filename | Story Arc |
|-----------|----------|-----------|
| 01 | `01_The_Ice_Throne.cfg` | The Discovery |
| 02 | `02_Alliance_of_Ice.cfg` | The Discovery |
| 03 | `03_The_Frozen_Army.cfg` | The Discovery |
| 04 | `04_Heart_of_Winter.cfg` | The First Strike |
| 05 | `05_Coastal_Settlements.cfg` | The First Strike |
| 06 | `06_The_Scattered_Clans.cfg` | The First Strike |
| 07 | `07_Naga_Alliance.cfg` | The Invasion Begins |
| 08 | `08_Frostwhisper_Prophecy.cfg` | The Invasion Begins |
| 09 | `09_Fall_of_the_North.cfg` | The Invasion Begins |
| 10 | `10_Grimjaw_Rising.cfg` | Awakening the Dark |
| 11 | `11_Tombs_Awakened.cfg` | Awakening the Dark |
| 12 | `12_Darkness_Spreads.cfg` | Awakening the Dark |
| 13 | `13_The_Last_Stand.cfg` | The Price of Awakening |
| 14 | `14_The_Escape.cfg` | The Price of Awakening |
| 15 | `15_Exodus.cfg` | The Price of Awakening |

---

## Expected Map Files

### File Naming Convention: `##_scenario_name.map`

All files should be placed in: `campaigns/rise_of_the_frost_king/maps/`

| Scenario # | Filename |
|-----------|----------|
| 01 | `01_the_ice_throne.map` |
| 02 | `02_alliance_of_ice.map` |
| 03 | `03_the_frozen_army.map` |
| 04 | `04_heart_of_winter.map` |
| 05 | `05_coastal_settlements.map` |
| 06 | `06_the_scattered_clans.map` |
| 07 | `07_naga_alliance.map` |
| 08 | `08_frostwhisper_prophecy.map` |
| 09 | `09_fall_of_the_north.map` |
| 10 | `10_grimjaw_rising.map` |
| 11 | `11_tombs_awakened.map` |
| 12 | `12_darkness_spreads.map` |
| 13 | `13_the_last_stand.map` |
| 14 | `14_the_escape.map` |
| 15 | `15_exodus.map` |

---

## Scenario WML Configuration

### Minimal Required Fields

Each scenario file must contain:

```wml
#textdomain wesnoth-Ice_Age

[scenario]
    id=##_Scenario_ID
    name= _ "##. Scenario Name"
    map_data="{~add-ons/wesnoth.iceage/campaigns/rise_of_the_frost_king/maps/##_scenario_name.map}"
    
    turns=NUMBER
    victory_when_enemies_defeated=yes
    
    [side]
        side=1
        controller=human
        team_name=players
        user_team_name= _ "Ice Folk"
        faction=ice_dwellers
        color=blue
    [/side]
    
    [side]
        side=2
        controller=ai
        team_name=enemies
        user_team_name= _ "Enemies"
        faction=FACTION
        color=COLOR
    [/side]
    
    [event]
        name=start
        # Starting dialogue/events
    [/event]
    
    [event]
        name=victory
        [endlevel]
            result=victory
            bonus=yes
            next_scenario=##_Next_Scenario_ID
        [/endlevel]
    [/event]

[/scenario]
```

### Paths Used in WML

#### Map Path Template
```wml
map_data="{~add-ons/wesnoth.iceage/campaigns/rise_of_the_frost_king/maps/##_scenario_name.map}"
```

#### Next Scenario Field
```wml
next_scenario=##_Next_Scenario_ID
```

Example:
```wml
next_scenario=02_Alliance_of_Ice
```

---

## Campaign Flow

### Story Progression

```
01_The_Ice_Throne
    ↓
02_Alliance_of_Ice
    ↓
03_The_Frozen_Army
    ↓
04_Heart_of_Winter
    ↓
05_Coastal_Settlements
    ↓
06_The_Scattered_Clans
    ↓
07_Naga_Alliance
    ↓
08_Frostwhisper_Prophecy
    ↓
09_Fall_of_the_North
    ↓
10_Grimjaw_Rising
    ↓
11_Tombs_Awakened
    ↓
12_Darkness_Spreads
    ↓
13_The_Last_Stand
    ↓
14_The_Escape
    ↓
15_Exodus
    ↓
[Campaign End]
```

---

## Automatic File Loading

Once scenario files are in place and referenced in `scenarios/_main.cfg`, they will:

1. Be automatically loaded when the campaign is selected
2. Appear in the campaign menu with proper naming
3. Load in sequence based on `next_scenario` field
4. Transition automatically when victory is achieved

### Example Loading Process

When campaign is launched:
```
1. Load: campaigns/rise_of_the_frost_king/_main.cfg
2. Include: campaigns/rise_of_the_frost_king/scenarios/_main.cfg
3. Include: 01_The_Ice_Throne.cfg
4. Load: campaigns/rise_of_the_frost_king/maps/01_the_ice_throne.map
5. Start Gameplay
6. On Victory → Load 02_Alliance_of_Ice.cfg
```

---

## Quick Checklist for New Scenarios

- [ ] Scenario `.cfg` file created with proper naming: `##_Name.cfg`
- [ ] Scenario file placed in `campaigns/rise_of_the_frost_king/scenarios/`
- [ ] Map `.map` file created with proper naming: `##_name.map`
- [ ] Map file placed in `campaigns/rise_of_the_frost_king/maps/`
- [ ] Scenario referenced in `scenarios/_main.cfg`
- [ ] WML has correct `id` field matching filename
- [ ] `map_data` path points to correct map file
- [ ] `next_scenario` field set to next scenario (except for scenario 15)
- [ ] All required WML tags present
- [ ] No syntax errors in WML
- [ ] Tested in game

---

## Directory Structure (Complete)

```
wesnoth.iceage/
└── campaigns/
    └── rise_of_the_frost_king/
        ├── _main.cfg
        ├── scenarios/
        │   ├── _main.cfg
        │   ├── 01_The_Ice_Throne.cfg
        │   ├── 02_Alliance_of_Ice.cfg
        │   ├── 03_The_Frozen_Army.cfg
        │   ├── 04_Heart_of_Winter.cfg
        │   ├── 05_Coastal_Settlements.cfg
        │   ├── 06_The_Scattered_Clans.cfg
        │   ├── 07_Naga_Alliance.cfg
        │   ├── 08_Frostwhisper_Prophecy.cfg
        │   ├── 09_Fall_of_the_North.cfg
        │   ├── 10_Grimjaw_Rising.cfg
        │   ├── 11_Tombs_Awakened.cfg
        │   ├── 12_Darkness_Spreads.cfg
        │   ├── 13_The_Last_Stand.cfg
        │   ├── 14_The_Escape.cfg
        │   └── 15_Exodus.cfg
        └── maps/
            ├── 01_the_ice_throne.map
            ├── 02_alliance_of_ice.map
            ├── 03_the_frozen_army.map
            ├── 04_heart_of_winter.map
            ├── 05_coastal_settlements.map
            ├── 06_the_scattered_clans.map
            ├── 07_naga_alliance.map
            ├── 08_frostwhisper_prophecy.map
            ├── 09_fall_of_the_north.map
            ├── 10_grimjaw_rising.map
            ├── 11_tombs_awakened.map
            ├── 12_darkness_spreads.map
            ├── 13_the_last_stand.map
            ├── 14_the_escape.map
            └── 15_exodus.map
```

---

## How Files Connect

### Campaign File (_main.cfg)
```
├── Defines campaign metadata
├── Sets first_scenario = 01_The_Ice_Throne
└── Includes scenarios/_main.cfg (which includes all 15 scenario files)
```

### Scenarios Main File (scenarios/_main.cfg)
```
├── Includes 01_The_Ice_Throne.cfg
├── Includes 02_Alliance_of_Ice.cfg
├── ... (all 15 scenarios)
└── When scenario loaded, it automatically loads its referenced map
```

### Scenario Files (##_Name.cfg)
```
├── Contains game logic, events, units
├── References its map file via map_data field
├── Specifies next_scenario for campaign progression
└── Wesnoth loads the map from maps/ folder automatically
```

### Map Files (##_name.map)
```
├── Binary file created by Wesnoth Map Editor
├── Contains terrain data
├── No modifications needed once created
└── Automatically loaded when scenario specifies it
```

---

## Related Documentation

- **Full Creation Guide**: See `SCENARIO-CREATION-GUIDE.md`
- **GitHub Issue #16**: Campaign tracking issue with detailed requirements
- **Sub-Issues #17-#31**: Individual scenario creation tasks
