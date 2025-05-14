class Encryptor:
    def __init__(self, shift: int):
        self.shift = shift

    def encrypt(self, plaintext: str) -> str:
        ans = ""
        for ch in plaintext:
            if ch == " ":
                ans += " "
            elif ch.isupper():
                ans += chr((ord(ch) + self.shift - 65) % 26 + 65)
            elif ch.islower():
                ans += chr((ord(ch) + self.shift - 97) % 26 + 97)
            else:
                ans += ch
        return ans
