
# Bear Rider - Implementation TODO

**Unit Line**: Bear Rider (Frost Clans)
**Status**: Design Complete ✅ | Implementation Ready ⏳
**Design Document**: `bear-rider-design.md`

---

## 📋 Implementation Phases

### Phase 0: Prerequisite - Sprite Quality Standards

**Reference**: See `../SPRITE-QUALITY-STANDARDS.md` for complete specifications

**High-Quality Standard for Bear Rider** (31 sprites per unit level):

| Animation | Frames | Per Level | Total (4 levels) |
|-----------|--------|-----------|------------------|
| Idle | 1 | 4 | 4 |
| Movement | 8 | 32 | 128 |
| Melee Attack | 6 | 24 | 96 |
| Ranged Attack (Throw) | 6 | 24 | 96 |
| Defense | 4 | 16 | 64 |
| Death | 6 | 24 | 96 |
| **SUBTOTAL** | **31/unit** | **124/level** | **484 sprites** |

**Optional Maximum Quality Add-ons**:
- Advancement Animation: 4 frames × 4 levels = 16 sprites
- Special Ability (Rampage): 6 frames × 4 levels = 24 sprites

**TOTAL FOR BEAR RIDER LINE**: 484 sprites (high quality) → 524 sprites (maximum quality)

---

## ✅ Phase 1: Configuration Files (WML)

- [ ] Create `cfg/bear-rider.cfg` with unit_type definitions
- [ ] Define all 4 unit levels (Cub, Rider, Champion, Warlord)
- [ ] Create movement_type definition (heavy cavalry)
- [ ] Define attack types:
  - [ ] Melee claw attack (primary)
  - [ ] Toss/throw attack (ranged, if applicable)
- [ ] Define special abilities:
  - [ ] Rampage (charge damage bonus)
  - [ ] Stomp (AOE damage, if applicable)
- [ ] Set up advancement chain (Cub → Rider → Champion → Warlord)
- [ ] Configure cost, experience, HP, movement values from design doc
- [ ] Add unit-specific sounds reference:
  - [ ] `bear-rider-die.ogg` (death sound)
  - [ ] `bear-rider-hit.ogg` (optional impact sound)

**Quality Checklist**:
- [ ] No duplicate unit IDs
- [ ] All required WML attributes present
- [ ] Advancement chain properly linked
- [ ] Stats match design document exactly

---

## 🎨 Phase 2: Base Sprite Graphics

**Specifications**: 72×72 PNG-32 (transparent), sRGB color profile

### Level 1: Cub
- [ ] `images/units/frost_clans/bear-rider-cub-idle.png` (1 sprite)
- [ ] `images/units/frost_clans/bear-rider-cub-move[1-8].png` (8 sprites)
- [ ] `images/units/frost_clans/bear-rider-cub-attack[1-6].png` (6 sprites)
- [ ] `images/units/frost_clans/bear-rider-cub-ranged[1-6].png` (6 sprites)
- [ ] `images/units/frost_clans/bear-rider-cub-defend[1-4].png` (4 sprites)
- [ ] `images/units/frost_clans/bear-rider-cub-death[1-6].png` (6 sprites)

### Level 2: Rider
- [ ] `images/units/frost_clans/bear-rider-idle.png` (1 sprite)
- [ ] `images/units/frost_clans/bear-rider-move[1-8].png` (8 sprites)
- [ ] `images/units/frost_clans/bear-rider-attack[1-6].png` (6 sprites)
- [ ] `images/units/frost_clans/bear-rider-ranged[1-6].png` (6 sprites)
- [ ] `images/units/frost_clans/bear-rider-defend[1-4].png` (4 sprites)
- [ ] `images/units/frost_clans/bear-rider-death[1-6].png` (6 sprites)

### Level 3: Champion
- [ ] `images/units/frost_clans/bear-rider-champion-idle.png` (1 sprite)
- [ ] `images/units/frost_clans/bear-rider-champion-move[1-8].png` (8 sprites)
- [ ] `images/units/frost_clans/bear-rider-champion-attack[1-6].png` (6 sprites)
- [ ] `images/units/frost_clans/bear-rider-champion-ranged[1-6].png` (6 sprites)
- [ ] `images/units/frost_clans/bear-rider-champion-defend[1-4].png` (4 sprites)
- [ ] `images/units/frost_clans/bear-rider-champion-death[1-6].png` (6 sprites)

### Level 4: Warlord
- [ ] `images/units/frost_clans/bear-rider-warlord-idle.png` (1 sprite)
- [ ] `images/units/frost_clans/bear-rider-warlord-move[1-8].png` (8 sprites)
- [ ] `images/units/frost_clans/bear-rider-warlord-attack[1-6].png` (6 sprites)
- [ ] `images/units/frost_clans/bear-rider-warlord-ranged[1-6].png` (6 sprites)
- [ ] `images/units/frost_clans/bear-rider-warlord-defend[1-4].png` (4 sprites)
- [ ] `images/units/frost_clans/bear-rider-warlord-death[1-6].png` (6 sprites)

**Total Phase 2**: 124 sprites

**Quality Checklist**:
- [ ] All frames 72×72 pixels
- [ ] Transparent background (no white/solid color)
- [ ] Consistent art style across all 4 levels
- [ ] Clear unit progression visible (size/armor increase)
- [ ] Movement loop smooth (frame 8 transitions to frame 1)
- [ ] Attack frames show dynamic weapon motion
- [ ] Defense frames show visible impact reaction
- [ ] Death animation has clear falling progression

---

## 🖼️ Phase 3: Portrait Images

### Unit Portraits
- [ ] `images/portraits/bear-rider-cub.webp` (300x300+ px, main portrait)
- [ ] `images/portraits/bear-rider.webp` (300x300+ px, main portrait)
- [ ] `images/portraits/bear-rider-champion.webp` (300x300+ px, main portrait)
- [ ] `images/portraits/bear-rider-warlord.webp` (300x300+ px, main portrait)

### Transparent Variants (for help dialogs)
- [ ] `images/portraits/transparent/bear-rider-cub-transparent.webp`
- [ ] `images/portraits/transparent/bear-rider-transparent.webp`
- [ ] `images/portraits/transparent/bear-rider-champion-transparent.webp`
- [ ] `images/portraits/transparent/bear-rider-warlord-transparent.webp`

**Total Phase 3**: 8 portrait images

**Quality Checklist**:
- [ ] WebP format with quality ≥ 85%
- [ ] Minimum 300×300 pixels
- [ ] High detail facial features
- [ ] Clear character personality
- [ ] Transparent variants have clean alpha channel
- [ ] No JPEG artifacts or compression issues

---

## ⚔️ Phase 4: Attack Icons

- [ ] `images/attacks/claw-attack.png` (16x16 or 32x32, claw/melee icon)
- [ ] `images/attacks/bear-throw.png` (16x16 or 32x32, throw/ranged icon)

**Total Phase 4**: 2 attack icons

**Quality Checklist**:
- [ ] Clear icon representation at small scale
- [ ] Consistent with Wesnoth icon style
- [ ] No background (transparent)
- [ ] Readable at 16×16 display size

---

## 🔊 Phase 5: Audio Assets

### Death Sounds
- [ ] `sounds/bear-rider-die.ogg` (OGG Vorbis, 1-2 seconds)
  - Recording: Low growl/roar fading with impact sound
  - Volume: Normalized to -6dB peak
  - Format: 44.1 kHz, mono

### Optional Impact Sounds
- [ ] `sounds/bear-rider-hit.ogg` (OGG Vorbis, 0.5 seconds)
  - Recording: Meaty impact sound
  - Usage: Triggered on melee hit

### Optional Ability Sounds
- [ ] `sounds/rampage-trigger.ogg` (OGG Vorbis, 0.3 seconds, if Rampage ability)
  - Recording: Aggressive roar/charge sound
  - Usage: When Rampage ability activates

**Total Phase 5**: 1-3 audio files

**Quality Checklist**:
- [ ] OGG Vorbis format (not MP3, WAV, etc.)
- [ ] 44.1 kHz sample rate
- [ ] Mono or stereo (mono preferred for space)
- [ ] No clipping or distortion
- [ ] Appropriate for Wesnoth game audio

---

## 🎬 Phase 6: Animation Definitions (WML)

In `cfg/bear-rider.cfg`, add:

- [ ] `[attack_anim]` section for melee claw attack
  - [ ] Frame offset sequence for realistic attack motion
  - [ ] Sound trigger at impact frame
  - [ ] Smooth transition back to idle
  
- [ ] `[attack_anim]` section for ranged throw attack
  - [ ] Frame offset sequence for throw motion
  - [ ] Projectile effect (if applicable)
  - [ ] Sound trigger at release frame

- [ ] Optional `[defend_anim]` section
  - [ ] Custom defense animation mapping
  
- [ ] Optional `[death_anim]` section
  - [ ] Custom death animation with extended hold frame

- [ ] Optional `[movement_anim]` section
  - [ ] Map 8-frame walk cycle to smooth movement
  - [ ] Frame rate: 100ms per frame

**Quality Checklist**:
- [ ] All animation frames reference correct image files
- [ ] Offset values create smooth, realistic motion
- [ ] Sound cues aligned with visual impact moments
- [ ] No animation glitches or frame skipping
- [ ] Looping animations transition smoothly

---

## 📦 Phase 7: Deployment

- [ ] Copy all `.cfg` files to `../../units/frost_clans.cfg` (append to existing)
- [ ] Copy all sprites to `../../images/units/frost_clans/` (organized by unit)
- [ ] Copy all portraits to `../../images/portraits/` (with transparent variants)
- [ ] Copy attack icons to `../../images/attacks/`
- [ ] Copy all sounds to `../../sounds/`
- [ ] Update `../../_main.cfg` to reference new units (if not auto-loaded)
- [ ] Update faction configuration to enable recruitment (if needed)

**Deployment Checklist**:
- [ ] All file paths correct in WML references
- [ ] No duplicate files in deployment
- [ ] Addon folder structure matches requirements
- [ ] Binary paths updated in `_main.cfg`
- [ ] No file permission issues

---

## ✨ Phase 8: Testing & QA

### In-Game Testing
- [ ] Load addon in Wesnoth
- [ ] Verify Bear Rider appears in recruit menu (Frost Clans)
- [ ] Recruit all 4 unit levels (Cub → Rider → Champion → Warlord)
- [ ] Test unit movement (verify 8-frame walk animation plays smoothly)
- [ ] Test melee attack (verify claw animation and damage calculation)
- [ ] Test ranged attack (verify throw animation and projectile)
- [ ] Test defense animation (take damage in-game, watch defend animation)
- [ ] Test death animation (unit should display death sequence, then disappear)
- [ ] Test advancement (recruit Cub, gain 600 XP, verify advances to Rider)
- [ ] Verify all sound effects play (death sound on unit defeat)

### Visual QA
- [ ] Unit sprites display centered in hex
- [ ] No graphical glitches or clipping
- [ ] Animation frames blend smoothly with no jittering
- [ ] Portrait displays correctly in unit info dialog
- [ ] Attack icons display in attack selection menu

### Functionality QA
- [ ] Stats match design document (HP, cost, movement, damage)
- [ ] Abilities function as designed (Rampage bonus activates)
- [ ] Terrain modifiers work (defense bonuses on forest, mountain, etc.)
- [ ] Experience/advancement calculations correct
- [ ] Unit respects recruitment cost limits
- [ ] No script errors or WML parse errors in debug log

**Total Testing Time**: 30-45 minutes per unit line

---

## 📝 Quality Metrics

| Metric | Target | Status |
|--------|--------|--------|
| Total Sprites (4 levels) | 484 | ⏳ |
| Configuration Files | 1 `.cfg` | ⏳ |
| Portrait Images | 8 | ⏳ |
| Attack Icons | 2 | ⏳ |
| Audio Assets | 1-3 | ⏳ |
| Animation Definitions | 2-4 | ⏳ |
| In-Game Testing | Pass | ⏳ |
| User Stories Satisfied | 6 (charge, rampage, strength) | ⏳ |

---

## 🚀 Recommended Implementation Order

1. **Start with Configuration** (Phase 1) - Set up unit structure first
2. **Create Placeholder Graphics** (Phase 2) - Simple 72×72 image with unit name, allows testing
3. **Define Animations** (Phase 6) - Link animations to placeholder graphics
4. **Test in Wesnoth** (Phase 8) - Verify core functionality works
5. **Create Final Graphics** (Phases 2-3) - Replace placeholders with polished art
6. **Add Audio** (Phase 5) - Sound design after visual testing complete
7. **Final QA** (Phase 8 extended) - Full polish pass
8. **Deploy** (Phase 7) - Move to addon folder for distribution

---

## 📌 Notes

- **Design Reference**: See `bear-rider-design.md` for all stat specifications
- **Quality Standard**: Aiming for HIGH QUALITY (31 sprites/unit) as baseline
- **Sprite Tool Recommendation**: Aseprite for professional-quality frame-by-frame animation
- **WML Syntax**: Reference `../IMPLEMENTATION-GUIDE.md` for WML template
- **Testing Build**: Can test with placeholder graphics before final art is complete
- **Parallel Work**: Art team can create sprites while programmers write WML configs

---

**Last Updated**: October 30, 2025
**Status**: Ready for Implementation 🚀
