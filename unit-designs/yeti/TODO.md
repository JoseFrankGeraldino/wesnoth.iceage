# Yeti - Implementation TODO

**Unit Line**: Yeti (Ice Dwellers)
**Status**: Design Complete ✅ | Implementation Ready ⏳
**Design Document**: `yeti-design.md`

---

## 📋 Quick Reference

**High-Quality Standard**: 31 sprites per unit level
**Total for 4-level line**: 124 sprites
**Line Type**: Heavy Melee (brutish strength-based)
**Faction**: Ice Dwellers

---

## ✅ Phase 1: Configuration Files

- [ ] Create `cfg/yeti.cfg`
- [ ] Define 4 levels: Yeti → Saber Yeti → Ice Berserker → Ancient Yeti
- [ ] Melee attacks: Claw (primary), Roar/Stun (secondary)
- [ ] Abilities: Thick Hide, Regeneration, Mountainborn
- [ ] Stats from official Wesnoth Yeti line (142 HP, 151 cost, etc.)
- [ ] All advancement chains properly configured

---

## 🎨 Phase 2: Base Sprite Graphics (124 sprites)

### All 4 Levels
- [ ] Level 1 (Yeti): idle + move(8) + attack(6) + ranged(6) + defend(4) + death(6) = 31
- [ ] Level 2 (Saber Yeti): 31 sprites
- [ ] Level 3 (Ice Berserker): 31 sprites
- [ ] Level 4 (Ancient Yeti): 31 sprites

**Special Note**: Large, imposing creature - position carefully on 72×72 canvas to avoid clipping

---

## 🖼️ Phase 3: Portrait Images (8 images)

- [ ] Yeti, Saber Yeti, Ice Berserker, Ancient Yeti portraits
- [ ] Transparent variants for each

---

## ⚔️ Phase 4: Attack Icons (2 icons)

- [ ] Claw melee attack icon
- [ ] Roar/stun attack icon

---

## 🔊 Phase 5: Audio Assets

- [ ] `yeti-die.ogg` (deep growl/roar with impact)
- [ ] Optional: claw attack sounds, roar ability sounds

---

## 🎬 Phase 6: Animation Definitions

- [ ] Claw attack animation (swipe motion)
- [ ] Roar attack animation (intimidating stance)
- [ ] Defense animation (bracing)
- [ ] Death animation (collapse)
- [ ] Movement animation (8 frames, heavy footsteps implied)

---

## 📦 Phase 7: Deployment

- [ ] Deploy all files to addon folder

---

## ✨ Phase 8: Testing

- [ ] Load and test all 4 levels
- [ ] Verify Thick Hide ability (armor/defense)
- [ ] Verify Regeneration (passive healing)
- [ ] Verify Mountainborn (terrain advantages)
- [ ] Test advancement from Yeti → Ancient Yeti
- [ ] Verify all stats match official line (142 HP, etc.)
- [ ] Check all attacks and animations

---

**Last Updated**: October 30, 2025
**Status**: Ready for Implementation 🚀
