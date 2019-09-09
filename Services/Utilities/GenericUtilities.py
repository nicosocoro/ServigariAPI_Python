# API message responses

success_msg = {
    'id': 200,
    'description': 'Success',
    'status': 'OK'
}

err_connection_msg = {
    'id': 400,
    'description': 'An error ocurred while trying to connect to API.',
    'status': 'ERROR'
}

err_not_found_msg = {
    'id': 404,
    'description': 'The resource you requested was not found.',
    'status': 'ERROR'
}