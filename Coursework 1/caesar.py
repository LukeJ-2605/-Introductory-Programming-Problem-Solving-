# Coursework Assessment 1
# Name: Luke Johnson
# Student No: 2222880

# A Caesar Cipher Program
import os.path
'''This function prints a welcoming message at the start of the program.'''
def welcome(): 
    print('Welcome to the Caesar Cipher')
    print('This program encrypts and decrypts text with the Caesar Cipher.')
    return

'''This function asks the user for input for the mode, message and shift, and returns it. '''
def enter_message(): 
    mode = ''
    message = ''
    shift = 0
    while True:
        mode = input('Would you like to encrypt (e) or decrypt (d): ')
        while mode != 'e' and mode != 'd':
            print('Invalid Mode')
            mode = input('Would you like to encrypt (e) or decrypt (d): ')
        if mode == 'e':
            message = input ('What message would you like to encrypt: ')
        elif mode == 'd':
                message = input('What message would you like to decrypt: ')
        shift = input('What is the shift number: ')
        while shift.isdigit() == False:
            print('Invalid Shift')
            shift = input('What is the shift number: ')
        if shift.isdigit():
            shift = int(shift)     
        return (mode, message, shift)
    
'''This function encrypts the user's message, based on the user's chosen shift and returns it.
This is done by using an alphabet and searching for each character in the message before adding the shift.'''
def encrypt(message,shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted_message = ''
    message = str.upper(message)
    for c in message:
        if c in alphabet:
            i = alphabet.index(c)
            j = (i + shift) % 26
            encrypted_message = encrypted_message + alphabet[j]
        else:
            encrypted_message = encrypted_message + c
    return encrypted_message

'''This function takes the user's message and shift and decrypts it. It uses the alphabet to search
for characters in the message and minuses the shift from those characters to return the decrypted message.'''
def decrypt(message,shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decrypted_message = ''
    message = str.upper(message)
    for c in message:
        if c in alphabet:
            i = alphabet.index(c)
            j = (26 + i - shift) % 26
            decrypted_message = decrypted_message + alphabet[j]
        else:
            decrypted_message = decrypted_message + c
    return decrypted_message
      
'''This function takes the user's filname, mode and shift, and either encrypts or decrypts the text in the file,
based on the selected mode and shift, then adds it to a list. It then returns the list.'''
def process_file(filename, mode, shift):
    list_messages = []  
    file = open(filename, 'r')
    if mode == 'e':
        for line in file:
            line = encrypt(line, shift)
            list_messages.append(line)
    else:
        for line in file:
            line = decrypt(line, shift)
            list_messages.append(line)
    file.close()
    return list_messages

'''This function takes the information from the list, and writes it onto a new file called 'results.txt'. The
information is written to the new text file on multiple lines so that each message is on a seperate line'''
def write_messages(lines):
    file = open('results.txt','w')
    for line in lines:
        file.write(line + '\n')
    file.close()
    print('Output written to results.txt')
    return

'''This function checks that there is a file by the name given by the user.'''
def is_file(filename):
    return os.path.exists(filename)

'''This function is similiar to the enter_message function. However, it also asks for a file name as input
and allows the user to encrypt or decrypt messages that are stored on a text file. The user can also still
use the console to encrypt or decrypt messages they input into the program.'''
def message_or_file():
    mode = ''
    filename = None
    message = None
    shift = 0
    while True:
        mode = input('Would you like to encrypt (e) or decrypt (d): ')
        while mode != 'e' and mode != 'd':
            print('Invalid Mode')
            mode = input('Would you like to encrypt (e) or decrypt (d): ')
        if mode == 'e':
            source = input('Would you like to read from a file (f) or the console (c)? ')
        if mode == 'd':
            source = input('Would you like to read from a file (f) or the console (c)? ')
        while source != 'f' and source != 'c':
            print('Invalid Source')
            source = input('Would you like to read from a file (f) or the console (c)? ')
        if source == 'f':
             filename= input('Enter a filename: ')
             while is_file(filename) == False:
                           print('Invalid Filename')
                           filename = input ('Enter a filename: ')
        if source == 'c' and mode == 'e':
            message = input ('What message would you like to encrypt: ')
        elif source == 'c' and mode == 'd':
            message = input ('What message would you like to decrypt: ')
            
        shift = input('What is the shift number: ')
        while shift.isdigit() == False:
            print('Invalid Shift')
            shift = input('What is the shift number: ')
        if shift.isdigit():
            shift = int(shift)
        return (mode, message, filename, shift)
    

'''This function is where all the other functions are placed in order for them to run. Each function is
placed within a loop and at the end of the program, the user is asked if they would like to encrypt or
decrypt another message. If the user says yes, the program continues, if the user says no a goodbye
message is displayed and the program closes.'''
def main():
    welcome() 
    while True:
        mode, message, filename, source, shift = message_or_file()
        if source == 'f' and is_file(filename) == True:
            lines = process_file(filename, mode, shift)
            write_messages(lines)
        elif source == 'c' and mode == 'e':
            encrypted_message = encrypt(message, shift)
            print(encrypted_message)
        elif source == 'c' and mode == 'd':
            decrypted_message = decrypt(message, shift)
            print(decrypted_message)
        run_again = input('Would you like to encrypt or decrypt another message? (y/n):')
        while run_again != 'y' and run_again != 'n':
            print('Invalid Answer')
            run_again = input('Would you like to encrypt or decrypt another message? (y/n):')
        if run_again == 'y':
            continue
        if run_again == 'n':
            print('Thanks for using the caeser cipher, goodbye!')
            break
            
        
        return


if __name__ == '__main__':
    main()
