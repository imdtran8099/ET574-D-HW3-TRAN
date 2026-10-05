# list of three students named Jon, Kim and Lee
students = ['Jon', 'Kim', 'Lee']

# function to print 'Hi name' for each student in the list
def greet_students():
    for student in students:
        print(f'Hi {student}')

# call the function
greet_students()
# change Jon to John
students[1] = 'John'