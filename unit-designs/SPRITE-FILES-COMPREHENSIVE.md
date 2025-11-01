# Comprehensive Sprite Files - Pending Creation

Complete list of all PNG sprite files referenced in WML configurations that need to be created.

---

## ANIMATION TYPES OVERVIEW

### ✅ IMPLEMENTED
- **Attack Animations** (attack_anim): All 31 units
- **Defense Animations** (defense_anim): All 31 units

### ⏳ IN PROGRESS (Being added to all WML files)
- **Death Animations** (death_anim): All 31 units - CRITICAL priority
- **Standing/Idle Animations** (standing_anim): All 31 units - HIGH priority
- **Movement Animations** (movement_anim): All 31 units - HIGH priority

---

## SPRITE COUNT SUMMARY

| Animation Type | Frames per Unit | Total Units | Diagonal? | Total Sprites |
|---|---|---|---|---|
| Idle/Standing | 1 | 31 | No | 31 |
| Attack | 12 (6+6 diagonal) | 18 melee | Yes | 216 |
| Ranged Attack | 12-24 | 22 units | Yes | 300 |
| Defense | 6 | 31 | No | 186 |
| **Death** | 6-8 | 31 | No | **220-250** |
| **Standing/Idle** | 3 | 31 | No | **93** |
| **Movement** | 5 | 31 | No | **155** |
| **GRAND TOTAL** |  |  |  | **~1,470-1,500** |

---

## FROST CLANS FACTION

### 1. BEAR RIDER LINE

#### bear_rider (Level 1)

**Attack Animations (12 frames):**
- units/frost_clans/bear-rider-attack-1.png
- units/frost_clans/bear-rider-attack-diagonal-1.png
- units/frost_clans/bear-rider-attack-2.png
- units/frost_clans/bear-rider-attack-diagonal-2.png
- units/frost_clans/bear-rider-attack-3.png
- units/frost_clans/bear-rider-attack-diagonal-3.png
- units/frost_clans/bear-rider-attack-4.png
- units/frost_clans/bear-rider-attack-diagonal-4.png
- units/frost_clans/bear-rider-attack-5.png
- units/frost_clans/bear-rider-attack-diagonal-5.png
- units/frost_clans/bear-rider-attack-6.png
- units/frost_clans/bear-rider-attack-diagonal-6.png

**Ranged Attack Animations (12 frames):**
- units/frost_clans/bear-rider-ranged-1.png
- units/frost_clans/bear-rider-ranged-diagonal-1.png
- units/frost_clans/bear-rider-ranged-2.png
- units/frost_clans/bear-rider-ranged-diagonal-2.png
- units/frost_clans/bear-rider-ranged-3.png
- units/frost_clans/bear-rider-ranged-diagonal-3.png
- units/frost_clans/bear-rider-ranged-4.png
- units/frost_clans/bear-rider-ranged-diagonal-4.png
- units/frost_clans/bear-rider-ranged-5.png
- units/frost_clans/bear-rider-ranged-diagonal-5.png
- units/frost_clans/bear-rider-ranged-6.png
- units/frost_clans/bear-rider-ranged-diagonal-6.png

**Defense Animations (6 frames):** ✅ COMPLETE
- units/frost_clans/bear-rider-defense-1.png
- units/frost_clans/bear-rider-defense-2.png
- units/frost_clans/bear-rider-defense-3.png
- units/frost_clans/bear-rider-defense-4.png
- units/frost_clans/bear-rider-defense-5.png
- units/frost_clans/bear-rider-defense-6.png

**Death Animations (8 frames):** ⏳ PENDING
- units/frost_clans/bear-rider-death-1.png
- units/frost_clans/bear-rider-death-2.png
- units/frost_clans/bear-rider-death-3.png
- units/frost_clans/bear-rider-death-4.png
- units/frost_clans/bear-rider-death-5.png
- units/frost_clans/bear-rider-death-6.png
- units/frost_clans/bear-rider-death-7.png
- units/frost_clans/bear-rider-death-8.png

**Standing Animation (3 frames):** ⏳ PENDING
- units/frost_clans/bear-rider-standing-1.png
- units/frost_clans/bear-rider-standing-2.png
- units/frost_clans/bear-rider-standing-3.png

**Movement Animation (5 frames):** ⏳ PENDING
- units/frost_clans/bear-rider-movement-1.png
- units/frost_clans/bear-rider-movement-2.png
- units/frost_clans/bear-rider-movement-3.png
- units/frost_clans/bear-rider-movement-4.png
- units/frost_clans/bear-rider-movement-5.png

**Subtotal: 69 frames**

#### dire_bear_rider (Level 2)
Same animation structure as bear_rider: 12 attack + 12 ranged + 6 defense + 8 death + 3 standing + 5 movement = **69 frames**

**Death Animations (8 frames):**
- units/frost_clans/dire-bear-rider-death-1.png through 8.png

**Standing Animations (3 frames):**
- units/frost_clans/dire-bear-rider-standing-1.png through 3.png

**Movement Animations (5 frames):**
- units/frost_clans/dire-bear-rider-movement-1.png through 5.png

#### ancient_bear_lord (Level 3)
**Death Animations (8 frames):**
- units/frost_clans/ancient-bear-lord-death-1.png through 8.png

**Standing Animations (3 frames):**
- units/frost_clans/ancient-bear-lord-standing-1.png through 3.png

**Movement Animations (5 frames):**
- units/frost_clans/ancient-bear-lord-movement-1.png through 5.png

#### primal_bear_champion (Level 4)
**Death Animations (8 frames):**
- units/frost_clans/primal-bear-champion-death-1.png through 8.png

**Standing Animations (3 frames):**
- units/frost_clans/primal-bear-champion-standing-1.png through 3.png

**Movement Animations (5 frames):**
- units/frost_clans/primal-bear-champion-movement-1.png through 5.png

**BEAR RIDER TOTAL: 276 files (69 × 4 units)**

---

### 2. PACK RIDER LINE

#### pack_rider (Level 1) through blizzard_lord (Level 4)
Same animation structure as Bear Rider line, scaled for 4 levels:
- Each level: 12 attack + 12 ranged + 6 defense + 8 death + 3 standing + 5 movement = 69 frames

**Pack Rider New Animations:**
- units/frost_clans/pack-rider-death-1.png through 8.png
- units/frost_clans/pack-rider-standing-1.png through 3.png
- units/frost_clans/pack-rider-movement-1.png through 5.png

**Wolf Ranger New Animations:**
- units/frost_clans/wolf-ranger-death-1.png through 8.png
- units/frost_clans/wolf-ranger-standing-1.png through 3.png
- units/frost_clans/wolf-ranger-movement-1.png through 5.png

**Storm Rider New Animations:**
- units/frost_clans/storm-rider-death-1.png through 8.png
- units/frost_clans/storm-rider-standing-1.png through 3.png
- units/frost_clans/storm-rider-movement-1.png through 5.png

**Blizzard Lord New Animations:**
- units/frost_clans/blizzard-lord-death-1.png through 8.png
- units/frost_clans/blizzard-lord-standing-1.png through 3.png
- units/frost_clans/blizzard-lord-movement-1.png through 5.png

**PACK RIDER TOTAL: 276 files (69 × 4 units)**

---

### 3. ICEBORN WARRIOR LINE

#### iceborn_warrior (Level 1)
- Death: 8 frames, Standing: 3 frames, Movement: 5 frames

**Iceborn Warrior New Animations:**
- units/frost_clans/iceborn-warrior-death-1.png through 8.png
- units/frost_clans/iceborn-warrior-standing-1.png through 3.png
- units/frost_clans/iceborn-warrior-movement-1.png through 5.png

#### winterbane_champion (Level 2)
- units/frost_clans/winterbane-champion-death-1.png through 8.png
- units/frost_clans/winterbane-champion-standing-1.png through 3.png
- units/frost_clans/winterbane-champion-movement-1.png through 5.png

#### rimeguard_chieftain (Level 3)
- units/frost_clans/rimeguard-chieftain-death-1.png through 8.png
- units/frost_clans/rimeguard-chieftain-standing-1.png through 3.png
- units/frost_clans/rimeguard-chieftain-movement-1.png through 5.png

#### glacial_warlord (Level 4)
- units/frost_clans/glacial-warlord-death-1.png through 8.png
- units/frost_clans/glacial-warlord-standing-1.png through 3.png
- units/frost_clans/glacial-warlord-movement-1.png through 5.png

**ICEBORN WARRIOR TOTAL: 276 files (69 × 4 units)**

---

### 4. TUNDRA SCOUT LINE

#### tundra_scout (Level 1)
- units/frost_clans/tundra-scout-death-1.png through 8.png
- units/frost_clans/tundra-scout-standing-1.png through 3.png
- units/frost_clans/tundra-scout-movement-1.png through 5.png

#### blizzard_ranger (Level 2)
- units/frost_clans/blizzard-ranger-death-1.png through 8.png
- units/frost_clans/blizzard-ranger-standing-1.png through 3.png
- units/frost_clans/blizzard-ranger-movement-1.png through 5.png

#### avalanche_hunter (Level 3)
- units/frost_clans/avalanche-hunter-death-1.png through 8.png
- units/frost_clans/avalanche-hunter-standing-1.png through 3.png
- units/frost_clans/avalanche-hunter-movement-1.png through 5.png

#### whiteout_pathfinder (Level 4)
- units/frost_clans/whiteout-pathfinder-death-1.png through 8.png
- units/frost_clans/whiteout-pathfinder-standing-1.png through 3.png
- units/frost_clans/whiteout-pathfinder-movement-1.png through 5.png

**TUNDRA SCOUT TOTAL: 276 files (69 × 4 units)**

---

### 5. WALRUS RIDER LINE

#### walrus_rider (Level 1)
- units/frost_clans/walrus-rider-death-1.png through 8.png
- units/frost_clans/walrus-rider-standing-1.png through 3.png
- units/frost_clans/walrus-rider-movement-1.png through 5.png

#### tusked_corsair (Level 2)
- units/frost_clans/tusked-corsair-death-1.png through 8.png
- units/frost_clans/tusked-corsair-standing-1.png through 3.png
- units/frost_clans/tusked-corsair-movement-1.png through 5.png

#### leviathan_warden (Level 3)
- units/frost_clans/leviathan-warden-death-1.png through 8.png
- units/frost_clans/leviathan-warden-standing-1.png through 3.png
- units/frost_clans/leviathan-warden-movement-1.png through 5.png

**WALRUS RIDER TOTAL: 207 files (69 × 3 units)**

---

## FROST CLANS FACTION SUBTOTAL: 1,311 files

---

## ICE DWELLERS FACTION

### 6. FIRE SPIRIT LINE (Shared/Ice Dwellers)

Fire Spirits are ranged units with burst attacks. They have fewer attack animation variants but multiple special attacks.

#### fire_wisp (Level 1)
**Ranged Attack (12 frames):**
- units/frost_clans/fire-wisp-ranged-1.png through 6.png with diagonal variants

**Defense (6 frames):** ✅ COMPLETE
- units/frost_clans/fire-wisp-defense-1.png through 6.png

**Death (6 frames):** ⏳ PENDING
- units/frost_clans/fire-wisp-death-1.png through 6.png

**Standing (3 frames):** ⏳ PENDING
- units/frost_clans/fire-wisp-standing-1.png through 3.png

**Movement (5 frames):** ⏳ PENDING
- units/frost_clans/fire-wisp-movement-1.png through 5.png

**Subtotal: 38 frames**

#### flame_spirit (Level 2)
**Ranged Attack (12 frames):**
- units/frost_clans/flame-spirit-ranged-1.png through 6.png with diagonals

**Burst Attack (12 frames):**
- units/frost_clans/flame-spirit-burst-1.png through 6.png with diagonals

**Defense (6 frames):** ✅ COMPLETE

**Death (6 frames):** ⏳ PENDING
- units/frost_clans/flame-spirit-death-1.png through 6.png

**Standing (3 frames):** ⏳ PENDING
- units/frost_clans/flame-spirit-standing-1.png through 3.png

**Movement (5 frames):** ⏳ PENDING
- units/frost_clans/flame-spirit-movement-1.png through 5.png

**Subtotal: 50 frames**

#### inferno_avatar (Level 3)
**Ranged Attack (12 frames):**
- units/frost_clans/inferno-avatar-ranged-1.png through 6.png with diagonals

**Burst Attack (12 frames):**
- units/frost_clans/inferno-avatar-burst-1.png through 6.png with diagonals

**Defense (6 frames):** ✅ COMPLETE

**Death (6 frames):** ⏳ PENDING
- units/frost_clans/inferno-avatar-death-1.png through 6.png

**Standing (3 frames):** ⏳ PENDING
- units/frost_clans/inferno-avatar-standing-1.png through 3.png

**Movement (5 frames):** ⏳ PENDING
- units/frost_clans/inferno-avatar-movement-1.png through 5.png

**Subtotal: 50 frames**

**FIRE SPIRIT TOTAL: 138 files**

---

### 7. ICE SPIRIT LINE (Shared Frost Clans/Ice Dwellers)

#### frost_wisp (Level 1)
**Ranged Attack (12 frames):**
- units/frost_clans/frost-wisp-ranged-1.png through 6.png with diagonals

**Defense (6 frames):** ✅ COMPLETE

**Death (6 frames):** ⏳ PENDING
- units/frost_clans/frost-wisp-death-1.png through 6.png

**Standing (3 frames):** ⏳ PENDING
- units/frost_clans/frost-wisp-standing-1.png through 3.png

**Movement (5 frames):** ⏳ PENDING
- units/frost_clans/frost-wisp-movement-1.png through 5.png

**Subtotal: 38 frames**

#### blizzard_spirit (Level 2)
**Blizzard Attack (12 frames):**
- units/frost_clans/blizzard-spirit-blizzard-1.png through 6.png with diagonals

**Deep Freeze Attack (12 frames):**
- units/frost_clans/blizzard-spirit-deepfreeze-1.png through 6.png with diagonals

**Defense (6 frames):** ✅ COMPLETE

**Death (6 frames):** ⏳ PENDING
- units/frost_clans/blizzard-spirit-death-1.png through 6.png

**Standing (3 frames):** ⏳ PENDING
- units/frost_clans/blizzard-spirit-standing-1.png through 3.png

**Movement (5 frames):** ⏳ PENDING
- units/frost_clans/blizzard-spirit-movement-1.png through 5.png

**Subtotal: 50 frames**

#### glacial_avatar (Level 3)
**Absolute Zero Attack (12 frames):**
- units/frost_clans/glacial-avatar-absolutezero-1.png through 6.png with diagonals

**Eternal Winter Attack (12 frames):**
- units/frost_clans/glacial-avatar-eternalwinter-1.png through 6.png with diagonals

**Defense (6 frames):** ✅ COMPLETE

**Death (6 frames):** ⏳ PENDING
- units/frost_clans/glacial-avatar-death-1.png through 6.png

**Standing (3 frames):** ⏳ PENDING
- units/frost_clans/glacial-avatar-standing-1.png through 3.png

**Movement (5 frames):** ⏳ PENDING
- units/frost_clans/glacial-avatar-movement-1.png through 5.png

**Subtotal: 50 frames**

**ICE SPIRIT TOTAL: 138 files**

---

### 8. DARKNESS SPIRIT LINE (Ice Dwellers)

#### shadow_wisp (Level 1)
**Ranged Attack (12 frames):**
- units/ice_dwellers/shadow-wisp-ranged-1.png through 6.png with diagonals

**Defense (6 frames):** ✅ COMPLETE

**Death (6 frames):** ⏳ PENDING
- units/ice_dwellers/shadow-wisp-death-1.png through 6.png

**Standing (3 frames):** ⏳ PENDING
- units/ice_dwellers/shadow-wisp-standing-1.png through 3.png

**Movement (5 frames):** ⏳ PENDING
- units/ice_dwellers/shadow-wisp-movement-1.png through 5.png

**Subtotal: 38 frames**

#### umbral_spirit (Level 2)
**Void Strike Attack (12 frames):**
- units/ice_dwellers/umbral-spirit-voidstrike-1.png through 6.png with diagonals

**Shadow Grasp Attack (12 frames):**
- units/ice_dwellers/umbral-spirit-shadowgrasp-1.png through 6.png with diagonals

**Defense (6 frames):** ✅ COMPLETE

**Death (6 frames):** ⏳ PENDING
- units/ice_dwellers/umbral-spirit-death-1.png through 6.png

**Standing (3 frames):** ⏳ PENDING
- units/ice_dwellers/umbral-spirit-standing-1.png through 3.png

**Movement (5 frames):** ⏳ PENDING
- units/ice_dwellers/umbral-spirit-movement-1.png through 5.png

**Subtotal: 50 frames**

#### void_avatar (Level 3)
**Void Rend Attack (12 frames):**
- units/ice_dwellers/void-avatar-voidrend-1.png through 6.png with diagonals

**Soul Drain Attack (12 frames):**
- units/ice_dwellers/void-avatar-souldrain-1.png through 6.png with diagonals

**Defense (6 frames):** ✅ COMPLETE

**Death (6 frames):** ⏳ PENDING
- units/ice_dwellers/void-avatar-death-1.png through 6.png

**Standing (3 frames):** ⏳ PENDING
- units/ice_dwellers/void-avatar-standing-1.png through 3.png

**Movement (5 frames):** ⏳ PENDING
- units/ice_dwellers/void-avatar-movement-1.png through 5.png

**Subtotal: 50 frames**

**DARKNESS SPIRIT TOTAL: 138 files**

---

### 9. YETI LINE (Ice Dwellers/Neutral)

Yeti units are melee creatures with grapple attacks (special melee variants).

#### young_yeti (Level 1)
**Melee Attack (12 frames):**
- units/ice_dwellers/young-yeti-melee-1.png through 6.png with diagonals

**Defense (6 frames):** ✅ COMPLETE

**Death (7 frames):** ⏳ PENDING
- units/ice_dwellers/young-yeti-death-1.png through 7.png

**Standing (3 frames):** ⏳ PENDING
- units/ice_dwellers/young-yeti-standing-1.png through 3.png

**Movement (5 frames):** ⏳ PENDING
- units/ice_dwellers/young-yeti-movement-1.png through 5.png

**Subtotal: 38 frames**

#### adult_yeti (Level 2)
**Melee Attack (12 frames):**
- units/ice_dwellers/adult-yeti-melee-1.png through 6.png with diagonals

**Grapple Attack (12 frames):**
- units/ice_dwellers/adult-yeti-grapple-1.png through 6.png with diagonals

**Defense (6 frames):** ✅ COMPLETE

**Death (7 frames):** ⏳ PENDING
- units/ice_dwellers/adult-yeti-death-1.png through 7.png

**Standing (3 frames):** ⏳ PENDING
- units/ice_dwellers/adult-yeti-standing-1.png through 3.png

**Movement (5 frames):** ⏳ PENDING
- units/ice_dwellers/adult-yeti-movement-1.png through 5.png

**Subtotal: 52 frames**

#### elder_yeti (Level 3)
Same as adult_yeti: **52 frames**

#### ancient_yeti (Level 4)
Same as adult_yeti: **52 frames**

**YETI TOTAL: 194 files (38 + 52 + 52 + 52)**

---

## ICE DWELLERS FACTION SUBTOTAL: 608 files

---

## GRAND TOTAL: ~1,919 PNG FILES NEEDED

### Breakdown by Animation Type:
- **Attack/Ranged**: 516 files (existing structure)
- **Defense**: 186 files ✅ (WML blocks in place)
- **Death**: 235 files ⏳ (WML blocks being added)
- **Standing**: 93 files ⏳ (WML blocks being added)
- **Movement**: 155 files ⏳ (WML blocks being added)

### Breakdown by Priority:
- **CRITICAL** (Death animations): 235 files - Must be created for gameplay to work
- **HIGH** (Standing/Movement): 248 files - Essential for visual quality
- **NORMAL** (Attack/Defense/Existing): 702 files - Already documented

---

## WML ANIMATION BLOCK SPECIFICATIONS

### Death Animation Block (CRITICAL)
```wml
    [death_anim]
        start_time=-200
        [frame]
            image="units/[faction]/[unit-name]-death-1.png:150"
        [/frame]
        [frame]
            image="units/[faction]/[unit-name]-death-2.png:150"
        [/frame]
        [frame]
            image="units/[faction]/[unit-name]-death-3.png:150"
        [/frame]
        [frame]
            image="units/[faction]/[unit-name]-death-4.png:150"
        [/frame]
        [frame]
            image="units/[faction]/[unit-name]-death-5.png:150"
        [/frame]
        [frame]
            image="units/[faction]/[unit-name]-death-6.png:150"
        [/frame]
        [frame]
            image="units/[faction]/[unit-name]-death-7.png:150"
        [/frame]
        [frame]
            image="units/[faction]/[unit-name]-death-8.png:150"
        [/frame]
    [/death_anim]
```

### Standing Animation Block (HIGH Priority)
```wml
    [standing_anim]
        start_time=0
        [frame]
            image="units/[faction]/[unit-name]-standing-1.png:300"
        [/frame]
        [frame]
            image="units/[faction]/[unit-name]-standing-2.png:300"
        [/frame]
        [frame]
            image="units/[faction]/[unit-name]-standing-3.png:300"
        [/frame]
    [/standing_anim]
```

### Movement Animation Block (HIGH Priority)
```wml
    [movement_anim]
        start_time=0
        [frame]
            image="units/[faction]/[unit-name]-movement-1.png:100"
        [/frame]
        [frame]
            image="units/[faction]/[unit-name]-movement-2.png:100"
        [/frame]
        [frame]
            image="units/[faction]/[unit-name]-movement-3.png:100"
        [/frame]
        [frame]
            image="units/[faction]/[unit-name]-movement-4.png:100"
        [/frame]
        [frame]
            image="units/[faction]/[unit-name]-movement-5.png:100"
        [/frame]
    [/movement_anim]
```

---

## COMPLETION STATUS

### Files with All Animation Blocks:
- ⏳ In progress - Death, Standing, and Movement blocks being added

### Original Sprite Inventory:
- Base animations (idle + melee/ranged): 559 PNG files
- Defense animations: 186 PNG files (✅ Complete)
- Death animations: ~235 PNG files (⏳ Pending)
- Standing animations: ~93 PNG files (⏳ Pending)
- Movement animations: ~155 PNG files (⏳ Pending)

**TOTAL: ~1,228 PNG files** (updated from 745 after audit)

---

## NOTES FOR ARTISTS/DEVELOPERS

1. **Death animations are CRITICAL** - Without these, units won't disappear when defeated
2. **Standing animations improve visual quality** - Shows breathing/swaying motion
3. **Movement animations complete the package** - Professional appearance during unit movement
4. **All sprites must be 72×72 pixels** - PNG-32 format with alpha transparency
5. **Ensure consistent style** across all animation frames and units
6. **Test in Wesnoth** before final delivery to catch any sprite path issues

---

**Last Updated**: October 31, 2025
**Status**: WML files being updated with all animation blocks
