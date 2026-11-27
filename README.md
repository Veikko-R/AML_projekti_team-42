# Machine Learning Project

## AML_projekti_team-42
Assignment for course applied machine learning by group 42

---

## Project description

**Football 1x2 score predictor for Aston Villa**

This project predicts the result of Aston Villa matches in the 1x2 format: **1** (home win), **X** (draw) or **2** (away win). Only matches where Aston Villa played, home or away, are used.

---

## Team members

- **Veikko Rauta** (Prediction model)
- **Juuso Kinnunen** (Role)
- **Lassi Töytäri** (Pre-processing)

---

## Data

- **Source:** *([Club Football Match Data (2000-2025)](https://www.kaggle.com/datasets/adamgbor/club-football-match-data-2000-2025/data))*
- **Coverage:** *(Aston Villa matches)*
- **Storage:** the data is kept in the shared Google Drive folder `AML_project_data` and is not included in this repo.

---

## Features

- **Teams:** `HomeTeam`, `AwayTeam`
- **Team strength:** `HomeElo`, `AwayElo` (Elo ratings before the match)
- **Recent form:** `Form3Home`, `Form5Home`, `Form3Away`, `Form5Away` (results over the last 3 and 5 matches)
- **Half-time score:** `HTHome`, `HTAway`
- **Betting odds:** `OddHome`, `OddDraw`, `OddAway`

**Target:** `FTResult` (full-time result: home win, draw or away win)

---

## Model

- **Model used:** *(XGBoost)*
- **Train/test split:** *(e.g. by season, 80/20)*
- **Evaluation metric:** *(e.g. accuracy, log loss)*

---

## Results

*(Add the main result when ready, and compare it against a baseline such as always predicting a home win.)*

---

## Repository structure

- `01_data_exploration_and_preprocessing.ipynb`
- `03_model_training.ipynb`
- `requirements.txt`: Python libraries the project needs

---
