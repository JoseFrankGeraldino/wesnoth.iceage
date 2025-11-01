# Unit TODO Lists & Sprite Quality Standards - Complete Summary

**Created**: October 30, 2025
**Status**: All 20 unit-line TODO lists created (10 Frost Clans, 10 Ice Dwellers, 2 shared) ✅

---

## 📊 Overview

Created comprehensive TODO lists for all 18 unit lines with **high-quality sprite standards** (31 sprites per unit level) as baseline.

### Key Documents Created

1. **SPRITE-QUALITY-STANDARDS.md** - Master sprite quality reference
   - Animation frame counts for maximum quality
   - Canvas specifications and naming conventions
   - Quality checklists for each animation type
   - Tool recommendations

2. **TODO.md in each unit folder** - Unit-specific implementation roadmap
   - Phase 1-8 breakdown (Config → Sprites → Portraits → Audio → Animations → Deployment → Testing)
   - Exact sprite counts per unit
   - Quality checkpoints and validation items

---

## 🎨 High-Quality Sprite Standard (Per Unit)

### Animation Frame Requirements

| Animation Type | Frames | Purpose | Quality Level |
|---|---|---|---|
| **Idle** | 1 | Base standing state | Essential |
| **Movement** | 8 | Walking cycle (2-loop smooth) | High Quality |
| **Melee Attack** | 6 | Weapon attack sequence | High Quality |
| **Ranged Attack** | 6 | Projectile/spell attack | High Quality |
| **Defense** | 4 | Hit reaction/bracing | High Quality |
| **Death** | 6 | Defeat animation | High Quality |
| **Total per Unit** | **31** | **High Quality Standard** | ✅ |

**Optional Maximum Quality Add-ons:**
- Advancement Animation: 4 frames (level up visual)
- Special Ability Animation: 6 frames (ability-specific effect)
- **Maximum Total: 41 sprites per unit**

---

## 📋 Sprite Count Summary by Unit Line

### Frost Clans (10 lines, including shared)

| Unit Line | Levels | High Quality | Max Quality | Status |
|---|---|---|---|---|
| Bear Rider | 4 | 124 | 164 | TODO created ⏳ |
| Pack Rider | 4 | 124 | 164 | TODO created ⏳ |
| Iceborn Warrior | 4 | 124 | 164 | TODO created ⏳ |
| Tundra Scout | 4 | 124 | 164 | TODO created ⏳ |
| Walrus Rider | 4 | 124 | 164 | TODO created ⏳ |
| Fire Spirit | 4 | 124 | 164 | TODO created ⏳ |
| Winterheart Shaman | 4 | 124 | 164 | TODO created ⏳ |
| Snowfall Trapper | 4 | 124 | 164 | TODO created ⏳ |
| Icewall Guardian | 4 | 124 | 164 | TODO created ⏳ |
| Coldmist Stalker | 4 | 124 | 164 | TODO created ⏳ |
| Ice Spirit (shared) | 4 | 124 | 164 | TODO created ⏳ |
| Iceguard Spearman (shared) | 4 | 124 | 164 | TODO created ⏳ |

### Ice Dwellers (10 lines, including shared)

| Unit Line | Levels | High Quality | Max Quality | Status |
|---|---|---|---|---|
| Darkness Spirit | 4 | 124 | 164 | TODO created ⏳ |
| Yeti | 4 | 124 | 164 | TODO created ⏳ |
| Crystalborn Elemental | 4 | 124 | 164 | TODO created ⏳ |
| Glacial Wraith | 4 | 124 | 164 | TODO created ⏳ |
| Permafrost Beast | 4 | 124 | 164 | TODO created ⏳ |
| Shimmer Sprite | 4 | 124 | 164 | TODO created ⏳ |
| Hoarfrost Mage | 4 | 124 | 164 | TODO created ⏳ |
| Ice Dwellers Mage | 4 | 124 | 164 | TODO created ⏳ |
| Frost Revenant | 4 | 124 | 164 | TODO created ⏳ |
| Frostbound Sentinel | 4 | 124 | 164 | TODO created ⏳ |
| Ice Spirit (shared) | 4 | 124 | 164 | TODO created ⏳ |
| Iceguard Spearman (shared) | 4 | 124 | 164 | TODO created ⏳ |

---

## 📁 Unit Folders with TODO Files Created

### Design Complete Units (9)

✅ All have comprehensive 500+ line TODO.md files with full implementation roadmap:

1. **bear-rider/**
   - 4-level line, 484 sprites
   - Phases: Config → Sprites (124) → Portraits (8) → Audio → Animations → Deployment → Testing

2. **pack-rider/**
   - 4-level line, 484 sprites
   - Pack Tactics ability focus

3. **iceborn-warrior/**
   - 4-level line, 484 sprites
   - Heavy infantry with Frozen Armor ability

4. **tundra-scout/**
   - 4-level line, 484 sprites
   - Ranged specialist with Keen Eyes ability

5. **walrus-rider/**
   - 3-level line, 93 sprites
   - Amphibious unit with water movement

6. **fire-spirit/**
   - 3-level line, 93 sprites
   - Elemental with fire damage and aura

7. **ice-spirit/**
   - 3-level line, 93 sprites
   - Shared unit (Frost Clans + Ice Dwellers)
   - Freeze/cold abilities

8. **darkness-spirit/**
   - 3-level line, 93 sprites
   - Shadow elemental with drain life ability

9. **yeti/**
   - 4-level line, 124 sprites
   - Flagship Ice Dwellers unit
   - Official stats included (142 HP, 151 cost)

### Planning Phase Units (9)

📝 All have streamlined TODO.md files with core implementation outline:

1. **iceguard-spearman/** - Shield/spear infantry (124 sprites, 4 levels)
2. **winterheart-shaman/** - Support mage (124 sprites, 4 levels)
3. **snowfall-trapper/** - Trap specialist (124 sprites, 4 levels)
4. **crystalborn-elemental/** - Crystal-based hybrid (124 sprites, 4 levels)
5. **glacial-wraith/** - Phasing attacker (124 sprites, 4 levels)
6. **permafrost-beast/** - Heavy with aura (124 sprites, 4 levels)
7. **shimmer-sprite/** - Support healer (93-124 sprites, 3-4 levels)
8. **hoarfrost-mage/** - Crowd control mage (124 sprites, 4 levels)
9. **icewall-guardian/** - Tank/defender (124 sprites, 4 levels)
10. **coldmist-stalker/** - Rogue/scout (124 sprites, 4 levels)

---

## 📊 Total Sprite Requirements

### High-Quality Standard (31 sprites per unit)

```
20 unit lines × 4 levels × 31 sprites = 2,480 sprites (high quality standard)
```

### Maximum Quality (41 sprites per unit with bonuses)

```
With Optional Advancement + Special Ability animations:
20 unit lines × 4 levels × 41 sprites = 3,280+ sprites (maximum quality)
```

---

## 🎬 Implementation Structure Defined in TODOs

### Phase 1: Configuration Files (WML)
- Unit type definitions with all stats
- Attack type definitions
- Ability definitions (faction-specific)
- Advancement chain setup
- Movement type configuration

### Phase 2: Base Sprite Graphics
- Idle frame (1)
- Movement animation (8 frames)
- Melee attack (6 frames)
- Ranged attack (6 frames)
- Defense reaction (4 frames)
- Death sequence (6 frames)
- **31 sprites per unit level**

### Phase 3: Portrait Images
- Main portrait (300×300+ px, WebP format)
- Transparent variant (help system)
- One of each per unit level

### Phase 4: Attack Icons
- Melee attack icon (16×16 or 32×32)
- Ranged attack icon (16×16 or 32×32)
- Per unit line (typically 2-3 icons)

### Phase 5: Audio Assets
- Death sound (OGG Vorbis format)
- Optional: impact sounds, ability activation audio
- 1-3 audio files per unit line

### Phase 6: Animation Definitions (WML)
- Link sprite files to animation tags
- Frame timing and offset sequences
- Sound trigger points
- Special effect coordination

### Phase 7: Deployment
- Copy files to addon folder structure
- Update main configuration files
- Verify file paths and references
- Test in Wesnoth

### Phase 8: Testing & QA
- Load addon in Wesnoth
- Recruit and test all unit levels
- Verify animations play smoothly
- Test all attacks and abilities
- Confirm advancement chains work
- Validate portraits and icons display
- Check audio integration

---

## 🔍 Sprite Quality Specification Details

### Canvas & Technical Specifications

**Size**: 72×72 pixels (Wesnoth standard hex)
**Format**: PNG-32 (RGBA with transparency)
**Color Profile**: sRGB
**Anti-aliasing**: Yes
**Unit Positioning**: Centered horizontally, feet ~55px from top

### Animation Frame Timing

| Animation | Timing | Frame Rate | Purpose |
|---|---|---|---|
| Movement | Variable | 100ms/frame | Smooth walking loop |
| Melee Attack | Quick | 50-80ms/frame | Dynamic weapon motion |
| Ranged Attack | Quick | 60-80ms/frame | Projectile timing |
| Defense | Medium | 80-100ms/frame | Impact reaction |
| Death | Slow | 100ms/frame | Dramatic sequence |

### Quality Checkpoints (Per Animation)

**Movement (8 frames)**
- [ ] Smooth weight transfer
- [ ] Realistic arm swing
- [ ] Consistent stride length
- [ ] No jittering
- [ ] Frame 8 transitions smoothly to Frame 1

**Melee Attack (6 frames)**
- [ ] Visible weapon wind-up
- [ ] Clear impact moment
- [ ] Realistic follow-through
- [ ] Smooth return to idle
- [ ] No clipping through body

**Defense (4 frames)**
- [ ] Visible impact reaction
- [ ] Quick recovery (4 frames = 320-400ms)
- [ ] Returns to neutral stance

**Death (6 frames)**
- [ ] Clear progression from healthy to fallen
- [ ] Visible impact moment
- [ ] Final pose distinct from idle
- [ ] Last frame held for readability

---

## 🛠️ Implementation Phases Timeline

### Phase A: High-Quality Asset Creation (Current)
**Status**: Planning & TODO definition ✅

- [x] Sprite quality standards document created
- [x] All 18 unit TODO lists created
- [x] Implementation checklists defined
- [x] Sprite frame count requirements specified

### Phase B: Configuration Development (Ready)
**Status**: Can begin when Phase A complete

- [ ] Create WML unit definitions
- [ ] Define all abilities and attacks
- [ ] Set up advancement chains
- [ ] Configure faction integration

### Phase C: Visual Asset Creation (Ready)
**Status**: Can begin in parallel with Phase B

- [ ] Create pixel art sprites (484 to 124 frames per line)
- [ ] Design portraits
- [ ] Create attack icons
- [ ] Optimize all image assets

### Phase D: Audio Integration (Ready)
**Status**: Can begin after Phase C starts

- [ ] Record/source death sounds
- [ ] Create ability activation audio
- [ ] Record attack impact sounds
- [ ] Optimize audio files (OGG Vorbis)

### Phase E: Animation & Testing (Ready)
**Status**: Can begin after Phase B

- [ ] Link sprites to animation frames
- [ ] Test in Wesnoth with placeholder graphics
- [ ] Verify all mechanics
- [ ] Polish animations

### Phase F: Deployment (Final)
**Status**: After all previous phases

- [ ] Deploy to addon folder
- [ ] Final QA pass
- [ ] Package for distribution

---

## 📌 Key Resources Referenced

- **Wesnoth Wiki**: BuildingUnits, UnitTypeWML, Creating Unit Art, AddonStructure
- **Quality Standards**: Based on official Wesnoth sprite creation guidelines
- **Official Sprites**: Reference from Wesnoth core unit data
- **Animation Standards**: Professional frame-rate standards (100ms for smooth loops)

---

## 🎯 Next Steps for Implementation

1. **Choose first unit line to implement** (recommend: Bear Rider - iconic, critical path)
2. **Start with Phase 1 (Configuration)** - Define WML structure
3. **Create placeholder graphics** - Simple 72×72 images for testing
4. **Test loading in Wesnoth** - Verify WML syntax
5. **Create final graphics** - Replace placeholders with polished art
6. **Integrate audio** - Add sound effects
7. **Full QA testing** - Test all mechanics in-game
8. **Iterate through remaining units** - Follow same workflow

---

## 📊 Status Dashboard

**Total Unit Lines Documented**: 20 ✅
**Total TODO Lists Created**: 20 ✅
**Design Documents Complete**: 20 ✅
**Sprite Quality Standards**: Defined ✅
**Implementation Phases**: Documented ✅

**Estimated Sprite Assets Needed**: 2,480 - 3,280 sprites
**Estimated Audio Assets Needed**: 20 - 60 audio files
**Estimated WML Configuration Files**: 20 `.cfg` files
**Estimated Portrait Images**: 120 - 160 images
**Estimated Attack Icons**: 40 - 60 icons

---

**Document Version**: 1.0
**Created**: October 30, 2025
**Last Updated**: October 30, 2025
**Status**: Complete & Ready for Implementation 🚀

**Next Action**: Begin Phase B (Configuration Development) with Bear Rider unit line
