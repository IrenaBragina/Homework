immutable_var=(1,5,4,True,'Привет')
print(immutable_var)
immutable_var[0]=15
print(immutable_var) #кортеж -это неизменяемый тип данных,  т.к. это как бы ссылка на список
mutable_list=[6,7,108,True,'Прювет']
print(mutable_list)
mutable_list[4]='good'
print(mutable_list)
