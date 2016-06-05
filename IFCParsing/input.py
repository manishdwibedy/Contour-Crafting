import os

class Input(object):
    def __init__(self, filename):
        self.filename = filename
        directory = os.path.dirname(os.path.abspath(__file__))
        self.file_location = os.path.join(directory, 'data', self.filename)

    def read(self):
        file = open(self.file_location)
        self.file_contents = file.read()

    def readFirstLine(self):
        with open(self.file_location) as file:
            return file.readline()

    def get_file_contents(self):
        return self.file_contents
