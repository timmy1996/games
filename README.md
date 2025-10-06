## Steam Game Analytics — Power BI Ready Data Model  

This project transforms a raw dataset of games, reviews, achievements, and player interactions from the Steam platform into a clean, normalized **star schema** ready for use in Power BI or any modern BI tool.  

The raw data was sourced from [Steam Game Data on Kaggle](https://www.kaggle.com/datasets/artyomkruglov/gaming-profiles-2025-steam-playstation-xbox/). While the broader dataset also covers PlayStation and Xbox, this project focuses exclusively on Steam data to design and demonstrate an efficient analytical model.  

---

### Overview  

The original dataset contains multi-valued fields and deeply nested relationships that are not directly compatible with Power BI's relational model.  

In this project, the following steps were undertaken:  

- **Clean and validate** raw data using `pandas` (handle missing values, inconsistent types, etc.)  
- **Normalize** multi-valued attributes such as developers, genres, and publishers  
- **Design and build** reusable **dimension**, **fact**, and **bridge** tables  
- **Add a standardized Date dimension** for temporal analysis and time-based measures  
- **Export** the final Power BI–ready schema for visualization and dashboarding  
- **Develop a concise Power BI report** showcasing how a well-modeled dataset enables faster insights and cleaner visual analytics
  
See `03_power_bi_report.ipynb` for Power BI screenshots and a mini discussion.
---

### Project Structure  

The raw and processed data files are not uploaded due to size constraints but can be reproduced using the provided notebooks and the original Kaggle dataset.  

```text
games/
├── notebooks/                # Documented data workflows
│   ├── 01_steam_data_clean_up.ipynb
│   ├── 02_data_normalisation.ipynb
│   └── 03_power_bi_report.ipynb
│
├── utils/                    # Reusable Python utility functions
│   └── data_utils.py
│
├── images/                   # Power BI screenshots
│
├── README.md
└── requirements.txt
