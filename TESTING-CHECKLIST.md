# 🔍 Era Testing Checklist

## **Critical Issue**: Factions show Drake units instead of Ice Age units

### **Step 1: Restart Wesnoth Completely**
- [ ] Close Wesnoth entirely
- [ ] Relaunch Wesnoth 
- [ ] Go to Multiplayer → Create Multiplayer Game

### **Step 2: Look for Our Eras**
Check if these eras appear in the Era dropdown:
- [ ] "Super Simple Test" 🔥 **NEWEST - Test this first!**
- [ ] "Minimal Debug Test"
- [ ] "Default + Ice Age" 
- [ ] "Default + Dunefolk + Ice Age"
- [ ] "Pure Ice Age"

### **Step 3: Test Super Simple Era** 🔥
Select "Super Simple Test" era:
- [ ] Can you see "Ice Test" faction?
- [ ] When you select "Ice Test", do you see "Ice Test Unit" or standard Loyalist units?
- [ ] Can you select "Ice Test Unit" as leader?

### **Previous Test Results Analysis:**
✅ Addon loads (eras appear in dropdown)  
✅ Factions show in selection  
❌ BUT faction shows standard Loyalist units instead of our custom units

### **Step 4: Report Results**
**If you see Drake units in "Minimal Debug Test":**
→ The addon isn't loading at all

**If you see our units in "Minimal Debug Test":**
→ The original eras have configuration problems

**If "Minimal Debug Test" doesn't appear:**
→ The addon files aren't being recognized by Wesnoth

## **Quick Diagnostic**

### What should you see in "Minimal Debug Test"?
- **Faction name**: "Frost Test" 
- **Leader unit**: "Frost Warrior" (not any Drake unit)
- **Unit portrait**: Should be a human warrior with axe

### What indicates the problem?
- **Drake units appear**: Addon loading failure
- **No custom eras listed**: Addon not installed correctly
- **Error messages**: WML syntax problems

---
**Next steps depend on test results!**