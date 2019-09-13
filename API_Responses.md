# API responses
The structure of the response depends on the success or failure of the resquest

# Error
**The error structure is always the same** 

You can find the full list of errors in [List of API"s errors](https://github.com/nicosocoro/ServigariAPI_Python/blob/master/API_List_Errors.md)

If the request fails, it will return a JSON with the structure:

```json 
error_JSON = {
    "id": "number depending on the error",
    "status": "ERROR",
    "description": "description of the error that ocurrs during the request"
}
```

## Clients

**Definition - Get all clients**

Returns a list of JSON objects filled with all the clients stored 

`GET /Clients`
```json
client = {
    "id": 1,
    "Name": "Nicolás",
    "Lastname": "Socoró", 
    "Location": "San Nicolás",
    "Adress": "Adress",
    "Email": "nicolassocoro@gmail.com",
    "Birthdate": 19960603,
    "UserRegistry": "admin",
    "DateRegistry": 20190901
},
{
    "id": 2,
    "Name": "Juansito",
    "Lastname": "Pérez", 
    "Location": "Rosario",
    "Adress": "AdressRosario",
    "Email": "juansito@perez.com",
    "Birthdate": 19800308,
    "UserRegistry": "another_user",
    "DateRegistry": 20190913
},

```

**Definition - Get specific client**

`GET /Clients/[id]`

Returns the client with ID = [id] (if exists)

**Success**

Suppose ***/Clients/1***

```json
client = {
    "id": 1,
    "Name": "Nicolás",
    "Lastname": "Socoró", 
    "Location": "San Nicolás",
    "Adress": "Adress",
    "Email": "nicolassocoro@gmail.com",
    "Birthdate": 19960603,
    "UserRegistry": "admin",
    "DateRegistry": 20190901
}
```

**Possible errors numbers**
* 401