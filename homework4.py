immutable_var = 1, 2.5, True, 'String'
print(immutable_var)
# immutable_var[1] = 2 кортеж относится к неизменяемым типам данных
mutable_list = [1, 2.5, True, 'String']
print(mutable_list)
mutable_list[3] = mutable_list[3].upper()
mutable_list[1] = 2
mutable_list[2] = 2.5
print(mutable_list[1:4:2])
print(True not in mutable_list)
print(mutable_list[0:4:3])
print(mutable_list)
#immutable_var = immutable_var + mutable_list
immutable_var = ((1, 2.4, False) * 2)
print(immutable_var)