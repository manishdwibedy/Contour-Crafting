from input import Input
from detection import IFC_Detector
from metadata import MetaData

class IFCParsing(object):
    def __init__(self, filename):
        self.filename = filename

    def parse(self):
        '''
        Parsing the file.
        :return: returning the parsed content if the file is an IFC file, otherwise None
        '''
        detector = IFC_Detector(self.read_first_line())
        ifc_derected = detector.detect()
        if ifc_derected:
            self.read()
            metadata = MetaData(self.lines)
            self.metadata = metadata.get_metadata()
            return self.lines
        else:
            return None

    def read_first_line(self):
        '''
        Reading the first line of the file
        :return: the first line of the file
        '''
        file_input = Input(self.filename)
        return file_input.readFirstLine()

    def read(self):
        '''
        Reading the complete file
        :return:
        '''
        file_input = Input(self.filename)
        file_input.read()
        content = file_input.get_file_contents()
        self.lines = content.splitlines()