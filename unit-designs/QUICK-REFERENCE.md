# Unit-Designs Folder - Master Index & Quick Reference

**Last Updated**: October 31, 2025
**Status**: All 20 unit lines (10 Frost Clans, 10 Ice Dwellers, 2 shared) documented with implementation TODOs ✅

---

## 📚 Documentation Files in This Folder

### Core Reference Documents

1. **README.md** - Main unit-designs overview with combat matrix
2. **IMPLEMENTATION-GUIDE.md** - Complete 8-phase implementation workflow
3. **SPRITE-QUALITY-STANDARDS.md** - High-quality sprite specifications (31 frames/unit)
4. **TODO-SUMMARY.md** - This master summary with sprite counts and timeline

---

## 🎯 Quick Access by Unit

### ✅ Design Complete (20 unit lines: 10 Frost Clans, 10 Ice Dwellers, 2 shared)

#### Frost Clans (10 lines, including shared)

| Unit Line | Folder | Design | TODO | Levels | Sprites |
|---|---|---|---|---|---|
| **Bear Rider** | `bear-rider/` | ✅ | ✅ | 4 | 124 |
| **Pack Rider** | `pack-rider/` | ✅ | ✅ | 4 | 124 |
| **Iceborn Warrior** | `iceborn-warrior/` | ✅ | ✅ | 4 | 124 |
| **Tundra Scout** | `tundra-scout/` | ✅ | ✅ | 4 | 124 |
| **Walrus Rider** | `walrus-rider/` | ✅ | ✅ | 4 | 124 |
| **Fire Spirit** | `fire-spirit/` | ✅ | ✅ | 4 | 124 |
| **Winterheart Shaman** | `winterheart-shaman/` | ✅ | ✅ | 4 | 124 |
| **Snowfall Trapper** | `snowfall-trapper/` | ✅ | ✅ | 4 | 124 |
| **Icewall Guardian** | `icewall-guardian/` | ✅ | ✅ | 4 | 124 |
| **Coldmist Stalker** | `coldmist-stalker/` | ✅ | ✅ | 4 | 124 |
| **Ice Spirit** (shared) | `ice-spirit/` | ✅ | ✅ | 4 | 124 |
| **Iceguard Spearman** (shared) | `iceguard-spearman/` | ✅ | ✅ | 4 | 124 |

#### Ice Dwellers (10 lines, including shared)

| Unit Line | Folder | Design | TODO | Levels | Sprites |
|---|---|---|---|---|---|
| **Darkness Spirit** | `darkness-spirit/` | ✅ | ✅ | 4 | 124 |
| **Yeti** | `yeti/` | ✅ | ✅ | 4 | 124 |
| **Crystalborn Elemental** | `crystalborn-elemental/` | ✅ | ✅ | 4 | 124 |
| **Glacial Wraith** | `glacial-wraith/` | ✅ | ✅ | 4 | 124 |
| **Permafrost Beast** | `permafrost-beast/` | ✅ | ✅ | 4 | 124 |
| **Shimmer Sprite** | `shimmer-sprite/` | ✅ | ✅ | 4 | 124 |
| **Hoarfrost Mage** | `hoarfrost-mage/` | ✅ | ✅ | 4 | 124 |
| **Ice Dwellers Mage** | (planned) | ✅ | ✅ | 4 | 124 |
| **Frost Revenant** | (planned) | ✅ | ✅ | 4 | 124 |
| **Frostbound Sentinel** | (planned) | ✅ | ✅ | 4 | 124 |
| **Ice Spirit** (shared) | `ice-spirit/` | ✅ | ✅ | 4 | 124 |
| **Iceguard Spearman** (shared) | `iceguard-spearman/` | ✅ | ✅ | 4 | 124 |

**Subtotal**: 20 unit lines × 4 levels × 31 sprites/level = **2,480 sprites** (high quality)

---

### 📝 All Unit Lines Planned (20 lines)

All 20 unit lines (10 Frost Clans, 10 Ice Dwellers, 2 shared) have comprehensive TODOs and design documentation. Each line consists of 4 units (levels 1–4), and each unit requires 31 sprites for high quality.

---

## 🎨 Sprite Requirements at a Glance

### High-Quality Standard (31 sprites per unit)

```
Idle (1) + Movement (8) + Melee Attack (6) + Ranged Attack (6) + 
Defense (4) + Death (6) = 31 sprites per unit level
```

### Multiplication Table

| Unit Levels | Sprites/Level | Total per Line |
|---|---|---|
| 4 levels | 31 | 124 sprites |

### Current Project (High Quality)

- **20 unit lines**: 2,480 sprites

### With Optional Maximum Quality (add Advancement + Special Ability)

- 41 sprites per level (instead of 31)
- Additional 10 sprites per unit × 20 unit lines × 4 levels = 800 sprites
- **MAXIMUM TOTAL**: 3,280+ sprites

---

## 📋 TODO Structure in Each Folder

### Each unit folder contains:

1. **[unit-name]-design.md** - Comprehensive design specification (500+ lines)
   - Stats and progression
   - Combat roles and abilities
   - Lore and flavor text
   - Faction alignment

2. **TODO.md** - Implementation checklist (Phase 1-8)
   - Phase 0: Sprite quality prerequisite
   - Phase 1: Configuration files (WML)
   - Phase 2: Base sprites (124 sprites for 4-level line)
   - Phase 3: Portrait images (8 images)
   - Phase 4: Attack icons (2-3 images)
   - Phase 5: Audio assets (1-3 OGG files)
   - Phase 6: Animation definitions (WML)
   - Phase 7: Deployment
   - Phase 8: Testing & QA

### Completed Units
- 500+ line TODO with detailed sprite breakdown per level

### Planning Units
- Streamlined TODO with phase overview (ready for expansion)

---

## 🚀 Implementation Priority Order

### Tier 1: Flagship/Essential (Start Here)
1. **Bear Rider** - Iconic Frost Clans unit, charge mechanic core gameplay
2. **Walrus Rider** - Unique amphibious mechanic, franchise identity
3. **Yeti** - Legendary Ice Dwellers centerpiece

### Tier 2: Core Gameplay
4. **Fire Spirit** - Elemental variety, balance
5. **Ice Spirit** - Shared unit, both factions
6. **Darkness Spirit** - Ice Dwellers identity

### Tier 3: Supporting Units
7. **Iceborn Warrior** - Heavy melee core
8. **Tundra Scout** - Ranged core
9. **Pack Rider** - Specialist mechanics

### Tier 4: Planning Phase (Later)
10-18. Planning phase units (complete detailed design first)

---

## 📊 Resource Checklist

### Per Completed Unit (9 units done)

- [x] Design document (500+ lines) ✅
- [x] TODO list (Phase 1-8) ✅
- [x] Sprite frame count specified (31/unit level) ✅
- [ ] Configuration file (.cfg)
- [ ] 31 sprite PNGs per level
- [ ] 4-8 portrait images
- [ ] 2-3 attack icons
- [ ] 1-3 audio files (OGG)
- [ ] Animation WML definitions
- [ ] In-game testing

### Per Planning Unit (9 units)

- [x] Design overview ✅
- [x] TODO stub (Phase 1-5) ✅
- [x] Sprite estimate (31/unit level) ✅
- [ ] Complete design document
- [ ] Configuration file
- [ ] Assets (sprites, audio, icons)
- [ ] Animation definitions
- [ ] Testing

---

## 🔍 File Naming Conventions

### Design Documents
```
[unit-line-name]-design.md
Example: bear-rider-design.md
```

### Implementation TODOs
```
TODO.md (in each unit folder)
```

### Sprite Files (Target Structure)
```
images/units/[faction]/[unit-name]-[level]-[animation][frame].png
Example: images/units/frost_clans/bear-rider-champion-move1.png
```

### Audio Files (Target Structure)
```
sounds/[unit-name]-die.ogg
Example: sounds/bear-rider-die.ogg
```

### Configuration Files (Target Structure)
```
units/[faction].cfg
Example: units/frost_clans.cfg
```

---

## 🎬 Animation Frame Reference

### Standard Animation Breakdown (31 frames per unit)

| Animation | Count | Notes |
|---|---|---|
| Idle | 1 | Static, standing pose |
| Movement | 8 | Full 2-cycle walk loop |
| Melee Attack | 6 | Wind-up, strike, follow-through, recovery |
| Ranged Attack | 6 | Aim, draw, release, follow-through, recovery |
| Defense | 4 | Neutral → impact → recovery → neutral |
| Death | 6 | Reaction → fall → impact → final pose (held) |

### Optional Maximum Quality Add-ons

| Animation | Count | Notes |
|---|---|---|
| Advancement | 4 | Level up visual effect |
| Special Ability | 6 | Ability-specific animation |

---

## ✅ Quality Assurance Checklist

### Before Starting Implementation
- [x] All 18 unit TODOs created ✅
- [x] Sprite quality standards documented ✅
- [x] Implementation phases defined ✅
- [x] Frame counts specified ✅
- [x] File naming conventions established ✅

### Before Creating Graphics
- [ ] Pixel art software installed (Aseprite/GIMP/Krita)
- [ ] Sound editing software installed (Audacity)
- [ ] 72×72 canvas template prepared
- [ ] Color palette defined for consistency

### Before Deployment
- [ ] All sprites created (31 per level)
- [ ] All audio recorded (OGG format)
- [ ] All WML configuration written
- [ ] Animations tested in Wesnoth
- [ ] All abilities functional
- [ ] No clipping or visual glitches

---

## 📞 Quick Reference Links

### In This Folder

- **IMPLEMENTATION-GUIDE.md** - How to convert designs → playable units
- **SPRITE-QUALITY-STANDARDS.md** - Technical specifications for sprites
- **TODO-SUMMARY.md** - Complete overview and timeline
- **README.md** - Combat matrix and unit relationships

### External Resources

- [Wesnoth BuildingUnits Wiki](https://wiki.wesnoth.org/BuildingUnits)
- [Wesnoth UnitTypeWML Wiki](https://wiki.wesnoth.org/UnitTypeWML)
- [Wesnoth AddonStructure Wiki](https://wiki.wesnoth.org/AddonStructure)
- [Wesnoth Creating Unit Art](https://wiki.wesnoth.org/Creating_Unit_Art)

---

## 🎯 Your Next Steps

1. **Choose implementation starting point** → Bear Rider (Tier 1)
2. **Open `bear-rider/TODO.md`** → Follow Phase 1 (WML Config)
3. **Read SPRITE-QUALITY-STANDARDS.md** → Understand sprite requirements
4. **Create placeholder graphics** → Simple test sprites
5. **Test in Wesnoth** → Verify loading and mechanics
6. **Iterate** → Replace placeholders with final art

---

## 📈 Project Statistics

**Total Unit Lines**: 20 (10 Frost Clans, 10 Ice Dwellers, 2 shared)
**Completed Designs**: 20 ✅
**Total Unit Levels**: 80
**Estimated Sprites**: 2,480 - 3,280
**Estimated Audio Files**: 20 - 60
**Estimated Configuration Files**: 20
**Estimated Portrait Images**: 120 - 160
**Estimated Attack Icons**: 40 - 60

---

**This is your central hub for Ice Age addon unit implementation.**
**All necessary documentation is linked above.** 
**Start with TODO.md in your chosen unit folder!** 🚀

---

**Created**: October 30, 2025
**Status**: Ready for Implementation
**Version**: 1.0
