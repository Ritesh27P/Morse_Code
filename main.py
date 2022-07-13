from flask import Flask, render_template, request

# Dictionary representing the morse code chart
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
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

non_accept_value = ['!', '@', '#', '$', '%', '^', '&', '*', '+']

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    error = None
    if request.method == "POST":
        message = request.form.get('message')
        message = message.upper()
        cipher = ''
        for letter in message:
            if letter in non_accept_value:
                error = "letter not accepted in Morse Code"
                break
            elif letter != ' ':
                cipher += MORSE_CODE_DICT[letter] + ' '
            else:
                cipher += ' '
        return render_template('index.html', message=cipher, error=error)
    return render_template('index.html', message=" ", error=error)


if __name__ == "__main__":
    app.run(debug=True)
