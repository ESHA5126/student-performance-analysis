import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/student_performance.csv")
print("Shape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())
print("\nSummary:\n", df.describe())

plt.figure(figsize=(8,5))
plt.scatter(df["study_hours"], df["final_score"], alpha=0.65)
plt.xlabel("Study Hours per Week")
plt.ylabel("Final Score")
plt.title("Study Hours vs Final Score")
plt.tight_layout()
plt.savefig("study_hours_vs_score.png", dpi=150)
plt.show()

attendance = df.groupby("attendance_rate")["final_score"].mean()
plt.figure(figsize=(8,5))
plt.plot(attendance.index, attendance.values, marker="o")
plt.xlabel("Attendance Rate (%)")
plt.ylabel("Average Final Score")
plt.title("Attendance vs Average Final Score")
plt.tight_layout()
plt.savefig("attendance_vs_score.png", dpi=150)
plt.show()

print("\nAverage score:", round(df["final_score"].mean(), 2))
print("Study/score correlation:", round(df["study_hours"].corr(df["final_score"]), 2))
print("Attendance/score correlation:", round(df["attendance_rate"].corr(df["final_score"]), 2))
