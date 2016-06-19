import numpy as np
import math
from common.constant import IDLE_RATIO, EDGE_TPYE

def getDistance(graph, start_node, end_node):
    if start_node in graph.node and end_node in graph.node:
        start_node = graph.node[start_node]
        end_node = graph.node[end_node]
        x_diff = start_node['X'] - end_node['X']
        y_diff = start_node['Y'] - end_node['Y']
        distance = pow((x_diff ** 2) * IDLE_RATIO + y_diff ** 2, 0.5)
        return distance
    else:
        return -1

def findAngle(graph, edge_pair, degrees=False):
    '''
    Finding the angle between the edge pair in the graph
    :param graph:  the graph information
    :param edge_pair: the edge pair
    :return: the angle in radians
    '''
    vectors = []
    for edge in edge_pair:

        point_1 = graph.node[edge[0]]
        point_2 = graph.node[edge[1]]

        # Computing the vector
        vector = {
            'X' : point_1['X'] - point_2['X'],
            'Y' : point_1['Y'] - point_2['Y'],
        }

        # Appending the vector
        vectors.append((vector['X'], vector['Y']))

    angle_rad = angle_between(vectors)

    if degrees:
        return math.degrees(angle_rad)
    return angle_rad

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(vector_pair):
    '''
    Returns the angle in radians between the pair of two vectors ::
    :param vector_pair:
    :return: Angle in radians
    '''
    v1_u = unit_vector(vector_pair[0])
    v2_u = unit_vector(vector_pair[1])
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

def get_edge_cost(edge_data):
    if 'ROTATION_COST' in edge_data:
        return edge_data['ROTATION_COST']
    elif 'IDLE_COST' in edge_data:
        return edge_data['IDLE_COST']
    else:
        return edge_data['DEPOSITION_COST']

def get_edge_type_cost(edge_data):
    type = ''
    cost = 0

    if 'DEPOSITION_COST' in edge_data:
        type = EDGE_TPYE.DEPOSITION
        cost = edge_data['DEPOSITION_COST']
    else:
        if 'ROTATION_COST' in edge_data:
            type = EDGE_TPYE.ROTATION
            cost = edge_data['ROTATION_COST']
        elif 'IDLE_COST' in edge_data:
            type = EDGE_TPYE.IDLE
            cost =  edge_data['IDLE_COST']

    return {
        'type': type,
        'cost': cost
    }

def merge_two_dicts(x, y):
    '''Given two dicts, merge them into a new dict as a shallow copy.'''
    z = x.copy()
    z.update(y)
    return z

def split_parameters(line):

    parameter_list = []
    last_character = line[0]
    valid_seperator_characters = "#\$.(),"
    current_parameter = ''
    for character in line:

        # Encountered a seperator
        if character in valid_seperator_characters or last_character in valid_seperator_characters:
            print 'seperator'
        elif character == "'":
            continue
        else:
            current_parameter += character
