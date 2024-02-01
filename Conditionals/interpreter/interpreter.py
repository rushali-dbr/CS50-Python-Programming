def interpreter(x, y, z):
    match y:
        case "+":
            return float(x+z)
        case "-":
            return float(x-z)
        case "*":
            return float(x*z)
        case "/":
            return float(x/z)

def main():
    exp = input("Expression: ").strip()
    spaceIdx = exp.find(" ");
    x = int(exp[0:spaceIdx])
    y = exp[spaceIdx+1]
    z = int(exp[spaceIdx+3:])
    print(interpreter(x, y, z))

main()

