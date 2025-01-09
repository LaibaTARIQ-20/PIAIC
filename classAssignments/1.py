name ="laiba"
teachers_name=[name]
print("memory address of name is: ", id(name))
print("memory address of teachers name is: ",id(teachers_name[0]))

if id(name)== id(teachers_name[0]):
  print("same address")
else:
  print("They have different addresses")

