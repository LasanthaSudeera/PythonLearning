"""
    Pickle can be used to serialize files
    """
import pickle
import student

# Serializing
f = open("student.dat", "wb")
s = student.Student(123, "Jane Doe", 23)
pickle.dump(s, f)
f.close()

# Deserializing
f = open("student.dat", "rb")
s = pickle.load(f)
s.display()
f.close()
