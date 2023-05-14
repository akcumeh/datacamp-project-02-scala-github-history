# DataCamp Projects Series: 02 - The GitHub History of Scala

_DataCamp Project Series_ is a series of the major projects I completed under the DataCamp [**Data Scientist with Python**](https://app.datacamp.com/learn/career-tracks/data-scientist-with-python) track.

## Table of contents
- [Introduction](#introduction)
    - [About](#about-the-project)
    - [Prerequisites](#prerequisites)
    - [Goals](#goals)
- [The Project](#the-project)
    - [Data Used In This Project](#datasets)
    - [The Code](#code)
    - [Findings](#what-i-learned)
    - [Conclusion](#conclusion)
- [Relevant Links](#links)

## Introduction

### About the project

> **"** In this project, you'll be challenged to read in, clean up, and visualize the real-world project repository of Scala that spans data from a version control system (Git) as well as a project hosting site (GitHub). You will find out who has had the most influence on its development and who are the experts. **"**

### Prerequisites

**Technology:**
> Python

To be able to take on this project, I needed to have learned:

1. **Courses:**
    - [Joining Data with `pandas`](https://app.datacamp.com/learn/courses/joining-data-with-pandas)

2. **Concepts:**
    - Data Manipulation
    - Data Visualization
    - Joining and merging datasets

### Goals

In taking on this project, I was trying to:
- use the provided data to investigate a trend
- visualize the data
- draw a definitive conclusion based on the data

## The Project

### Datasets

The following datasets were used in the project:

- [`pulls_2011-2013`](datasets/pulls_2011-2013.csv), a dataset containing the basic information about the pull requests from the end of 2011 to the end of 2013.
- [`pulls_2014-2018`](datasets/pulls_2014-2018.csv), a dataset containing the basic information about the pull requests from 2014 to the end of 2018.
- [`pull_files`](datasets/pull_files.csv), the files that were modified by each pull request.

### Code

The code used for investigation and visualization was written in simple Python, starting by importing `pandas` and `matplotlib.pyplot` modules to provide the needed functionality.

The raw code can be found [here](analyzer.py).

### What I learned

From this project, I was able to gain:

- A short revision on how to **read files in `pandas`**.
- A revision of simple data manipulation tricks like **merging** and **pivoting tables**.
- A revision of simple data visualization, such as making plots using `matplotlib`.

### Conclusion

The project was carried out to find out who made the most contributions most recently to Scala's development on GitHub. By choosing a specific file in the project (`src/compiler/scala/reflect/reify/phases/Calculate.scala`) and studying its changes and contribution history, we narrowed the answer to some people such as *bjornregnell*, *retronym*, *soc*, *starblood*, *xeno-by* and *zuvizudar*, with more of specific and recent contributions observed on the file from two users: *xeno-by* and *retronym*.

(It should be noted that these people are the ones who contributed the most, as well as most recently, to a **single, randomly-selected file**, chosen in order to simplify analysis, and not the people who contributed most to the Scala project as a whole on Github.)

![Contributors' Activity on chosen file](plots/Fig%203%20-%20Most%20Recent%20Contributors'%20Activity.png)

## Links

Relevant links to the project:

- [Project Home](https://app.datacamp.com/learn/projects/163)
- [Track Home](https://app.datacamp.com/learn/career-tracks/data-scientist-with-python)
- [DataCamp Workspace](https://app.datacamp.com/workspace/w/3f72b674-b6bb-4b92-b286-2289a33ae36f)

Thanks for reading this far! Follow me:
- [Twitter](https://twitter.com/akcumeh)
- [GitHub](https://github.com/akcumeh)