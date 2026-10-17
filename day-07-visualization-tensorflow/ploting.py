# Matplot , Seaborn & Tensorflow

# 1. Matplot
print("Matplotlib")
import matplotlib.pyplot as plt

students = ["Ali", "Ahmed", "Sara", "Ayesha"]
marks = [85, 70, 90, 78]

plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()



# Seaborn

print("Seaborn")

import seaborn as sns
import matplotlib.pyplot as plt

students = ["Ali", "Ahmed", "Sara", "Ayesha"]
marks = [85, 70, 90, 78]

sns.barplot(x=students, y=marks)

plt.title("Student Marks Using Seaborn")
plt.show()


