
# # args is a tuple
# # the number of arguments for the function can vary because the asterix operator
# # collects all the arguments into a tuple. It is a positional argument
# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#
#     return total
#
# print(add(4, 5, 6))

# # **kwargs store in dictionary

# class Car:
#
#     def __init__(self, **kw):
#         self.make = kw["make"]
#         self.model = kw["model"]
#
#
# my_car = Car(make="Nissan", model="GT-R")
# print(my_car.model)


# class Car:
#
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#
#
# my_car = Car(make="Nissan")
# print(my_car.model)