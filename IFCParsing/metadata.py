import re, ast

class MetaData(object):
    def __init__(self, lines):
        self.lines = lines
        self.commentInProgress = False

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
                continue

            # If the header section has started, but not yet ended
            if header_started and line.strip() != 'ENDSEC;':
                if len(line) > 0:
                    header_lines.append(line)
            # If the header section has not yet started
            elif not header_started:
                continue
            # If the header section has ended
            else:
                break

        return header_lines

    def extract_metadata(self):
        header_info = self.extract_metadata_section()

        metadata_info = {}
        for header_line in header_info:
            self.extra_header_info_line(header_line, metadata_info)

        return metadata_info

    def extra_header_info_line(self, line, metadata_info):
        # Detecting whether a comment line is in progress
        if line.startswith('/*'):
            self.commentInProgress = True
            print 'Comment Started!'
        if not self.commentInProgress:
            self.extract_header_info(line, metadata_info)
        else:
            print 'comment - ' + line
            if line.endswith('*/'):
                self.commentInProgress = False
                print 'Comment Ended!'

    def extract_header_info(self, line, metadata_info):
        if line.startswith('FILE_DESCRIPTION'):
            found_description_regex = re.search(r'FILE_DESCRIPTION(.*);', line)
            if found_description_regex:
                description = found_description_regex.group(1)
                description_escaped = ast.literal_eval(description)

                view_defination_string = description_escaped[0]

                view_defination_regex = re.search(r'ViewDefinition \[(.*)\]', view_defination_string)

                if view_defination_regex:
                    view_defination = view_defination_regex.group(1)
                    metadata_info['view_defination'] = view_defination
                pass
        elif line.startswith('FILE_NAME'):
            pass
        elif line.startswith('FILE_SCHEMA'):
            pass

        pass
    def get_metadata(self):
        '''
        Returning the metadata content
        :return: metadata object
        '''
        metadata = self.extract_metadata()
        if len(metadata) > 0:
            return metadata
        else:
            return None
