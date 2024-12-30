Dict={101:'python',201:'java',301:'c',401:'c++'}
print(Dict)
print(type(Dict))
print("--------------------------------")
print(Dict[101])
print(Dict[201])
print(Dict[301])
print(Dict[401])
Dict[501]='sql'
print("---------------------------")
print(Dict)
Dict[101]='Flutter'
print("--------------------------")
print(Dict)
#delete
c={10,20,30}
del c
del Dict[301]
print(Dict)