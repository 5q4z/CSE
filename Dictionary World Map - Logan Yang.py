world_map = {
    'WESTHOUSE': {
        'NAME': "West of House",
        'DESCRIPTION': "You are west of the white house",
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'SOUTH': 'SOUTHHOUSE'
        }
    },
    'NORHTHOUSE': {
        'NAME': "North of House",
        'DESCRIPTION': "You are north of the white house",
        'PATHS': {
            'SOUTH': 'WESTHOUSE'
        }
    },
    'SOUTHHOUSE': {
        'NAME': "South of House",
        'DESCRIPTION': "You are south of the white house",
        'PATHS': {
            'NORTH': 'WESTHOUSE'
        }
    }
}
