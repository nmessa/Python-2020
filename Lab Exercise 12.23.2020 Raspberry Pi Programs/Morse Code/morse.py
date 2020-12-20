import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

def codeGen(s):
    output = ''
    s = s.lower()    #put string in lower case to reduce dictionary size
    for i in range(len(s)):
        if s[i] == '\n':
            output += '\n'
            continue
        output += convert(s[i])
        output += '   '
    print (output)
    for i in range(len(output)):
        if output[i] == '.':
            dot()
        if output[i] == '-':
            dash()
        if output[i] == ' ':
            time.sleep(0.1)

def convert(letter):
    #International Morse Code dictionary
    table = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.',
                 'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---',
                 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---',
                 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
                 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--',
                 'z':'--..', ' ':'       ', '1':'.----', '2':'..---',
                 '3':'...--', '4':'....-', '5':'.....', '6':'-....',
                 '7':'--...', '8':'---..', '9':'----.', '0':'-----'}
    if letter in table.keys():
        return table[letter]
    else:		#handle other characters where code does not exist in dictionary
        return ''     # 2 single quotes

def dot():
    GPIO.output(18, True)
    time.sleep(0.1)
    GPIO.output(18, False)
    time.sleep(0.1)

def dash():
    GPIO.output(18, True)
    time.sleep(1)
    GPIO.output(18, False)
    time.sleep(0.1)

phrase = raw_input("Enter a phrase: ")
codeGen(phrase)
