import csv
from pprint import pprint
from Fileutilities.absolutepath import absolute_path


def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class CsvReader:
    data = []

    def __init__(self, filepath):
        self.data = []
        try:
            with open(absolute_path(filepath)) as text_data:
                csv_data = csv.DictReader(text_data, delimiter=',')
                for row in csv_data:
                    self.data.append(row)
        except OSError:
            print('cannot open', filepath)
        # pprint(self.data)

    def return_data_as_objects(self, class_name):
        objects = []
        for row in self.data:
            objects.append(ClassFactory(class_name, row))
        return objects
