# Unit Designs Documentation

This folder contains comprehensive design documentation for all unit lines in the Wesnoth Ice Age addon.

## Unit Lines (Balanced Distribution)

There are now **10 Frost Clans unit lines**, **10 Ice Dwellers unit lines**, and **2 shared lines** (Ice Spirit, Iceguard Spearman). Each line consists of 4 units (levels 1–4), except where noted. Shared lines are available to both factions.

### Frost Clans Unit Lines

1. [Bear Rider](./bear-rider/)  
2. [Pack Rider](./pack-rider/)  
3. [Walrus Rider](./walrus-rider/)  
4. [Tundra Scout](./tundra-scout/)  
5. [Fire Spirit](./fire-spirit/)  
6. [Winterheart Shaman](./winterheart-shaman/)  
7. [Snowfall Trapper](./snowfall-trapper/)  
8. [Iceborn Warrior](./iceborn-warrior/)  
9. [Icewall Guardian](./icewall-guardian/)  
10. [Coldmist Stalker](./coldmist-stalker/)  
**Shared:** [Ice Spirit](./ice-spirit/)  
**Shared:** [Iceguard Spearman](./iceguard-spearman/)

### Ice Dwellers Unit Lines

1. [Darkness Spirit](./darkness-spirit/)  
2. [Yeti](./yeti/)  
3. [Crystalborn Elemental](./crystalborn-elemental/)  
4. [Glacial Wraith](./glacial-wraith/)  
5. [Permafrost Beast](./permafrost-beast/)  
6. [Shimmer Sprite](./shimmer-sprite/)  
7. [Hoarfrost Mage](./hoarfrost-mage/)  
8. [Ice Dwellers Mage] (planned)  
9. [Frost Revenant] (planned)  
10. [Frostbound Sentinel] (planned)  
**Shared:** [Ice Spirit](./ice-spirit/)  
**Shared:** [Iceguard Spearman](./iceguard-spearman/)

**Note:** The two shared lines (Ice Spirit, Iceguard Spearman) are available to both factions and count toward the 10 lines for each.

---

## Design Principles

### Balance Framework
1. **Cost vs Performance**: Higher level units require proportional resource investment
2. **Role Definition**: Each unit has specific tactical purpose and counter-plays
3. **Elemental Trinity**: Fire/Ice/Darkness spirits create strategic rock-paper-scissors dynamics
4. **Faction Identity**: Units reflect their culture and magical traditions

### Progression System
- **Level 1 (Novice)**: Basic abilities, lower stats, lowest cost
- **Level 2 (Expert)**: Enhanced abilities, improved stats, moderate cost
- **Level 3 (Elite)**: Ultimate abilities, highest stats, premium cost

### Thematic Consistency
All units follow consistent design language:
- Visual aesthetics match their source (mounted, elemental, etc.)
- Abilities reflect lore and environmental interaction
- Color palettes support visual clarity in combat

---

## Combat Interaction Matrix

| Unit | Effective Against | Weak To | Synergizes With |
|------|------------------|---------|-----------------|
| Bear Rider | Light units, siege | Ranged attacks | Iceborn Warriors |
| Pack Rider | Support units, archers | Heavy melee | Tundra Scouts |
| Walrus Rider | Fire units, land cavalry | Pack Riders, desert units | Bear Rider |
| Iceborn Warrior | Mixed squads | Extreme cold | Tundra Scouts |
| Tundra Scout | Heavy units, flyers | Cavalry | Iceborn Warriors |
| Fire Spirit | Ice Spirits, plants | Water, Ice, Walrus Riders | Frost Clans |
| Ice Spirit | Fire Spirits, lava | Fire, Sun | Darkness Spirits |
| Darkness Spirit | Magical units | Light, Holy | Any faction |
| Yeti | Melee fighters, heavy units | Fire attacks, ranged | Ice Dwellers, Mountains |

---

## Asset Organization

Each unit folder contains:
- `[unitname]-design.md` - Comprehensive design document
- Unit sprites and artwork (as developed)
- Animation reference materials (future)
- Ability effect specifications (future)

---

## Future Development

### Planned Additions
- Visual sprite assets for all units
- Animation specifications and timing
- Sound design and effect notes
- Detailed balance testing results
- Campaign integration guidelines

### Expansion Opportunities
- Additional unit variations and specializations
- Faction-specific unit modifications
- Seasonal/terrain-specific unit variants
- Hero units and special commanders

---

**Last Updated**: October 30, 2025
**Status**: Active Development
