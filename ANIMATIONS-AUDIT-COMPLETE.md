# Missing Animations - Comprehensive Audit

## Animation Types in Wesnoth

### ✅ Already Implemented
- **attack_anim** - Attack animations (melee and ranged)
- **defense_anim** - Damage/hurt animations (recently added)

### ❌ MISSING - CRITICAL

#### 1. Death Animations (`[death_anim]`)
**Status**: NOT PRESENT IN ANY FILE
**Required**: YES - Plays when a unit dies on the battlefield
**Sprites needed**: 1 per unit type
**Typical format**: 5-10 frame death animation with final pose

**Example needed**:
```wml
    [death_anim]
        start_time=-150
        [frame]
            image="units/frost_clans/[unit-name]-death-1.png:100"
        [/frame]
        [frame]
            image="units/frost_clans/[unit-name]-death-2.png:100"
        [/frame]
        ... (more frames)
        [frame]
            image="units/frost_clans/[unit-name]-death-final.png"
        [/frame]
    [/death_anim]
```

**Total sprites needed**: 31 death animations × 5-8 frames = ~200-250 PNG files

#### 2. Idle/Standing Animations (`[standing_anim]`)
**Status**: Partially handled - uses default `image=` attribute
**Required**: OPTIONAL but recommended for visual quality
**Sprites needed**: Multiple frames per unit (gentle breathing/swaying animation)
**Benefit**: Much more polished appearance

**Example needed**:
```wml
    [standing_anim]
        start_time=-150
        [frame]
            image="units/frost_clans/[unit-name]-idle-1.png:150"
        [/frame]
        [frame]
            image="units/frost_clans/[unit-name]-idle-2.png:150"
        [/frame]
    [/standing_anim]
```

**Total sprites needed**: 31 units × 2-4 frames = ~62-124 PNG files

#### 3. Movement Animations (`[movement_anim]`)
**Status**: NOT PRESENT
**Required**: OPTIONAL but highly recommended
**Sprites needed**: Walking/moving cycle frames
**Benefit**: Professional visual feedback when units move

**Example needed**:
```wml
    [movement_anim]
        [frame]
            image="units/frost_clans/[unit-name]-move-1.png:75"
        [/frame]
        [frame]
            image="units/frost_clans/[unit-name]-move-2.png:75"
        [/frame]
        ...
    [/movement_anim]
```

**Total sprites needed**: 31 units × 4-6 frames = ~124-186 PNG files

### Summary of Missing Animations

| Animation Type | Present | Priority | Sprites Needed | Total |
|---|---|---|---|---|
| attack_anim | ✅ YES | CRITICAL | Already counted | - |
| defense_anim | ✅ YES | CRITICAL | 186 (31 × 6) | 186 |
| death_anim | ❌ NO | **CRITICAL** | 31 × ~6 | ~186-248 |
| standing_anim | ❌ NO | High | 31 × ~3 | ~93-124 |
| movement_anim | ❌ NO | High | 31 × ~5 | ~155 |
| **TOTAL** | | | | **~700-1100** |

### Previous Sprite Count
- Base animations (idle + melee + ranged): 559 PNG files
- Defense animations: 186 PNG files
- **Subtotal**: 745 PNG files

### Updated Sprite Count with ALL Animations
- Base + Defense: 745 PNG files
- Death animations: ~200-250 PNG files
- Standing animations: ~93-124 PNG files  
- Movement animations: ~155 PNG files
- **NEW TOTAL: ~1,193-1,274 PNG files**

## Priority Recommendations

### Tier 1 (CRITICAL - Required for basic gameplay)
1. Death animations - Must have for units to disappear properly
2. Defense animations - Already added ✅

### Tier 2 (HIGH - Significant visual improvement)
3. Standing/Idle animations - Makes units look alive
4. Movement animations - Professional appearance when moving

### Implementation Strategy
1. **Add all `[death_anim]` blocks NOW** - ~200 PNG files
2. Add `[standing_anim]` blocks - Optional, ~100 PNG files  
3. Add `[movement_anim]` blocks - Optional, ~155 PNG files

Total: ~1,200 PNG sprite files for complete animation coverage

