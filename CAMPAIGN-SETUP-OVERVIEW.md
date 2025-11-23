# Campaign Scenario Setup - Complete Overview

## What's Been Done

### ✓ Campaign Infrastructure Set Up
- Campaign configuration files created and organized
- 15 scenario references already in place in `scenarios/_main.cfg`
- Binary paths configured for automatic resource loading
- Campaign flow properly defined with `first_scenario` and `next_scenario` fields

### ✓ Comprehensive Documentation Created
1. **SCENARIO-CREATION-GUIDE.md** - Full step-by-step tutorial including:
   - File structure and organization
   - Complete Wesnoth Map Editor tutorial with all controls
   - WML scenario configuration templates
   - Difficulty level setup
   - Testing procedures
   
2. **SCENARIO-REFERENCE.md** - Quick reference including:
   - File naming conventions
   - Expected directory structure
   - All 15 scenario files and map files
   - Campaign flow diagram
   - Integration checklist
   
3. **SCENARIO-IMPLEMENTATION-SUMMARY.md** - Complete implementation status including:
   - What's already configured
   - How automatic loading works
   - What needs to be created
   - Quick start instructions

### ✓ GitHub Issues Created and Configured
- **Issue #16** (Parent): Enhanced with detailed 15-scenario creation guide
- **Issues #17-#31** (Sub-issues): Individual scenarios tracked
- **All assigned to**: NetzerGeraldino

### ✓ Campaign Files Updated
- `campaigns/rise_of_the_frost_king/_main.cfg` - Campaign definition with first_scenario set
- `campaigns/rise_of_the_frost_king/scenarios/_main.cfg` - All 15 scenarios referenced

---

## How This Works

### The Automatic Loading System

```
Campaign Loads
    ↓
_main.cfg (Campaign Definition)
    ↓
Defines first_scenario = 01_The_Ice_Throne
    ↓
scenarios/_main.cfg (Includes all 15 scenarios)
    ↓
Each scenario automatically loads when reached
    ↓
Maps automatically loaded from campaigns/rise_of_the_frost_king/maps/
    ↓
Game Displays Scenario
    ↓
On Victory → Next scenario loads automatically via next_scenario field
```

---

## File Locations

### Configuration Files (Already in Place)
```
wesnoth.iceage/
├── SCENARIO-CREATION-GUIDE.md ✓
├── SCENARIO-REFERENCE.md ✓
├── SCENARIO-IMPLEMENTATION-SUMMARY.md ✓
└── campaigns/rise_of_the_frost_king/
    ├── _main.cfg ✓
    └── scenarios/
        └── _main.cfg ✓
```

### Files to Be Created by Developers

**Scenario Config Files** (15 total)
```
campaigns/rise_of_the_frost_king/scenarios/
├── 01_The_Ice_Throne.cfg (TO CREATE)
├── 02_Alliance_of_Ice.cfg (TO CREATE)
├── 03_The_Frozen_Army.cfg (TO CREATE)
├── 04_Heart_of_Winter.cfg (TO CREATE)
├── 05_Coastal_Settlements.cfg (TO CREATE)
├── 06_The_Scattered_Clans.cfg (TO CREATE)
├── 07_Naga_Alliance.cfg (TO CREATE)
├── 08_Frostwhisper_Prophecy.cfg (TO CREATE)
├── 09_Fall_of_the_North.cfg (TO CREATE)
├── 10_Grimjaw_Rising.cfg (TO CREATE)
├── 11_Tombs_Awakened.cfg (TO CREATE)
├── 12_Darkness_Spreads.cfg (TO CREATE)
├── 13_The_Last_Stand.cfg (TO CREATE)
├── 14_The_Escape.cfg (TO CREATE)
└── 15_Exodus.cfg (TO CREATE)
```

**Map Files** (15 total)
```
campaigns/rise_of_the_frost_king/maps/
├── 01_the_ice_throne.map (TO CREATE)
├── 02_alliance_of_ice.map (TO CREATE)
├── 03_the_frozen_army.map (TO CREATE)
├── 04_heart_of_winter.map (TO CREATE)
├── 05_coastal_settlements.map (TO CREATE)
├── 06_the_scattered_clans.map (TO CREATE)
├── 07_naga_alliance.map (TO CREATE)
├── 08_frostwhisper_prophecy.map (TO CREATE)
├── 09_fall_of_the_north.map (TO CREATE)
├── 10_grimjaw_rising.map (TO CREATE)
├── 11_tombs_awakened.map (TO CREATE)
├── 12_darkness_spreads.map (TO CREATE)
├── 13_the_last_stand.map (TO CREATE)
├── 14_the_escape.map (TO CREATE)
└── 15_exodus.map (TO CREATE)
```

---

## Step-by-Step for Creating a Scenario

### 1. Choose Your Scenario
Pick any scenario from 1-15 based on:
- GitHub issue assigned to you (Issues #17-#31)
- Story phase alignment
- Your preference

### 2. Create the Map
1. Open Wesnoth Map Editor
2. Create a map appropriate to the scenario
3. Use the comprehensive tutorial in SCENARIO-CREATION-GUIDE.md
4. Save as: `##_scenario_name.map` in `campaigns/rise_of_the_frost_king/maps/`

Example: `01_the_ice_throne.map`

### 3. Create the Scenario Configuration
1. Create a new `.cfg` file
2. Follow the template in SCENARIO-CREATION-GUIDE.md or SCENARIO-REFERENCE.md
3. Configure:
   - Scenario ID and name
   - Map path reference
   - Player and enemy sides
   - Units and starting positions
   - Dialogue and events
   - Next scenario reference
4. Save as: `##_Scenario_Name.cfg` in `campaigns/rise_of_the_frost_king/scenarios/`

Example: `01_The_Ice_Throne.cfg`

### 4. Test the Scenario
1. Launch Wesnoth
2. Select "Rise of the Frost King" campaign
3. Play on Easy, Normal, and Hard difficulty
4. Verify:
   - Map loads correctly
   - Units appear properly
   - Dialogue displays
   - Victory/defeat conditions work
   - Next scenario loads

### 5. Verify Integration
Check that:
- [ ] File appears in campaign
- [ ] Previous scenario flows to this one
- [ ] This scenario flows to next one
- [ ] Map loads without errors
- [ ] All units spawn correctly

---

## Campaign Story Structure

### Part 1: The Discovery (Scenarios 1-3)
- Graksul discovers first ice settlements
- Frostwhisper's warnings begin
- Ice folk still believe they're safe

### Part 2: The First Strike (Scenarios 4-6)
- Orc leader Graksul returns
- First villages fall
- Realization of the threat

### Part 3: The Invasion Begins (Scenarios 7-9)
- Orcs ally with Naga
- Coastal settlements overrun
- Frostwhisper becomes a leader

### Part 4: Awakening the Dark (Scenarios 10-12)
- Grimjaw opens the Frozen Tombs
- Ancient evil awakens
- Common enemy emerges

### Part 5: The Price of Awakening (Scenarios 13-15)
- Desperate final battles
- Evacuation of survivors
- Campaign culmination

---

## Naming Conventions

### Scenario Files
```
##_Full_Name_With_Capitals_And_Underscores.cfg

Examples:
- 01_The_Ice_Throne.cfg
- 05_Coastal_Settlements.cfg
- 15_Exodus.cfg
```

### Map Files
```
##_full_name_with_lowercase_and_underscores.map

Examples:
- 01_the_ice_throne.map
- 05_coastal_settlements.map
- 15_exodus.map
```

**Important**: Map names must be lowercase!

---

## Expected File References

### In Campaign _main.cfg
```
first_scenario=01_The_Ice_Throne
```

### In Each Scenario File
```wml
map_file=~add-ons/wesnoth.iceage/campaigns/rise_of_the_frost_king/maps/##_scenario_name.map
```

### Between Scenarios
```wml
next_scenario=##_Next_Scenario_ID
```

Example flow:
```
01_The_Ice_Throne → next_scenario=02_Alliance_of_Ice
02_Alliance_of_Ice → next_scenario=03_The_Frozen_Army
... and so on ...
15_Exodus → (final scenario, no next_scenario needed)
```

---

## Key Documentation Files

### For Comprehensive Details
📖 **SCENARIO-CREATION-GUIDE.md** - 400+ lines of detailed instructions
- Map Editor full tutorial
- WML configuration guide
- Difficulty setup
- Integration checklist

### For Quick Reference
📋 **SCENARIO-REFERENCE.md** - Quick lookup reference
- File naming conventions
- Directory structure
- Campaign flow
- Checklist format

### For Implementation Status
📊 **SCENARIO-IMPLEMENTATION-SUMMARY.md** - Current status and what's needed
- What's been configured
- How loading works
- What needs creation
- Quick start guide

### In GitHub
🐙 **Issue #16** - Full requirements and guide in parent issue
- Comprehensive scenario creation guide
- Step-by-step process
- Expected names and paths
- Wesnoth map editor tutorial
- All requirements documented

---

## Support

### When Creating Scenarios

1. **Read SCENARIO-CREATION-GUIDE.md first** for comprehensive instructions
2. **Check SCENARIO-REFERENCE.md** for quick lookups
3. **Review your GitHub issue** for specific requirements
4. **Follow the templates** provided in the guides
5. **Test thoroughly** on all difficulty levels

### If Something Doesn't Load

Check:
1. File names match naming convention (capitalization matters!)
2. Files are in correct directories
3. Map path in scenario file is correct
4. No syntax errors in WML
5. Scenario is referenced in scenarios/_main.cfg (it already is)

### Useful Resources

- **Wesnoth Documentation**: https://wiki.wesnoth.org/
- **Map Editor Manual**: https://wiki.wesnoth.org/EditorManual
- **WML Reference**: https://wiki.wesnoth.org/WML
- **Scenario WML**: https://wiki.wesnoth.org/ScenarioWML

---

## Next Steps

1. ✓ Infrastructure set up (COMPLETE)
2. ✓ Documentation created (COMPLETE)
3. ✓ GitHub issues assigned (COMPLETE)
4. → **Start creating scenarios** (NetzerGeraldino)
5. → Test each scenario when complete
6. → Mark GitHub issues as complete

---

## Quick Checklist for Each Scenario

- [ ] GitHub issue assigned to you
- [ ] Story requirements understood from issue
- [ ] Map created in Map Editor
- [ ] Map saved in correct location with correct name
- [ ] Scenario .cfg file created
- [ ] All required WML fields filled in
- [ ] Scenario file saved in correct location with correct name
- [ ] Tested on Easy difficulty
- [ ] Tested on Normal difficulty
- [ ] Tested on Hard difficulty
- [ ] Previous scenario flows to this one
- [ ] This scenario flows to next one
- [ ] GitHub issue marked as complete

---

## Campaign Status

**Total Scenarios**: 15
**Scenarios Complete**: 0
**Infrastructure**: ✓ Complete
**Documentation**: ✓ Complete
**Campaign Ready For**: Scenario Creation

---

**All infrastructure is in place. Ready for scenario creation to begin!**
