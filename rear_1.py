class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = {}
        self.courses_in_progress = []
        self.grades = {}
        self.evaluates_lectures = []

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.evaluates_lectures and course in lecturer.teaches_the_course:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def av_gr(self):
        sum_gr = 0
        len_gr = 0
        for course in self.grades.values():
            sum_gr += sum(course)
            len_gr += len(course)

        average_grade = round(sum_gr / len_gr) if len_gr > 0 else 0
        return average_grade


    def set_evaluates_lectures(self, courses):
        self.evaluates_lectures = courses


    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.av_gr()} \nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.teaches_the_course = []
        self.grades = {}

    def av_gr(self):
        sum_gr = 0
        len_gr = 0
        for course in self.grades.values():
            sum_gr += sum(course)
            len_gr += len(course)

            average_grade = round(sum_gr / len_gr)
            return average_grade

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.av_gr()}"


class Rewiewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"


best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python', 'Git']
best_student.set_evaluates_lectures(['Python'])
best_student.finished_courses = ['Введение в программирование']
cool_mentor = Rewiewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

good_mentor_l = Lecturer('Some', 'Buddy')
good_mentor_l.teaches_the_course += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 8)
cool_mentor.rate_hw(best_student, 'Python', 10)
best_student.rate_lecturer(good_mentor_l, 'Python', 5)

print(cool_mentor)
print(good_mentor_l)
print(best_student)