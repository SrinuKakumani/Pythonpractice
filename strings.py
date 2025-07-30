#Get the character at position 7
a = "Hello, World!"
print(a[7])

#loop through the characters in a string
for a in "apple":
    print(a)

#To get the length of a string
a = "Hello, World!"
print(len(a))


#To check if a certain phrase or character is present in a string
x = "This is Srinu Kakumani from Kandukur"
print("free" in x)

# To specify the start index and the end index
x = "Hello, World!"
print(x[3:5]);

# TO start from the beginning
x="This is Srinu Kakumani from Kandukur";
print(x[:7]);

# To end at the end
x = "Hi there, how are you doing today?";
print(x[7:]);

# To convert the text to uppercase 
x = "What is your ambition in life?";
print(x.upper());

# To convert the text to lowercase
x="WHO IS YOUR INSPIRATION IN LIFE?";
print(x.lower());

# To remove whitespace from the beginning and the end of a string
x = "           Hi friends, what's up?            ";
print(x.strip());

# To replace a string with another string
x = "Hi this is Drinu Kakumani from Kandukur";
print(x.replace("Drinu", "Srinu"));

# To concat two strings
x = "Srinu";
y = " Kakumani";
z = x + y;
print(z);

# To add space betwwen two strings while concatenating
x = "Srinu";
y = "Kakumani";
z = x + "    " + y;
print(z);

# To insert an illegal character in a string
x = "This is \"SrinuKakumani\" from Kandukur";
print(x);


