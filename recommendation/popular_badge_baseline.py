import csv
from collections import Counter
from itertools import chain

from datasets import badges2008 as dataset


def badges_frequency(dataset_name):
    """Counting all badge occurrences"""

    with open(dataset_name) as csvfile:
        reader = csv.reader(csvfile)

        badges = chain(*[row[1:] for row in reader])

    return Counter(badges)


badge_freq = badges_frequency(dataset.all_badges)
most_common_badges = [badge[0] for badge in badge_freq.most_common(5)]

with open(dataset.test_set) as file:
    reader = csv.reader(file)
    badges = next(reader)[1:]

    test_set = [[int(x) for x in row[1:]] for row in reader]

with open(dataset.validation_set) as file:
    reader = csv.reader(file)

    eval_set = [badge[1] for badge in reader]

tp = 0
fp = 0
for k, test in enumerate(test_set):
    test_badges = [badges[index] for index in
                   [i for i, j in enumerate(test) if j == 1]]

    selected_badge = None
    for badge in most_common_badges:
        if badge not in test_badges:
            selected_badge = badge
            break

    if selected_badge == eval_set[k]:
        tp += 1
    else:
        fp += 1

print('Precision:', tp / (tp + fp))
