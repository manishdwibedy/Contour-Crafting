
class IFC_Detector(object):
    def __init__(self, line):
        self.line = line
        self.ISO = 'ISO-10303-21;'

    def detect(self):
        '''
        Detecting wherether the file is an IFC file or not using the first line's content
        :return: True if the file is an IFC file, otherwise false
        '''
        if self.line.strip() == self.ISO:
            return True
        else:
            return False
