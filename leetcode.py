def getEncryptedString(self, s: str, k: int) -> str:
    i = 0
    temps = ""
    while i < len(s):
        j = (i + k) % len(s)
        temps += s[j]
        i += 1

    return temps