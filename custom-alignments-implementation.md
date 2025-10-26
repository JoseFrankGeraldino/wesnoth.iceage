# Custom Alignments Implementation Guide

## 🌅 **Technical Implementation for Ice Age Alignments**

This document provides the technical details for implementing the two new custom alignments in the Battle for Wesnoth Ice Age expansion: **Twilight** and **Solaris-Noctis**.

---

## 📋 **Alignment Definitions**

### **WML Implementation Structure**

In Wesnoth, alignments are implemented through the `[time]` tags in scenarios and unit alignment properties. Here's how to implement the custom alignments:

#### **Core Alignment Files Needed:**

```
# New files to create:
alignments/
├── twilight.cfg         # Twilight alignment definition
└── solaris_noctis.cfg   # Solaris-Noctis alignment definition

# Modified files:
_main.cfg             # Include custom alignments
units/                # Update unit files with new alignments
```

---

## 🌆 **Twilight Alignment Implementation**

### **WML Code Structure:**

```wml
# In alignments/twilight.cfg
[alignment]
    id=twilight
    name= _ "twilight"
    description= _ "Twilight units fight best during dawn and dusk, drawing power from transition moments."
    
    # Time-based damage modifiers
    [time_area]
        id=twilight_bonus
        [time]
            id=dawn
            name= _ "Dawn"
            image=misc/time-schedules/default/dawn.png
            lawful_bonus=25
            neutral_bonus=0
            chaotic_bonus=-25
            twilight_bonus=25         # Custom property
            solaris_noctis_bonus=-25  # Weak during transitions
        [/time]
        
        [time]
            id=dusk  
            name= _ "Dusk"
            image=misc/time-schedules/default/dusk.png
            lawful_bonus=25
            neutral_bonus=0
            chaotic_bonus=-25
            twilight_bonus=25         # Custom property
            solaris_noctis_bonus=-25  # Weak during transitions
        [/time]
        
        [time]
            id=midday
            name= _ "Midday"
            image=misc/time-schedules/default/midday.png
            lawful_bonus=25
            neutral_bonus=0
            chaotic_bonus=-25
            twilight_bonus=-25        # Custom penalty during extremes
            solaris_noctis_bonus=25   # Strong during extremes
        [/time]
        
        [time]
            id=midnight
            name= _ "Midnight"
            image=misc/time-schedules/default/midnight.png
            lawful_bonus=-25
            neutral_bonus=0
            chaotic_bonus=25
            twilight_bonus=-25        # Custom penalty during extremes
            solaris_noctis_bonus=25   # Strong during extremes
        [/time]
        
        # Additional time periods...
    [/time_area]
[/alignment]
```

### **Unit Implementation:**

```wml
# In unit files, use:
[unit_type]
    id=Twilight_Shaman
    name= _ "Twilight Shaman"
    # ... other properties ...
    alignment=twilight
    
    # Optional: Custom abilities that enhance twilight theme
    [abilities]
        [twilight_power]
            id=twilight_power
            name= _ "twilight power"
            description= _ "This unit gains additional abilities during dawn and dusk."
            
            [filter_self]
                [filter_location]
                    time_of_day=dawn,dusk
                [/filter_location]
            [/filter_self]
            
            # Add regeneration during twilight hours
            [regenerate]
                value=4
                affects_self=yes
            [/regenerate]
        [/twilight_power]
    [/abilities]
[/unit_type]
```

---

## 🌟 **Solaris-Noctis Alignment Implementation**

### **Key Features:**
- **Bonus**: +25% during midday (blazing sun power) and midnight (deepest cold power)
- **Penalty**: -25% during dawn and dusk (weak during transitions)
- **Theme**: Extremes of fire and ice, peak power moments, elemental mastery

### **WML Structure:**

```wml
# In alignments/solaris_noctis.cfg
[alignment]
    id=solaris_noctis
    name= _ "solaris-noctis"
    description= _ "Solaris-Noctis units harness the power of extremes - blazing sun and deepest cold, strongest at the peak moments of day and night."
    
    # Custom schedule with solaris-noctis bonuses
    [schedule]
        [time]
            id=midday
            solaris_noctis_bonus=25    # Peak sun power
        [/time]
        [time]
            id=midnight  
            solaris_noctis_bonus=25    # Peak cold power
        [/time]
        [time]
            id=dawn
            solaris_noctis_bonus=-25   # Weak during transitions
        [/time]
        [time]
            id=dusk
            solaris_noctis_bonus=-25   # Weak during transitions
        [/time]
        [time]
            id=morning
            solaris_noctis_bonus=0     # Neutral during in-between times
        [/time]
        [time]
            id=afternoon
            solaris_noctis_bonus=0     # Neutral during in-between times
        [/time]
        [time]
            id=first_watch
            solaris_noctis_bonus=0     # Neutral during in-between times
        [/time]
        [time]
            id=second_watch
            solaris_noctis_bonus=0     # Neutral during in-between times
        [/time]
    [/schedule]
[/alignment]
```

### **Extreme-Enhanced Abilities:**

```wml
# Solaris-Noctis units have dual-nature abilities
[abilities]
    [extremes_mastery]
        id=fire_ice_mastery
        name= _ "extremes mastery"
        description= _ "This unit channels fire at midday and ice at midnight, gaining special powers during peak hours."
        
        # Fire power at midday
        [filter_self]
            [filter_location]
                time_of_day=midday
            [/filter_location]
        [/filter_self]
        [effect]
            apply_to=attack
            range=melee
            [set_specials]
                mode=append
                [burns]
                    id=solar_flame
                    name= _ "solar flame"
                    description= _ "This attack burns enemies with solar fire."
                [/burns]
            [/set_specials]
        [/effect]
        
        # Ice power at midnight  
        [filter_self]
            [filter_location]
                time_of_day=midnight
            [/filter_location]
        [/filter_self]
        [effect]
            apply_to=attack
            range=melee
            [set_specials]
                mode=append
                [freeze]
                    id=deep_freeze
                    name= _ "deep freeze"
                    description= _ "This attack freezes enemies with arctic cold."
                [/freeze]
            [/set_specials]
        [/effect]
    [/extremes_mastery]
[/abilities]
```

---

## ⚙️ **Integration with Existing Systems**

### **Schedule Modifications**

To implement custom alignments system-wide, scenarios need updated schedules:

```wml
# In scenario files:
[scenario]
    id=example_scenario
    # ... other properties ...
    
    # Custom schedule with all alignment support
    {EXTENDED_SCHEDULE_WITH_CUSTOM_ALIGNMENTS}
    
    # Or manual schedule definition:
    [time_area]
        [time]
            id=dawn
            name= _ "Dawn"
            image=misc/time-schedules/default/dawn.png
            red=0
            green=0  
            blue=0
            lawful_bonus=25
            neutral_bonus=0
            chaotic_bonus=-25
            twilight_bonus=25
            solaris_bonus=25
            noctis_bonus=-25
        [/time]
        # ... repeat for all time periods
    [/time_area]
[/scenario]
```

### **Macros for Easy Implementation**

```wml
# Create macros in _main.cfg for easy use:

#define TWILIGHT_TRANSITION_BONUS
    twilight_bonus=25
    solaris_noctis_bonus=-25
#enddef

#define SOLARIS_NOCTIS_EXTREME_BONUS  
    twilight_bonus=-25
    solaris_noctis_bonus=25
#enddef

#define NEUTRAL_TIME_PROPERTIES
    twilight_bonus=0
    solaris_noctis_bonus=0
#enddef

#define DAWN_DUSK_TIME_PROPERTIES
    {TWILIGHT_TRANSITION_BONUS}
#enddef

#define MIDDAY_MIDNIGHT_TIME_PROPERTIES
    {SOLARIS_NOCTIS_EXTREME_BONUS}
#enddef
```

---

## 🎮 **Testing and Validation**

### **Test Scenarios**

Create test scenarios to verify alignment behavior:

```wml
# test_alignments.cfg
[scenario]
    id=test_custom_alignments
    name= _ "Alignment Testing"
    
    [side]
        side=1
        controller=human
        recruit=Twilight_Shaman,Fire_Ice_Elemental,Flame_Wraith
    [/side]
    
    [event]
        name=start
        [message]
            speaker=narrator
            message= _ "Test custom alignments at different times of day."
        [/message]
        
        # Force time changes for testing
        [time_area]
            # Cycle through all time periods
        [/time_area]
    [/event]
[/scenario]
```

### **Balance Validation**

Monitor alignment performance across different time periods:

```wml
# Debug events to track alignment effectiveness
[event]
    name=attack_end
    [filter_attack]
        [filter_attacker]
            alignment=twilight,solaris_noctis  
        [/filter_attacker]
    [/filter_attack]
    
    [message]
        speaker=narrator
        message= _ "Custom alignment unit attacked with $time_of_day modifier."
    [/message]
[/event]
```

---

## 🔧 **Implementation Priority**

### **Phase 1: Core Mechanics**
1. Create basic alignment definitions
2. Implement time-of-day modifiers
3. Test with simple units

### **Phase 2: Advanced Features**
4. Add alignment-specific abilities
5. Create synergy with existing ice abilities
6. Implement terrain interactions

### **Phase 3: Polish**
7. Balance testing across scenarios
8. Visual effects for alignment bonuses
9. UI indicators for time-based bonuses

---

## 📚 **Technical Notes**

- **Compatibility**: Ensure alignment system works with existing Wesnoth time schedules
- **Performance**: Custom alignments should not impact game performance
- **Multiplayer**: All players must have consistent alignment definitions
- **Localization**: All alignment names and descriptions need translation support

This implementation creates a rich tactical layer where timing becomes crucial to army composition and battle strategy, perfectly fitting the ice age theme of survival through adaptation and timing.