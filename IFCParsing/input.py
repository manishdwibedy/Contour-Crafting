import os

class Input(object):
    def __init__(self, filename):
        self.filename = filename
        self.directory = os.path.dirname(os.path.abspath(__file__))

    def read(self):
        file_location = os.path.join(self.directory, 'data', self.filename)
        file = open(file_location)

        self.file_contents = file.read()

    def get_file_contents(self):
        return self.file_contents
