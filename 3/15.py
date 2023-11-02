age = 27
txt = 'My name is Timur, I am ' + str(age)
print(txt)
age = 27
txt = 'My name is Timur, I am {}'.format(age)
print(txt)
age = 27
name = 'Timur'
profession = 'math teacher'
txt = 'My name is {0}, I am {1}, I work as a {2}'.format(name, age, profession)
print(txt)
name = 'Timur'
txt = 'My name is {0}-{0}-{0}'.format(name)
print(txt)
first_name = 'Timur'
last_name = 'Guev'
age = 27
profession = 'math teacher'
affiliation = 'BeeGeek'
print('Hello, {0} {1}. You are {2}. You are a {3}. You were a member of {4}'
               .format(first_name, last_name, age, profession, affiliation))
first_name = 'Timur'
last_name = 'Guev'
age = 27
profession = 'math teacher'
affiliation = 'BeeGeek'
print(f'Hello, {first_name} {last_name}. You are {age}. You are a {profession}. You were a member of {affiliation}')
