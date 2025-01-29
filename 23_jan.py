import pandas as pd

data = {
    "department":["hr", 'it', "hr", "it", "finanace"],
    "employees":["alice", "bob", "charlie", "david", "eve"],
    "salary":[50000,4000,25000,800000,60000]
}

df = pd.DataFrame(data)

#group by department and calculate average salary
avg_salary =df.group.py("deparment")["salary"].mean()
print("average salary by department:")
print(avg_salary)