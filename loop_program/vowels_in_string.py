string = input("enter the sentence: ")
count = 0
string = string.lower()
for ch in string:
    if ch in "aeiou":
        count= count + 1


print(f"Number of Vowels= {count}")