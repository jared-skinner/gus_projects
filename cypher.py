class Cypher:
    def __init__(self):
        self.encode_dictionary = {
            "a": "m",
            "b": "t",
            "c": "s",
            "d": "f",
            "e": "l",
            "f": "c",
            "g": "u",
            "h": "k",
            "i": "a",
            "j": "y",
            "k": "g",
            "l": "w",
            "m": "j",
            "n": "b",
            "o": "o",
            "p": "q",
            "q": "n",
            "r": " ",
            "s": "e",
            "t": "v",
            "u": "z",
            "v": "x",
            "w": "d",
            "x": "i",
            "y": "h",
            "z": "p",
            " ": "r",            
        }

        self.decode_dictionary = {v: k for k, v in self.encode_dictionary.items()}
        

    def encode(self, message):
        output_message = ""
        for letter in message:
            output_message = output_message + self.encode_dictionary[letter]
        return output_message
    
    def decode(self, message):
        input_message = ""
        for letter in message:
            input_message = input_message + self.decode_dictionary[letter]
        return input_message  

def main():
    # input the message you want to encode

    options = input("encode or decode? ")

    if options == "encode":
        x = input("do you have a message? ")
        print(x)
        y = Cypher()
        new_message = y.encode(x)
        print(new_message)
    elif options == "decode":
        x = input("do you have a message? ")
        print(x)
        y = Cypher()
        new_message = y.decode(x)
        print(new_message)

if __name__ == "__main__":
    main()