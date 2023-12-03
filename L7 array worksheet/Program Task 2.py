data = [34, 12, 99, 54, 89, 6, 25, 80, 67]
min = data[0]
max = data[0]

for i in range(len(data)):
    if data[i] > max:
        max = data[i]
    elif data[i] < min:
        min = data[i]

print(min, max)