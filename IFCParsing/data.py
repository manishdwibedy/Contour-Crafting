import re, ast

class Data(object):
    def __init__(self, lines):
        self.lines = lines
        self.commentInProgress = False
        self.label_list = ('GUID', 'IfcOwnerHistory', 'Project Name', 'Project Description', None, None, None, 'IfcUnitAssignment', 'IfcGeometricRepresentationContext')
        self.data_tag_info = {}

    def extract_data_section(self):
        '''
        Extracting the header section of the IFC file
        :return: a list of header lines
        '''
        data_section_info = {}
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
                if len(line_info) == 1:
                    continue
                label = line_info[0].strip()
                info = line_info[1].strip()
                self.data_tag_info[label] = info
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
                    value = self.extract_info_tag(ifc_project_info, data_section_info)
                    data_section_info

            # If the data section has not yet started
            elif not data_started:
                continue


        return data_lines

    def extract_info_tag(self, ifc_project_info, data_section_info):
        # Every parameter has a corresponding label
        if len(self.label_list) == len(ifc_project_info):
            for index in range(len(ifc_project_info)):
                parameter = ifc_project_info[index]
                label = self.label_list[index]

                # If the label is missing, skip the parameter altogether
                if label:
                    # If the parameter is actually a reference
                    if parameter.startswith('#'):
                        name, value = self.extract_tag_info(parameter)
                        pass
                    # If the parameter is actually some concrete value
                    else:
                        if parameter == '$':
                            data_section_info[label] = None
                        else:
                            data_section_info[label] = parameter

    def extract_tag_info(self, parameter):
        '''
        Extracting the tag content recursively
        :param parameter: the tag value to look for. For eg. #23
        :return: the tag value
        '''
        value = {}
        name = ''

        # If the parameter has been seen earlier
        if parameter in self.data_tag_info:
            # The content of the paramter
            tag_content = self.data_tag_info[parameter]

            # The regex to extract the name and the content of the tag
            tag_regex = re.search(r'(.*)\((.*)\);', tag_content)

            # If the regex search was successful
            if tag_regex:
                # Tag's name
                name = tag_regex.group(1)
                # Tag's content
                tag_content_value = tag_regex.group(2)

                # If the tag content contain some reference to a parameter
                if '#' in tag_content_value:
                    sub_parameters = re.findall(r'#[0-9]+', tag_content_value)
                    for sub_parameter in sub_parameters:
                        tag_name, tag_value = self.extract_tag_info(sub_parameter)
                        value[tag_name] = tag_value
                    return name, value
                # if the value is actually some concreate object
                else:
                    return name, tag_content_value

        else:
            return None, value
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