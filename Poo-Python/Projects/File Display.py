def main():
    file = open("numbers.txt","r")
    numbers = file.read()
    file.close()
    print(numbers)

main()
