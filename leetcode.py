def clearDigits(self, s: str) -> str:
    s_list = list(s)
    i = 1
    while i < len(s_list):
        if s_list[i].isdigit():
            del s_list[i]
            del s_list[i - 1]
            i = 1
        else:
            i += 1

    return ''.join(s_list)  