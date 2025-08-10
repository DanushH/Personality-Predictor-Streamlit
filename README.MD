
<h1 align="center">Personality Prediction App</h1>

## Overview

An interactive web application built with **Streamlit** that predicts whether a person leans more toward **introversion** or **extroversion** based on lifestyle and social habits.

## Features

* User-friendly interface for inputting personal/social habits.

* Real-time prediction using a pre-trained machine learning model.

* Intuitive sliders, dropdowns, and buttons for easy interaction.

* Lightweight, no need for backend setup — deployable anywhere.

## Input Features

* The model uses the following inputs:

| Feature | Description | Range / Type |
| --------------------------- | ------------------------------------ | ------------ |
| `Time_spent_Alone` | Hours spent alone daily | 0–11 (hours) |
| `Stage_fear` | Presence of stage fright | Yes / No |
| `Social_event_attendance` | Frequency of attending social events | 0–10 |
| `Going_outside` | Frequency of going outside | 0–7 |
| `Drained_after_socializing` | Feeling drained after socializing | Yes / No |
| `Friends_circle_size` | Number of close friends | 0–15 |
| `Post_frequency` | Social media posting frequency | 0–10 |


## How to Run Locally
 
### Clone this repository

```bash

git  clone  https://github.com/DanushH/Personality-Predictor-Streamlit.git

```

### Install dependencies

```bash

pip  install  -r  requirements.txt

```

### Run the app

```bash

streamlit  run  app.py

```



## Tech Stack

*  **[Python 3](https://www.python.org/downloads/)**

*  **[Streamlit](https://docs.streamlit.io/)**

*  **[Scikit-learn](https://scikit-learn.org/stable/supervised_learning.html)** 

* **[CatBoostClassifier](https://catboost.ai/docs/en/concepts/python-reference_catboostclassifier)**


* Find the Kaggle Notebook of the data pre-processing and model training steps here:

[![Kaggle][kaggle-shield]][kaggle-url]



## Contributions

* Feel free to fork this repository, make changes, and submit pull requests. Any improvements or fixes are always welcome!


## Contact

* Contact me on:

[![LinkedIn][linkedin-shield]][linkedin-url]


## License

* This project is licensed under the MIT License — feel free to use and modify.


<br/>

<!-- MARKDOWN LINKS & IMAGES -->

[linkedin-shield]: https://img.shields.io/badge/Linkedin-black?style=for-the-badge&logo=linkedin&logoColor=%230277BD
[linkedin-url]: https://linkedin.com/in/danushika-herath
[kaggle-shield]: https://img.shields.io/badge/Kaggle-black%3F?style=for-the-badge&logo=kaggle&logoColor=%2320BEFF&color=black
[kaggle-url]: https://www.kaggle.com/code/danuherath/introversion-prediction-binary-classification

<br/>
