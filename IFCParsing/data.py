import re, ast

class Data(object):
    def __init__(self, lines):
        self.lines = lines
        self.commentInProgress = False

    def extract_data_section(self):
        '''
        Extracting the header section of the IFC file
        :return: a list of header lines
        '''

        data_info = {}
        data_lines = []
        data_started = False
        for line in self.lines:
            # Header section started
            if line.strip() == 'DATA;':
                data_started = True
                continue

            # If the data section has started, but not got the tag 'IFCPROJECT' we looking for
            if data_started and len(line) > 0:
                line_info = line.split('=')
                label = line_info[0].strip()
                info = line_info[1].strip()
                data_info[label] = info
                # If the main tag is encountered
                if 'IFCPROJECT' in line.strip():
                    found_ifc_project_regex = re.search(r'IFCPROJECT\((.*)\);', info)
                    ifc_project = found_ifc_project_regex.group(1)

                    ifc_project = ifc_project.replace('(', '')
                    ifc_project = ifc_project.replace(')', '')

                    ifc_project_info = []
                    values = ifc_project.split(',')
                    for val in values:
                        try:
                            ifc_project_info.append(ast.literal_eval(val))
                        except:
                            ifc_project_info.append(val)

            # If the data section has not yet started
            elif not data_started:
                continue


        return data_lines

    def extract_data(self):
        data_lines = self.extract_data_section()

        data_info = {}
        for data_line in data_lines:
            self.extra_data_info_line(data_line, data_info)

        return data_info

    def extra_data_info_line(self, line, data_info):
        # Detecting whether a comment line is in progress
        if line.startswith('/*'):
            self.commentInProgress = True
            print 'Comment Started!'
        if not self.commentInProgress:
            self.extract_data_info(line, data_info)
        else:
            print 'comment - ' + line
            if line.endswith('*/'):
                self.commentInProgress = False
                print 'Comment Ended!'

    def extract_data_info(self, line, data_info):
        if line.startswith('FILE_DESCRIPTION'):
            found_file_schema_regex = re.search(r'FILE_DESCRIPTION(.*);', line)
            if found_file_schema_regex:
                file_schema_string = found_file_schema_regex.group(1)
                file_schema_string_escaped = ast.literal_eval(file_schema_string)

                filename_string = file_schema_string_escaped[0]

                view_defination_regex = re.search(r'ViewDefinition \[(.*)\]', filename_string)

                if view_defination_regex:
                    view_defination = view_defination_regex.group(1)
                    data_info['view_defination'] = view_defination
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
                    data_info['file_name'] = file_name_info
            pass
        elif line.startswith('FILE_SCHEMA'):
            found_file_schema_regex = re.search(r'FILE_SCHEMA(.*);', line)
            if found_file_schema_regex:
                file_schema_string = found_file_schema_regex.group(1)
                file_schema_string_escaped = ast.literal_eval(file_schema_string)
                data_info['file_schema'] = file_schema_string_escaped

            pass

        pass

    def get_data(self):
        '''
        Returning the data content
        :return: data object
        '''
        data = self.extract_data()
        if len(data) > 0:
            return data
        else:
            return None
