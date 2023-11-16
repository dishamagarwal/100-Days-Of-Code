class Encryption:
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