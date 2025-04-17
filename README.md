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
## About the dataset
This is a labelled dataset designed to support web bot detection research to distinguish between human visitors and web bots. The dataset was created by the Multimodal Data Fusion and Analytics (M4D) group, consisting of scientists and researchers.(Iliou et al., 2021) The data was gathered through a web server that hosted web pages retrieved from Wikipedia and included details such as mouse movement coordinates, click patterns, and web logs.

More information on the dataset can be found here: https://m4d.iti.gr/web-bot-detection-dataset/

## References
Christos Iliou, Theodoros Kostoulas, Theodora Tsikrika, Vasilis Katos, Stefanos Vrochidis, and Ioannis Kompatsiaris. 2021. Detection of Advanced Web Bots by Combining Web Logs with Mouse Behavioural Biometrics. Digital Threats 2, 3, Article 24 (September 2021), 26 pages. https://doi.org/10.1145/3447815

## Acknowledgements
The dataset is derived from the Multimodal Data Fusion and Analytics Group. All rights to the dataset belong to the original authors.

## License
CC BY-NC-SA
