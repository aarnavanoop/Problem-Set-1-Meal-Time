def main():
    actual_time = input("What is the time?: ")


    if 7.00 <= convert(actual_time) <= 8.00:
        print("breakfast time")
    elif 12.00 <= convert(actual_time) <= 13.00:
        print("lunch time")
    elif 18.00 <= convert(actual_time) <= 19.00:
        print("dinner time")

def convert(time):
    x,y = time.split(":")
    x = float(x)
    y = float(y)/60
    return x + y


if __name__ == "__main__":
    main()