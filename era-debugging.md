# Ice Age Era Testing - Simplified Configuration

## 🚨 **Current Issue Analysis**

Based on the screenshots and testing:

### **Problem**: Leader Selection Not Working
1. **Frost Clans**: Shows "Random" option but no individual leader units selectable
2. **Ice Dwellers**: No "Random" option at all, completely broken leader selection

### **Potential Causes**
1. **Custom Alignments**: `solaris_noctis` and `twilight` may not be recognized by Wesnoth
2. **Unit Loading Order**: Units might not be loaded before eras are processed
3. **ID Mismatches**: Spaces vs underscores in unit IDs
4. **WML Syntax Errors**: Preventing proper unit recognition

### **Immediate Debugging Steps**

#### **Step 1: Check Wesnoth Debug Console**
- Look for WML parsing errors when loading the addon
- Check for unrecognized unit type errors
- Verify custom alignments don't cause issues

#### **Step 2: Test with Standard Alignments** 
Try temporarily changing custom alignments to standard ones:
- `solaris_noctis` → `neutral`
- `twilight` → `neutral` 

#### **Step 3: Simplify Era Configuration**
Test with only basic leader units:
- Frost Clans: Only `Frost Chieftain` as leader
- Ice Dwellers: Only `Frost Lord` as leader

#### **Step 4: Verify Unit Loading**
Ensure unit files are loaded before era definitions in `_main.cfg`

### **Quick Fix to Test**

Create a minimal test era with only standard alignments and basic leaders to isolate the issue:

```wml
[era]
    id=era_ice_age_test
    name= _ "Ice Age Test"
    description= _ "Minimal test era for debugging"
    
    [multiplayer_side]
        id=frost_clans_test
        name= _ "Frost Clans Test"
        type=Frost Chieftain
        leader=Frost Chieftain
        random_leader=Frost Chieftain
        terrain_liked=Ai,Aa,Ms,Gs
        recruit=Frost Warrior,Frost Scout
        flag=flags/frost-clans-flag.png
    [/multiplayer_side]
[/era]
```

If this works, gradually add complexity to identify the breaking point.

### **Root Cause Hypothesis** 🚨 **UPDATED AFTER TESTING**
Most likely causes in order of probability:
1. **Custom alignments preventing unit loading** ⚡ **PRIMARY SUSPECT**
2. **WML syntax error in unit definitions causing file rejection** 
3. **Unit loading order issue**
4. **ID mismatch between era and unit definitions**

### **Critical Discovery** 🚨
**Test Result**: Selecting "Frost Clans (Test)" recruits Drake units instead of Ice Age units!
- **Diagnosis**: Ice Age units are NOT loading at all
- **Fallback Behavior**: Wesnoth defaults to Drake faction when units can't be found
- **Immediate Fix**: Test with completely standard alignments (`neutral`) to isolate the issue

### **Next Actions** 🚨 **SYSTEMATIC DEBUGGING**

#### **Phase 1: Confirm Addon Loading**
1. **Restart Wesnoth completely** - Addon changes require full restart
2. **Check addon appears in Multiplayer** - Verify addon is recognized by Wesnoth
3. **Look for "Minimal Debug Test" era** - New ultra-simple test era added

#### **Phase 2: Check Wesnoth Debug Output** 
1. **Launch Wesnoth with debug console** (if available)
2. **Check for WML parsing errors** during addon loading
3. **Look for specific error messages** about unit types or era definitions

#### **Phase 3: Isolate the Problem**
- **If "Minimal Debug Test" shows Drake units**: Addon not loading at all
- **If "Minimal Debug Test" shows our units**: Original eras have configuration issues  
- **If no custom eras appear**: Addon loading problem

#### **Phase 4: Potential Root Causes**
1. **Addon not installed correctly** in Wesnoth
2. **WML syntax errors** preventing entire addon from loading
3. **File permissions** or path issues
4. **Wesnoth version compatibility** issues