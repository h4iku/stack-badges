import csv
import random
from collections import OrderedDict
from itertools import chain


def build_dict(dataset_name):
    """Build badges dictionary from the dataset"""

    with open(dataset_name) as csvfile:
        reader = csv.reader(csvfile)

        user_badges = OrderedDict((row[0], row[1:]) for row in reader)

    return user_badges


def expand_user_badges(user_badges):
    """Build user badge matrix"""

    badges = sorted(list(set(chain(*user_badges.values()))))
    expanded_dataset = OrderedDict((uid, [1 if badge in bs else 0
                                          for badge in badges])
                                   for uid, bs in user_badges.items())
    return badges, expanded_dataset


def generate_train_test(badges, expanded_dataset):

    train_set = expanded_dataset
    test_set = OrderedDict()
    evaluation_set = OrderedDict()

    for uid, bs in train_set.items():
        # Users with more than 5 badges randomly selected for test
        if sum(bs) > 5 and random.randint(0, 4) == 0:
            indices = [i for i, x in enumerate(bs) if x == 1]

            # Randomly select one badge (hold-one-out)
            selection = random.choice(indices)
            bs[selection] = 0

            train_set[uid] = bs
            test_set[uid] = bs
            evaluation_set[uid] = badges[selection]

    # Write sets on files
    with open('train_set.csv', 'w') as file:
        file.write('UserId,' + ','.join(badges) + '\n')
        for uid, bs in train_set.items():
            file.write(str(uid) + ',' + ','.join(str(b) for b in bs) + '\n')

    with open('test_set.csv', 'w') as file:
        file.write('UserId,' + ','.join(badges) + '\n')
        for uid, bs in test_set.items():
            file.write(str(uid) + ',' + ','.join(str(b) for b in bs) + '\n')

    with open('validation_set.csv', 'w') as file:
        for uid, badge in evaluation_set.items():
            file.write(str(uid) + ',' + badge + '\n')


DATASET = 'badges.csv'
user_badges = build_dict(DATASET)
badges, expanded_dataset = expand_user_badges(user_badges)

generate_train_test(badges, expanded_dataset)
