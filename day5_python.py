# Creating a List

skills = ["Python", "HTML", "Git", "GitHub"]

print("My Skills:")
for skill in skills:
    print(skill)

print("\nTotal Skills:", len(skills))

# Add a new skill
skills.append("SQL")

print("\nUpdated Skills:")
for skill in skills:
    print(skill)