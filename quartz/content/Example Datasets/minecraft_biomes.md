![[Pasted image 20260219081230.png]]

Lava Chicken!

This dataset contains information about the many different [minecraft](https://www.minecraft.net/en-us) biomes. This is a fun dataset, containing the dominant biome for a 128x128 section, and the counts of each block for said section.

A common analysis for this dataset would be to use the [[Box and Whiskers plot]] to see which biome has the most or least of something. 
### Dataset Structure
| **Attribute**      | **Type**    | **Description**                                                  |
| ------------------ | ----------- | ---------------------------------------------------------------- |
| **dominant_biome** | Categorical | The primary biome type assigned to this 128x128 section.         |
| **air**            | Numerical   | Count of standard air blocks.                                    |
| **andesite**       | Numerical   | Count of andesite (gray igneous rock) blocks.                    |
| **cave_air**       | Numerical   | Count of air blocks specifically located within cave structures. |
| **clay**           | Numerical   | Count of clay blocks (usually found in lush caves or rivers).    |
| **deepslate**      | Numerical   | Count of deepslate (dark stone found in lower elevations).       |
| **diamond_ore**    | Numerical   | Count of diamond ore blocks (high-value mineral).                |
| **diorite**        | Numerical   | Count of diorite (white igneous rock) blocks.                    |
| **dirt**           | Numerical   | Count of standard dirt blocks.                                   |
| **granite**        | Numerical   | Count of granite (reddish igneous rock) blocks.                  |
| **grass_block**    | Numerical   | Count of surface grass blocks with soil.                         |
| **gravel**         | Numerical   | Count of gravity-affected gravel blocks.                         |
| **kelp_plant**     | Numerical   | Count of underwater kelp vegetation blocks.                      |
| **lava**           | Numerical   | Count of fluid lava blocks.                                      |
| **moss_block**     | Numerical   | Count of mossy vegetation blocks.                                |
| **sand**           | Numerical   | Count of sand blocks (common in deserts and beaches).            |
| **seagrass**       | Numerical   | Count of standard underwater seagrass.                           |
| **short_grass**    | Numerical   | Count of small surface vegetation (formerly "grass").            |
| **stone**          | Numerical   | Count of the most common gray stone blocks.                      |
| **tall_seagrass**  | Numerical   | Count of two-block high underwater seagrass.                     |
| **tuff**           | Numerical   | Count of tuff (gray volcanic rock found in deep layers).         |
| **water**          | Numerical   | Count of fluid water blocks.                                     |


>[!question] Lab Questions
> 1. What is a better predictor of granite counts? The dominant biome or the diorite counts? 
> 2. What is the relationship between the count of kelp and the count of water? Why might this be?
> 3. Which biome has the most sand? Why might this be? 
> 4. Does any particular biome have the most diamonds? Or is it even? 
> 5. Of the block types, which 2 are the best for predicting the biome? 

### Dataset Source
The **minecraft-chunks** dataset, authored by **Pi1lot** and published on **Kaggle** in **2026**
[Link](https://www.kaggle.com/datasets/pi1lot/minecraft-chunks?resource=download)

This project uses a dataset containing Minecraft blocks and biomes for research and educational purposes. Minecraft, its name, brand, and assets are trademarks and copyrights of Mojang Synergies AB / Microsoft Corporation. **DataScratch** is not affiliated with or endorsed by Mojang or Microsoft.