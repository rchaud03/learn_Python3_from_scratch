listA = ["Ronald", "Pouchon", "Maxime"]
listB = ["Fabiola", "Cindy", "Sherly"]

for man, woman in zip(listA, listB):
    print(man + " & " + woman)

print("-" *20)

listC = ["Dre", "Cornelius", "Ronald"]
listD = ["Shivone", "Giovani", "Jia", "Tiffany M"]

for man2, woman2 in zip(listC, listD):
    print(man2 + " & " + woman2)