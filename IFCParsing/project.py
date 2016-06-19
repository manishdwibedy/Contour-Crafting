import re, ast
from common.utility import split_parameters

class Project(object):
    def __init__(self, lines):
        self.lines = lines
        self.project_tag_info = {}
        self.commentInProgress = False
        self.label_list = ['GlobalId','OwnerHistory','Name','Description','RefLatitude','RefLongitude','RefElevation','LandTitleNumber','SiteAddress']



    def extract_project_section(self):
        '''
        Extracting the header section of the IFC file
        :return: a list of header lines
        '''
        project_section_info = {}
        project_lines = []
        project_started = False
        for line in self.lines:
            # Header section started
            if line.strip() == 'DATA;':
                project_started = True
                continue

            # If the project section has started, but not got the tag 'IFCPROJECT' we looking for
            if project_started and len(line) > 0:
                line_info = line.split('=')
                if len(line_info) == 1:
                    continue
                label = line_info[0].strip()
                info = line_info[1].strip()
                self.project_tag_info[label] = info
                # If the main tag is encountered
                if 'IFCSITE' in line.strip():
                    project_lines.append(info)

            # If the project section has not yet started
            elif not project_started:
                continue


        return project_lines

    def extract_info_tag(self, ifc_project_info, project_section_info):
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
                        project_section_info[name] = value
                    # If the parameter is actually some concrete value
                    else:
                        if parameter == '$':
                            project_section_info[label] = None
                        else:
                            project_section_info[label] = parameter
        return project_section_info
    def extract_tag_info(self, parameter):
        '''
        Extracting the tag content recursively
        :param parameter: the tag value to look for. For eg. #23
        :return: the tag value
        '''
        value = {}
        name = ''

        # If the parameter has been seen earlier
        if parameter in self.project_tag_info:
            # The content of the paramter
            tag_content = self.project_tag_info[parameter]

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
                    return name, self.extract_concrete_tag(tag_content_value)

        else:
            return None, value

    def extract_concrete_tag(self, tag_content_value):
        parameters = tag_content_value.split(',')

        tag_value = []
        for parameter in parameters:
            if not parameter == '$':
                try:
                    parameter = ast.literal_eval(parameter)
                    if len(parameter) > 0:
                        tag_value.append(parameter)
                except:
                    print 'Error!!'

        if len(tag_value) > 0:
            return ';'.join(tag_value)
        return tag_value

    def extract_project(self):
        project_lines = self.extract_project_section()

        project_info = {}
        for project_line in project_lines:
            self.extract_project_info_line(project_line, project_info)

        return project_info

    def extract_project_info_line(self, line, project_info):
        # Detecting whether a comment line is in progress
        if line.startswith('/*'):
            self.commentInProgress = True
            print 'Comment Started!'
        if not self.commentInProgress:
            self.extract_project_info(line, project_info)
        else:
            print 'comment - ' + line
            if line.endswith('*/'):
                self.commentInProgress = False
                print 'Comment Ended!'

    def extract_project_info(self, line, project_info):
        project_section_info = {}
        found_ifc_project_regex = re.search(r'IFCSITE\((.*)\);', line)
        ifc_project = found_ifc_project_regex.group(1)

        # ifc_project = ifc_project.replace('(', '')
        # ifc_project = ifc_project.replace(')', '')

# '#\$.()
# '\\'2AR5DOWMH3evn1gxNP$CO2\\',#41,\\'Default\\',$,\\'\\',#219,$,$,.ELEMENT.,(42,21,31,181945),(-71,-3,-24,-263305),0.,$,$'
        ifc_project_info = []
        values = split_parameters(ifc_project)
        # values = ifc_project.split(',')
        for val in values:
            try:
                ifc_project_info.append(ast.literal_eval(val))
            except:
                ifc_project_info.append(val)
        self.extract_info_tag(ifc_project_info, project_section_info)
        project_section_info

        pass

    def get_project(self):
        '''
        Returning the project content
        :return: project object
        '''
        project = self.extract_project()
        if len(project) > 0:
            return project
        else:
            return None
