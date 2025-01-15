# These are the alphabet that will be used in this project:
lowercase_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

lowercase_alphabet_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
lowercase_alphabet_2 = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

uppercase_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

uppercase_alphabet_1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
uppercase_alphabet_2 = ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Ask user to create the amount of shift
n_shift = int(input('Type the first number of shift you want: '))
m_shift = int(input('Type the second number of shift you want: '))

# Create a list and add all the text in raw_text.txt
text_list = []
with open('raw_text.txt','r') as raw_text:
    text = raw_text.read()
    for letter in text:
        text_list.append(letter)



#Create a function for encryption
def encryption():
    #Loop through list
    for each in text_list:
        # Create the condition to find out whether the letter is the lowercase letter or the uppercase letter
        # for the next steps
        if each in lowercase_alphabet:
           # These if statements will check whether the letter belongs to the first half of the alphabet or the second:
           if each in lowercase_alphabet_1:
               # Saving the letter into a variable:
               position = lowercase_alphabet_1.index(each)
               # Calculate the shift based on the rules given in the question:
               shift = n_shift * m_shift
               # Next, calculating the shift:
               changed_position = position + shift
               # The result of this calculation will return the position of the letter after decrypted:
               new_position = changed_position % len(lowercase_alphabet_1)
               # Open the encrypted file to add the new letter into it:
               with open('encrypted_text.txt', 'a') as encrypted_text:
                   encrypted_text.write(lowercase_alphabet_1[new_position])
           # These are the procedures for the lowercase letter belongings to the second half
           elif each in lowercase_alphabet_2:
                position = lowercase_alphabet_2.index(each)
                shift = n_shift + m_shift
                changed_position = position - shift
                new_position = changed_position % len(lowercase_alphabet_2)
                with open('encrypted_text.txt', 'a') as encrypted_text:
                     encrypted_text.write(lowercase_alphabet_2[new_position])
        # These are procedures for the uppercase letters
        elif each in uppercase_alphabet:
            # First half of uppercase alphabet:
            if each in uppercase_alphabet_1:
               position = uppercase_alphabet_1.index(each)
               shift = n_shift
               changed_position = position - shift
               new_position = changed_position % len(uppercase_alphabet_1)
               with open('encrypted_text.txt', 'a') as encrypted_text:
                    encrypted_text.write(uppercase_alphabet_1[new_position])
            # Second half of uppercase alphabet:
            elif each in uppercase_alphabet_2:
                position = uppercase_alphabet_2.index(each)
                shift = n_shift ** 2
                changed_position = position + shift
                new_position = changed_position % len(uppercase_alphabet_2)
                with open('encrypted_text.txt', 'a') as encrypted_text:
                    encrypted_text.write(uppercase_alphabet_2[new_position])
        # If it is special character or a black, skip it by adding it without changing:
        else:
            with open('encrypted_text.txt', 'a') as encrypted_text:
                encrypted_text.write(each)
encryption()

# Create a list which will hold the encrypted_text to decrypt them:
decrypted_texts = []
with open('encrypted_text.txt', 'r') as encrypted_text:
    encryption = encrypted_text.read()
    for letter in encryption:
        decrypted_texts.append(letter)

# The codes for decryption is the same with encryption, only the difference is changing to the opposite sign compared to
# encryption function to return the letter index into its original index
def decryption():
    for each in decrypted_texts:
        if each in lowercase_alphabet:
           if each in lowercase_alphabet_1:
               position = lowercase_alphabet_1.index(each)
               shift = n_shift * m_shift
               changed_position = position - shift
               new_position = changed_position % len(lowercase_alphabet_1)
               with open('decrypted_text.txt', 'a') as decrypted_text:
                   decrypted_text.write(lowercase_alphabet_1[new_position])
           elif each in lowercase_alphabet_2:
                position = lowercase_alphabet_2.index(each)
                shift = n_shift + m_shift
                changed_position = position + shift
                new_position = changed_position % len(lowercase_alphabet_2)
                with open('decrypted_text.txt', 'a') as decrypted_text:
                     decrypted_text.write(lowercase_alphabet_2[new_position])
        elif each in uppercase_alphabet:
            if each in uppercase_alphabet_1:
               position = uppercase_alphabet_1.index(each)
               shift = n_shift
               changed_position = position + shift
               new_position = changed_position % len(uppercase_alphabet_1)
               with open('decrypted_text.txt', 'a') as decrypted_text:
                    decrypted_text.write(uppercase_alphabet_1[new_position])

            elif each in uppercase_alphabet_2:
                position = uppercase_alphabet_2.index(each)
                shift = n_shift ** 2
                changed_position = position - shift
                new_position = changed_position % len(uppercase_alphabet_2)
                with open('decrypted_text.txt', 'a') as decrypted_text:
                    decrypted_text.write(uppercase_alphabet_2[new_position])
        else:
            with open('decrypted_text.txt', 'a') as decrypted_text:
                decrypted_text.write(each)
decryption()

# Delete the encrypted text for the next run
# with open('encrypted_text.txt', 'w') as encrypted_text:
#     encrypted_text.write('')
# with open('decrypted_text.txt', 'w') as decrypted_text:
#     decrypted_text.write('')
