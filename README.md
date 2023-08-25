# **TraderGenerator (for Minecraft)**

### **TraderGenerator: Creating Custom Traders Made Easy!**

TraderGenerator is a unique semi-programming language designed to simplify the process of generating commands for custom traders within Minecraft. With its intuitive syntax, you can effortlessly create simple scripts to generate custom traders tailored to your needs.

---
## Comments
Comment lines begin with `/`:
```
/ This is a comment line!
```

Remember, comments and commands cannot coexist on the same line:
```
emerald => stone / This will not function as intended
$ Test: {id:"minecraft:iron_pickaxe",tag:{Damage:249}} / This will also not work as intended
```

---
## Item Variables
Create item variables by starting a line with `$`.
Each variable has a name and a value, separated by a `:`:
```
$ NameHere: ValueHere
```

The value is expressed in NBT format. Here's an example of a variable:
```
$ Coin: {id: "minecraft:command_block", tag:{display:{Name:'{"text":"coin","bold":true,"color":"gold"}'}}}
```
This creates a variable named `Coin`, which represents a command block with a custom name.

---
## Trades
A trade line consists of three parts:
- Buy: The item to place in the first slot.
- BuyB: The item to place in the second slot (optional).
- Sell: The item that the trader will give to the player.

Items can be either item variables or item IDs.
You can use an asterisk `*` followed by a number to indicate the quantity of an item.
Here are examples of trade configurations:
```
stone => oak_log
Coin * 5 => diamond * 2
oak_log * 2, stone * 3 => PowerPickaxe
```

---
## Code Formatting
1. Variable names should be in ComelCase.
2. `:`, `*`, `=>`, `,` should be spaced like this: `Name: Value`, `name * amount`, `buy => sell`, `a, b`
3. Varible name should represnet it's value.
4. Code should be split in sections (example):
   ```
   / Variables
   $ Coin: {id: "minecraft:command_block", tag:{display:{Name:'{"text":"coin","bold":true,"color":"gold"}'}}}
   $ SlimeCollector2000: {id:"minecraft:wooden_hoe", tag:{display:{Name:'{"text":"Slime collector 2000","bold":true,"color":"pink"}'},Unbreakable:1b,Enchantments:[{id:"minecraft:looting",lvl:5}],AttributeModifiers:[{AttributeName:"generic.attack_damage",Name:"generic.attack_damage",Amount:2,Operation:0,UUID:[I;439,684,724,99],Slot:"mainhand"}]}}

   / Get Coins
   slime_ball * 64 => Coin
   slime_ball * 64, slime_ball * 64 => Coin * 2
   emerald * 2 => Coin

   / Misc
   Coin * 2 => oak_log * 5
   Coin * 15 => water_bucket
   Coin * 10 => lava_bucket
   Coin * 5 => villager_spawn_egg
   Coin * 5 => bookshelf * 20

   / Tools
   Coin * 5 => SlimeCollector2000
   Coin => wooden_axe
   Coin => wooden_hoe
   Coin => wooden_pickaxe
   Coin => wooden_shovel
   Coin => wooden_sword
   Coin * 2 => stone_axe
   Coin * 2 => stone_hoe
   Coin * 2 => stone_pickaxe
   Coin * 2 => stone_shovel
   Coin * 2 => stone_sword
   Coin * 5 => iron_axe
   Coin * 5 => iron_hoe
   Coin * 5 => iron_pickaxe
   Coin * 5 => iron_shovel
   Coin * 5 => iron_sword
   Coin * 15 => diamond_axe
   Coin * 15 => diamond_hoe
   Coin * 15 => diamond_pickaxe
   Coin * 15 => diamond_shovel
   Coin * 15 => diamond_sword

   / Armor
   Coin => leather_helmet
   Coin => leather_chestplate
   Coin => leather_leggings
   Coin => leather_boots
   Coin * 5 => iron_helmet
   Coin * 5 => iron_chestplate
   Coin * 5 => iron_leggings
   Coin * 5 => iron_boots
   Coin * 15 => diamond_helmet
   Coin * 15 => diamond_chestplate
   Coin * 15 => diamond_leggings
   Coin * 15 => diamond_boots
   ```
