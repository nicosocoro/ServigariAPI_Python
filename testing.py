# import os
# print(os.getenv('Database'))

# dirpath = os.getcwd()
# print("current directory is : " + dirpath)
# foldername = os.path.basename(dirpath)

# class test():
#     def __init__(self):
#         pass

#     def decoradora(function_externa):
#         def funcion_interior():
#             print("Inicio")
#             function_externa()
#             print("Fin")

#         return funcion_interior

#     @decoradora
#     def prueba(self):
#         print("esta es la funcion prueba")
 
# t = test()
# t.prueba()


# def decoradora(funcion_externa):
#     def funcion_interna():
#         print("hola")
#         funcion_externa()
#         print("fin")
    
#     return funcion_interna

# @decoradora
# def test():
#     print("cuerpo")

# test()
import sqlite3

with sqlite3.connect('Registers.db') as conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM Client")
    result = cur.fetchall()
print(result)

# def decorator(external_function):
#     def internal_function():
#         result = 'testingh'
#         external_function()
#         return result
#     return internal_function

# @decorator
# def test():
#     print('dentro de p')

# r = test()
# print(r)