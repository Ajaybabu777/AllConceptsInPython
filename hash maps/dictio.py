import pandas as nihar

employeeDict = {
    "employees": [
        {"id": 1, "name": "raghu", "designation": "CEO"},
        {"id": 2, "name": "ram", "designation": "Trainee"},
        {"id": 3, "name": "rajan", "designation": "Trainer"},
        {"id": 4, "name": "Urjit", "designation": "Intern"}
    ]
}

table = nihar.DataFrame(employeeDict["employees"])
print(table)