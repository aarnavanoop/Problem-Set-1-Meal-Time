def main():
    actual_time = input("What is the time?: ")
    if check(actual_time):
        check_12_hour(actual_time)
    else:
        check_24_hour(actual_time)

def check(x):
    if "a.m." in x or "p.m." in x:
        return True
    else:
        return False


def convert(time):
    x,y = time.split(":")
    x = float(x)
    y = float(y)/60
    return x + y


def check_24_hour(z):
    if 7.00 <= convert(z) <= 8.00:
        print("breakfast time")
    elif 12.00 <= convert(z) <= 13.00:
        print("lunch time")
    elif 18.00 <= convert(z) <= 19.00:
        print("dinner time")

def check_12_hour(y):
    if "a.m." in y:
        y = y.strip("a.m.")
        if 7.00 <= convert(y) <= 8.00:
            print("breakfast time")
    elif "p.m." in y:
        y = y.strip("p.m.")
        if 12.00 <= convert(y) <= 13.00:
            print("lunch time")
        elif 18.00 <= convert(y) <= 19.00:
            print("dinner time")
    else:
        pass




if __name__ == "__main__":
    main()