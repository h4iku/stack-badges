#### `data`:
Contains badges dataset for different time periods which are extracted from [`Badges.xml` data of Stack Overflow](https://archive.org/details/stackexchange) using `preprocessing/extract_badges.py`.
* `generated_dataset`: Contains randomly generated train and test dataset from badges dataset using `preprocessing/train_test_generation.py`.
  
#### `preprocessing`:
* `extract_badges.py`: Extracts badges for users which are awarded within the `begin_year` and `end_year` time period from the `Badges.xml` file. It writes the output as a `csv` file in the format of `UserId,badge1,badg2,...`
* `train_test_generation.py`: Generates train and test set from `badges.csv` file for `recommendation/` algorithms.

#### `recommendation`:
* `collaborative_filtering.py`: Implementation of the item-based collaborative filtering method to recommend badges and evaluate the results.
* `popular_badge_baseline.py`: Implementation of the baseline algorithm which recommends popular badges to each user.
