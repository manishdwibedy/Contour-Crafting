import re, ast

class Header(object):
    def __init__(self, lines):
        self.lines = lines
        self.commentInProgress = False

    def extract_header_section(self):
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

    def extract_header(self):
        header_info = self.extract_header_section()

        header_info = {}
        for header_line in header_info:
            self.extra_header_info_line(header_line, header_info)

        return header_info

    def extra_header_info_line(self, line, header_info):
        # Detecting whether a comment line is in progress
        if line.startswith('/*'):
            self.commentInProgress = True
            print 'Comment Started!'
        if not self.commentInProgress:
            self.extract_header_info(line, header_info)
        else:
            print 'comment - ' + line
            if line.endswith('*/'):
                self.commentInProgress = False
                print 'Comment Ended!'

    def extract_header_info(self, line, header_info):
        if line.startswith('FILE_DESCRIPTION'):
            found_file_schema_regex = re.search(r'FILE_DESCRIPTION(.*);', line)
            if found_file_schema_regex:
                file_schema_string = found_file_schema_regex.group(1)
                file_schema_string_escaped = ast.literal_eval(file_schema_string)

                filename_string = file_schema_string_escaped[0]

                view_defination_regex = re.search(r'ViewDefinition \[(.*)\]', filename_string)

                if view_defination_regex:
                    view_defination = view_defination_regex.group(1)
                    header_info['view_defination'] = view_defination
                pass
        elif line.startswith('FILE_NAME'):
            found_file_schema_regex = re.search(r'FILE_NAME(.*);', line)
            file_name_defination = ('file_name', 'creation_time', 'creating_user', 'creating user org', 'pre-processor', 'app_name', 'authorizing_user')
            if found_file_schema_regex:
                file_schema_string = found_file_schema_regex.group(1)
                file_schema_string_escaped = ast.literal_eval(file_schema_string)

                file_name_info = {}
                if len(file_schema_string_escaped) == len(file_name_defination):
                    for index in range(len(file_schema_string_escaped)):
                        label = file_name_defination[index]
                        value = file_schema_string_escaped[index]
                        file_name_info[label] = value
                    header_info['file_name'] = file_name_info
            pass
        elif line.startswith('FILE_SCHEMA'):
            found_file_schema_regex = re.search(r'FILE_SCHEMA(.*);', line)
            if found_file_schema_regex:
                file_schema_string = found_file_schema_regex.group(1)
                file_schema_string_escaped = ast.literal_eval(file_schema_string)
                header_info['file_schema'] = file_schema_string_escaped

            pass

        pass

    def get_header(self):
        '''
        Returning the header content
        :return: header object
        '''
        header = self.extract_header()
        if len(header) > 0:
            return header
        else:
            return None
