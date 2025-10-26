# Developer User Stories - Ice Age Campaign

## Current Status: ⚠️ **Prototype/Framework Complete**

The campaigns are currently in a **playable prototype state** with basic structure but missing essential content and assets. The following work is needed to make them production-ready.

---

## 📖 **Content & Storytelling**

### **High Priority - Required for Playability**

#### **📍 Campaign Maps**
- [ ] **Create scenario map files** (.map format)
  - Missing: All 17 scenario maps (currently using placeholder references)
  - Required: Custom terrain layouts for each scenario
  - Tools: Wesnoth Map Editor (built into the game)
  - Current: Scenarios reference non-existent map files

#### **🎭 Character Development**
- [ ] **Expand dialogue and storyline**
  - Current: Basic placeholder dialogue
  - Needed: Rich character interactions, plot development
  - Focus: Make Thorvald, Glacius, and other leaders compelling
  - Add: Character backstories, motivations, relationships

#### **📜 Scenario Objectives & Events**
- [ ] **Design victory/defeat conditions**
  - Current: Basic "defeat enemies" objectives
  - Needed: Varied objectives (rescue, survival, exploration, etc.)
  - Add: Mid-scenario events, plot twists, choices

#### **🎨 Visual Assets**
- [ ] **Campaign portraits** (recommended: 400x400px PNG)
  - Thorvald (Frost Clans leader)
  - Glacius (Ice Dwellers leader)
  - Erik (Frost Warrior companion)
  - Frost King (main antagonist)
  - Various scenario NPCs

- [ ] **Campaign artwork**
  - Campaign selection images
  - Scenario splash screens
  - Story sequence backgrounds

#### **🎵 Audio (Optional but Recommended)**
- [ ] **Custom music themes**
  - Winter/ice ambient tracks
  - Battle music for frost-themed combat
  - Emotional themes for story moments

---

## 🎮 **Gameplay Design**

#### **⚖️ Balance & Difficulty**
- [ ] **Unit statistics tuning**
  - Current: Basic stats assigned
  - Needed: Playtesting and balance adjustments
  - Focus: Make both factions viable and interesting

- [ ] **Scenario difficulty progression**
  - Easy start with tutorial elements
  - Gradual complexity increase
  - Fair but challenging final scenarios

#### **🎯 Mission Design**
- [ ] **Unique scenario mechanics**
  - Environmental hazards (blizzards, ice breaking)
  - Time-sensitive objectives
  - Multiple solution paths
  - Alliance/betrayal mechanics

#### **🏆 Player Rewards**
- [ ] **Gold and carryover balancing**
- [ ] **Special items or abilities between scenarios**
- [ ] **Unlockable content or achievements**

---

## 🧪 **Testing & Validation**

#### **🎮 Gameplay Testing**
- [ ] **Unit recruitment testing**
  - Verify all 15 units can be recruited properly
  - Test advancement paths work correctly
  - Validate attack animations and sound effects
  - Check unit costs and availability balance

- [ ] **Campaign flow testing**
  - Test scenario transitions between campaigns
  - Verify gold carryover mechanics work as intended
  - Test save/load functionality across scenarios
  - Ensure story continuity between scenarios

- [ ] **Combat balance testing**
  - Playtest faction matchups for fairness
  - Test unit effectiveness in different terrain types
  - Validate special abilities function correctly
  - Check AI behavior and difficulty scaling

#### **🔧 Technical Validation**
- [ ] **Era System Testing** ⚡ *HIGH PRIORITY* 🚨 **CRITICAL ISSUES FOUND**
  - ✅ All 4 eras appear in multiplayer setup (including test era)
  - ✅ "Default + Dunefolk + Ice Age" era shows all 9 factions correctly  
  - 🚨 **CRITICAL**: Frost Clans shows "Random" option but no leader units selectable
  - 🚨 **CRITICAL**: Ice Dwellers shows no "Random" option and no leader units
  - 🚨 **CRITICAL**: Test era "Frost Clans (Test)" recruits DRAKE units instead of Ice Age units
  - 🚨 **ROOT ISSUE**: Faction mapping completely broken - wrong units being loaded
  - 🚨 **HYPOTHESIS**: Ice Age units not loading at all, falling back to default Drake faction
  - [ ] Validate faction recruitment lists work properly (blocked by unit loading failure)
  - [ ] Test random leader selection functions correctly (blocked by unit loading failure)

- [ ] **Faction Configuration Testing** ⚡ *HIGH PRIORITY*
  - Verify all 16 Frost Clans unit types are recognized
  - Test Frost Clans recruitment (Frost Warrior, Frost Scout, Pack_Rider, Bear_Rider)
  - Verify all 7 Ice Dwellers unit types are recognized
  - Test Ice Dwellers recruitment (Ice Elemental, Frost Wraith, Ice Beast)
  - Validate leader options work (Frost Chieftain, Frost_Warlord, Ancient_Bear_Lord, Primal_Bear_Champion)

- [ ] **Unit Progression Testing** ⚡ *HIGH PRIORITY*
  - Test all 4-level advancement chains work correctly
  - Verify Pack_Rider → Wolf_Ranger → Storm_Rider → Blizzard_Lord progression
  - Test Bear_Rider → Dire_Bear_Rider → Ancient_Bear_Lord → Primal_Bear_Champion progression
  - Validate custom alignments (solaris_noctis, twilight) function properly
  - Test pack frenzy mechanics with random adjacent targeting

- [ ] **WML Syntax Validation** ⚡ *HIGH PRIORITY* 🎯 **ROOT CAUSE IDENTIFIED**
  - ✅ **VERIFIED**: All 23 units properly defined in code
  - ✅ **VERIFIED**: All image files are valid standard Wesnoth images  
  - ✅ **VERIFIED**: Loading order is correct (units → eras → campaigns)
  - ✅ **VERIFIED**: Leader units (`Frost Chieftain`, `Frost_Warlord`, etc.) exist and properly defined
  - 🚨 **ROOT CAUSE**: Custom alignments (`solaris_noctis`, `twilight`) not recognized by Wesnoth 1.18
  - 🚨 **RESULT**: Unit files rejected during parsing, causing fallback to Drake faction
  - 🎯 **SOLUTION**: Replace custom alignments with standard ones (`lawful`, `neutral`) for immediate fix
  - [ ] Test custom movement types (bear_mounted, snow_dog_mounted) load correctly  
  - [ ] Validate custom abilities don't cause crashes
  - � **CONFIRMED ASSETS**:
    - 16 Frost Clans units using standard Wesnoth human-loyalist images ✅
    - 7 Ice Dwellers units using standard Wesnoth undead/monster images ✅
    - No custom image files required ✅

- [ ] **Cross-platform compatibility**
  - Test on Windows, Mac, Linux if possible
  - Verify different Wesnoth 1.18 versions
  - Check Steam vs standalone installations
  - Validate add-on loading and recognition

- [ ] **Performance testing**
  - Test large battles for performance issues
  - Check memory usage during long campaigns
  - Validate loading times for scenarios
  - Test multiplayer stability if implemented

---

## 📚 **Documentation**

#### **📖 Player Guides**
- [ ] **Campaign introduction/tutorial**
- [ ] **Faction strategy guides**
- [ ] **Walkthrough hints for difficult scenarios**

#### **🌍 World Building**
- [ ] **Detailed lore document**
- [ ] **Character relationship charts**
- [ ] **Timeline of events across all campaigns**

---

## 🎨 **Asset Creation Guidelines**

### **Map Requirements**
- Use Wesnoth's built-in Map Editor
- Focus on snow, ice, and mountain terrain
- Include villages, keeps, and strategic chokepoints
- Size: Typically 30x30 to 50x50 hexes

### **Portrait Specifications**
- Format: PNG with transparency
- Size: 400x400 pixels recommended
- Style: Match Wesnoth's art direction
- Mood: Reflect character personality and campaign tone

### **Story Integration**
- Each scenario should advance the overarching plot
- Character development should be consistent across campaigns
- Dialogue should feel natural and engaging
- Cultural references should draw from the Ice Mythology Guide

---

## 📋 **Priority Order**

1. **🔥 Critical (Blocks Gameplay)**
   - Create basic map files for each scenario
   - Expand core dialogue and objectives

2. **⚡ High Priority**
   - Character portraits and main artwork
   - Balance unit statistics
   - Design unique scenario mechanics

3. **📈 Medium Priority**
   - Additional story content and character development
   - Environmental audio and music
   - Advanced gameplay features

4. **✨ Polish Phase**
   - Achievement system
   - Detailed lore documentation
   - Advanced visual effects

---

## 🤝 **Collaboration Notes**

- **Testing**: Regular playtesting needed after each major addition
- **Feedback Loop**: Iterate on player feedback for story and balance
- **Version Control**: Document changes and maintain changelog
- **Art Direction**: Maintain consistent visual style across all assets

The framework is solid - now it needs your creative content to bring these campaigns to life!