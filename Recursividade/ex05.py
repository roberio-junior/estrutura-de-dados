def inverter_string(text: str) -> str:
    if len(text) == 0:
        return ""
    return text[-1] + inverter_string(text[:-1])

string = "Robério"
invertida = inverter_string(string)

print(f"A inversão da string '{string}' é '{invertida}'.")
