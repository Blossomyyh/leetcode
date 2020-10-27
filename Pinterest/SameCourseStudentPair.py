'''
print out all same lessons between diffrent pair of students


'''
test1 = [("1", "A"), ("2", "B"), ("5", "E"), ("1", "B"), ("2", "A"), ("2", "E")]
from collections import defaultdict
def sameCourseStudentPair(test):
    # dic
    students = set()
    dictionary = defaultdict(list)
    for person, course in test:
        dictionary[person].append(course)
        students.add(person)

    def sameCourse(listA, listB):
        same = []
        setA = set(listA)
        for i in listB:
            if i in setA:
                same.append(i)
        return same

    result = defaultdict(list)
    studentsList = list(students)
    for i in range(len(studentsList)):
        for j in range(i+1, len(studentsList)):
            listA = dictionary[studentsList[i]]
            listB = dictionary[studentsList[j]]
            result[(studentsList[i], studentsList[j])] = sameCourse(listA, listB)

    return result

print(sameCourseStudentPair(test1))