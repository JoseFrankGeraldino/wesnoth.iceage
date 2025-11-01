# Iceborn Warrior - Implementation TODO

**Unit Line**: Iceborn Warrior (Frost Clans)
**Status**: Design Complete ✅ | Implementation Ready ⏳
**Design Document**: `iceborn-warrior-line-design.md`

---

## 📋 Quick Reference

**High-Quality Standard**: 31 sprites per unit level
**Total for 4-level line**: 484 sprites
**Line Type**: Heavy Infantry (melee-focused)

---

## ✅ Phase 1: Configuration Files

- [ ] Create `cfg/iceborn-warrior.cfg`
- [ ] Define 4 levels: Neophyte → Warrior → Champion → Warlord
- [ ] Melee attacks: Ice Blade (primary)
- [ ] Abilities: Frozen Armor, Glacial Fortitude
- [ ] Stats match design document

---

## 🎨 Phase 2: Base Sprite Graphics (484 sprites)

### All 4 Levels
- [ ] Level 1 (Neophyte): idle + move(8) + attack(6) + ranged(6) + defend(4) + death(6) = 31
- [ ] Level 2 (Warrior): 31 sprites
- [ ] Level 3 (Champion): 31 sprites  
- [ ] Level 4 (Warlord): 31 sprites

**File Pattern**: `iceborn-warrior-[level]-[animation][frame].png`

---

## 🖼️ Phase 3: Portrait Images (8 images)

- [ ] Neophyte, Warrior, Champion, Warlord main portraits
- [ ] Transparent variants for each (4 images)

---

## ⚔️ Phase 4: Attack Icons (2-3 icons)

- [ ] Ice blade melee attack icon
- [ ] Optional ranged attack icon

---

## 🔊 Phase 5: Audio Assets

- [ ] `iceborn-warrior-die.ogg` (death sound)
- [ ] Optional: ability activation sounds

---

## 🎬 Phase 6: Animation Definitions

- [ ] Melee attack animation (ice blade swing)
- [ ] Defense animation (bracing with armor)
- [ ] Death animation
- [ ] Movement animation (8 frames, heavy/armored gait)

---

## 📦 Phase 7: Deployment

- [ ] Deploy all files to addon folder

---

## ✨ Phase 8: Testing

- [ ] Load, recruit, and test all 4 levels
- [ ] Verify Frozen Armor ability
- [ ] Verify Glacial Fortitude mechanics
- [ ] Test advancement progression
- [ ] Check all animations

---

**Last Updated**: October 30, 2025
**Status**: Ready for Implementation 🚀
