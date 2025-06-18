def average(grades):
    return sum(grades.values()) / len(grades)

class_B = {
    "j": 1,
    "e": 5,
    "n": 8,
    "o": 9
}

class_C = {
    "p": 40,
    "e": 35,
    "n": 30,
    "n": 25,
    "u": 20,
    "e": 15,
    "n": 10,
    "g": 5
}

print(f"Average for class B: {average(class_B)}")
print(f"Average for class C: {average(class_C)}")