import input

class IFCParsing(object):
    def __init__(self, filename):
        self.filename = filename

    def parse(self):
        self.read()
        pass

    def read(self):
        file_input = input.Input(self.filename)
        file_input.read()
        self.content = file_input.get_file_contents()