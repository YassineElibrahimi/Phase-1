# 1. BASIC VARIABLES
age = 22
temperature = 17.4
name = "Alex"
is_student = True

print("Basic variables:")
print(f"Age: {age}, Type: {type(age)}")
print(f"Temperature: {temperature}, Type: {type(temperature)}")
print(f"Name: {name}, Type: {type(name)}")
print(f"Is student: {is_student}, Type: {type(is_student)}")
print()

# 2. LISTS
fruits = ["apple", "banana", "orange", "grape"]
print("Fruits list:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Sliced (first two):", fruits[:2])
print()

# 3. LIST OPERATIONS
fruits.append("mango")
print("After adding mango:", fruits)

fruits[1] = "blueberry"
print("After changing index 1:", fruits)

print("Length of list:", len(fruits))
print()

# 4. PRACTICE: STUDENT GRADES
grades = [85, 92, 78, 90, 88]
print("Student grades:", grades)
print("Highest grade:", max(grades))
print("Lowest grade:", min(grades))
print("Average grade:", sum(grades) / len(grades))
print()

# 5. CHALLENGE: TEMPERATURE CONVERTER
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Try changing celsius to 0, 100, -40