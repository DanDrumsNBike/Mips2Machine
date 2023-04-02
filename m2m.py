def Converter():
    import time
    print("Please enter how many lines of code you want to convert.")
    lines = input()
    pcmax = int(lines)*4
    print(f"You want to convert {lines} lines, and your program counter is from 0 to {pcmax}\n")
    time.sleep(2)
    print(f"Please enter your {lines} lines of Mips code")
    print("please enter the register number, EX: $4 = $a0, $0 = $zero")
    count = 0
    code = []
    while count < int(lines):
        temp = input()
        code.append(temp)
        count = count + 1
    print(code)
    return
    pass

def codechecker(code):