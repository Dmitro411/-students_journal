from crud import *

while True:
    print("1. Створити студента")
    print("2. Створити курс")
    print("3. Отримати всіх студентів")
    print("4. Отримати всі курси")
    print("5. Записати студента на курс")
    print("6. Отримати всі курси, на які записані студенти")
    print("7. Вийти")
    print("93. Упасть")
    
    choice = input("Виберіть дію: ")
    if choice == "1":
        name = input("Введіть ім'я студента: ")
        age = input("Введіть вік студента: ")
        major = input("Введіть спеціальність студента: ")
        create_student(name, age, major)
        print("Студент створений")
    elif choice == "7":
        break

cursor.close()
conn.close()