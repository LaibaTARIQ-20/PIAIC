#Find out all the methods of the sting in python using `dir()` function. Leave dunder methods starting with `__`.
sting_methods = [method for method in dir(str) if not method.startswith('__')]
print(sting_methods)

myself="my name is Laiba.I am 20 years old."

print("Capitalize:",myself.capitalize())

print("casefold:",myself.casefold())

#print("center: ",myself.center())

print("encode:",myself.encode())

print("lower:","Laiba".lower())

print("upper:",myself.upper())

print("join:","-",myself.join(["python","is","awsome"]))

print("istitle:",myself.istitle())

#print("removeprefix:",myself.removeprefix())

print("title:",myself.title())

print("count:",myself.count("laiba"))

print("replace:",myself.replace("javascript","python"))
