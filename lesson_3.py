# #инкапсуляция
# # публичный без нтжных подчеркиваний 
# # защишен с одним нижним подчеркиванием
# 3 скрытый с 2 нижними подчеркиваниями
# class Cat:
#     def __init__(self,name,age):
#         self,_name = name
#         self,_age = age 

#         def may(self):
#             print(f'{self.name} may\n')
#             (f'age is {self.age}')


class Person:
    def __init__(self, name, last_name,age,key)
    self._name = _name
    self._lastname = _lastname
    self._age = age 
    self._key = key 
    
    
    def keys(slef):
        print(self._name)

    def _s(self):
        print(self._name,self._key)    

per1 = Person('beka','d.y',19,'1234567')



per1.name = 'ivan'
per1.key = 'wegghj'
print(per1.name)
per1.keys()
per1._s()

# p = 'wefggfth'
# print(dir(p))
# print(p.upper())

# class Micro:
#     def __init__(self,name):
#         self.name = name
        

#     def on(self):
#         print('start')

#     def time(self):
#         print('import time')

#     def _off(self):
#         print('stop')

#     def open(self):
#         print('при открытии двери микроволновка автоматически останавливается')
#         print('off')

#     def stop(self):
#         print('stop')    


# c = Micro('Samsung')
# c.on()
# c.open() 
# c._off()   

# class Чайник:
#     def __init__(self):



#     def on(self = 1):
#         pass
#     def _on(self):
#         print('on')
#     def _woter(self):
#         print('агревать воду')
#     def off(self):
#         print('выключить')


# h = Чайник('tefal')
# h.on() 
# h._woter()       