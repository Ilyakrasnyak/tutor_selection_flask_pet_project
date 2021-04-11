import json


class DataHandler:

    def __init__(self, address):
        self.address = '/home/ilyakrasnyak/PycharmProjects/tutor_selection_flask_pet_project/' \
                       'tutor_selection_flask_pet_project/data/' + address

    def get(self):
        with open(self.address, 'r') as data:
            return json.load(data)

    def append(self, data):
        with open(self.address, 'a') as file:
            json.dump(data, file, indent=4)
