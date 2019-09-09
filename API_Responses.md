# API responses
The structure of the response depends on the success or failure of the resquested

# Error
**The error structure is always the same** 

You can find the full list of errors in [List of API's errors](https://github.com/user/repo/blob/branch/other_file.md)

If the request fails, it will return a JSON with the structure:

```json 
error_JSON = {
    'id': id_number, #the number depends of the error 
    'status': 'ERROR',
    'description': 'description of the error that ocurrs during the request'
}
```

## Clients

**Definition**

Returns a list of JSON objects filled with all the clients stored 

`GET /Clients`
```json
client = {
    'id': 1,
    'Name': 'Nicolás',
    'Lastname': 'Socoró', 
    'Location': 'San Nicolás',
    'Adress': 'Adress',
    'Email': 'nicolassocoro@gmail.com',
    'Birthdate': 19960603,
    'UserRegistry': 'admin',
    'DateRegistry': 20190901
}
```

`GET /Clients/[id]`

Returns the client with ID = [id] (if exists)

**On success**
```json
client = {
    'id': 1,
    'Name': 'Nicolás',
    'Lastname': 'Socoró', 
    'Location': 'San Nicolás',
    'Adress': 'Adress',
    'Email': 'nicolassocoro@gmail.com',
    'Birthdate': 19960603,
    'UserRegistry': 'admin',
    'DateRegistry': 20190901
}
```

**Error**
```json 
error_JSON = {
    'id': id_number, #the number depends of the error 
    'status': 'ERROR',
    'description': 'description of the error that ocurrs during the request'
}
```