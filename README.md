# Wesnoth: Ice Age Expansion

A comprehensive Battle for Wesnoth expansion featuring two new ice-themed factions and four interconnected campaigns set in a frozen world.

## Project Overview

This expansion introduces the frozen northern lands beyond the known world, where ancient ice civilizations have thrived in isolation until recent events threaten their very existence. Players will experience an epic saga through the eyes of ice folk heroes as they face invasion, survival, and the struggle to restore balance to their world.

## Features

### Two New Factions

#### 1. Frost Clans
Hardy northern warriors who have adapted to life in the frozen wastes. They are fierce fighters who use the cold to their advantage.

**Unit Types:**
- Frost Warrior → Frost Champion → Frost Chieftain
- Frost Scout → Frost Ranger
- Frost Rider → Frost Knight

**Faction Traits:**
- Balanced faction with good infantry, ranged, and cavalry units
- Cold damage on most attacks
- Neutral alignment

#### 2. Ice Dwellers
Mystical beings born from the eternal ice, commanding the powers of frost and cold.

**Unit Types:**
- Ice Elemental → Greater Ice Elemental → Frost Lord
- Frost Wraith → Frost Banshee
- Ice Beast → Frost Behemoth

**Faction Traits:**
- Magical and spectral units
- Strong cold resistance but weak to fire
- Powerful but expensive units

### Implemented Campaigns (Current Status)

#### 1. The Frozen Wastes (Introductory)
**Difficulty:** Easy  
**Play as:** Frost Clans  
**Scenarios:** 5

Lead the Frost Clans as they struggle to survive an increasingly harsh winter. Secure resources, defend against raiders, and discover ancient caverns that may provide shelter.

#### 2. Rise of the Frost King (Continuation)
**Difficulty:** Normal  
**Play as:** Frost Clans  
**Scenarios:** 4

A powerful Frost King emerges, seeking to plunge the world into eternal winter. Unite the clans and face this ancient threat before it's too late.

#### 3. The Ice Dwellers' Pact (Parallel Story)
**Difficulty:** Normal  
**Play as:** Ice Dwellers  
**Scenarios:** 4

Experience the ice age from the perspective of Glacius, an ancient Frost Lord. Decide whether to help or hinder the mortal clans in their struggle, and ultimately choose to stand against the tyrannical Frost King.

#### 4. The Great Thaw (Final Campaign)
**Difficulty:** Hard  
**Play as:** Frost Clans (with Ice Dwellers as allies)  
**Scenarios:** 4

With the Frost King defeated, work with the Ice Dwellers to restore balance to the world and end the eternal winter once and for all.

### Future Expansion Plans
The current implementation provides a solid foundation. Future plans include expanding to the original vision:

- **Extended campaign series** with multi-generational storyline
- **Additional scenarios** bringing total to 70+
- **Complex political intrigue** involving all major Wesnoth factions
- **Enhanced mechanics** and special abilities

## Installation

1. Download or clone this repository
2. Copy the entire folder to your Wesnoth user data directory under `data/add-ons/`
   - Linux: `~/.local/share/wesnoth/1.XX/data/add-ons/`
   - Windows: `Documents\My Games\Wesnoth1.XX\data\add-ons\`
   - macOS: `~/Library/Application Support/Wesnoth_1.XX/data/add-ons/`
3. Launch Battle for Wesnoth
4. The campaigns will appear in the campaign selection menu
5. The factions will be available in multiplayer

## Development Status

- ✅ **Phase 1:** Foundation & Design - Mythology research, unit templates, campaign summaries
- ✅ **Phase 2:** Technical Implementation - WML structure, unit coding, basic campaigns
- 📋 **Phase 3:** Campaign Enhancement - Expanded scenarios, advanced scripting
- ⏳ **Phase 4:** Asset Creation - Custom graphics, sounds, portraits
- ⏳ **Phase 5:** Testing & Balancing - Community testing, refinement
- ⏳ **Phase 6:** Extended Content - Multi-generational campaigns

## Project Files

- `faction_units_template.md` - Unit design template with Dunefolk reference
- `campaign_summaries.md` - Detailed summaries of planned expanded campaigns
- `project_plan.md` - Complete development roadmap and technical details
- `STRUCTURE.md` - Technical documentation of current implementation

## Story Overview

The world is gripped by an eternal winter. The Frost Clans, hardy northern warriors, struggle to survive as the cold grows ever more severe. Ancient Ice Dwellers, beings of pure frozen magic, awaken from their slumber. At the center of it all looms the Frost King, an ancient entity seeking to freeze the world forever.

Through four interconnected campaigns, experience an epic tale of survival, alliance, and the struggle to restore balance between ice and warmth.

## Credits

**Author:** Jose Geraldino  
**Version:** 1.0.0  
**License:** GPL v2+ (code), CC-BY-SA (art assets)

## Technical Details

- Compatible with Battle for Wesnoth 1.14+
- Uses standard Wesnoth WML (Wesnoth Markup Language)
- Current: 17 scenarios across 4 campaigns
- 15 unique unit types (7 Frost Clans, 8 Ice Dwellers)

## Contributing

Contributions are welcome! Feel free to:
- Report bugs or balance issues
- Suggest new scenarios or features
- Submit translations
- Improve unit sprites or portraits

## Version History

### 1.0.0 (2025)
- Initial release
- Two factions: Frost Clans and Ice Dwellers
- Four campaigns with 17 total scenarios
