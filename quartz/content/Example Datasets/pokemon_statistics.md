![[Pasted image 20260219123250.png]]
*(I can't put an image of pokemon due to copyright)*

*Gotta Graph 'em all*

Originally inspired by the childhood joy of insect collecting, this data captures the core attributes of hundreds of unique species across multiple generations.

### Dataset Structure

| **Attribute**         | **Type**    | **Description**                                                         |
| --------------------- | ----------- | ----------------------------------------------------------------------- |
| **name**              | String      | The unique identifier for the creature species.                         |
| **pokedex_number**    | Numerical   | The ID assigned in the national/regional species index.                 |
| **type1**             | Categorical | The primary elemental affinity (e.g., Grass, Fire, Water).              |
| **type2**             | Categorical | The secondary elemental affinity, if applicable.                        |
| **base_total**        | Numerical   | The aggregate sum of all six primary combat statistics.                 |
| **hp**                | Numerical   | Count of Hit Points; represents the creature's total vitality.          |
| **attack**            | Numerical   | Numerical power used for physical-based offensive maneuvers.            |
| **defense**           | Numerical   | Resistance value against physical-based incoming damage.                |
| **sp_attack**         | Numerical   | Numerical power used for elemental/energy-based maneuvers.              |
| **sp_defense**        | Numerical   | Resistance value against elemental/energy-based incoming damage.        |
| **speed**             | Numerical   | Determines turn-order priority during an encounter.                     |
| **height_m**          | Numerical   | The vertical measurement of the species in meters.                      |
| **weight_kg**         | Numerical   | The mass of the species measured in kilograms.                          |
| **capture_rate**      | Numerical   | A mathematical coefficient (1–255) determining catch difficulty.        |
| **base_egg_steps**    | Numerical   | Count of steps required to hatch an egg of this species.                |
| **base_happiness**    | Numerical   | The starting affinity value between a trainer and the creature.         |
| **experience_growth** | Numerical   | The total XP required for the species to reach its maximum level.       |
| **classfication**     | String      | The biological category label (e.g., "Seed Pokémon").                   |
| **percentage_male**   | Numerical   | The probability ratio (0–100) of the creature being male.               |
| **generation**        | Numerical   | The specific release era (1–7+) in which the species was introduced.    |
| **is_legendary**      | Boolean     | Binary flag (0 or 1) indicating if the species is a rare mythic entity. |
>[!question] Lab Questions
> 1. Use the [[Box and Whiskers plot]] to determine which pokemon type(typ1) has the most attack on average. 
> 2. Is there any correlation between speed and attack? 
> 3. Is there any correlation between defense and hp?
> 4. Build a model to predict a Pokemon attack using it's height and weight to predict hp. 
### Dataset Source

Data for this project was sourced from **The Complete Pokemon Dataset** (2018), curated by Rounak Banik and hosted on Kaggle.
[Link](https://www.kaggle.com/datasets/rounakbanik/pokemon?resource=download)

This project uses a dataset containing Pokémon statistics for research and educational purposes. Pokémon and Pokémon character names are trademarks and copyrights of Nintendo, Game Freak, and Creatures Inc. DataScratch is not affiliated with or endorsed by Nintendo.