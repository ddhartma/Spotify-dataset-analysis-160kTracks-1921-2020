# Spotify dataset analysis: 160k tracks between 1921-2020

In this study based on a Spotify Dataset from Kaggle with 160k tracks released between 1921 and 2020 a set of input features and their dependence on song popularity has been studied.  
This [dataset](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks) can be found on the Kaggle webpage.

During the dataset analysis of a set of questions came up:  

1. In order to write a popular song, is the key and mode of the song important?
2. What are those songs with high popularity but zero tempo, zero danceability and zero speechiness?
3. 1955-1960: The popularity level climbs up - Who are the most famous artists at this time?
4. Which actual top artists write/have the most popular songs?
5. How do you become a famous song writer?

The answers to this CRISP questions can be found in the jupyter notebook. Or on my medium blog post.

## DataFrame Summary:
- The dataset splits into 170653 rows and 19 columns. Those 19 data columns are divided into 13 numerical and 6 categorical columns.
- **numerical** columns:
    - acousticness: The relative metric of the track being acoustic, (Ranges from 0 to 1)
    - danceability: The relative measurement of the track being danceable, (Ranges from 0 to 1)
    - energy: The energy of the track,  (Ranges from 0 to 1)
    - duration_ms: The length of the track in milliseconds (ms), (Integer typically ranging from 200k to 300k)
    - instrumentalness:, The relative ratio of the track being instrumental, (Ranges from 0 to 1)
    - valence: The positiveness of the track, (Ranges from 0 to 1)
    - popularity: The popularity of the song lately, default country = US, (Ranges from 0 to 100)
    - tempo:The tempo of the track in Beat Per Minute (BPM), (Float typically ranging from 50 to 150)
    - liveness: The relative duration of the track sounding as a live performance, (Ranges from 0 to 1)
    - loudness: Relative loudness of the track in decibel (dB), (Float typically ranging from -60 to 0)
    - speechiness: The relative length of the track containing any kind of human voice, (Ranges from 0 to 1)
    - year: The release year of track, (Ranges from 1921 to 2020)
    - id, The primary identifier for the track, generated by Spotify

- **categorical** columns:
    - key: The primary key of the track encoded as integers in between 0 and 11 (starting on C as 0, C# as 1 and so on…)
    - artists: The list of artists credited for production of the track
    - release_date: Date of release mostly in yyyy-mm-dd format, however precision of date may vary
    - name: The title of the track
    - mode: The binary value representing whether the track starts with a major (1) chord progression or a minor (0)
    - explicit: The binary value whether the track contains explicit content or not, (0 = No explicit content, 1 = Explicit content)

## Important results in terms of data handling:
- There are no real NaN values
- However, there are songs with zero tempo but with a relatively high popularity in some cases. This subset is identical to subsets with 0 danceability and 0 spechiness.
- It was found out that those 'songs' with zero tempo (zero danceability, zero speechiness) are not real songs but noises or sounds. It seems that those 'sounds' are popular because they seem to have a positive affect on deep sleep or for relaxation. As the CRISP goal is to give an answer to a song writer 'How to write popular ***real*** songs', those data has been removed from the dataset.    

This project was part of the Udacity Nanodegree program [Data Science](https://www.udacity.com/).

This analysis is based on a jupyter notebook and Python files.

## Setup Instructions

The notebook **Spotifiy_160k_1921_2020_analysis.ipynb** contains the investigation process of the dataset and and the results.
The following is a brief set of instructions on setting up a managed notebook instance, from which the notebooks can be completed and run.

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites: Installation of Python via Anaconda and Command Line Interaface
- Install [Anaconda](https://www.anaconda.com/distribution/). Install Python 3.7 - 64 Bit
- If you need a good Command Line Interface (CLI) under Windowsa you could use [git](https://git-scm.com/). Under Mac OS use the pre-installed Terminal.

- Upgrade Anaconda via
```
$ conda upgrade conda
$ conda upgrade --all
```

- Optional: In case of trouble add Anaconda to your system path. Write in your CLI
```
$ export PATH="/path/to/anaconda/bin:$PATH"
```

### Clone the project
- Open your Command Line Interface
- Change Directory to your project older, e.g. `cd my_github_projects`
- Clone the Github Project inside this folder with Git Bash (Terminal) via:
```
$ git clone https://github.com/ddhartma/Around-The-World-Image-Classifier.git
```

- Change Directory
```
$ cd Spotify-dataset-analysis-160kTracks-1921-2020
```

- Create a new Python environment via the provided yml file. Inside Git Bash (Terminal) write:
```
$ conda create --name spotify_analysis
```

- Install the following packages (via pip or conda)
```
numpy = 1.17.4
pandas = 0.24.2
matplotlib = 3.1.0
tensorflow = 1.14.0
seaborn = 0.9.0
scikit-learn = 0.21.2
```

- Check the environment installation via
```
$ conda env list
```

- Activate the installed spotify_analysis environment via
```
$ conda activate spotify_analysis
```

### Open and run the notebook
Now that the repository has been cloned into the notebook instance you may navigate to the notebook. Run the notebook via

```
jupyter notebook Spotifiy_160k_1921_2020_analysis.ipynb
```


## Acknowledgments
* This is a project of the Udacity Nanodegree program 'Data Science'. Please check this [link](https://www.udacity.com) for more information
* The categorical AritistsTransformer class in this work was developed by [Guy Kahana & Anat Peled](https://www.kaggle.com/anatpeled/spotify-popularity-prediction/comments)
