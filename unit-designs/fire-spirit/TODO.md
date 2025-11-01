# Fire Spirit - Implementation TODO

**Unit Line**: Fire Spirit (Frost Clans)
**Status**: Design Complete ✅ | Implementation Ready ⏳
**Design Document**: `fire-spirit-design.md`

---

## 📋 Quick Reference

**High-Quality Standard**: 31 sprites per unit level
**Total for 3-level line**: 93 sprites
**Line Type**: Elemental Ranged (fire-based magic)
**Faction**: Frost Clans

---

## ✅ Phase 1: Configuration Files

- [ ] Create `cfg/fire-spirit.cfg`
- [ ] Define 3 levels: Flame Spirit → Inferno → Conflagration
- [ ] Ranged attack: Fireball (primary, fire damage)
- [ ] Optional melee: Flame Touch (secondary)
- [ ] Abilities: Ignite, Fire Aura
- [ ] Special: Fire resistance, weakness to cold
- [ ] Stats match design document

---

## 🎨 Phase 2: Base Sprite Graphics (93 sprites)

### All 3 Levels
- [ ] Level 1 (Flame Spirit): idle + move(8) + attack(6) + ranged(6) + defend(4) + death(6) = 31
- [ ] Level 2 (Inferno): 31 sprites
- [ ] Level 3 (Conflagration): 31 sprites

**Special Note**: Elemental spirit - design should reflect flames/aura effects, translucent appearance

---

## 🖼️ Phase 3: Portrait Images (6 images)

- [ ] Flame Spirit, Inferno, Conflagration portraits
- [ ] Transparent variants

---

## ⚔️ Phase 4: Attack Icons (2 icons)

- [ ] Fireball ranged attack icon
- [ ] Flame touch melee icon

---

## 🔊 Phase 5: Audio Assets

- [ ] `fire-spirit-die.ogg` (magical dissipation sound)
- [ ] Optional: fireball impact sound, ability trigger sounds

---

## 🎬 Phase 6: Animation Definitions

- [ ] Fireball ranged attack (with particle effect implication)
- [ ] Melee flame touch animation
- [ ] Fire aura animation (ambient glow/effect)
- [ ] Death animation (fade/dissipate effect)
- [ ] Movement animation (floating/drifting motion)

---

## 📦 Phase 7: Deployment

- [ ] Deploy all files to addon folder

---

## ✨ Phase 8: Testing

- [ ] Load and test all 3 levels
- [ ] Verify Ignite ability (sets unit on fire)
- [ ] Verify Fire Aura (damage aura around spirit)
- [ ] Test cold resistance/weakness
- [ ] Check fireball attack range and damage
- [ ] All animations and sounds

---

**Last Updated**: October 30, 2025
**Status**: Ready for Implementation 🚀
