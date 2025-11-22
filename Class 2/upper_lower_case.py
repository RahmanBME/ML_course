n=input("do you want to play the game [yes/no]"). lower()

if n=="yes":
    print("play the game")
else:
    print("exit)")


n=input("do you want to play the game [yes/no]"). upper()

if n=="YES":
    print("play the game")
else:
    print("exit)")

n2="Bangladesh"

print(n2.lower()) # all the letter will be lowered
print(n2.upper()) # all the letrer wil be upperd

#Remove whitespace from the text, strip() has to be used

n3="     Biomedical  Engineetring"

print(n3.strip())

# the function of the replace function

print(n3.replace("B","M")) # B will be replaced by M
# Function of split function

n4="I am abdur rahman and i am a student of department of biomedical engineering"

print(n4.split()) #each word will be given in a list



