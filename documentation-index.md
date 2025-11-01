# Ice Age Expansion - Documentation Index

## 📚 **Quick Navigation Guide**

This index provides a complete overview of all documentation files in the Ice Age expansion project, making it easy to locate and update information efficiently.

---

## 🗂️ **Core Documentation Files**

### **📋 Project Overview**
- **File**: `README.md`
- **Purpose**: Main project description, installation instructions, feature overview
- **Last Updated**: Initial creation
- **Update When**: Major feature additions, release information changes

### **📋 Project Management**
- **File**: `frost-clans-progression.md` 
- **Purpose**: Complete Frost Clans faction progression system and strategic analysis
- **Content**: 4-level unit trees, experience scaling, tactical implications, power analysis
- **Last Updated**: Extended unit system implementation
- **Update When**: Unit balance changes, progression modifications, strategic analysis updates

---

## 🏔️ **Faction Documentation**

### **❄️ Frost Clans (IMPLEMENTED)**

#### **📁 Unit Design Files**
- **Directory**: `unit-designs/`
- **Purpose**: Individual unit line documentation files
- **Files**: 
  - `bear-rider-design.md` - Bear cavalry progression
  - `infantry-line-design.md` - Frost Warrior line
  - `ranged-line-design.md` - Frost Scout line  
  - `snow-dog-cavalry-design.md` - Pack Rider line
- **Last Updated**: Reorganized into dedicated unit design directory
- **Update When**: Unit balance changes, ability modifications, new unit lines added

#### **⚔️ All Unit Lines**
- **File**: `units/frost_clans.cfg` (WML Implementation)
- **Purpose**: Complete WML definitions for all Frost Clans units
- **Content**: 16 total units across 4 progression lines with custom abilities
- **Key Features**: Higher XP requirements, dual alignment system, elite level 4 powers
- **Last Updated**: Extended to 4+ levels with enhanced abilities
- **Update When**: Unit stats changes, new abilities, balance adjustments

#### **🎖️ Faction Recruitment**
- **File**: `factions/frost_clans.cfg` (WML Implementation) 
- **Purpose**: Faction definition and recruitment options
- **Content**: Recruitable units, terrain preferences, AI behavior
- **Last Updated**: Added Bear_Rider to recruitment list
- **Update When**: New recruitable units, faction behavior changes

### **🧊 Ice Dwellers (PLANNED)**
- **Status**: Not yet implemented
- **Planned Features**: Magical ice specialists, 4+ level progression system
- **Next Steps**: Apply same progression philosophy as Frost Clans with unique abilities

---

## 🔧 **Technical Implementation**

### **🌍 Era Integration**
- **File**: `eras.cfg`
- **Purpose**: Defines multiplayer eras that include Ice Age factions
- **Content**: Three eras - Default+Ice Age, Default+Dunefolk+Ice Age, Pure Ice Age
- **Last Updated**: Complete era system with faction integration
- **Update When**: New factions added, era balance changes, multiplayer integration updates

### **📚 Era Documentation**
- **File**: `era-integration.md`
- **Purpose**: Complete guide to multiplayer era system and strategic implications
- **Content**: Era descriptions, faction roles, AI behavior, strategic recommendations
- **Last Updated**: Full integration system with 3 era options
- **Update When**: Era mechanics change, faction balance updates, strategic meta shifts

### **🚶 Movement Systems**
- **File**: `movement_types.cfg`
- **Purpose**: Custom movement types for specialized units
- **Content**: bear_mounted (excellent ice/forest, poor water), ice_beast planned
- **Last Updated**: Bear Rider implementation
- **Update When**: New unit types require custom movement, terrain interactions change

### **🎮 Game Extensions**
- **File**: `game-extensions/custom-alignments-and-mechanics.md`
- **Purpose**: Custom alignments (Solaris-Noctis, Twilight) and ice-themed mechanics
- **Content**: Alignment definitions, strategy matrix, tactical implications, ice abilities
- **Last Updated**: Moved from main faction file to dedicated extensions directory
- **Update When**: Alignment mechanics change, new alignments added, ice abilities modified

### **🎯 Abilities System**
- **File**: `custom-abilities.md`
- **Purpose**: Complete reference for all custom faction abilities
- **Content**: 20+ designed abilities including signature powers and tactical abilities
- **Last Updated**: Initial comprehensive design
- **Update When**: New abilities added, existing abilities modified, balance changes

---

## 🔥 **Specialized Units**

### **🔥 Fire Units Integration**
- **File**: `fire-units-design.md`
- **Purpose**: Design document for fire creatures integrated into ice factions
- **Content**: 4 fire units (2 per faction) with thematic integration and balance
- **Key Features**: Fire/ice tension, strategic balance, narrative richness
- **Last Updated**: Added Bear Rider to Frost Clans section
- **Update When**: Fire unit implementation, balance changes, new fire creatures

---

## 📝 **Templates and Reference**

### **📋 Faction Design Template**
- **File**: `faction_units_template.md`
- **Purpose**: Template and reference for faction design with examples
- **Content**: Unit categories, alignment system, implementation examples using Frost Clans
- **Last Updated**: Replaced examples with actual Frost Clans implementation
- **Update When**: New factions designed, template improvements, reference updates

### **📋 Documentation Index** (This File)
- **File**: `documentation-index.md`
- **Purpose**: Central navigation and file organization guide
- **Content**: Complete file listing, update triggers, content summaries
- **Update When**: New files created, major content changes, reorganization

---

## 🎮 **Campaign and Scenarios**

### **📚 Campaign Files** (TO BE DOCUMENTED)
- **Location**: `campaigns/` directory
- **Status**: Exist but not yet documented in detail
- **Contents**: 4 campaigns with scenario files
- **Next Steps**: Create comprehensive campaign documentation

---

## 🔄 **Update Workflow Guide**

### **When Adding New Units:**
1. Update WML files (`units/*.cfg`)
2. Update faction recruitment (`factions/*.cfg`) 
3. Update progression documentation (`*-progression.md`)
4. Update template examples (`faction_units_template.md`)
5. Update this index if new files created

### **When Modifying Abilities:**
1. Update WML implementations
2. Update `custom-abilities.md` reference
3. Update specific unit design documents
4. Update faction progression analysis

### **When Adding New Factions:**
1. Create faction-specific design document
2. Implement WML files (`units/`, `factions/`)
3. Update `faction_units_template.md` with examples
4. Update this index with new files
5. Update project overview (`README.md`)

### **When Balancing:**
1. Update WML stat values
2. Update progression analysis documents  
3. Update tactical implications in faction documents
4. Update ability descriptions if mechanics change

---

## 📊 **File Size and Complexity Guide**

### **Large, Complex Files (Require Careful Updates)**
- `frost-clans-progression.md` - Comprehensive faction analysis
- `units/frost_clans.cfg` - Complete WML implementation
- `faction_units_template.md` - Full template with examples

### **Medium Files (Moderate Updates)**
- `bear-rider-design.md` - Specific unit line documentation
- `custom-alignments-implementation.md` - Technical alignment guide
- `fire-units-design.md` - Specialized unit integration

### **Small Files (Quick Updates)**
- `movement_types.cfg` - Simple WML definitions
- `factions/*.cfg` - Faction recruitment lists
- Configuration and setup files

---

## 🎯 **Priority Update Targets**

### **High Priority** (Frequently Updated)
- Unit WML files when balancing
- Progression documentation when adding levels
- Faction templates when adding examples

### **Medium Priority** (Occasional Updates)
- Ability documentation when adding powers
- Alignment documentation when mechanics change
- Design documents when major reworks occur

### **Low Priority** (Rare Updates)
- This index when restructuring
- README when major features complete
- Template structure when methodology changes

---

## 🔍 **Quick Search References**

### **Find Unit Stats**: Check `units/*.cfg` and `*-progression.md` files
### **Find Abilities**: Check `custom-abilities.md` and specific unit design files  
### **Find Alignment Info**: Check `custom-alignments-implementation.md` and `faction_units_template.md`
### **Find Balance Data**: Check progression documents and unit design files
### **Find Implementation Code**: Check WML files (`*.cfg`) and implementation guides

This index serves as the central navigation hub for the entire Ice Age expansion documentation ecosystem. Keep it updated as the project grows!