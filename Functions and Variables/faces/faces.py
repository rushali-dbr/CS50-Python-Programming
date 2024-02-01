def convert(msg):
    msg = msg.replace(':)', '🙂')
    msg = msg.replace(':(', '🙁')
    return msg

def main():
    userInput = input()
    print(convert(userInput))

main()
