

def calculate_grade(line):
    line = line[:-1]
    data_list = line.split(',')
    name = data_list[0]
    midterm1 = int(data_list[1])
    midterm2 = int(data_list[2])
    final = int(data_list[3])
    final_grade = midterm1 * (3/10) + midterm2 * (3/10) + final * (4/10)
    

    if (final_grade >= 90):
        letter_grade = 'AA'
    elif (final_grade >= 85):
        letter_grade = 'BA'
    elif (final_grade >= 80):
        letter_grade = 'BB'
    elif (final_grade >= 75):
        letter_grade = 'CB'
    elif (final_grade >= 70):
        letter_grade = 'CC'
    elif (final_grade >= 65):
        letter_grade = 'DC'
    elif (final_grade >= 60):
        letter_grade = 'DD'
    elif (final_grade >= 55):
        letter_grade = 'FD'
    else:
        letter_grade = 'FF'

    if (letter_grade in ['FF', 'FD']):
        validity = '(Fail)'
    else:
        validity = '(Pass)'

    return name + '---->' + letter_grade + validity + '\n'

# file.txt = the file where grades are written.

with open('file.txt', 'r', encoding='utf-8') as file:
    to_be_appended_list = []

    for line in file:
        to_be_appended_list.append(calculate_grade(line))
        print(to_be_appended_list)

## to create a new file with final notes written.

    with open('grades.txt', 'w', encoding='utf-8') as file2:
        for line in to_be_appended_list:
            file2.write(line)

#A new file has been created on the desktop of your computer.(grades)