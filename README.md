## Steam Game Analytics — Power BI Ready Data Model


This project transforms a raw dataset of games, reviews, achievements, and player interactions from the Steam platform into a clean, normalized **star schema** ready for use in Power BI or any modern BI tool.
The raw data used in this project was sourced from [Steam Game Data on Kaggle](https://www.kaggle.com/datasets/artyomkruglov/gaming-profiles-2025-steam-playstation-xbox/). We focus on the Steam platform but there are playstation and Xbox datasets as well.
---

### Overview

The dataset multi-valued fields, deeply nested relationships which may not be ideal for Power BI. In this project, we shall do the following tasks:

- Clean and validate data using pandas (missing values etc)
- Normalise multi-valued attributes like developers, genres, and publishers
- Create reusable dimension, fact, and bridge tables
- Add standardised date dimensions for temporal slicing
- Export a complete Power BI–ready schema

---

### Project Structure

```text
games/
├── notebooks/                # Documented data workflows
│   ├── steam_data_clean_up.ipynb
│   ├── data_normalisation.ipynb
│   └── 03_export_and_powerbi_notes.ipynb
│
├── utils/                    # Reusable Python utility functions
│   └── data_utils.py
│
├── data/
│   ├── raw/                  # Original dataset
│   ├── cleaned/              # Cleaned intermediate outputs
│   └── normalised/           # Final Power BI–ready tables
│       ├── games_dim.csv
│       ├── prices_fact.csv
│       ├── dev_game_map.csv
│       └── ...
│
├── README.md
└── requirements.txt
