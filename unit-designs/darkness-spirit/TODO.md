# Darkness Spirit - Implementation TODO

**Unit Line**: Darkness Spirit (Ice Dwellers)
**Status**: Design Complete ✅ | Implementation Ready ⏳
**Design Document**: `darkness-spirit-design.md`

---

## 📋 Quick Reference

**High-Quality Standard**: 31 sprites per unit level
**Total for 3-level line**: 93 sprites
**Line Type**: Elemental Shadow (dark/shadow magic)
**Faction**: Ice Dwellers

---

## ✅ Phase 1: Configuration Files

- [ ] Create `cfg/darkness-spirit.cfg`
- [ ] Define 3 levels: Shadow Wisp → Void Spirit → Abyss Lord
- [ ] Ranged attack: Shadow Bolt (primary, shadow damage)
- [ ] Melee attack: Void Touch (secondary)
- [ ] Abilities: Drain Life, Umbral Cloak, Shadow Merge
- [ ] Special: Shadow resistance, vulnerability to light
- [ ] Stats match design document

---

## 🎨 Phase 2: Base Sprite Graphics (93 sprites)

### All 3 Levels
- [ ] Level 1 (Shadow Wisp): idle + move(8) + attack(6) + ranged(6) + defend(4) + death(6) = 31
- [ ] Level 2 (Void Spirit): 31 sprites
- [ ] Level 3 (Abyss Lord): 31 sprites

**Special Note**: Shadow elemental - design should show dark aura, translucent shadow effects, void-like appearance

---

## 🖼️ Phase 3: Portrait Images (6 images)

- [ ] Shadow Wisp, Void Spirit, Abyss Lord portraits
- [ ] Transparent variants

---

## ⚔️ Phase 4: Attack Icons (2 icons)

- [ ] Shadow bolt ranged attack icon
- [ ] Void touch melee icon

---

## 🔊 Phase 5: Audio Assets

- [ ] `darkness-spirit-die.ogg` (ethereal dissipation sound)
- [ ] Optional: void/shadow sounds, ability trigger audio

---

## 🎬 Phase 6: Animation Definitions

- [ ] Shadow bolt ranged attack
- [ ] Void touch melee attack
- [ ] Umbral Cloak animation (cloaking effect)
- [ ] Death animation (fade/void effect)
- [ ] Movement animation (shadow gliding)

---

## 📦 Phase 7: Deployment

- [ ] Deploy all files to addon folder

---

## ✨ Phase 8: Testing

- [ ] Load and test all 3 levels
- [ ] Verify Drain Life ability (lifesteal mechanic)
- [ ] Verify Umbral Cloak (damage reduction)
- [ ] Verify Shadow Merge (movement concealment)
- [ ] Test shadow resistance and light vulnerability
- [ ] Check all attacks and animations

---

**Last Updated**: October 30, 2025
**Status**: Ready for Implementation 🚀
