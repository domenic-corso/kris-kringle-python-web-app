import json

class AbstractDAO:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_raw(self):
        f = open(self.file_path)
        raw = json.load(f)
        f.close()

        return raw

    def save_raw(self, data):
        f = open(self.file_path, 'w')
        json.dump(data, f, indent=4)
        f.close()