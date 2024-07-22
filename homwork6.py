my_dict={'Denis':1982,'Natasha':1983,'Gleb':2016}
print(my_dict)
print(my_dict.get('Denis'))
print(my_dict.get('Inna'))
my_dict['Inna']=2019
my_dict['Anna']=2001
print(my_dict)
D = my_dict.pop('Denis')
print(D)
print(my_dict)
my_set={9,'дом',209}
print(my_set)
my_set.add('подъезд')
my_set.add(1)
a = my_set.remove(209)
print(my_set)