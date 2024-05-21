def texto_a_morse(texto):
    codigo_morse = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': ' '
    }
    texto_morse = []
    for letra in texto.upper():
        if letra in codigo_morse:
            texto_morse.append(codigo_morse[letra])
        else:
            texto_morse.append(' ')
    return texto_morse

def escodigomorse(texto):
    return all(caracter in ['.', '-', ' '] for caracter in texto)

def morse_a_texto(morse):
    codigo_morse = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
        '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
        '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6',
        '--...': '7', '---..': '8', '----.': '9', '-----': '0', ' ': ' '
    }
    texto = []
    lista_morse = morse.split(' ')
    for morse_letras in lista_morse:
        if morse_letras in codigo_morse:
            texto.append(codigo_morse[morse_letras])
        else:
            texto.append(' ')
    return ''.join(texto).strip()

def cuenta_simbolos(morse_lista):
    puntos = sum(morse.count('.') for morse in morse_lista)
    rayas = sum(morse.count('-') for morse in morse_lista)
    return puntos, rayas

def transformar(texto):
    if escodigomorse(texto):
        resultado = morse_a_texto(texto)
        print(f"Texto: {resultado}")
        return resultado
    else:
        resultado_morse = texto_a_morse(texto)
        print(f"Codigo Morse: {' '.join(resultado_morse)}")
        return resultado_morse

PalabraFrase = input("Introduzca una palabra o frase: ")
vector_morse = transformar(PalabraFrase)
if isinstance(vector_morse, list):
    puntos, rayas = cuenta_simbolos(vector_morse)
    print(f"Vector Morse: {vector_morse}")
    print(f"Total Puntos: {puntos}, Total Rayas: {rayas}")

MorseCodigo = input("Introduzca el codigo morse: ")
CodigoaTexto = transformar(MorseCodigo)
print(f"Texto a Codigo Morse: {CodigoaTexto}")
