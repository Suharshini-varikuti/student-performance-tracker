import pandas as pd
import matplotlib.pyplot as plt

# Load CSV Data
df = pd.read_csv("student_scores.csv")

# Print student data
print("Student Data:\n", df)

# Calculate average marks
df['Average'] = df[['Maths', 'Science', 'English']].mean(axis=1)

# Identify topper
topper = df[df['Average'] == df['Average'].max()]
print("\nTopper:\n", topper[['Name', 'Average']])

# Pass/fail logic
df['Result'] = df['Average'].apply(lambda x: 'Pass' if x >= 35 else 'Fail')

# Summary
print("\nPerformance Summary:\n", df[['Name', 'Average', 'Result']])
# Plotting marks
df.plot(x='Name', y=['Maths', 'Science', 'English'], kind='bar')
plt.title("Subject-wise Performance")
plt.ylabel("Marks")
plt.xlabel("Students")
plt.legend(loc='lower right')
plt.tight_layout()
plt.show()