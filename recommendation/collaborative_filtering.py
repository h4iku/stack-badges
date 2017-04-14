import pandas as pd
from scipy.spatial.distance import cosine
import csv


def simi_score(history, similarities):
    return sum(history * similarities) / sum(history + similarities)


# Reading the train data
train_set = pd.read_csv("dataset/train_set.csv")

# Dropping "UserId" column
userid_dropped = train_set.drop('UserId', 1)

# Creating a placeholder data frame for badge vs badge similarity
data_calc = pd.DataFrame(index=userid_dropped.columns, columns=userid_dropped.columns)

# Filling the placeholder with cosine similarity values
for i in range(len(data_calc.columns)):
    for j in range(i + 1, len(data_calc.columns)):
        data_calc.ix[i, j] = 1 - cosine(userid_dropped.ix[:, i], userid_dropped.ix[:, j])
        # Copying matrix's upper triangle to lower triangle
        data_calc.ix[j, i] = data_calc.ix[i, j]
    # And the main diameter is one
    data_calc.ix[i, i] = 1
        
# A placeholder for 10 neighbor badges to each badge
badge_neighbors = pd.DataFrame(index=data_calc.columns, columns=range(1, 11))

# Filling neighboring badge names
for i in range(len(data_calc.columns)):
    badge_neighbors.ix[i] = data_calc.ix[:, i].sort_values(ascending=False)[:10].index

# Reading the test data
test_set = pd.read_csv("dataset/test_set.csv")
userid_dropped = test_set.drop('UserId', 1)
# Creating a placeholder matrix for similarities
data_sims = pd.DataFrame(index=test_set.index, columns=test_set.columns)
data_sims.ix[:, :1] = test_set.ix[:, :1]  # Filling the UserId column

# Iterating through all rows, skipping the user column
# and filling others with similarity scores
for i in range(len(data_sims.index)):
    user = data_sims.index[i]  # Contains user index
    
    for j in range(1, len(data_sims.columns)):
        badge = data_sims.columns[j]  # Contains badge name
        
        if test_set.ix[i][j] >= 1:  # If the user already has the badge
            data_sims.ix[i][j] = 0
        else:
            similar_badge_names = badge_neighbors.ix[badge]
            similar_badge_vals = data_calc.ix[badge].sort_values(ascending=False)[:10]
            user_badges = userid_dropped.ix[user, similar_badge_names]
            
            data_sims.ix[i][j] = simi_score(user_badges, similar_badge_vals)

# 2 recommendation for each user
badge_recommend = pd.DataFrame(index=data_sims.index, columns=['UserId', '1', '2'])
badge_recommend.ix[:, 0] = data_sims.ix[:, 0]  # Copying the UserId column

# Replacing badge names
for i in range(len(data_sims.index)):
    badge_recommend.ix[i, 1:] = data_sims.ix[i, :].sort_values(ascending=False).ix[1:3].index


# Validating the recommendations
val_file = open('dataset/validation_set.csv')
reader = csv.reader(val_file)

tp = [0] * 2
fp = [0] * 2
for i, row in enumerate(reader):
    if badge_recommend.ix[i, 1] in row[1:]:
        tp[0] += 1
    else:
        fp[0] += 1
    
    # Top 2 badge recommendation    
    recs = list(badge_recommend.ix[i, 1:])
    if [x for x in recs if x in row[1:]]:
        tp[1] += 1
    else:
        fp[1] += 1
        
print(tp[0] / (tp[0] + fp[0]))
print(tp[1] / (tp[1] + fp[1]))

val_file.close()

