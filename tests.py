print('A')

print('..A..\n.B.B.\nC...C\n')

print('..A..\n.B.B.\nC...C\n.B.B.\n..A..')

# Data Input - One Character
import string


def rows(char):
    alphabet = string.ascii_uppercase
    index = alphabet.index(char)
    # Develop an Algorithm for char 'Z'
    combined_alphabet = list(alphabet[0:index]) + list(alphabet[index::-1])

    # Create the characters on each line
    for char in combined_alphabet:
        i = combined_alphabet.index(char)
        j = alphabet.index(char)
        l = len(combined_alphabet)
        
        if char == "A":
            whitespace = "." * ((l - 1)//2)
            combined_alphabet[i] = whitespace + char + whitespace
        if char != "A":
            mspace = j
            ltspace = "." * (l-2)//2)
            combined_alphabet[i] = ltspace + char + mspace + char + ltspace
    
   for i in range(index * 2 + 1):
            if i == index - countrow or i == index + countrow: 
# Data Store  - List of lines (Type String)
diamond_list = ['..A..','.B.B.','C...C','.B.B.','..A..']

# Data Processing - Add a newline on each line
diamond = "\n".join(diamond_list)

# Data Output - Printing to Console/stdout
print(diamond)
