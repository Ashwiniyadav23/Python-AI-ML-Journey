# for loop

num = 10
sum = 0
for i in range(num) :
    sum+= i
print(sum)

# while loop

s = 3
i = 1
sum = 0
while i <= s:
    sum+= i
    i = i + 1
print(sum)


# do while loop

count = 0

while True:
    print("Count:", count)   # runs first
    count += 1

    if count >= 3:           # condition checked after
        break