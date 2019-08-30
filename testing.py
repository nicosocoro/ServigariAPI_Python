# import os
# print(os.getenv('Database'))

# dirpath = os.getcwd()
# print("current directory is : " + dirpath)
# foldername = os.path.basename(dirpath)

class test:
    def decoradora(self, function_externa):
        def funcion_interior():
            print("Inicio")
            function_externa()
            print("Fin")

        return funcion_interior

    @decoradora
    def prueba(self):
        print("esta es la funcion prueba")

t = test()
t.prueba()


# prueba()

# class test:
#     # def __init__(self, op):
#     #     self.p = op

#     def __call__(self, op):
#         print(op)

# test().__call__("hola")

# # test("hola")


