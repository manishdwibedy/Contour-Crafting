
class MetaData(object):
    def __init__(self, lines):
        self.lines = lines

    def extract_metadata_section(self):
        '''
        Extracting the header section of the IFC file
        :return: a list of header lines
        '''

        header_lines = []
        header_started = False
        for line in self.lines:
            # Header section started
            if line.strip() == 'HEADER;':
                header_started = True

            # If the header section has started, but not yet ended
            if header_started and line.strip() != 'ENDSEC;':
                header_lines.append(line)
            # If the header section has not yet started
            elif not header_started:
                continue
            # If the header section has ended
            else:
                break

        self.header_lines = header_lines




    def get_metadata(self):
        self.extract_metadata_section()
        if self.header_lines:
            return self.header_lines
        else:
            return None
