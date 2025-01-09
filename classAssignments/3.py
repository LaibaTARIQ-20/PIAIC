list_methods = [method for method in dir(list) if not method.startswith('__')]
print(list_methods)