# Ice Spirit - Implementation TODO

**Unit Line**: Ice Spirit (Frost Clans & Ice Dwellers)
**Status**: Design Complete ✅ | Implementation Ready ⏳
**Design Document**: `ice-spirit-design.md`

---

## 📋 Quick Reference

**High-Quality Standard**: 31 sprites per unit level
**Total for 3-level line**: 93 sprites
**Line Type**: Elemental Ranged (ice/cold-based magic)
**Faction**: Frost Clans & Ice Dwellers (shared unit)

---

## ✅ Phase 1: Configuration Files

- [ ] Create `cfg/ice-spirit.cfg`
- [ ] Define 3 levels: Frost Spirit → Ice Elemental → Glacial Colossus
- [ ] Ranged attack: Frost Bolt (primary, cold damage)
- [ ] Optional melee: Ice Shard (secondary)
- [ ] Abilities: Freeze, Frozen Ground, Shatter
- [ ] Resistances: Cold resistance, vulnerability to fire
- [ ] Stats match design document

---

## 🎨 Phase 2: Base Sprite Graphics (93 sprites)

### All 3 Levels
- [ ] Level 1 (Frost Spirit): idle + move(8) + attack(6) + ranged(6) + defend(4) + death(6) = 31
- [ ] Level 2 (Ice Elemental): 31 sprites
- [ ] Level 3 (Glacial Colossus): 31 sprites

**Special Note**: Ice elemental - design should show crystalline structure, frost effects, icy aura

---

## 🖼️ Phase 3: Portrait Images (6 images)

- [ ] Frost Spirit, Ice Elemental, Glacial Colossus portraits
- [ ] Transparent variants

---

## ⚔️ Phase 4: Attack Icons (2 icons)

- [ ] Frost bolt ranged attack icon
- [ ] Ice shard melee icon

---

## 🔊 Phase 5: Audio Assets

- [ ] `ice-spirit-die.ogg` (shattering/dissipating sound)
- [ ] Optional: frost bolt impact, freeze effect sounds

---

## 🎬 Phase 6: Animation Definitions

- [ ] Frost bolt ranged attack (ice projectile launch)
- [ ] Melee ice shard attack
- [ ] Freeze effect animation (opponent immobilized)
- [ ] Death animation (shattering effect)
- [ ] Movement animation (gliding/sliding motion)

---

## 📦 Phase 7: Deployment

- [ ] Deploy all files to addon folder
- [ ] Make available to both Frost Clans and Ice Dwellers factions

---

## ✨ Phase 8: Testing

- [ ] Load and test all 3 levels in both factions
- [ ] Verify Freeze ability (immobilizes targets)
- [ ] Verify Frozen Ground (terrain effect)
- [ ] Verify Shatter ability
- [ ] Test cold resistance and fire vulnerability
- [ ] Check all attacks, animations, and sounds

---

**Last Updated**: October 30, 2025
**Status**: Ready for Implementation 🚀
