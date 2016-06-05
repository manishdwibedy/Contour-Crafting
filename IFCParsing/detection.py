
class IFC_Detector(object):
    def __init__(self, line):
        self.line = line
        self.ISO = 'ISO-10303-21;'

    def detect(self):
        if self.line.strip() == self.ISO:
            return True
        else:
            return False
