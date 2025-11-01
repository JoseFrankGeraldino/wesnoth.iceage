# Pack Rider - Implementation TODO

**Unit Line**: Pack Rider (Frost Clans)
**Status**: Design Complete ✅ | Implementation Ready ⏳
**Design Document**: `pack-rider-line-design.md`

---

## 📋 Implementation Phases

### Phase 0: Prerequisite - Sprite Quality Standards

**Reference**: See `../SPRITE-QUALITY-STANDARDS.md` for complete specifications

**High-Quality Standard for Pack Rider** (31 sprites per unit level):

| Animation | Frames | Per Level | Total (4 levels) |
|-----------|--------|-----------|------------------|
| Idle | 1 | 4 | 4 |
| Movement | 8 | 32 | 128 |
| Melee Attack | 6 | 24 | 96 |
| Ranged Attack (Ranged) | 6 | 24 | 96 |
| Defense | 4 | 16 | 64 |
| Death | 6 | 24 | 96 |
| **TOTAL** | **31/unit** | **124/level** | **484 sprites** |

**TOTAL FOR PACK RIDER LINE**: 484 sprites (high quality)

---

## ✅ Phase 1: Configuration Files (WML)

- [ ] Create `cfg/pack-rider.cfg` with unit_type definitions
- [ ] Define all 4 unit levels (Pup, Pack Rider, Alpha, Pack Master)
- [ ] Create movement_type definition (swift, skirmisher)
- [ ] Define attack types:
  - [ ] Melee bite/slash attack (primary)
  - [ ] Ranged projectile attack (secondary)
- [ ] Define special abilities:
  - [ ] Pack Tactics (bonus when near allies)
  - [ ] Swift Strike (higher hit chance)
- [ ] Set up advancement chain (Pup → Pack Rider → Alpha → Pack Master)
- [ ] Configure cost, experience, HP, movement values
- [ ] Add unit-specific sounds reference:
  - [ ] `pack-rider-die.ogg` (death sound)

**Quality Checklist**:
- [ ] No duplicate unit IDs
- [ ] All required WML attributes present
- [ ] Advancement chain properly linked
- [ ] Stats match design document exactly

---

## 🎨 Phase 2: Base Sprite Graphics (484 sprites total)

**Specifications**: 72×72 PNG-32 (transparent), sRGB color profile

### Level 1: Pup
- [ ] `images/units/frost_clans/pack-rider-pup-idle.png` (1)
- [ ] `images/units/frost_clans/pack-rider-pup-move[1-8].png` (8)
- [ ] `images/units/frost_clans/pack-rider-pup-attack[1-6].png` (6)
- [ ] `images/units/frost_clans/pack-rider-pup-ranged[1-6].png` (6)
- [ ] `images/units/frost_clans/pack-rider-pup-defend[1-4].png` (4)
- [ ] `images/units/frost_clans/pack-rider-pup-death[1-6].png` (6)
**Subtotal**: 31 sprites

### Level 2: Pack Rider
- [ ] `images/units/frost_clans/pack-rider-idle.png` (1)
- [ ] `images/units/frost_clans/pack-rider-move[1-8].png` (8)
- [ ] `images/units/frost_clans/pack-rider-attack[1-6].png` (6)
- [ ] `images/units/frost_clans/pack-rider-ranged[1-6].png` (6)
- [ ] `images/units/frost_clans/pack-rider-defend[1-4].png` (4)
- [ ] `images/units/frost_clans/pack-rider-death[1-6].png` (6)
**Subtotal**: 31 sprites

### Level 3: Alpha
- [ ] `images/units/frost_clans/pack-rider-alpha-idle.png` (1)
- [ ] `images/units/frost_clans/pack-rider-alpha-move[1-8].png` (8)
- [ ] `images/units/frost_clans/pack-rider-alpha-attack[1-6].png` (6)
- [ ] `images/units/frost_clans/pack-rider-alpha-ranged[1-6].png` (6)
- [ ] `images/units/frost_clans/pack-rider-alpha-defend[1-4].png` (4)
- [ ] `images/units/frost_clans/pack-rider-alpha-death[1-6].png` (6)
**Subtotal**: 31 sprites

### Level 4: Pack Master
- [ ] `images/units/frost_clans/pack-rider-master-idle.png` (1)
- [ ] `images/units/frost_clans/pack-rider-master-move[1-8].png` (8)
- [ ] `images/units/frost_clans/pack-rider-master-attack[1-6].png` (6)
- [ ] `images/units/frost_clans/pack-rider-master-ranged[1-6].png` (6)
- [ ] `images/units/frost_clans/pack-rider-master-defend[1-4].png` (4)
- [ ] `images/units/frost_clans/pack-rider-master-death[1-6].png` (6)
**Subtotal**: 31 sprites

**Quality Checklist**:
- [ ] 72×72 pixels per frame
- [ ] Smooth 8-frame movement loop
- [ ] Dynamic attack animations
- [ ] Clear progression across 4 levels

---

## 🖼️ Phase 3: Portrait Images (8 images)

- [ ] `images/portraits/pack-rider-pup.webp`
- [ ] `images/portraits/pack-rider.webp`
- [ ] `images/portraits/pack-rider-alpha.webp`
- [ ] `images/portraits/pack-rider-master.webp`
- [ ] `images/portraits/transparent/pack-rider-pup-transparent.webp`
- [ ] `images/portraits/transparent/pack-rider-transparent.webp`
- [ ] `images/portraits/transparent/pack-rider-alpha-transparent.webp`
- [ ] `images/portraits/transparent/pack-rider-master-transparent.webp`

---

## ⚔️ Phase 4: Attack Icons (2 icons)

- [ ] `images/attacks/bite-attack.png` (melee icon)
- [ ] `images/attacks/pack-ranged.png` (ranged icon)

---

## 🔊 Phase 5: Audio Assets

- [ ] `sounds/pack-rider-die.ogg` (OGG Vorbis, death howl/yelp)
- [ ] `sounds/pack-tactics-activate.ogg` (optional, ability activation sound)

---

## 🎬 Phase 6: Animation Definitions (WML)

- [ ] `[attack_anim]` for bite/melee attack
- [ ] `[attack_anim]` for ranged attack
- [ ] Optional `[movement_anim]` for 8-frame walk cycle
- [ ] Sound triggers aligned with impact frames

---

## 📦 Phase 7: Deployment

- [ ] Copy config files to `../../units/frost_clans.cfg`
- [ ] Copy sprites to `../../images/units/frost_clans/`
- [ ] Copy portraits to `../../images/portraits/`
- [ ] Copy attack icons to `../../images/attacks/`
- [ ] Copy sounds to `../../sounds/`

---

## ✨ Phase 8: Testing & QA

- [ ] Load addon and recruit all 4 levels
- [ ] Test movement animation (8 frames smooth)
- [ ] Test melee attack (bite animation)
- [ ] Test ranged attack
- [ ] Test Pack Tactics ability
- [ ] Test advancement progression
- [ ] Test death animation and sound
- [ ] Verify all stats match design doc

---

## 📝 Quality Metrics

| Metric | Target |
|--------|--------|
| Total Sprites | 484 |
| Config Files | 1 |
| Portraits | 8 |
| Attack Icons | 2 |
| Audio Assets | 1-2 |

---

**Last Updated**: October 30, 2025
**Status**: Ready for Implementation 🚀
