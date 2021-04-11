from core.data_handler import DataHandler


class Teacher:

    def __init__(self, id_):
        self.id_ = id_
        self.data = self.get_by_id()
        self.free_time = self.get_free_time()

    def get_by_id(self):
        data = DataHandler('teachers.json').get()
        return list(filter(lambda x: x['id'] == self.id_, data))[0]

    def get_free_time(self):
        result = dict()
        for day, time in self.data['free'].items():
            result[day] = [k for k, v in time.items() if v is True]
        return result


if __name__ == '__main__':
    test = Teacher(1)
    print(test.free_time)
