FILE = "password.txt"


def save_wifi(name, password):
    f = open(FILE, "w+")
    f.write(name + ":" + password)
    f.close()


def get_wifi_password():
    try:
        f = open(FILE, "r")
        contents = f.read()
        data = contents.split(":")
        print(data)
        f.close()
        if len(data) > 1:
            return [data[0], data[1].replace("\n", "")]
        return ""
    except OSError:
        return ""
