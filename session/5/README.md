# Session 5 - Reading a File


```mermaid
graph TD
    start["🌲 The Enchanted Forest Gate"]
    forest_path["🌿 The Mysterious Forest Path<br/>reward: magic_rope"]
    village_square["🏘️ The Friendly Village Square<br/>reward: silver_key"]
    old_tree["🌳 The Ancient Talking Tree"]
    stream_crossing["🌊 The Babbling Brook Crossing<br/>reward: golden_coin"]
    bakery["🥖 The Magic Bakery<br/>reward: magic_flour"]
    wizard_tower["🏰 The Wise Wizard's Tower<br/>reward: crystal_compass"]
    tree_house["🏠 The Cozy Tree House<br/>reward: fairy_dust"]
    underground_cave["🕳️ The Glowing Underground Cave<br/>reward: ancient_map"]
    stone_bridge["🌉 The Ancient Stone Bridge<br/>reward: stone_tablet"]
    secret_cellar["🍷 The Secret Magical Cellar"]
    garden_maze["🌹 The Enchanted Garden Maze<br/>reward: rainbow_flower"]
    spell_room["⚡ The Mystical Spell Room<br/>reward: magic_wand"]
    library["📚 The Ancient Magic Library<br/>reward: wisdom_scroll"]
    fairy_glade["🧚 The Sparkling Fairy Glade"]
    crystal_chamber["💎 The Hidden Crystal Chamber<br/>reward: master_key"]
    mountain_peak["⛰️ The Majestic Mountain Peak"]
    rainbow_pool["🌈 The Rainbow Reflection Pool"]
    victory["🏆 Victory! The Forest is Saved!"]

    start --> forest_path
    start --> village_square
    forest_path -->|"magic_rope"| old_tree
    forest_path --> stream_crossing
    forest_path --> village_square
    village_square -->|"silver_key"| bakery
    village_square -->|"golden_coin"| wizard_tower
    village_square --> forest_path
    old_tree -->|"crystal_compass"| tree_house
    old_tree --> underground_cave
    stream_crossing --> fairy_glade
    stream_crossing --> stone_bridge
    stream_crossing -->|"golden_coin"| wizard_tower
    bakery --> secret_cellar
    bakery -->|"magic_flour"| garden_maze
    wizard_tower --> spell_room
    wizard_tower --> library
    wizard_tower -->|"magic_rope"| old_tree
    tree_house --> fairy_glade
    underground_cave -->|"ancient_map,wisdom_scroll"| crystal_chamber
    stone_bridge -->|"stone_tablet,magic_wand"| mountain_peak
    secret_cellar -->|"ancient_map,wisdom_scroll"| crystal_chamber
    garden_maze --> fairy_glade
    spell_room -->|"stone_tablet,magic_wand"| mountain_peak
    library -->|"ancient_map,wisdom_scroll"| crystal_chamber
    fairy_glade --> rainbow_pool
    crystal_chamber --> rainbow_pool
    mountain_peak --> rainbow_pool
    rainbow_pool --> victory
```