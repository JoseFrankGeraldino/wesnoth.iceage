#!/usr/bin/env python3
"""
Script to fix animation blocks in all WML unit files.
This removes old (incorrect) animation blocks and adds correct ones.
"""

import os
import re
from pathlib import Path

# Define unit configurations with their sprite names
UNITS_CONFIG = {
    # Bear Rider Line
    'bear_rider.cfg': [
        ('bear_rider', 8),
        ('dire_bear_rider', 8),
        ('ancient_bear_lord', 8),
        ('primal_bear_champion', 8),
    ],
    # Pack Rider Line
    'pack_rider.cfg': [
        ('pack_rider', 8),
        ('wolf_ranger', 8),
        ('storm_rider', 8),
        ('blizzard_lord', 8),
    ],
    # Iceborn Warrior Line
    'iceborn_warrior.cfg': [
        ('iceborn_warrior', 8),
        ('winterbane_champion', 8),
        ('rimeguard_chieftain', 8),
        ('glacial_warlord', 8),
    ],
    # Tundra Scout Line
    'tundra_scout.cfg': [
        ('tundra_scout', 8),
        ('blizzard_ranger', 8),
        ('avalanche_hunter', 8),
        ('whiteout_pathfinder', 8),
    ],
    # Walrus Rider Line
    'walrus_rider.cfg': [
        ('walrus_rider', 8),
        ('tusked_corsair', 8),
        ('leviathan_warden', 8),
    ],
    # Fire Spirit Line
    'fire_spirit.cfg': [
        ('fire_wisp', 6),
        ('flame_spirit', 6),
        ('inferno_avatar', 6),
    ],
    # Ice Spirit Line
    'ice_spirit.cfg': [
        ('frost_wisp', 6),
        ('blizzard_spirit', 6),
        ('glacial_avatar', 6),
    ],
    # Darkness Spirit Line
    'darkness_spirit.cfg': [
        ('shadow_wisp', 6),
        ('umbral_spirit', 6),
        ('void_avatar', 6),
    ],
    # Yeti Line
    'yeti.cfg': [
        ('young_yeti', 7),
        ('adult_yeti', 7),
        ('elder_yeti', 7),
        ('ancient_yeti', 7),
    ],
}


def get_faction(filename):
    """Determine faction based on filename."""
    if filename in ['bear_rider.cfg', 'pack_rider.cfg', 'iceborn_warrior.cfg', 
                    'tundra_scout.cfg', 'walrus_rider.cfg', 'fire_spirit.cfg', 'ice_spirit.cfg']:
        return 'frost_clans'
    elif filename in ['darkness_spirit.cfg', 'yeti.cfg']:
        return 'ice_dwellers'
    return 'frost_clans'


def create_death_anim(unit_sprite_name, death_frames):
    """Create death animation block with correct sprite names (using hyphens)."""
    sprite_name = unit_sprite_name.replace('_', '-')
    frames = []
    for i in range(1, death_frames + 1):
        frames.append(f'        [frame]\n            image="units/{{faction}}/{sprite_name}-death-{i}.png:150"\n        [/frame]')
    
    return f'''    [death_anim]
        start_time=-200
{chr(10).join(frames)}
    [/death_anim]
'''


def create_standing_anim(unit_sprite_name):
    """Create standing animation block."""
    sprite_name = unit_sprite_name.replace('_', '-')
    frames = [
        '        [frame]\n            image="units/{faction}/' + sprite_name + f'-standing-1.png:300"\n        [/frame]',
        '        [frame]\n            image="units/{faction}/' + sprite_name + f'-standing-2.png:300"\n        [/frame]',
        '        [frame]\n            image="units/{faction}/' + sprite_name + f'-standing-3.png:300"\n        [/frame]',
    ]
    
    return f'''    [standing_anim]
        start_time=0
{chr(10).join(frames)}
    [/standing_anim]
'''


def create_movement_anim(unit_sprite_name):
    """Create movement animation block."""
    sprite_name = unit_sprite_name.replace('_', '-')
    frames = []
    for i in range(1, 6):
        frames.append(f'        [frame]\n            image="units/{{faction}}/{sprite_name}-movement-{i}.png:100"\n        [/frame]')
    
    return f'''    [movement_anim]
        start_time=0
{chr(10).join(frames)}
    [/movement_anim]
'''


def remove_animation_block(content, unit_id, anim_type):
    """Remove an animation block for a specific unit."""
    # Find and remove the animation block
    pattern = rf'(\s*\[{anim_type}\].*?\[/{anim_type}\]\s*(?=\[(?:death_anim|standing_anim|movement_anim|\[/unit_type\])))'
    content = re.sub(pattern, '', content, flags=re.DOTALL)
    return content


def process_file(filepath, filename):
    """Process a single WML file and fix all animations."""
    faction = get_faction(filename)
    units = UNITS_CONFIG.get(filename, [])
    
    if not units:
        print(f"  ⚠ Skipping {filename} - not in configuration")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # For each unit in the file
    for unit_id, death_frames in units:
        # Find the unit_type block for this unit
        unit_pattern = rf'(\[unit_type\]\s*id={unit_id}\b.*?)(\[/unit_type\])'
        match = re.search(unit_pattern, content, re.DOTALL)
        
        if not match:
            print(f"  ⚠ Could not find unit_type block for {unit_id}")
            continue
        
        unit_start = match.start(1)
        unit_end = match.end(1)
        unit_block = match.group(1)
        
        # Remove any existing animation blocks for this unit
        unit_block_clean = re.sub(r'\s*\[death_anim\].*?\[/death_anim\]\s*', '', unit_block, flags=re.DOTALL)
        unit_block_clean = re.sub(r'\s*\[standing_anim\].*?\[/standing_anim\]\s*', '', unit_block_clean, flags=re.DOTALL)
        unit_block_clean = re.sub(r'\s*\[movement_anim\].*?\[/movement_anim\]\s*', '', unit_block_clean, flags=re.DOTALL)
        
        # Build the new animations to add
        death_anim = create_death_anim(unit_id, death_frames).replace('{faction}', faction)
        standing_anim = create_standing_anim(unit_id).replace('{faction}', faction)
        movement_anim = create_movement_anim(unit_id).replace('{faction}', faction)
        
        new_animations = death_anim + standing_anim + movement_anim
        
        # Replace the unit block with cleaned one + new animations
        new_unit_block = unit_block_clean + new_animations
        content = content[:unit_start] + new_unit_block + content[unit_end:]
        
        print(f"  ✓ {unit_id} - fixed all animation blocks")
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True


def main():
    """Main entry point."""
    # Find all WML unit files in unit-designs
    unit_designs_path = Path(__file__).parent
    
    processed = 0
    skipped = 0
    
    for filename in UNITS_CONFIG.keys():
        # Find the file in unit-designs subdirectories
        found = False
        for cfg_file in unit_designs_path.rglob('*.cfg'):
            if cfg_file.name == filename:
                print(f"Processing: {filename}")
                if process_file(str(cfg_file), filename):
                    processed += 1
                else:
                    skipped += 1
                found = True
                break
        
        if not found:
            print(f"⚠ Not found: {filename}")
            skipped += 1
    
    print(f"\n{'='*60}")
    print(f"Summary: {processed} files processed, {skipped} skipped/errors")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
