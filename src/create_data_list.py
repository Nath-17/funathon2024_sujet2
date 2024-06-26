import yaml
def create_data_list(source_file):
    with open(source_file, 'r') as file:
        catalogue = yaml.safe_load(file)
    return catalogue