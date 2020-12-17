[image1]: sklearn_linearRegression_result.png "sklearn_output"
# Spotify dataset analysis: 160k tracks between 1921-2020

In this study based on a Spotify Dataset from Kaggle with 160k tracks released between 1921 and 2020 a set of input features and their dependence on song popularity has been studied.  
This [dataset](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks) can be found on the Kaggle webpage.

## Business Understanding (aim of this study)
The aim of this study was to analyze via CRISP-DM (CROSS INDUSTRY STANDARD PROCESS FOR DATA MINING) if one can build model which can predict song popularities based on the given dataset features.

In detail, the CRISP-DM questions were:

1. **Question 1:** In order to write a popular song, is the key and mode of the song important?
2. **Question 2:** 1955-1960: The popularity level climbs up - Who are the most famous artists at this time?
3. **Question 3:** Which actual top artists write/have the most popular songs?
4. **Question 4:** How do you become a famous song writer?
5. **Question 5:** What are those songs with high popularity but zero tempo, zero danceability and zero speechiness?

## DataFrame Overview
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

## Data understanding and preparation
The notebook **Spotifiy_160k_1921_2020_analysis.ipynb** contains the dataset investigation steps and and all the results.

- **NaN values:** There are no real NaN values

- **Dropping Rows:** However, there are songs with zero tempo but with a relatively high popularity in some cases. This subset is identical to subsets with 0 danceability and 0 speechiness. It was found out that those 'zero tempo songs' are not real songs but noises or sounds. They are highly popular because they seem to have a positive effect on a restful sleep or for relaxation. As the CRISP goal is to give an answer to a song writer 'How to write popular ***real*** songs', those data has been removed from the dataset.

- **Dropping Columns:**

  - ***id:*** It splits into 170653 unique entires. This is the number of rows in the dataset. This column can be removed from the dataset.
  - ***name:*** This text value has too less power for a popularity prediction. There are 133638 unique entries (78% of the dataframe). There are some dublicates, but too less, to justify its transformation to dummy variables.
  - ***release-date:*** As it can be already seen from the min and max values in the descriptive statistics table there is some mixture in the datetime formats. It can be ignored as the focus relies on a yearly based analysis. This information is already provided in the 'year' column.


- **Creating Dummies:**

  - ***artists:*** For sure, this is an important column for popularity. By intuition it is clear, that for an already famous artist it will be more easy to produce a new popular song than for an unknown artist.
  - ***mode:*** This is a categorical variable with 0 and 1.
  - ***key:*** A categorical variable with values ranging between 0 and 11, each value for one note.
  - ***explicit*** is a categorical variable with 0 and 1.

For these categorical variables dummy variables are needed to build a predicting model.

## Modeling:
- The main modeling approach in this Jupyter notebook is done based on a sklearn Linear Regression. There is still room for optimization as the R-squared value (a measure of how much of the data variability can be explained by the model) is only 66% for training and 63% for testing.
- As discussed in the notebook there are nonlinear tendencies for valence, acousticness, danceability, energy, instrumentalness and liveness. In future approaches linearization steps are needed if one will keep going on with linear regressions or deep learning nonlinear model should be tested. Some preliminary work has been done on that, but it still needs optimization.

## Evaluation (most important results):
- **Answer to Question 1:** Although there seems to be a slight preference for C# minor we have seen that primary key and mode of a song does not play a major role with respect to song popularity

- **Answer to Question 2:** The top winners were: Elvis Presley, Chet Baker, Chuck Berry and Frank Sinatra.

- **Answer to Question 3:** Actual highly popular artists are: One Direction (with songs like "What Makes You Beautiful" or "Best Song Ever")
Ariana Grande (e.g. '7 rings') and (Ed Sheeran, e.g. 'Shape Of You')

- **Answer to Question 4:** It is easier to produce a popular song if you write for an already popular musician. Produce/write energetic, loud and danceable songs! Real studio productions are better than productions with live character. Do not write purely instrumental songs and do not intensify a strong acoustic environment within your song!

- **Answer to Question 5:** These are the doppped rows of noises and sounds.

The sklearn Linear regression result (see question 4):

![sklearn_output][image1]



## Read my blog post under medium

The answers to this CRISP questions and further information can be found in the jupyter notebook. Or check out my [medium](https://hartmann-david.medium.com/how-do-you-become-a-famous-song-writer-ff3a4668a8c8) blog post.

## Setup Instructions

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
$ git clone https://github.com/ddhartma/Spotify-dataset-analysis-160kTracks-1921-2020.git
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
### Attached files in the repository
- **Spotify_160k_1921_2020_analysis.ipynb** - the main file of this repository containing a CRISP-DM analysis, all coding steps and the important results.
- **plot_df** - a helper module containing three functions:
  - plot_df_line
  - plot_df_bar
  - plot_df_pie

  This module simplifies plotting line, bar and pie plots using matplotlib. It is called from the notebook and shortens the code for specially designed plots to a 'one code line'. This is done via default settings and overwriting them only when needed.  

- **sklearn_linearRegression_result.png** - an image of the sklearn Linear Regression result. It shows the weights for each interesting input feature as a bar plot.

- **README.md** - the readme file of this repository.

## Acknowledgments
* This is a project of the Udacity Nanodegree program 'Data Science'. Please check this [link](https://www.udacity.com) for more information.
* The categorical AritistsTransformer class in this work was developed by [Guy Kahana & Anat Peled](https://www.kaggle.com/anatpeled/spotify-popularity-prediction/comments)
