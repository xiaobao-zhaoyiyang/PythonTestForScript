import yaml


def read_yaml(filename):
    with open('../data/' + filename, 'r', encoding='utf-8') as f:
        return yaml.load(f, Loader=yaml.FullLoader)
