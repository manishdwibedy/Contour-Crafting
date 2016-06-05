import input
import detection

class IFCParsing(object):
    def __init__(self, filename):
        self.filename = filename

    def parse(self):
        detector = detection.IFC_Detector(self.read_first_line())
        ifc_derected = detector.detect()
        if ifc_derected:
            self.read()

    def read_first_line(self):
        file_input = input.Input(self.filename)
        return file_input.readFirstLine()

    def read(self):
        file_input = input.Input(self.filename)
        file_input.read()
        self.content = file_input.get_file_contents()