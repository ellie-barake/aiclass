# creating dictionary
student_grade={'ellie':70,'fils':80,'gift':85,'pixie':90,'barake':95,'fisto':73,'jade':83,'eren':75,'jake':94,'foe':69,'jike':0}
average_grade=sum(student_grade.values())/len(student_grade)
print(f"the average grade is:{average_grade}")

#highest_score
highest_score= max(student_grade.values())
for student, score in student_grade.items():
    if score ==highest_score:
        print(f"highest_score:{student}:with:{highest_score}")
# updating_grade
student_grade['ellie']= 92
print(student_grade)
# student with grade >80
        