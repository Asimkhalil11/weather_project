import os

def file_read():
    folder_path = "weatherfiles"
    files = os.listdir(folder_path)
    rows = []

    for file_name in files:
        file_path = os.path.join(folder_path,file_name)
        with open(file_path, "r") as f:
            contents = f.read()

        for row in contents.split("\n")[1:-1]:
            rows.append(row)

    return rows

file_values = file_read()

temps = []
for row in file_values:
    temp = row.split(",")[1]
    if temp:
        temps.append(float(temp))

if temps:
    min_temp = min(temps)
    max_temp = max(temps)
    print("Minimum temperature:", min_temp)
    print("Maximum temperature:", max_temp)
else:
    print("No values found.")

