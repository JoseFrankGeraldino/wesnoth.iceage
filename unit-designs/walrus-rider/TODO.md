# Walrus Rider - Implementation TODO

**Unit Line**: Walrus Rider (Frost Clans)
**Status**: Design Complete ✅ | Implementation Ready ⏳
**Design Document**: `walrus-rider-design.md`

---

## 📋 Quick Reference

**High-Quality Standard**: 31 sprites per unit level
**Total for 3-level line**: 93 sprites
**Line Type**: Amphibious Cavalry (water/land specialized)

---

## ✅ Phase 1: Configuration Files

- [ ] Create `cfg/walrus-rider.cfg`
- [ ] Define 3 levels: Walrus Rider → Tusked Warrior → Ancient Leviathan
- [ ] Melee attacks: Tusk Gore (primary), Ram Charge (secondary)
- [ ] Abilities: Aquatic Affinity, Amphibious Movement
- [ ] Custom movement_type (water-compatible)
- [ ] Stats match design document

---

## 🎨 Phase 2: Base Sprite Graphics (93 sprites)

### All 3 Levels
- [ ] Level 1 (Rider): idle + move(8) + attack(6) + ranged(6) + defend(4) + death(6) = 31
- [ ] Level 2 (Tusked Warrior): 31 sprites
- [ ] Level 3 (Ancient Leviathan): 31 sprites

**Special Consideration**: Walrus is larger aquatic mount, may need adjusted positioning on 72×72 canvas

---

## 🖼️ Phase 3: Portrait Images (6 images)

- [ ] Walrus Rider, Tusked Warrior, Ancient Leviathan portraits
- [ ] Transparent variants for each

---

## ⚔️ Phase 4: Attack Icons (2 icons)

- [ ] Tusk gore attack icon
- [ ] Ram charge attack icon

---

## 🔊 Phase 5: Audio Assets

- [ ] `walrus-rider-die.ogg` (walrus death sound)
- [ ] Optional: splashing water sounds, ability triggers

---

## 🎬 Phase 6: Animation Definitions

- [ ] Melee tusk attack animation
- [ ] Charge attack animation (ram motion)
- [ ] Defense animation (in-water defend)
- [ ] Death animation (aquatic setting)
- [ ] Movement animation (swimming/sliding motion)

---

## 📦 Phase 7: Deployment

- [ ] Deploy all files to addon folder
- [ ] Update movement_type in addon framework

---

## ✨ Phase 8: Testing

- [ ] Load and test all 3 levels
- [ ] Verify water movement (Aquatic Affinity)
- [ ] Test on water terrain (shallow water, deep water)
- [ ] Test land movement
- [ ] Verify Amphibious Movement ability
- [ ] Check all attacks and animations

---

**Last Updated**: October 30, 2025
**Status**: Ready for Implementation 🚀
