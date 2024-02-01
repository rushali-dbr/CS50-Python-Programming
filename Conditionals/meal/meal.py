def main():
    time = input("What time is it? ")
    convertedTime = convert(time)
    if 7.0 <= convertedTime <= 8.0:
        print("breakfast time")
    elif 12.0 <= convertedTime <= 13.0:
        print("lunch time")
    elif 18.0 <= convertedTime <= 19.0:
        print("dinner time")

def convert(time):
    idx = time.find(":")
    hour = float(time[0:idx])
    mint = float(time[idx+1:])
    mint = round(mint/60,2)
    return hour+mint


if __name__ == "__main__":
    main()
