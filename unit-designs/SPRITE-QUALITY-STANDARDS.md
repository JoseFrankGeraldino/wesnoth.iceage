# High-Quality Sprite Standards for Ice Age Addon

**Version**: 1.0
**Date**: October 30, 2025
**Quality Target**: Maximum recommended by Wesnoth creators

---

## 🎨 Canvas Specifications

### Base Canvas Size
- **Standard Hex Size**: 72×72 pixels
- **Reference Frame**: Center unit in hex, feet at ~55px from top
- **Format**: PNG-32 (Transparent background, RGBA)
- **Color Profile**: sRGB
- **Anti-aliasing**: Yes (for smooth lines)

---

## 📊 High-Quality Animation Frame Requirements

### 1. **Idle/Standing Animation** (Base State)
- **Frames**: 1 frame (static)
- **Purpose**: Default idle state displayed on map
- **Quality Details**:
  - Relaxed stance, neutral expression
  - Facing lower-right direction (standard Wesnoth orientation)
  - Shadow/base indicator at feet

---

### 2. **Movement/Walking Animation** (When Moving)
- **Frames**: 8 frames (MAXIMUM QUALITY - highest recommended)
- **Frame Rate**: 100ms per frame (80ms-120ms range acceptable)
- **Purpose**: Smooth walking cycle across map
- **Quality Details**:
  - Full 2-cycle loop for fluidity
  - Realistic weight distribution
  - Alternating leg movement
  - Body sway/balance dynamics
  
**Frame Progression**:
```
Frame 1: Left foot forward (extension)
Frame 2: Left foot contact
Frame 3: Right foot lifting
Frame 4: Mid-cycle push
Frame 5: Right foot forward (extension)
Frame 6: Right foot contact
Frame 7: Left foot lifting
Frame 8: Mid-cycle push (returns to Frame 1)
```

---

### 3. **Melee Attack Animation** (Close-range weapons)
- **Frames**: 6 frames (HIGH QUALITY - maximum recommended)
- **Frame Rate**: 50ms-80ms per frame (faster = more dynamic)
- **Purpose**: Sword, spear, axe attacks
- **Quality Details**:
  - Startup phase (1 frame): Preparation/wind-up
  - Strike phase (2 frames): Weapon contact point
  - Follow-through (2 frames): Momentum carrying through
  - Recovery (1 frame): Return to idle
  
**Frame Sequence**:
```
Frame 1: Wind-up (weapon raised/positioned)
Frame 2: Early strike (weapon moving toward target)
Frame 3: Impact (weapon at contact point)
Frame 4: Follow-through (weapon passing through)
Frame 5: Recovery start (weapon returning)
Frame 6: Recovery end (return to idle)
```

---

### 4. **Ranged Attack Animation** (Arrows, spells, projectiles)
- **Frames**: 6 frames (HIGH QUALITY - maximum recommended)
- **Frame Rate**: 60ms-80ms per frame
- **Purpose**: Bow, crossbow, magic ranged attacks
- **Quality Details**:
  - Stance adjustment (1 frame): Bracing/aiming position
  - Draw/Charge phase (2 frames): Drawing bow or charging spell
  - Release (1 frame): Moment of release
  - Follow-through (1 frame): Post-release motion
  - Recovery (1 frame): Return to stance
  
**Frame Sequence**:
```
Frame 1: Aiming stance (archer draws, mage raises staff)
Frame 2: Draw phase (bow fully drawn, spell building)
Frame 3: Peak tension (moment before release)
Frame 4: Release (projectile leaves, weapon returns)
Frame 5: Follow-through (continued motion from release)
Frame 6: Recovery (return to idle)
```

---

### 5. **Defensive/Block Animation** (When taking damage)
- **Frames**: 4 frames (HIGH QUALITY - maximum recommended)
- **Frame Rate**: 80ms-100ms per frame
- **Purpose**: Bracing/reacting to hits
- **Quality Details**:
  - Neutral stance (1 frame): Pre-damage pose
  - Impact reaction (2 frames): Visible impact/knockback
  - Recovery (1 frame): Return to stance
  
**Frame Sequence**:
```
Frame 1: Neutral ready stance
Frame 2: Hit impact (visible recoil/flinch)
Frame 3: Partial recovery
Frame 4: Full recovery to neutral
```

**Terrain-Specific Defense**:
- Create separate defense animation for units fighting on different terrain (optional for ultra-high quality)
- Example: Defensive stance differs for forest vs. open ground

---

### 6. **Death Animation** (Defeat sequence)
- **Frames**: 6 frames (HIGH QUALITY - maximum recommended)
- **Frame Rate**: 100ms per frame (slower, more dramatic)
- **Purpose**: Death/defeat of unit
- **Quality Details**:
  - Initial reaction (1 frame): First hit reaction
  - Falling (2 frames): Collapse/falling motion
  - Impact (1 frame): Landing
  - Final pose (2 frames): Death state (hold last frame 200ms)
  
**Frame Sequence**:
```
Frame 1: Hit reaction (stagger/flinch)
Frame 2: Beginning fall (loss of balance)
Frame 3: Mid-fall (descending)
Frame 4: Impact (body hitting ground)
Frame 5: Final death pose (settling)
Frame 6: Final death pose (hold - may repeat for 200ms+)
```

---

### 7. **Advancement/Promotion Animation** (Level up sequence)
- **Frames**: 4 frames (OPTIONAL - for extra polish)
- **Frame Rate**: 100ms per frame
- **Purpose**: Visual feedback when unit advances
- **Quality Details**:
  - Base pose with glow effect (1 frame)
  - Transformation start (1 frame): Magical effect buildup
  - Transformation peak (1 frame): Maximum effect intensity
  - New form (1 frame): Unit in advanced form
  
**Frame Sequence**:
```
Frame 1: Base with subtle glow
Frame 2: Effect buildup (aura growing)
Frame 3: Effect peak (maximum visual intensity)
Frame 4: Advanced form revealed
```

---

### 8. **Special Ability Animation** (Ability-specific)
- **Frames**: 4-6 frames (OPTIONAL - depends on ability)
- **Frame Rate**: 60ms-100ms per frame
- **Purpose**: Visual for special abilities (freeze, fire aura, etc.)
- **Quality Details**:
  - Varies by ability (spell effects, auras, buffs)
  - Should be distinct from basic attacks

**Examples**:
- **Freeze Ability**: Ice crystal formation around unit (4 frames)
- **Fire Aura**: Flame burst expanding (4 frames)
- **Healing**: Light burst emanating (4 frames)

---

## 📋 Total Sprite Count per Unit (Maximum Quality Build)

### Minimum Quality Standard
```
Idle (1) + Attack (6) + Defense (4) + Death (6) = 17 sprites per unit
```

### HIGH QUALITY STANDARD (Recommended for Ice Age)
```
Idle (1) + Movement (8) + Melee Attack (6) + Ranged Attack (6) + Defense (4) + Death (6) = 31 sprites per unit

Per unit line with 4 levels:
- Level 1: 31 sprites
- Level 2: 31 sprites  
- Level 3: 31 sprites
- Level 4: 31 sprites (if exists)
Total: 124 sprites per unit line (4-level line)
```

### MAXIMUM QUALITY STANDARD (Ultra-Premium)
```
Idle (1) + Movement (8) + Melee Attack (6) + Ranged Attack (6) + Defense (4) + Death (6) + 
Advancement (4) + Special Ability (6) = 41 sprites per unit

Per 4-level unit line:
Total: 164 sprites per unit line
```

---

## 🎬 Animation File Organization

### File Naming Convention
```
[unit-name]-[animation-type][frame-number].png

Examples:
bear-rider-idle.png                    (idle frame)
bear-rider-move1.png through -move8.png (movement frames)
bear-rider-attack1.png through -attack6.png (melee attack)
bear-rider-ranged1.png through -ranged6.png (ranged attack)
bear-rider-defend1.png through -defend4.png (defense frames)
bear-rider-death1.png through -death6.png (death frames)
```

### Optional Ultra-Quality Naming
```
bear-rider-advance1.png through -advance4.png (promotion animation)
bear-rider-ability-freeze1.png through -ability-freeze6.png (special ability)
```

---

## 🌟 Quality Checklist Per Animation Type

### Movement Animation (8 frames)
- [ ] Smooth weight transfer between legs
- [ ] Natural arm swing opposite leg motion
- [ ] Body sway realistic and subtle
- [ ] Consistent stride length
- [ ] All frames transition smoothly (frame 8 → frame 1)
- [ ] No jittering or unnatural jerks
- [ ] Feet position consistent across frames

### Melee Attack (6 frames)
- [ ] Weapon wind-up visible and convincing
- [ ] Impact frame shows contact clearly
- [ ] Follow-through demonstrates momentum
- [ ] Recovery returns smoothly to idle
- [ ] Attack timing matches expected weapon type
- [ ] No clipping through body
- [ ] Weight distribution realistic throughout

### Ranged Attack (6 frames)
- [ ] Aiming/charging pose distinct and clear
- [ ] Draw motion is smooth (2-frame draw)
- [ ] Release point is obvious
- [ ] Post-release recovery is natural
- [ ] Animation loops smoothly back to idle
- [ ] Projectile path is implied by final frame

### Defense Animation (4 frames)
- [ ] Visible reaction to impact
- [ ] Not overly dramatic (keep player visibility)
- [ ] Recovery is quick (4 frames = 320-400ms total)
- [ ] Returns to neutral stance smoothly

### Death Animation (6 frames)
- [ ] Clear progression from healthy to fallen
- [ ] Impact moment is visible
- [ ] Final pose is distinct from idle/defeat
- [ ] Final frame held long enough to read

---

## 📐 Directional Variants (Ultra-High Quality Optional)

For maximum quality, create directional variants:

### Suggested Approach (Requires 2x sprite count, but highest quality)
- **Primary**: 4 directions (N, NE, SE, S)
- **Result**: 4× sprite count per animation

Example for Bear Rider (4 directions):
```
bear-rider-north-move1.png through move8.png
bear-rider-northeast-move1.png through move8.png
bear-rider-southeast-move1.png through move8.png
bear-rider-south-move1.png through move8.png
```

### Wesnoth Standard (Single Direction)
- **Standard**: Single direction (all units face SE by default)
- **Result**: Standard sprite count (recommended for Ice Age addon)

---

## 🎯 Recommended Implementation Priority (by complexity)

### PHASE 1: Essential Animations (17 sprites/unit)
1. Idle (1)
2. Attack (6)
3. Defense (4)
4. Death (6)

**Quality**: Functional, playable addon

---

### PHASE 2: High-Quality Standard (31 sprites/unit)
Add to Phase 1:
5. Movement (8)
6. Ranged Attack (6)

**Quality**: Professional, polished addon

---

### PHASE 3: Maximum Quality (41 sprites/unit)
Add to Phase 2:
7. Advancement (4)
8. Special Ability (6)

**Quality**: Ultra-premium, flagship addon

---

## 📊 Sprite Requirements Summary

| Animation | Min Frames | High Quality | Max Quality | Purpose |
|-----------|-----------|-----------|-----------|---------|
| Idle | 1 | 1 | 1 | Standing state |
| Movement | - | 8 | 8 | Walking across map |
| Melee Attack | 6 | 6 | 6 | Close combat |
| Ranged Attack | - | 6 | 6 | Ranged combat |
| Defense | 4 | 4 | 4 | Damage reaction |
| Death | 6 | 6 | 6 | Defeat sequence |
| Advancement | - | - | 4 | Level up |
| Special Ability | - | - | 6 | Unique ability |
| **TOTAL/UNIT** | **17** | **31** | **41** |  |
| **TOTAL/4-LVL LINE** | **68** | **124** | **164** | Per 4-level unit |

---

## 🎨 Recommended Tools for High-Quality Sprites

- **Aseprite** (Professional, $19.99): Frame-by-frame animation, excellent for pixel art
- **GIMP + Plugins** (Free): Capable but requires manual setup
- **Krita** (Free): Excellent for painting, good animation support
- **LibreSprite** (Free, open-source): Aseprite-like, community maintained
- **Piskel** (Free, web-based): Quick prototyping, limited features

---

## 📝 Notes

- All quality standards assume 72×72 pixel canvas (Wesnoth standard hex)
- Frame rates should be consistent within each animation type
- Smooth 8-frame movement loop is professional standard (not 4-frame)
- Most mainline Wesnoth units use 6-frame attack/ranged animations
- Death animations are typically longer (more frames, slower pacing)

---

**ICE AGE ADDON STANDARD**: Aiming for **HIGH QUALITY** (31 sprites/unit) as baseline, with **MAXIMUM QUALITY** (41 sprites/unit) for tier-1 flagship units.

**Sprite Count Projections**:
- 9 completed design units × 31 sprites = **279 sprites** (high quality)
- 9 planning units × 31 sprites = **279 sprites** (future)
- **TOTAL**: 558 sprites for full addon (high quality standard)
