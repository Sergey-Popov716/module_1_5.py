immutable_var = ('Sergey', 100, [1, 2, 3])
print(immutable_var)
# immutable_var[0] = 200
# TypeError: 'tuple' object does not support item assignment
# Кортежи неизменяемы, нельзя изменить данные внутри кортежа
mutable_list = ['Anton', 2.0, 'six', [1, 2, 3], False]
mutable_list[0] = 'Dasha'
mutable_list[2] = 6
print(mutable_list)