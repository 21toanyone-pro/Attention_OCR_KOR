import datasets.fsns as fsns

DEFAULT_DATASET_DIR = 'datasets/data/fsns/train'

DEFAULT_CONFIG = {
    'name':
        'real_test',
    'splits': {
        'train': {
            'size': 1000000,
            'pattern': 'kor_train*'
        },
        'test': {
            'size': 0,
            'pattern': 'tfexample_test*'
        }
    },
    'charset_filename':
        'kor_datasets.txt',
    'image_shape': (50, 150, 3),
    'num_of_views':
        1,
    'max_sequence_length':
        37,
    'null_code':
        2445,
    'items_to_descriptions': {
        'image':
            'A [50 x 150 x 3] color image.',
        'label':
            'Characters codes.',
        'text':
            'A unicode string.',
        'length':
            'A length of the encoded text.',
        'num_of_views':
            'A number of different views stored within the image.'
    }
}


def get_split(split_name, dataset_dir=None, config=None):
  if not dataset_dir:
    dataset_dir = DEFAULT_DATASET_DIR
  if not config:
    config = DEFAULT_CONFIG

  return fsns.get_split(split_name, dataset_dir, config)