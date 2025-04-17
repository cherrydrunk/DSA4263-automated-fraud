# DSA4263-automated-fraud
DSA4263 Project on Automated Fraud Detection

## Project Description
This project applies a machine learning approach to bot fraud detection based on session behavior and metadata.

## Project Structure & Flow

```text
├── README.md            <- The top-level README for developers using this project.
├── .gitignore           <- List of directory to not be included in the repo
├── data
│   ├── raw              <- The original, immutable data dump.
│   ├── interim          <- Intermediate data that has been transformed.
│   └── processed        <- The final, canonical data sets for modeling.
├── notebooks            <- Exploratory Jupyter notebooks.
├── main.ipynb           <- Handles training of models and using trained models for predictions
├── preprocessing.ipynb  <- Handles data loading, cleaning, and preparation for modeling.
├── EDA.ipynb            <- Exploratory Data Analysis to understand data distributions.
└── requirements.txt     <- The requirements file for reproducing the analysis environment, 
                            e.g. generated with `pip freeze > requirements.txt
```
## Installation
### Prerequisites
- Python 3.8+ (or later)

### Steps
```bash
git clone https://github.com/cherrydrunk/DSA4263-automated-fraud.git
cd DSA4263-automated-fraud
pip install -r requirements.txt
```

## Acknowledgements
The dataset is derived from the Multimodal Data Fusion and Analytics Group. All rights to the dataset belong to the original authors.
