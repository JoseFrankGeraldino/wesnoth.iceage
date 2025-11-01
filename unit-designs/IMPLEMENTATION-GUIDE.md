# Unit Implementation Guide - Ice Age Addon

**Status**: Development & Implementation Planning
**Last Updated**: October 30, 2025

---

## 📋 Overview

This document outlines the complete implementation requirements for converting unit design documents into playable Wesnoth units. It serves as both a reference guide and a development checklist for the Ice Age addon.

Based on official Wesnoth documentation:
- [BuildingUnits](https://wiki.wesnoth.org/BuildingUnits)
- [AddonStructure](https://wiki.wesnoth.org/AddonStructure)
- [UnitTypeWML](https://wiki.wesnoth.org/UnitTypeWML)
- [Creating Unit Art](https://wiki.wesnoth.org/Creating_Unit_Art)

---

## 🏗️ Required Addon Structure

### Current Repository Structure (unit-designs folder)
```
unit-designs/
├── README.md (master documentation)
├── IMPLEMENTATION-GUIDE.md (this file)
├── [unit-line-name]/
│   └── [unit-line]-design.md (design documentation)
```

### Required Deployment Structure (add-ons folder)
```
add-ons/wesnoth.iceage/
├── _main.cfg (entry point)
├── units/
│   ├── _main.cfg (units collection loader)
│   ├── frost_clans.cfg (Frost Clans unit definitions)
│   └── ice_dwellers.cfg (Ice Dwellers unit definitions)
├── images/
│   ├── units/
│   │   ├── [faction-name]/
│   │   │   ├── [unit-name]-base.png (base idle frame)
│   │   │   ├── [unit-name]-attack[1-6].png (attack frames)
│   │   │   ├── [unit-name]-defend.png (defense frame)
│   │   │   └── [unit-name]-variations/ (optional)
│   │   └── ... (more unit images)
│   ├── attacks/
│   │   ├── [attack-name].png (attack icons)
│   │   └── ... (more attack icons)
│   ├── portraits/
│   │   ├── [unit-name].webp (large portrait 300x300)
│   │   ├── transparent/
│   │   │   └── [unit-name]-transparent.webp (portrait no background)
│   │   └── ... (more portraits)
│   └── halo/
│       └── ... (optional magical effects)
├── sounds/
│   ├── [unit-name]-die.ogg (death sound)
│   └── ... (more sound effects)
└── factions/
    └── [faction-name].cfg (faction configuration)
```

---

## 📝 Implementation Checklist by Unit

### Template for Each Unit Line

For **each unit line** (e.g., Bear Rider, Yeti, Fire Spirit), complete the following:

#### 1. **Configuration Files** ❌→⚙️→✅

**Location**: `units/[faction].cfg`

For each unit in the line, create WML configuration with:

```wml
[unit_type]
    id=[unique_id]
    name= _ "[Display Name]"
    race=[race_type]
    image="units/[faction]/[unit-name].png"
    profile="portraits/[unit-name].webp"
    hitpoints=[hp_value]
    movement_type=[movement_type]
    movement=[movement_points]
    experience=[experience_requirement]
    level=[unit_level]
    alignment=[alignment]
    advances_to=[next_unit_id]
    cost=[recruitment_cost]
    usage=[usage_type]
    description= _ "[Description text]"
    die_sound=[sound_file]
    
    # Movement/Defense
    [movement_costs]
        [terrain_name]=[cost]
    [/movement_costs]
    [defense]
        [terrain_name]=[defense_percent]
    [/defense]
    [resistance]
        [damage_type]=[resistance_percent]
    [/resistance]
    
    # Attacks
    [attack]
        name=[attack_name]
        description= _ "[Attack Display Name]"
        type=[damage_type]
        range=[attack_range]
        damage=[damage_value]
        number=[number_of_attacks]
        [specials]
            # Special attack properties
        [/specials]
    [/attack]
    
    # Abilities
    [abilities]
        # Unit abilities and special mechanics
    [/abilities]
    
    # Animations
    [attack_anim]
        [filter_attack]
            name=[attack_name]
        [/filter_attack]
        # Animation frames and timing
    [/attack_anim]
    
[/unit_type]
```

**Required for each unit:**
- ✅ Unique `id` attribute (no spaces, use underscores)
- ✅ Translatable `name` attribute
- ✅ All stat values (hp, movement, cost, etc.)
- ✅ At least one `[attack]` definition
- ✅ Proper `advances_to` or `advances_to=null` setup
- ✅ Audio reference (`die_sound`)

---

#### 2. **Unit Images** 🎨

**Location**: `images/units/[faction]/`

Each unit requires multiple image files:

##### 2a. Base Idle Frame
- **File**: `[unit-name].png`
- **Format**: PNG-32 (transparent)
- **Canvas Size**: 72×72 pixels (standard hex size)
- **Specifications**:
  - Centered horizontally in hex
  - Feet at approximately 55 pixels from top
  - Light source from artist's upper right
  - Unit faces lower right direction
  - Dark blue shadow at 60% opacity
  - No pure black outlines (#000000 prohibited)
  - Consistent naming with mainline units

##### 2b. Attack Animation Frames
- **Files**: `[unit-name]-attack[1-N].png` (minimum 4 frames, optimal 6)
- **Format**: PNG-32 (transparent)
- **Canvas Size**: 72×72 pixels
- **Specifications**:
  - Sequential animation frames
  - Progressive weapon motion
  - Number frames based on attack type
  - Directional attacks for straight motions (spears, etc.)

##### 2c. Defense Frame
- **File**: `[unit-name]-defend.png`
- **Format**: PNG-32 (transparent)
- **Canvas Size**: 72×72 pixels
- **Specifications**:
  - Unit in defensive/bracing stance
  - Optional separate ranged vs melee versions
  - Usually 2 frames if animated

##### 2d. Unit Portrait (Profile Image)
- **File**: `portraits/[unit-name].webp` (300x300+ pixels)
- **Format**: WebP (or PNG for transparency)
- **Specifications**:
  - Large format for unit information dialog
  - High quality, detailed appearance
  - Automatic scaling if ≥300px width/height

##### 2e. Small Portrait
- **File**: `portraits/transparent/[unit-name]-transparent.webp`
- **Format**: WebP with transparency
- **Specifications**:
  - Smaller version for help system
  - No background/transparent
  - Used when main portrait is unavailable

##### 2f. Attack Icons
- **File**: `attacks/[attack-name].png`
- **Format**: PNG-32 (transparent)
- **Canvas Size**: 16×16 or 32×32 pixels
- **Specifications**:
  - Small icon representing attack type
  - Displayed in attack dialogs
  - Weapon or attack type imagery

---

#### 3. **Sound Effects** 🔊

**Location**: `sounds/`

**Required Sounds**:
- `[unit-name]-die.ogg` - Death sound (OGG Vorbis format)

**Optional Sounds**:
- `[unit-name]-hit.ogg` - Hit impact sound
- `[unit-name]-miss.ogg` - Miss/dodge sound
- `[attack-name]-hit.ogg` - Attack-specific sounds

---

#### 4. **Animation Definitions** 🎬

Embedded in `.cfg` files via `[attack_anim]` and related tags.

**Required Animations**:
1. **Idle/Base**: Default standing animation (1 frame)
2. **Movement**: Walking/moving animation (4-6 frames)
3. **Attack**: Melee/ranged attack animation (per attack type)
4. **Defense**: Defensive/hit reaction (2-3 frames)
5. **Death**: Death/defeat animation (4-6 frames)
6. **Advance**: Leveling up animation (optional, 4 frames)

**WML Syntax Example**:
```wml
[attack_anim]
    [filter_attack]
        name=[attack_name]
    [/filter_attack]
    offset=0.0~-0.1,-0.1~0.4,0.4~0.5,0.5~0.4,0.4~0.2,0.2~0.0
    start_time=-300
    [frame]
        image="units/[faction]/[unit-name]-attack[1~6].png:[100*2,250]"
    [/frame]
    {SOUND:HIT_AND_MISS [sound].ogg {SOUND_LIST:MISS} -100}
    [frame]
        image="units/[faction]/[unit-name].png:100"
    [/frame]
[/attack_anim]
```

---

#### 5. **Movement Type Definition** 🚶

**Location**: `units/[faction].cfg` or shared units file

Define or reference movement types:
```wml
[movetype]
    name=[movetype_name]
    [movement_costs]
        flat=1
        frozen=1
        forest=2
        mountain=3
        # ... other terrains
    [/movement_costs]
    [defense]
        flat=40
        frozen=40
        forest=60
        mountain=50
        # ... other terrains
    [/defense]
    [resistance]
        blade=0
        cold=10
        fire=0
        # ... other damage types
    [/resistance]
[/movetype]
```

---

#### 6. **Race Definition** (if custom race needed)

**Location**: `units/[faction].cfg`

```wml
[race]
    id=[race_name]
    name= _ "[Race Display Name]"
    plural= _ "[Plural Name]"
    icon=misc/race-[race_name].png
    description= _ "[Description]"
    
    [traits]
        [trait]
            id=[trait_name]
            name= _ "[Trait Name]"
            description= _ "[Trait Effect]"
            [effect]
                apply_to=[stat]
                increase=[value]
            [/effect]
        [/trait]
    [/traits]
[/race]
```

---

## 🎯 Development Progress Matrix

### Unit Line Implementation Status

| Unit Line | Design Doc | Config Files | Base Images | Attack Frames | Defense Frame | Portraits | Sounds | Animations | Status |
|-----------|-----------|----------|-----------|-----------|----------|----------|--------|-----------|--------|
| **Bear Rider** | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Design |
| **Pack Rider** | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Design |
| **Iceborn Warrior** | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Design |
| **Tundra Scout** | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Design |
| **Walrus Rider** | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Design |
| **Fire Spirit** | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Design |
| **Ice Spirit** | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Design |
| **Darkness Spirit** | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Design |
| **Yeti** | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Design |
| **Iceguard Spearman** | 📝 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Planning |
| **Winterheart Shaman** | 📝 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Planning |
| **Snowfall Trapper** | 📝 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Planning |
| **Crystalborn Elemental** | 📝 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Planning |
| **Glacial Wraith** | 📝 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Planning |
| **Permafrost Beast** | 📝 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Planning |
| **Shimmer Sprite** | 📝 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Planning |
| **Hoarfrost Mage** | 📝 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Planning |
| **Icewall Guardian** | 📝 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Planning |
| **Coldmist Stalker** | 📝 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Planning |

**Legend**:
- ✅ Completed
- ⚙️ In Progress
- ❌ Not Started
- 📝 Planning Phase

---

## 🔄 Development Workflow: Design to Deployment

### Phase 1: Design Documentation ✅ (COMPLETE)
- [x] Create comprehensive unit design documents
- [x] Define all unit stats and abilities
- [x] Establish progression chains
- [x] Document combat roles and synergies
- [x] Finalize faction assignments

**Output**: `unit-designs/[unit-line]/[unit-line]-design.md` files

---

### Phase 2: Configuration Creation ⚙️ (READY TO START)

#### 2.1 Create Base Unit Configuration Files
**Location**: Source in `unit-designs/[unit-line]/cfg/`
**Deploy to**: `units/[faction].cfg`

Steps:
1. Create `unit-designs/[unit-line]/cfg/` folder for each unit line
2. Write WML `[unit_type]` definitions for all unit levels
3. Define progression chains (`advances_to` attributes)
4. Reference movement types and attack definitions
5. Include placeholder image paths (actual images created in Phase 3)

**Deliverable**: Complete `.cfg` files with all unit definitions

---

### Phase 3: Visual Assets Creation 🎨 (READY TO START)

#### 3.1 Sprite Art
1. Create pixel art for each unit (72×72 canvas)
2. Generate attack animation frames (4-6 frames per attack)
3. Create defense animation frames
4. Optimize all PNG files (transparent background)

**Tools Needed**: Aseprite, GIMP, or similar pixel art editor

#### 3.2 Portrait Art
1. Create high-resolution portraits (300x300+ pixels)
2. Create small transparent variants
3. Optimize WebP format

#### 3.3 Attack Icons
1. Create 16×16 or 32×32 attack icons
2. Ensure clarity at small scales

**Deliverable**: All image files organized in `images/units/` structure

---

### Phase 4: Audio Integration 🔊 (READY TO START)

1. Source or create death sounds (OGG Vorbis format)
2. Record attack sounds (impact, whoosh, magical effects)
3. Record unit-specific audio cues
4. Optimize audio files for game

**Location**: `sounds/`

---

### Phase 5: Animation Definition 🎬 (READY TO START)

1. Map image files to animation frames in WML
2. Define frame timing and transitions
3. Link animations to attacks and abilities
4. Test animation smoothness and timing

**Location**: `[attack_anim]` and `[defense_anim]` tags in `.cfg` files

---

### Phase 6: Deployment & Integration 📦

#### 6.1 Create Deployment Script
Create `deploy.sh` or `deploy.ps1`:

```bash
#!/bin/bash
# Copy configuration files
cp units/*.cfg ../../units/

# Copy images
cp -r images/* ../../images/

# Copy sounds
cp -r sounds/* ../../sounds/

# Update permissions and test
echo "Deployment complete!"
```

#### 6.2 Update Main Addon Files
1. Update `_main.cfg` to include new unit collections
2. Update faction files to recruit units
3. Update era files to enable in multiplayer

#### 6.3 Testing
1. Load addon in Wesnoth
2. Test unit recruitment in scenarios
3. Verify advancement chains
4. Test all attacks and animations
5. Check portrait displays

---

## 📂 File Organization Summary

### In unit-designs (Source)
```
unit-designs/
├── [unit-line-name]/
│   ├── [unit-line]-design.md (design doc - COMPLETE ✅)
│   ├── cfg/
│   │   └── [unit-line].cfg (unit WML definitions - TODO)
│   ├── images/
│   │   ├── [unit-name]-base.png (72×72 idle - TODO)
│   │   ├── [unit-name]-attack[1-6].png (attack frames - TODO)
│   │   ├── [unit-name]-defend.png (defense frame - TODO)
│   │   └── portraits/
│   │       ├── [unit-name].webp (main portrait - TODO)
│   │       └── [unit-name]-small.webp (small portrait - TODO)
│   ├── sounds/
│   │   └── [unit-name]-die.ogg (death sound - TODO)
│   ├── attacks/
│   │   └── [attack-name].png (attack icon - TODO)
│   └── notes.md (implementation notes - optional)
```

### In add-ons (Deployed)
```
add-ons/wesnoth.iceage/
├── units/
│   ├── frost_clans.cfg
│   ├── ice_dwellers.cfg
│   └── _main.cfg
├── images/
│   ├── units/
│   │   ├── frost_clans/
│   │   │   ├── [all base PNGs]
│   │   │   ├── [all attack frames]
│   │   │   └── [all defense frames]
│   │   ├── ice_dwellers/
│   │   │   └── [same structure]
│   │   ├── portraits/
│   │   │   ├── [all webp portraits]
│   │   │   └── transparent/
│   │   │       └── [all transparent webps]
│   │   └── attacks/
│   │       └── [all attack icons]
│   └── ...
├── sounds/
│   └── [all OGG files]
└── ...
```

---

## 🛠️ Tools & Resources

### Required Tools
- **Text Editor**: VS Code (with WML syntax highlighting extension)
- **Pixel Art Editor**: Aseprite (paid), GIMP (free), Piskel (web-based free)
- **Image Optimization**: ImageOptim, OptiPNG, PNGQuant
- **Audio**: Audacity (recording/editing), ffmpeg (conversion to OGG)
- **Version Control**: Git (track changes across development)

### Recommended VS Code Extensions
- WML Syntax Highlighter
- PNG/Image preview
- YAML/Config formatting

### Reference Materials
- [Wesnoth Wiki - BuildingUnits](https://wiki.wesnoth.org/BuildingUnits)
- [Wesnoth Wiki - UnitTypeWML](https://wiki.wesnoth.org/UnitTypeWML)
- [Wesnoth Wiki - AnimationWML](https://wiki.wesnoth.org/AnimationWML)
- [Wesnoth Wiki - Creating Unit Art](https://wiki.wesnoth.org/Creating_Unit_Art)
- Official Wesnoth game data: `C:\games\steam\steamapps\common\wesnoth\data\core\units\`

---

## 📋 Priority Implementation Order

### Tier 1: Core Units (Start First)
1. **Bear Rider** (iconic Frost Clans unit)
2. **Walrus Rider** (unique amphibious mechanic)
3. **Yeti** (legendary centerpiece unit)

### Tier 2: Essential Support
4. **Fire Spirit** (elemental balance)
5. **Ice Spirit** (faction availability)
6. **Darkness Spirit** (Ice Dwellers identity)

### Tier 3: Secondary Units
7. **Iceborn Warrior** (core unit)
8. **Tundra Scout** (core unit)
9. **Pack Rider** (core unit)

### Tier 4: Planning Phase (Later)
10. Remaining planned units (Shaman, Spearman, etc.)

---

## ✅ Validation Checklist

Before deploying any unit, verify:

- [ ] Unique unit `id` (no duplicates, no spaces)
- [ ] All required stats present (HP, cost, movement)
- [ ] At least one valid attack definition
- [ ] Image files exist at correct paths (72×72 PNG)
- [ ] Attack animation frames numbered sequentially
- [ ] Sound files in OGG Vorbis format
- [ ] Portrait images present (300x300 minimum)
- [ ] Advancement chains properly linked
- [ ] Unit loads without WML errors in-game
- [ ] Unit appears in recruit menu
- [ ] Advancement works correctly
- [ ] Animations play smoothly
- [ ] Unit stats match design document
- [ ] Attack damage calculations correct
- [ ] Terrain modifiers working (movement, defense)

---

## 🚀 Quick Start: Next Steps

1. **Choose first unit line** to implement (recommend: Bear Rider)
2. **Create `units/frost_clans.cfg`** with first unit WML
3. **Create placeholder images** (simple 72×72 PNGs with unit name)
4. **Test in Wesnoth** to verify loading
5. **Iteratively improve** (replace placeholders with real art)
6. **Deploy** via script to addon folder
7. **Repeat** for remaining units

---

## 📞 References & Support

- **Official Wesnoth Forums**: https://forums.wesnoth.org/
- **Wesnoth Wiki Main Page**: https://wiki.wesnoth.org/
- **WML Reference**: https://wiki.wesnoth.org/ReferenceWML
- **Add-on Development Forum**: https://forums.wesnoth.org/viewforum.php?f=8

---

**Document Version**: 1.0
**Last Updated**: October 30, 2025
**Status**: Complete Implementation Guide Ready
**Next Update**: After Phase 2 (Configuration Creation)
