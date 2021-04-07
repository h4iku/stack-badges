# Repository Description

Data and source code for the paper "Gamified Incentives: A Badge Recommendation Model to Improve User Engagement in Social Networking Websites". [[pdf](http://thesai.org/Downloads/Volume8No5/Paper_33-Gamified_Incentives_A_Badge_Recommendation.pdf)]

### `data`

Contains badges dataset for different time periods which are extracted from [`Badges.xml` data of Stack Overflow](https://archive.org/details/stackexchange) using `dataset_generation/extract_badges.py`.

* `dataset2008`: Contains randomly generated train and test dataset from badges dataset using `dataset_generation/train_test_generation.py` for badges that are awarded in the year 2008. The complete dataset for years 2008 to 2010 are compressed in the `datasets.zip` file and should be uncompressed like `dataset2008` to be used.
  
### `dataset_generation`

* `extract_badges.py`: Extracts badges for users which are awarded within the `begin_year` and `end_year` time period from the `Badges.xml` file. It writes the output as a `csv` file in the format of `UserId,badge1,badge2,...`.
* `train_test_generation.py`: Generates train and test set from `badges.csv` file for `recommendation/` algorithms.

### `recommendation`

* `collaborative_filtering.py`: Implementation of the item-based collaborative filtering method to recommend badges and evaluate the results.
* `popular_badge_baseline.py`: Implementation of the baseline algorithm which recommends popular badges to each user.
* `datasets.py`: This module contains the file paths of datasets for easier access in other modules. If you change the repository structure and the place of the `data` directory, you should modify `_DATASET_ROOT` in this module accordingly so that it points to the root directory where datasets reside in.
