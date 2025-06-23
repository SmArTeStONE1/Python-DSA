import matplotlib.pyplot as plt

# Marks obtained by students in different subjects in both Line and Bar chart
subjects = ['Math', 'Science', 'English', 'History', 'Art']
marks = [85, 90, 78, 88, 92]
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.bar(subjects, marks, color=['#FF5733', '#33FF57','#3357FF', '#F333FF', '#33FFF5'])
plt.title("Marks in Different Subjects - Bar Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.subplot(1, 2, 2)
plt.plot(subjects, marks, marker='o', color='blue')
plt.title("Marks in Different Subjects - Line Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()
