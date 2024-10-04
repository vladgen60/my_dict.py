grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_score_midl = []    # Создаем пустой список для средних оценок.
students_list = list(students)  # Преобразуем множество в список.
students_list = sorted(students_list)   # Сортируем список студентов по алфавиту.
student_dict = dict(zip(students_list,grades)) # Создаем словарь из списка студенов в качестве ключа и их оценок в качестве значений.

# По каждому студенту отдельно вычисляем его среднюю оценку и добавляем ее в список "students_score_midl".

Aaron = student_dict.pop('Aaron') 
Aaron_midl = sum(Aaron)/len(Aaron)
students_score_midl.append(Aaron_midl)
Bilbo = student_dict.pop('Bilbo')
Bilbo_midl = sum(Bilbo)/len(Bilbo)
students_score_midl.append(Bilbo_midl)
Johnny = student_dict.pop('Johnny')
Johnny_midl = sum(Johnny)/len(Johnny)
students_score_midl.append(Johnny_midl)
Khendrik = student_dict.pop('Khendrik')
Khendrik_midl = sum(Khendrik)/len(Khendrik)
students_score_midl.append(Khendrik_midl)
Steve = student_dict.pop('Steve')
Steve_midl = sum(Steve)/len(Steve)
students_score_midl.append(Steve_midl)

# Создаем из двух списков словарь и выводим его на экран.

students_dict_midl = dict(zip(students_list,students_score_midl)) 

print(students_dict_midl)