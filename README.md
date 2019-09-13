# ServigariAPI_Python
API that handles backend tasks in Servigari.

## What is Servigari?
Servigari is my dad's business which is engaged to repair home appliances. 
I took advantage of his need of managing the daily incomes and expenses to start this project.

Actually, I've developed a .NET Windows Application version. However, I decided to make its web version and, instead of re-using the .NET backend program, I'm taking advantage of the situation to learn new Python skills and ReactJS (in front-end). 

## Main goal of the project
This set of Python files were developed as an Introduction project in pursuit of my personal improvement.
The project is a small backend program were SQL queries are executed to retrieve and manage data (CRUD).

At a business level, it manages income and expenses from a home appliance repair familiar commerce.

At an architecture level, this project works as an API to handle all the transactions requested by the final user. 
**The UI will be developed in using ReactJS and will consume this Python API.** 

It's important to note that Python may not be the best option but, again, is only for personal improvements.

---

## Sections

This README guide it's divided in many sections. Also, it's complemented by other files such as [API_Responses.md](https://github.com/nicosocoro/ServigariAPI_Python/blob/master/API_Responses.md) and [API_List_Errors.md](https://github.com/nicosocoro/ServigariAPI_Python/blob/master/API_List_Errors.md)


## **First steps**

Execute **Database/RegistersDB_Creation.py** to ***initialize DB with the corresponds tables***.
Then, *in case you need or want to explore and test*, run **Database/SampleData.py** which fills the tables with some generic data.

## API

**Introduction**

To handle APIs requests, uses [Flask](https://www.fullstackpython.com/flask.html) and [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/) to handle permissions and limitations in the respective requests.  

### **API - Responses**

In this [file](https://github.com/nicosocoro/ServigariAPI_Python/blob/master/API_Responses.md) are defined all the possible responses depending on the resource requested.

### **API - List of Errores**

In this [file](https://github.com/nicosocoro/ServigariAPI_Python/blob/master/API_List_Errors.md)
are listed all the possible errores ocurred during the request.

The errores are defined with the structure **[ID] - [Description]**