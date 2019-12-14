import hashlib


def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def check(s):
    file = open("password_file.txt", "r")
    read = file.readlines()

    for line in read:
        arr = line.split(",")
        user = arr[0]
        salt_value = arr[1]
        hashedpassfromarr = arr[2].replace('\n', '')
        newhash = concatinate(s, salt_value)
        newhash = hash_with_sha256(newhash)
        if newhash == hashedpassfromarr:
            print(user + " password is: " + s)
        file.close()


def revise(s, n):
    if(len(s) == n):
        # print(s)
        check(s)
        return
    for i in range(10):
        revise(s + str(i), n)


def concatinate(s, salt):
    return s + salt


def main():
    for n in range(3, 8):
        revise("", n)
    hex_dig = hash_with_sha256('This is how you hash a string with sha256')
    print(hex_dig)


main()
