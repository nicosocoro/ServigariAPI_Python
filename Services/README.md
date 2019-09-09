## Introduction ##

This folder contains all files to define the API.

The files here are the ones which are consumed by externals APPs.
They will interact with the client application and retrieved the data required in JSON format.

### JSON object attributes names
All JSON attribute's names are defined in the folder **Utilities**. 
There are some Python files which store constants corresponding for each attribute name.

I implemented this modality in order to separate DB fields with the ones retrieved by the API.
That way, one field could be stored as 'Field_1_Database' in SQL Table but the API would name it 'Field1_API'.
