
inputKalimat =input('maskkan kalimatmu disini :')

def getReverse(kalimat):
    outputan=''
    listkata=inputKalimat.split(' ')
    for kata in listkata:
        outputan += kata[::-1] + ' '
    return outputan
    print(f'hasil balikan :{outputan}')
print(getReverse(inputKalimat))



'''
Abjad = {'A' : '.-',
'B':'-...',
'C' : '-.-.','D': '-..','E':'.','F':'..-.',
'G':'--.','H':'....','I':'..','J':'.---','K':'-.-',
'L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-',
'R':'.-.','S':'...','T':'-','U':'..-','V':'...-',
'W':'.--','X':'-..-','Y':'-.--','Z':'--..',' ':'|','1':'.----','2':'..---',
'3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..',
'9':'----.','0':'-----' }

x= input('masukkan kata/kalimat:')
y= list(x)


def kodeMorse(x):
    morseCode=''
    for i in x:
        morseCode += Abjad[i.upper()]
        # morseCode +='/'
    return morseCode
    
print(kodeMorse(x))
'''
'''
# caesar cipher
alpabet = 'abcdefghijklmnopqrstuvwxyz'
inputan= input('masukkan pesanmu :')
loncatan = int(input('masukkan jumlah loncatan :'))
outputan =''
for i in range(len(inputan)):
    karakter = inputan[i]
    # print(karakter)
    location = alpabet.find(karakter)
    newLocation= (location+loncatan)%26
    outputan += alpabet[newLocation]
print(outputan)
'''