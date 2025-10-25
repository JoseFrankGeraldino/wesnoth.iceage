# Wesnoth Ice Age - Project Development Plan

## Project Overview
**Goal:** Create a complete Battle for Wesnoth expansion featuring two new ice-themed factions and four interconnected campaigns spanning multiple generations.

---

## Phase 1: Foundation & Design (Current Phase)

### 1.1 Faction Selection ✓
Choose two civilizations from the mythology research:
- **Option A:** Norse (Jötnar/Frost Giants) + Slavic (Morozko's People)  
- **Option B:** Celtic (Cailleach's Clan) + Inuit (Sedna's Children)
- **Option C:** Norse (Ullr's Folk) + Mongolian/Siberian (Ice Shamans)

### 1.2 Unit Design ✓
- Complete the faction unit template for both chosen factions
- Design 8-12 units per faction across all categories
- Balance units against existing Wesnoth factions
- Create unique ice-themed abilities and mechanics

### 1.3 Campaign Structure ✓
- Detailed summaries completed for all 4 campaigns
- Character bloodline established
- Political complexity progression planned

---

## Phase 2: Technical Implementation

### 2.1 Wesnoth Add-on Structure
Create proper WML (Wesnoth Markup Language) files:
```
wesnoth.iceage/
├── _main.cfg                 # Main add-on configuration
├── _server.pbl              # Server publication info
├── factions/
│   ├── [faction1]/
│   │   ├── units/           # Individual unit definitions
│   │   └── _main.cfg        # Faction configuration
│   └── [faction2]/
│       ├── units/
│       └── _main.cfg
├── campaigns/
│   ├── The_Forbidden_North/
│   │   ├── _main.cfg
│   │   ├── scenarios/       # Individual scenario files
│   │   └── utils/          # Campaign-specific code
│   ├── The_Ice_Bleeds_Black/
│   ├── The_Long_Road_South/
│   └── The_Ice_Crown_Wars/
├── images/                  # Custom unit sprites and portraits
├── sounds/                  # Custom sound effects
└── translations/           # Multi-language support
```

### 2.2 Unit Implementation
For each unit, create WML files containing:
- Base statistics (HP, movement, cost, alignment)
- Attack definitions (damage, type, special abilities)
- Resistance values
- Advancement paths
- Animations and graphics references

### 2.3 Terrain and Special Mechanics
- Custom ice terrain types (if needed)
- Ice-specific abilities (freeze, blizzard, etc.)
- Weather effects
- Special victory conditions

---

## Phase 3: Campaign Development

### 3.1 Scenario Design Process
For each campaign:
1. **Story Development:** Detailed plot for each scenario
2. **Map Creation:** Custom maps using Wesnoth's map editor
3. **Scripting:** WML scripting for events, dialogue, objectives
4. **Balancing:** Difficulty testing and adjustment

### 3.2 Campaign 1: "The Forbidden North" (15 scenarios)
- Focus: Introduction to factions and world-building
- Complexity: Simple tactical combat
- Key Features: Tutorial elements, faction showcase

### 3.3 Campaign 2: "The Ice Bleeds Black" (16 scenarios)  
- Focus: Survival horror, multiple perspectives
- Complexity: Resource management, desperate tactics
- Key Features: Playing as both good and evil units

### 3.4 Campaign 3: "The Long Road South" (16 scenarios)
- Focus: Diplomacy and alliance-building  
- Complexity: Multi-faction interactions
- Key Features: Reputation system, branching paths

### 3.5 Campaign 4: "The Ice Crown Wars" (25 scenarios)
- Focus: Grand strategy and politics
- Complexity: Large-scale battles, multiple objectives
- Key Features: Faction management, multiple endings

---

## Phase 4: Asset Creation

### 4.1 Visual Assets
- Unit sprites (following Wesnoth art style)
- Unit portraits
- Terrain graphics (if custom terrain needed)
- Campaign story images
- UI elements

### 4.2 Audio Assets
- Battle sounds for ice-themed attacks
- Ambient sounds (wind, ice cracking, etc.)
- Music themes for campaigns (optional)

### 4.3 Text Assets
- Unit descriptions
- Campaign dialogue
- Help entries
- Translation frameworks

---

## Phase 5: Testing & Balancing

### 5.1 Unit Balance Testing
- Compare damage output vs existing factions
- Test unit synergies and counter-strategies
- Multiplayer balance verification

### 5.2 Campaign Testing
- Scenario difficulty progression
- Story coherence and pacing
- Technical bug identification

### 5.3 Community Testing
- Release beta versions for community feedback
- Incorporate suggestions and bug reports
- Performance optimization

---

## Phase 6: Publication & Maintenance

### 6.1 Add-on Server Publication
- Prepare _server.pbl file
- Upload to official Wesnoth add-on server
- Create forum announcement

### 6.2 Documentation
- Player guides
- Technical documentation for other modders
- Faction strategy guides

### 6.3 Post-Release Support
- Bug fixes
- Balance adjustments
- Community-requested features

---

## Current Status & Next Steps

### Completed ✅
- Mythology research for faction inspiration
- Unit design template with Dunefolk reference
- Detailed campaign summaries with character progression
- Project structure planning

### Immediate Next Steps 📋
1. **Choose your two favorite civilizations** from the mythology list
2. **Fill out the unit template** for both factions
3. **Create basic WML structure** for the add-on
4. **Design 2-3 basic units** as proof of concept

### Development Timeline Estimate
- **Phase 1:** 2-3 weeks (design completion)
- **Phase 2:** 4-6 weeks (technical setup)
- **Phase 3:** 12-16 weeks (campaign development)
- **Phase 4:** 6-8 weeks (asset creation)
- **Phase 5:** 3-4 weeks (testing)
- **Phase 6:** 1-2 weeks (publication)

**Total Estimated Timeline:** 6-8 months for complete project

---

## Required Skills & Resources

### Technical Skills Needed
- WML (Wesnoth Markup Language) programming
- Wesnoth map editor usage
- Basic scripting for events and dialogue
- Image editing (for unit sprites)

### Helpful Resources
- [Wesnoth Wiki - WML Reference](https://wiki.wesnoth.org/WML)
- [Wesnoth Forum - Add-on Development](https://forums.wesnoth.org/viewforum.php?f=8)
- [Unit Creation Tutorial](https://wiki.wesnoth.org/UnitWML)
- [Campaign Creation Guide](https://wiki.wesnoth.org/CampaignWML)

### Community Support
- Wesnoth development community is very helpful
- Existing add-ons can serve as code examples
- Art and music communities for asset creation