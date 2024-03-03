def create_variable(variable_name, value):
    globals()[variable_name] = value

create_variable("tom", "test")
print(tom)
