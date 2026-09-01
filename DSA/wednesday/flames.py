name1 = input("Enter first name: ").lower().replace(" ", "")
name2 = input("Enter second name: ").lower().replace(" ", "")


count = {}

for char in name1:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
remaining = 0

for char in name2:
    if char in count and count[char] > 0:
        count[char] -= 1
    else:
        remaining += 1
remaining += sum(count.values())
print("Remaining count:", remaining)


flames = ["F", "L", "A", "M", "E", "S"]
index = 0
while len(flames) > 1:
    index = (index + remaining - 1) % len(flames)
    flames.pop(index)

result = flames[0]

if result == "F":
    print("Friends")
elif result == "L":
    print("Love")
elif result == "A":
    print("Affection")
elif result == "M":
    print("Marriage")
elif result == "E":
    print("Enemies")
else:
    print("Siblings")