morse_code_eng = {'.-': 'A', '-...': 'B', '-.-.': 'C',
    '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I',
    '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U',
    '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z'}

lst_consonants_eng = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
                      'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
lst_vowels_eng = ['A', 'E', 'I', 'O', 'U']

morse_code_ru = {".-": "А", "-...": "Б", ".--": "В",
    "--.": "Г", "-..": "Д", ".": "Е", "...-": "Ж",
    "--..": "З", "..": "И", ".---": "Й", "-.-": "К",
    ".-..": "Л", "--": "М", "-.": "Н", "---": "О",
    ".--.": "П", ".-.": "Р", "...": "С", "-": "Т",
    "..-": "У", "..-.": "Ф", "....": "Х", "-.-.": "Ц",
    "---.": "Ч", "----": "Ш", "--.-": "Щ", ".--.-.": "Ъ",
    "-.--": "Ы", "-..-": "Ь", "..-..": "Э", "..--": "Ю", ".-.-": "Я"}

lst_consonants_ru = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'К', 'Л', 'М', 'Н', 'П',
                      'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ']
lst_vowels_ru = ['А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']


class MorseMsg:
    """
    A class for decoding messages from Morse code
    """
    def __init__(self, message):
        """
        The method that defines the instance messages in morse code
        :param message: a string that contains morse code
        """
        self.message = message

    def eng_decode(self):
        """
        A method that decodes a message into English
        :return: a string containing the decoded message
        """
        msg = []
        morse_code = self.message.split('  ')
        for word_code in morse_code:
            word = []
            for sign_code in word_code.split():
                letter = morse_code_eng[sign_code]
                word.append(letter)
            new_word = ''.join(word)
            msg.append(new_word)
        return ' '.join(msg)

    def ru_decode(self):
        """
        A method that decodes a message into Russian
        :return: a string containing the decoded message
        """
        msg = []
        morse_code = self.message.split('  ')
        for word_code in morse_code:
            word = []
            for sign_code in word_code.split():
                letter = morse_code_ru[sign_code]
                word.append(letter)
            new_word = ''.join(word)
            msg.append(new_word)
        return ' '.join(msg)

    def get_vowels(self, lang):
        """
        a method that returns vowel messages
        :param lang: a string containing the required language
        :return: a list containing all the vowels in the order they occur
        """
        vowels = []
        if lang == 'ru':
            for letter in self.ru_decode():
                if letter in lst_vowels_ru:
                    vowels.append(letter)
        if lang == 'eng':
            for letter in self.eng_decode():
                if letter in lst_vowels_eng:
                    vowels.append(letter)
        return vowels

    def get_consonants(self, lang):
        """
        A method that returns consonants from a message
        :param lang: a string containing the required language
        :return: a list containing all consonants in the order they occur
        """
        consonants = []
        if lang == 'ru':
            for letter in self.ru_decode():
                if letter in lst_consonants_ru:
                    consonants.append(letter)
        if lang == 'eng':
            for letter in self.eng_decode():
                if letter in lst_consonants_eng:
                    consonants.append(letter)
        return consonants

    def __str__(self):
        """
        The method outputs a string with a list of consonants and vowels
        :return: string with a list of consonants and vowels
        """
        return f'Consonant letters from a sentence in English: {self.get_consonants("eng")} \n' \
               f'Vowel letters from a sentence in English: {self.get_vowels("eng")}'

    def __repr__(self):
        """
        The method outputs a string with a list of consonants and vowels
        :return: string with a list of consonants and vowels
        """
        return self.__str__()
