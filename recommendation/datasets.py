from collections import namedtuple

_DATASET_ROOT = '../data/'
Dataset = namedtuple('Dataset', ['all_badges', 'train_set', 'test_set', 'validation_set'])

badges2008 = Dataset(
    _DATASET_ROOT + 'badges2008.csv',
    _DATASET_ROOT + 'dataset2008/train_set.csv',
    _DATASET_ROOT + 'dataset2008/test_set.csv',
    _DATASET_ROOT + 'dataset2008/validation_set.csv'
)

badges2008_2009 = Dataset(
    _DATASET_ROOT + 'badges2008-2009.csv',
    _DATASET_ROOT + 'dataset2008-2009/train_set.csv',
    _DATASET_ROOT + 'dataset2008-2009/test_set.csv',
    _DATASET_ROOT + 'dataset2008-2009/validation_set.csv'
)

badges2008_2010 = Dataset(
    _DATASET_ROOT + 'badges2008-2010.csv',
    _DATASET_ROOT + 'dataset2008-2010/train_set.csv',
    _DATASET_ROOT + 'dataset2008-2010/test_set.csv',
    _DATASET_ROOT + 'dataset2008-2010/validation_set.csv'
)
