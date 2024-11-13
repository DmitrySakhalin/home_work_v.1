class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        total_sum = sum(sum(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())
        return round(total_sum / total_count, 2) if total_count > 0 else 0

    def __str__(self):
        average_hw_grade = self.average_grade()
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)

        if not finished_courses_str:
            finished_courses_str = ""

        return f"""
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {average_hw_grade}
Курсы в процессе изучения: {courses_in_progress_str}
Завершенные курсы: {finished_courses_str}
"""


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"""
Имя: {self.name}
Фамилия: {self.surname}
"""


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if not self.grades:
            return 0

        total_sum = sum(sum(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())

        return round(total_sum / total_count, 2)

    def __str__(self):
        average_lecturer_grade = self.average_grade()

        return f"""
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {average_lecturer_grade}
"""


def calculate_student_average_grade(students, course):
    total_sum = 0
    total_count = 0

    for student in students:
        if course in student.grades:
            total_sum += sum(student.grades[course])
            total_count += len(student.grades[course])

    if total_count == 0:
        return 0

    return round(total_sum / total_count, 2)


def calculate_lecturer_average_grade(lecturers, course):
    total_sum = 0
    total_count = 0

    for lecturer in lecturers:
        if course in lecturer.grades:
            total_sum += sum(lecturer.grades[course])
            total_count += len(lecturer.grades[course])

    if total_count == 0:
        return 0

    return round(total_sum / total_count, 2)


student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses.append('Введение в программирование')
student1.grades['Python'] = [9.9]

student2 = Student('Alice', 'Smith', 'female')
student2.courses_in_progress += ['Python']
student2.grades['Python'] = [10, 9]

student3 = Student('Bob', 'Johnson', 'male')
student3.courses_in_progress += ['Python']
student3.grades['Python'] = [8, 7]

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(student1, 'Python', 9.9)
cool_mentor.rate_hw(student1, 'Python', 9.9)
cool_mentor.rate_hw(student1, 'Python', 9.9)

cool_mentor.rate_hw(student2, 'Python', 10)
cool_mentor.rate_hw(student2, 'Python', 9)

cool_mentor.rate_hw(student3, 'Python', 8)
cool_mentor.rate_hw(student3, 'Python', 7)

some_lecturer1 = Lecturer('John', 'Doe')
some_lecturer1.courses_attached += ['Python']
some_lecturer1.grades['Python'] = [9, 10]

some_lecturer2 = Lecturer('Mike', 'Davis')
some_lecturer2.courses_attached += ['Python']
some_lecturer2.grades['Python'] = [7, 8]

print(cool_mentor)

print(some_lecturer1)
print(some_lecturer2)

print(student1)
print(student2)
print(student3)


print(f"\nСредняя оценка за домашние задания по курсу Python: {calculate_student_average_grade([student1, student2, student3], 'Python')}")
print(f"\nСредняя оценка за лекции по курсу Python: {calculate_lecturer_average_grade([some_lecturer1, some_lecturer2], 'Python')}")