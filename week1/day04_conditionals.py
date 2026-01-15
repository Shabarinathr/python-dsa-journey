# basic if Statement 
# age = 20

# if age>=18:
#  print("you are adult")


 # if/else statement

# marks = 30

# if marks>=40:
#     print("Passed")
# else:
#     print("Failed")

# Excercise 1
# Grade Checker

# marks = 50
# pass_marks = 40

# if marks>pass_marks:
#     print("Passed")
# else:
#     print("Failed")


# Excercise 2
# TCS Eligiblity test

# gpa = 7.0
# backlogs = 1
# coding_test = 70

# if gpa>=7.0 and backlogs==0 and coding_test>=75:
#     print("TCS Ninja Eligible")
#     print("Prepare for interview")
# else:
#     print("Not Eligible yet")
#     print("Work on:", end=" ")
#     if gpa<7.0:
#         print("GPA",end=" ")
#     if backlogs>0:
#         print("Backlogs",end=" ")
#     if coding_test<75:
#         print("Coding",end=" ")

# elif (multiple choices)

# marks = 50
# if marks >= 90:
#     print("A grade")
# elif marks >= 80:
#     print("B grade")
# elif marks >= 70:
#     print("C grade")
# elif marks >= 60:
#     print("D grade")
# else :
#     print("Need Improvement")

# Unifeeder Task Checker

task_complexity=7
deadline_days=3
team_help_available=True

if task_complexity >= 8 or deadline_days <= 2:
    print("High Priority")
    print("Ask senior")
elif team_help_available:
    print("Medium Priority")
    print("Work with team")
else:
    print("Low Priority")
    print("Completed by EOD")