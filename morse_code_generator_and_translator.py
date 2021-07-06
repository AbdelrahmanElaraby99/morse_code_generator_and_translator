# morse code dictionary constant
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ' ': '/'}
# list out keys and values separately
KEY_LIST = list(MORSE_CODE_DICT.keys())
VAL_LIST = list(MORSE_CODE_DICT.values())
# creating the reverse morse code dictionary
MORSE_REVERSE_DICT = {VAL_LIST[index]: KEY_LIST[index] for index in range(len(KEY_LIST))}

# program's main loop
while True:
    choice = input("Enter 's' to input a string\nEnter 'm' to input morse code\nEnter 'off' to exit: ")
    if choice == "off":
        break
    elif choice == "s":
        string = input("Enter your string: ")
        string = string.upper()
        string_list = list(string)
        morse_list = [MORSE_CODE_DICT[char] for char in string_list]
        morse_string = " ".join(morse_list)
        print(morse_string)
    elif choice == "m":
        morse = input("Enter your morse code\n(letters separated by space, and words by ' / '): ")
        morse_letters = morse.split(" ")
        alphabet_letters = [MORSE_REVERSE_DICT[letter] for letter in morse_letters]
        string = "".join(alphabet_letters)
        print(string)
