# inverter_string.py
def inverter_string(s):
    return s[::-1]

if __name__ == "__main__":
    import sys
    string = sys.argv[1]
    invertida = inverter_string(string)
    print(f"String invertida: {invertida}")
