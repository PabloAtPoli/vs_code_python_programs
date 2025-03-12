
# Composition example
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        # Composition: Car "owns" the Engine—when the Car is destroyed, so is its Engine.
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car is driving")

# Aggregation example
class Student:
    def __init__(self, name):
        self.name = name

class School:
    def __init__(self, name):
        self.name = name
        # Aggregation: School holds references to Student objects, but those Students can exist independently.
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        for s in self.students:
            print(f"Student: {s.name}")

# Example usage:
if __name__ == "__main__":
    # Composition in action
    car = Car()
    car.drive()

    # Aggregation in action
    school = School("Green Valley High")
    student1 = Student("Alice")
    student2 = Student("Bob")
    school.add_student(student1)
    school.add_student(student2)
    school.list_students()

    # destroy the school object
    del school

    # The students still exist
    print("Students still exist in spite of the school being destroyed:")
    print(student1.name)
    print(student2.name)
