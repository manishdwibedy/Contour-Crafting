
def get_edge_cost(edge_data):
    if 'ROTATION_COST' in edge_data:
        return edge_data['ROTATION_COST']
    elif 'IDLE_COST' in edge_data:
        return edge_data['IDLE_COST']
    else:
        return edge_data['DEPOSITION_COST']