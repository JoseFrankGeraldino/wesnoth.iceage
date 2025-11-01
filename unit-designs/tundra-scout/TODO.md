# Tundra Scout - Implementation TODO

**Unit Line**: Tundra Scout (Frost Clans)
**Status**: Design Complete ✅ | Implementation Ready ⏳
**Design Document**: `tundra-scout-line-design.md`

---

## 📋 Quick Reference

**High-Quality Standard**: 31 sprites per unit level
**Total for 4-level line**: 484 sprites
**Line Type**: Ranged/Skirmisher (bow-focused)

---

## ✅ Phase 1: Configuration Files

- [ ] Create `cfg/tundra-scout.cfg`
- [ ] Define 4 levels: Scout → Ranger → Marksman → Sharpshooter
- [ ] Ranged attack: Bow (primary)
- [ ] Melee attack: Dagger (secondary)
- [ ] Abilities: Keen Eyes, Swift Retreat
- [ ] Stats match design document

---

## 🎨 Phase 2: Base Sprite Graphics (484 sprites)

### All 4 Levels
- [ ] Level 1 (Scout): idle + move(8) + attack(6) + ranged(6) + defend(4) + death(6) = 31
- [ ] Level 2 (Ranger): 31 sprites
- [ ] Level 3 (Marksman): 31 sprites
- [ ] Level 4 (Sharpshooter): 31 sprites

**File Pattern**: `tundra-scout-[level]-[animation][frame].png`

---

## 🖼️ Phase 3: Portrait Images (8 images)

- [ ] Scout, Ranger, Marksman, Sharpshooter portraits
- [ ] Transparent variants

---

## ⚔️ Phase 4: Attack Icons (2 icons)

- [ ] Bow/ranged attack icon
- [ ] Dagger melee icon

---

## 🔊 Phase 5: Audio Assets

- [ ] `tundra-scout-die.ogg`
- [ ] Optional: bow release sound, ability sounds

---

## 🎬 Phase 6: Animation Definitions

- [ ] Ranged attack (bow draw and release)
- [ ] Melee attack (dagger slash)
- [ ] Defense animation
- [ ] Death animation

---

## 📦 Phase 7: Deployment

- [ ] Deploy all files to addon folder

---

## ✨ Phase 8: Testing

- [ ] Load and test all 4 levels
- [ ] Verify Keen Eyes ability
- [ ] Verify Swift Retreat mechanic
- [ ] Test advancement chain
- [ ] Check all attacks and animations

---

**Last Updated**: October 30, 2025
**Status**: Ready for Implementation 🚀
