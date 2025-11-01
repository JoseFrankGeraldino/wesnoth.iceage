# Snow Dog Cavalry Design - Frost Clans Light Cavalry Redesign

## 🐺 Creative Naming Philosophy

Moving away from generic "Frost" naming conventions, the snow dog cavalry line embraces creative, thematic names that reflect both the pack nature of snow dogs and the progression from basic rider to legendary commander:

- **Pack Rider** → **Wolf Ranger** → **Storm Rider** → **Blizzard Lord**

Each name suggests increasing mastery of both mounted combat and pack coordination, culminating in the legendary Blizzard Lord who commands devastating avalanche attacks.

## 🎯 Pack Frenzy Mechanic

### Core Concept
Snow dog mounts have low individual attack damage but compensate with multiple attacks per turn. The pack frenzy mechanic creates unpredictable, tactical complexity where subsequent attacks target random adjacent enemies after the initial strike.

### Implementation Details

#### Level 1: Pack Rider - Pack Bite (4 attacks)
```wml
[attack]
    name=pack bite
    description=pack bite
    type=blade
    range=melee
    damage=3
    number=4
    [specials]
        [pack_frenzy]
        [/pack_frenzy]
    [/specials]
[/attack]
```

#### Level 2: Wolf Ranger - Pack Bite (5 attacks) + Skirmisher
```wml
[attack]
    name=pack bite
    description=pack bite  
    type=blade
    range=melee
    damage=4
    number=5
    [specials]
        [pack_frenzy]
        [/pack_frenzy]
    [/specials]
[/attack]
```

#### Level 3: Storm Rider - Pack Storm (6 magical attacks) + Leadership
```wml
[attack]
    name=pack storm
    description=pack storm
    type=magical
    range=melee
    damage=5
    number=6
    [specials]
        [pack_frenzy]
        [/pack_frenzy]
        [magical]
        [/magical]
    [/specials]
[/attack]
```

#### Level 4: Blizzard Lord - Pack Avalanche (7 magical attacks) + Leadership + Snow Vision
```wml
[attack]
    name=pack avalanche
    description=pack avalanche
    type=magical
    range=melee
    damage=6
    number=7
    [specials]
        [pack_frenzy]
        [/pack_frenzy]
        [magical]
        [/magical]
    [/specials]
[/attack]
```

## 🏔️ Snow Dog Mounted Movement Type

### Characteristics
- **High Mobility**: Excellent movement costs on most terrain
- **Pack Coordination**: Optimized for fast repositioning and flanking
- **Cold Resistance**: 20% resistance to cold damage
- **Forest Specialists**: Reduced movement costs in forests for pack hunting

### Movement Costs
```wml
[movement_costs]
    deep_water=4      # Cannot swim effectively
    shallow_water=2   # Can wade quickly
    flat=1           # Excellent on open terrain
    forest=1         # Pack hunters in woods
    hills=2          # Good hill climbers
    mountains=3      # Difficult for dogs
    frozen=1         # Natural ice runners
    cave=2           # Acceptable in caves
[/movement_costs]
```

### Defense Values
```wml
[defense]
    flat=50          # Good mobility defense
    forest=40        # Excellent in pack hunting terrain
    hills=50         # Standard hill defense
    frozen=30        # Outstanding on ice
    village=40       # Good in settlements
[/defense]
```

## ⚔️ Tactical Implications

### Pack Frenzy Strategy
1. **Primary Target Selection**: Player chooses initial attack target
2. **Pack Scatter**: Remaining 3-6 attacks randomly target adjacent enemies
3. **Area Denial**: Discourages enemy clustering around cavalry units
4. **Unpredictable Damage Distribution**: Creates tactical uncertainty for opponents

### Progression Benefits
- **Volume Over Power**: Multiple weak attacks vs. single strong attacks
- **Magical Scaling**: Level 3+ attacks bypass physical resistances
- **Leadership Support**: High-level units provide army-wide benefits
- **Mobility Scaling**: Movement increases from 7→10 across levels

### Counters and Weaknesses
- **Low Individual Damage**: Each attack is relatively weak
- **Positioning Dependent**: Requires adjacent enemies for full effectiveness
- **Fire Vulnerability**: Standard cold-adapted unit weakness
- **Deep Water Limitation**: Cannot cross rivers effectively

## 🌨️ Thematic Integration

### Cultural Context
Snow dogs represent the symbiotic relationship between the Frost Clans and their arctic environment. Unlike domesticated horses, snow dogs are pack hunters that maintain their wild instincts while serving as mounts.

### Visual Description
- **Pack Riders**: Young warriors learning to coordinate with individual snow dogs
- **Wolf Rangers**: Experienced hunters who understand pack dynamics
- **Storm Riders**: Elite cavalry who channel magical energy through their mounts
- **Blizzard Lords**: Legendary commanders whose mounts have become extensions of their will

### Environmental Harmony
The snow dog cavalry embodies the Frost Clans' philosophy of working with nature rather than dominating it. Their pack frenzy attacks represent the unleashing of primal hunting instincts in coordinated combat.

## 🔧 Implementation Status

### Completed Features ✅
- [x] Four-level progression with creative naming
- [x] Pack frenzy attack mechanics (4-7 attacks)
- [x] Progressive damage scaling (3→6 damage)
- [x] Magical damage transition at level 3+
- [x] Movement type progression (7→10 movement)
- [x] Snow dog mounted movement type
- [x] Twilight alignment integration
- [x] Higher XP requirements for late-game power

### Integration Points
- **Movement Types**: snow_dog_mounted defined in movement_types.cfg
- **Unit Definitions**: Complete progression in units/frost_clans.cfg
- **Documentation**: Updated in faction_units_template.md
- **Abilities**: Pack frenzy mechanics implemented in unit specials

### Balance Considerations
- **Early Game**: Weak individual attacks balanced by volume
- **Mid Game**: Magical damage provides utility against armored units
- **Late Game**: High mobility and leadership create elite shock cavalry
- **Experience Cost**: 40-50% higher XP requirements maintain faction balance

## 🎲 Pack Frenzy Mechanics Detail

### Random Targeting Algorithm
1. **First Attack**: Always hits player-selected target
2. **Subsequent Attacks**: Each randomly selects from adjacent hexes containing enemies
3. **No Double-Targeting**: Same enemy can be hit multiple times by chance
4. **Range Limitation**: Only affects hexes adjacent to the attacking unit

### Tactical Scenarios
- **Single Enemy**: Only first attack effective, others wasted
- **Dense Formation**: Maximum effectiveness with multiple adjacent targets
- **Flanking Position**: Ideal for hitting multiple enemy units simultaneously
- **Siege Breaking**: Excellent against clustered defensive positions

This design creates a unique cavalry experience where positioning and enemy formation awareness become critical tactical elements, while the creative naming system enhances the thematic identity of the Frost Clans faction.