# Scenario Creation Guide for Ice Age Campaign

## Overview

This guide provides step-by-step instructions for creating scenarios for the Wesnoth Ice Age mod. It covers file structure, WML configuration, map creation using the Wesnoth Map Editor, and integration into the campaign.

## Campaign Structure

### Campaign: Rise of the Frost King ("The Forbidden North")
- **15 Total Scenarios**
- **Campaign ID**: `Rise_of_the_Frost_King`
- **First Scenario**: `01_The_Ice_Throne`

## File Organization

### Directory Structure

```
wesnoth.iceage/
└── campaigns/
    └── rise_of_the_frost_king/
        ├── _main.cfg                    # Campaign configuration
        ├── scenarios/
        │   ├── _main.cfg                # Includes all scenario files
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

### Relative Paths Used in WML

- **Scenario Files**: `add-ons/wesnoth.iceage/campaigns/rise_of_the_frost_king/scenarios/`
- **Map Files**: `add-ons/wesnoth.iceage/campaigns/rise_of_the_frost_king/maps/`

## Step-by-Step Scenario Creation

### Step 1: Create the Scenario Configuration File (.cfg)

#### Naming Convention
```
##_Scenario_Name.cfg
```

Examples:
- `01_The_Ice_Throne.cfg`
- `05_Coastal_Settlements.cfg`
- `15_Exodus.cfg`

#### Basic Scenario Template

Create a new file with the following structure:

```wml
#textdomain wesnoth-Ice_Age

[scenario]
    id=01_The_Ice_Throne
    name= _ "01. The Ice Throne"
    map_file="add-ons/wesnoth.iceage/campaigns/rise_of_the_frost_king/maps/01_the_ice_throne.map"
    
    # Scenario timing
    turns=20
    victory_when_enemies_defeated=yes
    
    # Difficulty adjustments
    [side]
        side=1
        controller=human
        team_name=players
        user_team_name= _ "Ice Folk"
        faction=ice_dwellers
        color=blue
        gold=100
        
        [ai]
            passive_multiplier=1.0
        [/ai]
        
        # Starting units configuration
        [unit]
            type=Ice_Knight
            x=1
            y=1
        [/unit]
    [/side]
    
    [side]
        side=2
        controller=ai
        team_name=enemies
        user_team_name= _ "Orcs"
        faction=orcs
        color=red
        gold=150
        
        [ai]
            passive_multiplier=1.0
        [/ai]
        
        # Enemy units configuration
        [unit]
            type=Orcish_Archer
            x=10
            y=10
        [/unit]
    [/side]
    
    # Events
    [event]
        name=prestart
        [message]
            speaker=narrator
            message= _ "The invasion begins..."
            image="wesnoth-icon.png"
        [/message]
    [/event]
    
    [event]
        name=start
        [message]
            speaker=Frostwhisper
            message= _ "I sense an ancient darkness approaching our lands..."
        [/message]
    [/event]
    
    [event]
        name=victory
        [message]
            speaker=Frostwhisper
            message= _ "We have won this battle, but the war is far from over."
        [/message]
        [endlevel]
            result=victory
            bonus=yes
            next_scenario=02_Alliance_of_Ice
        [/endlevel]
    [/event]
    
    [event]
        name=defeat
        [message]
            speaker=narrator
            message= _ "The ice folk have been defeated..."
        [/message]
        [endlevel]
            result=defeat
        [/endlevel]
    [/event]

[/scenario]
```

#### Key WML Elements

| Element | Purpose |
|---------|---------|
| `id` | Unique scenario identifier |
| `name` | Display name in campaign menu |
| `map_data` | Path to the map file |
| `turns` | Number of turns (0 = unlimited) |
| `victory_when_enemies_defeated` | Auto-victory when all enemies defeated |
| `[side]` | Player or AI side configuration |
| `[event]` | Triggers for dialogue, logic, etc. |
| `next_scenario` | Which scenario loads after victory |

### Step 2: Create the Map Using Wesnoth Map Editor

#### Launching the Map Editor

1. Open **Wesnoth**
2. Click **Tools**
3. Select **Map Editor**
4. Choose **New Map** or **Load Map**

#### Setting Map Dimensions

- Recommended sizes: **20x20** to **25x25** for balanced gameplay
- Larger maps (30x30+) for epic battles
- Smaller maps (15x15) for quick skirmishes

#### Map Editor Controls

| Control | Action |
|---------|--------|
| **Left Mouse Click** | Place selected terrain |
| **Right Mouse Click** | Erase terrain |
| **Middle Mouse Drag** | Pan the map |
| **Scroll Wheel** | Zoom in/out |
| **WASD or Arrow Keys** | Navigate map |
| **H** | Toggle hex grid visibility |
| **Ctrl + Z** | Undo |
| **Ctrl + Y** | Redo |
| **Shift + Click** | Add to selection |
| **Ctrl + A** | Select all |

#### Terrain Types and Codes

```
Terrain Code Format: CODE[VARIATION][OVERLAY]

Examples:
G.    = Grass (default walkable)
W*    = Water (impassable)
M*    = Mountain (high defense, limited movement)
f*    = Forest (provides defense)
h*    = Hill (medium terrain)
C*    = Castle/Keep (capture point)
V*    = Village (resource + healing)
R*    = Road (fast movement)
```

#### Step-by-Step Map Creation

##### Phase 1: Base Terrain

1. **Select Base Terrain**: Click grass (G.) in the terrain palette
2. **Paint Base Layer**: Click and drag across the map to cover it
3. **Set Map Boundaries**: Ensure the entire map is covered

##### Phase 2: Strategic Features

1. **Add Water Features**:
   - Use water (W*) to create natural barriers
   - Create rivers or lakes as strategic chokepoints
   - Leave bridges or ford points for crossing

2. **Place Mountains**:
   - Click mountain (M*) to place
   - Create ridges for defensive positions
   - Use as impassable boundaries when needed

3. **Add Forests**:
   - Distribute forests (f*) for defense bonuses
   - Create clear sight lines where needed
   - Use for ambush positions

##### Phase 3: Player and Enemy Positions

1. **Mark Starting Positions**:
   - Use special hexagon overlays to mark spawn points
   - Click the "unit overlay" tool from the toolbar
   - Red hexagons for enemy starting positions
   - Blue hexagons for player starting positions

2. **Balance Positioning**:
   - Ensure fairness between both sides
   - Give defenders good defensive positions
   - Provide attackers with approach routes

##### Phase 4: Villages and Resources

1. **Place Villages** (V*):
   - 2-3 villages per player recommended
   - Spread across map for resource management
   - Place near starting positions for initial income

2. **Create Capture Points**:
   - Use castle/keep (C*) for strategic objectives
   - Place them as central control points
   - Mark in objectives

##### Phase 5: Routes and Connectivity

1. **Create Paths**:
   - Use roads (R*) for faster movement if desired
   - Ensure multiple routes when possible
   - Create tactical corridors between objectives

2. **Design Chokepoints**:
   - Use terrain to create natural bottlenecks
   - Balance difficulty - don't make it impossible
   - Allow flanking routes

##### Phase 6: Decorative Elements

1. **Add Objectives**:
   - Mark important locations visually
   - Use terrain variety for visual interest
   - Maintain playability despite visuals

2. **Polish**:
   - Use terrain transitions for smooth edges
   - Fill isolated tiles
   - Test sight lines

#### Map Editor Advanced Features

##### Brush Tool
- Create smooth terrain transitions
- Paint multiple tiles at once
- Available in the tool palette

##### Fill Tool
- Fill large areas quickly
- Select terrain and click to fill connected areas
- Use Ctrl+Click for different behavior

##### Copy/Paste
- Copy terrain sections: Select area + Ctrl+C
- Paste: Ctrl+V and position

##### Visibility (Fog of War)
- Use overlay tools to mark initial fog of war
- Mark starting vision radius for units
- Press 'V' to toggle visibility overlay

#### Saving Your Map

1. Click **File** → **Save Map As**
2. Use naming convention: `##_scenario_name.map`
   - Example: `01_the_ice_throne.map`
3. Save in: `campaigns/rise_of_the_frost_king/maps/`
4. Verify filename and location before saving

#### Testing Your Map

1. In Map Editor: **File** → **Test Map**
2. Loads scenario with your map
3. Test pathing and gameplay
4. Check unit movement ranges
5. Verify castle/village positions

### Step 3: Reference Scenario in Campaign

#### Update scenarios/_main.cfg

Add your scenario to `campaigns/rise_of_the_frost_king/scenarios/_main.cfg`:

```wml
# Part 1: The Discovery (Scenarios 1-3)
{~add-ons/wesnoth.iceage/campaigns/rise_of_the_frost_king/scenarios/01_The_Ice_Throne.cfg}
{~add-ons/wesnoth.iceage/campaigns/rise_of_the_frost_king/scenarios/02_Alliance_of_Ice.cfg}
{~add-ons/wesnoth.iceage/campaigns/rise_of_the_frost_king/scenarios/03_The_Frozen_Army.cfg}
```

The format `{~path/to/file.cfg}` tells Wesnoth to include that file.

#### Automatic Loading

Once referenced, your scenario will:
- Automatically load when reached in campaign
- Include all WML from the file
- Connect to previous/next scenarios via `next_scenario` field

### Step 4: Configure Difficulty Levels

#### Difficulty Multipliers

Add to each side in your scenario:

```wml
[side]
    # ... basic configuration ...
    
    [ai]
        passive_multiplier=1.0    # AI aggressiveness (1.0 = normal)
        aggression=0.5            # Attack tendency (0-1)
        caution=0.25              # Defensive caution (0-1)
    [/ai]
[/side]
```

#### Difficulty-Based Configuration

```wml
[scenario]
    # ... scenario setup ...
    
    # Easy mode adjustments
    [if]
        [variable]
            name=difficulty
            equals=EASY
        [/variable]
        [then]
            [side]
                side=2
                gold=100          # Reduce enemy gold
            [/side]
        [/then]
    [/if]
    
    # Hard mode adjustments
    [if]
        [variable]
            name=difficulty
            equals=HARD
        [/variable]
        [then]
            [side]
                side=2
                gold=300          # Increase enemy gold
            [/side]
        [/then]
    [/if]
[/scenario]
```

### Step 5: Add Dialogue and Story Events

#### Starting Dialogue

```wml
[event]
    name=start
    [message]
        speaker=Frostwhisper
        message= _ "The prophecy unfolds before us. We must prepare for what is coming."
    [/message]
    [message]
        speaker=Graksul
        message= _ "We stand ready!"
    [/message]
[/event]
```

#### Victory Events

```wml
[event]
    name=victory
    [message]
        speaker=Frostwhisper
        message= _ "Victory! But this is only the beginning of our struggle."
    [/message]
    [endlevel]
        result=victory
        bonus=yes
        next_scenario=02_Alliance_of_Ice
    [/endlevel]
[/event]
```

#### Defeat Events

```wml
[event]
    name=defeat
    [message]
        speaker=narrator
        message= _ "The ice folk have fallen. All is lost..."
        image="wesnoth-icon.png"
    [/message]
    [endlevel]
        result=defeat
    [/endlevel]
[/event]
```

### Step 6: Test and Validate

#### Pre-Launch Testing

1. **Syntax Check**: Verify WML has no syntax errors
2. **Map Validation**: Load map in editor
3. **Unit Placement**: Verify all units start correctly
4. **Message Text**: Ensure all dialogue displays properly

#### In-Game Testing

1. Load campaign in Wesnoth
2. Play scenario on each difficulty level
3. Verify:
   - Map loads without errors
   - Units appear correctly
   - Dialogue displays properly
   - Victory/defeat conditions work
   - Next scenario loads when victorious

#### Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| Map doesn't load | Check path in `map_data` field |
| Units don't appear | Verify unit types exist in game |
| Dialogue doesn't show | Check `#textdomain` declaration |
| Next scenario won't load | Verify `next_scenario` ID exists |
| Game crashes | Check for WML syntax errors |

### Step 7: Integration Checklist

Before marking scenario as complete:

- [ ] Scenario `.cfg` file created in `scenarios/` folder
- [ ] Map `.map` file created in `maps/` folder
- [ ] Scenario referenced in `scenarios/_main.cfg`
- [ ] Scenario ID follows naming convention: `##_Name`
- [ ] Map path correctly references map file
- [ ] Difficulty levels Easy, Normal, Hard configured
- [ ] Starting dialogue/events implemented
- [ ] Victory conditions working
- [ ] Defeat conditions working
- [ ] Next scenario correctly specified
- [ ] Tested on all difficulty levels
- [ ] Unit balance verified
- [ ] Map playability confirmed
- [ ] No syntax errors in WML
- [ ] Campaign flows smoothly to next scenario

## Campaign Scenario List

### Part 1: The Discovery (Scenarios 1-3)
- **01_The_Ice_Throne.cfg**
- **02_Alliance_of_Ice.cfg**
- **03_The_Frozen_Army.cfg**

### Part 2: The First Strike (Scenarios 4-6)
- **04_Heart_of_Winter.cfg**
- **05_Coastal_Settlements.cfg**
- **06_The_Scattered_Clans.cfg**

### Part 3: The Invasion Begins (Scenarios 7-9)
- **07_Naga_Alliance.cfg**
- **08_Frostwhisper_Prophecy.cfg**
- **09_Fall_of_the_North.cfg**

### Part 4: Awakening the Dark (Scenarios 10-12)
- **10_Grimjaw_Rising.cfg**
- **11_Tombs_Awakened.cfg**
- **12_Darkness_Spreads.cfg**

### Part 5: The Price of Awakening (Scenarios 13-15)
- **13_The_Last_Stand.cfg**
- **14_The_Escape.cfg**
- **15_Exodus.cfg**

## Useful Resources

### Wesnoth Documentation
- Official WML Reference: https://wiki.wesnoth.org/WML
- Scenario Tags: https://wiki.wesnoth.org/ScenarioWML
- Map Format: https://wiki.wesnoth.org/MapFormat
- Event System: https://wiki.wesnoth.org/EventWML

### Editor Tools
- Map Editor Guide: https://wiki.wesnoth.org/EditorManual
- Terrain Overview: https://wiki.wesnoth.org/TerrainCodes

### Tips & Best Practices
1. **Start Small**: Test scenarios individually before linking
2. **Consistency**: Use same map dimensions and style across campaign
3. **Balance**: Ensure fair difficulty progression
4. **Story**: Tie scenario objectives to narrative
5. **Testing**: Thoroughly test on all difficulty levels
6. **Save Often**: Use version control for campaign files

## Quick Reference: WML Tags

```wml
[scenario]         # Scenario container
[side]            # Player/AI side
[unit]            # Individual unit
[event]           # Game event trigger
[message]         # Dialogue box
[endlevel]        # End scenario
[if]/[then]/[else] # Conditional logic
```

## Support and Questions

For additional help:
- Check existing scenarios in this campaign
- Consult the Ice Age mod documentation
- Reference official Wesnoth wiki pages
- Test in the Map Editor before full integration
