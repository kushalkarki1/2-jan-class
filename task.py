# # main, even, odd, duplicate
# # take user input 15 times (int)
# main = []
# even = []
# odd = []
# duplicate = []

# # input = 10, 13, 16, 17, 20, 19, 78, 89, 16, 89, 90, 100, 12, 14, 7

# # main = [10, 13, 16, 17, 20, 19, 78, 89, 16, 89, 90, 100, 12, 14, 7]
# # even = [10, 16, 20, 78, 90, 100, 12, 14,]
# # odd = [13, 17, 19, 89, 7]
# # duplicate = [16, 89, ]

# for i in range(15):
#     num = int(input("Enter any number: "))
#     if num in main:
#         duplicate.append(num)
#     else:
#         if num % 2 == 0:
#             even.append(num)
#         else:
#             odd.append(num)
#     main.append(num)

# print(main)
# print(even)
# print(odd)
# print(duplicate)


# colors = ["yellow", "red", "orange", "blue", "violet", "red", "white"]
# colors_to_remove = ["red", "violet"]
# # ["yellow", "orange", "blue", "white"]


# fruits = ["apple", "guava", "grapes", "banana", "orange"]
# # replace "guava" and "grapes" with watermelon
# # ["apple", "watermelon", "banana", "orange"]


profile = {
    "name": "Ram",
    "gender": "Male",
    "education":[
        {"college": "ABC College", "level": "+2"},
        {"college": "XYZ College", "level": "Bachelor"},
    ],
    "addresses":[
        {
            "temporary": {
                "ward": 1,
                "city": "Kathmandu",
            },
            "permanent": {
                "ward": 2,
                "city": "Kavre",
            }
        }
    ]
}

# print(f"Name: {profile.get('name')}")
# print(f"Gender: {profile.get('gender')}")

# educations = profile.get("education")
# for education in educations:
#     print(f"College: {education.get('college')} and Level: {education.get('level')}")

# addresses = profile.get("addresses")
# for address in addresses:
#     for key, val in address.items():
#         print(key, val.get('ward'))


students = {
    "count": 2,
    "data": [
        {
            "name": "Ram",
            "address": "Tinknune",
            "course": "Python Django",
            "attendance": [
                {
                    "month": "January",
                    "total_working_days": 25,
                    "present": 24,
                    "absent": 1,
                    "leave": 0,
                },
                {
                    "month": "February",
                    "total_working_days": 28,
                    "present": 20,
                    "absent": 2,
                    "leave": 6,
                }
            ]
        },
        {
            "name": "Hari",
            "address": "Tinknune",
            "course": "Python Django",
            "attendance": [
                {
                    "month": "January",
                    "total_working_days": 25,
                    "present": 23,
                    "absent": 1,
                    "leave": 1,
                },
                {
                    "month": "February",
                    "total_working_days": 28,
                    "present": 27,
                    "absent": 0,
                    "leave": 1,
                }
            ]
        }
    ]
}

students = students.get("data")
for student in students:
    student_attendance = student.get("attendance")
    for attendance in student_attendance:
        print(attendance.get("month"), attendance.get("total_working_days"))