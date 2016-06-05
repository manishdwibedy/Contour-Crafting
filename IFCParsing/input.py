import os

class Input(object):
    def __init__(self, filename):
        self.filename = filename
        directory = os.path.dirname(os.path.abspath(__file__))
        self.file_location = os.path.join(directory, 'data', self.filename)

    def read(self):
        '''
        Reading the complete file
        :return:
        '''
        file = open(self.file_location)
        self.file_contents = file.read()

    def readFirstLine(self):
        '''
        Reading only the first line and returning it for detection purposes
        :return: the first line of the file
        '''
        with open(self.file_location) as file:
            return file.readline()

    def get_file_contents(self):
        '''
        Returning the file's content
        :return: file's content
        '''
        return self.file_contents
