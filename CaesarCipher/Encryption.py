class Encryption:
    # abstraction: combined version of encode and decode
    def caesar(self, text, shift, type):
        coded = ""
        bounds = 26
        if type == "decode":
            shift *= -1
        else:
            bounds *= -1
        for ch in text:
            asc = ord(ch)
            if (97 <= asc and asc <= 122) or (65 <= asc and asc <= 90):
                asc += shift
                if (asc < 65) or asc > 122 or (asc > 90 and asc < 97):
                    asc += bounds
            coded += chr(asc)
        return coded

        return code
    def encode(self, s, shift) -> str:
        coded = ""
        for cur in s:
            asc = ord(cur)
            if (97 <= asc and asc <= 122) or (65 <= asc and asc <= 90):
                asc += shift
                if (asc > 122) or (asc > 90 and asc < 97):
                    asc -= 26
            coded += chr(asc)
        return coded

    def decode(self, s, shift) -> str:
        coded = ""
        for cur in s:
            asc = ord(cur)
            if (97 <= asc and asc <= 122)  or (65 <= asc and asc <= 90):
                asc -= shift
                if (asc < 97 and asc > 90) or (asc < 65):
                    asc += 26
            coded += chr(asc)
        return coded

encryption = Encryption()
type = input("Type encode to encrypt and decode to decrypt:\n")
word = input("Enter the word to code:\n")
shift = int(input("Enter the shift number:\n"))

if type == "encode":
    print(encryption.encode(word, shift))
elif type == "decode":
    print(encryption.decode(word, shift))
else:
    print("Incorrect input:(")
# ALT version
# if type == 'encode' or type == 'decode':
#     print(encryption.caesar(word, shift, type))