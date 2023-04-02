def Converter():
    lines = input()
    pcmax = int(lines) * 4
    code = []
    while len(code) < int(lines):
        code.append(input())
    print(code,pcmax)
    return
    pass

def codechecker(code): # make sure code is an actual valid line of code
    check = code.upper()
    check = check.replace(",","")
    check = check.split(" ")
    validlist = ['ADD', 'ADDI', 'ADDIU', 'ADDU', 'AND', 'ANDI', 'LUI', 'NOR', 'OR', 'ORI', 'SLT', 'SLTI', 'SLTIU', 'SLTU', 'SUB', 'SUBU', 'XOR', 'XORI',
                 'SLL', 'SLLV', 'SRA', 'SRAV', 'SRL', 'SRLV', 'DIV', 'DIVU', 'MFHI', 'MFLO', 'MTHI', 'MTLO', 'MULT', 'MULTU', 'BEQ', 'BGEZ', 'BGEZAL',
                   'BGTZ', 'BLEZ', 'BREAK', 'J', 'JAL', 'JALR', 'JR', 'MFC0', 'LB', 'LBU', 'LH', 'LHU', 'LW', 'SB', 'SH', 'SW','$0', '$1', '$2', '$3', '$4', '$5', '$6', '$7', '$8', '$9', '$10', '$11', '$12', '$13', '$14', '$15', '$16', '$17', '$18', '$19', '$20',
                  '$21', '$22', '$23', '$24', '$25', '$26', '$27', '$28', '$29', '$30', '$31', '$ZERO', '$AT', '$V0', '$V1', '$A0', '$A1', '$A2', '$A3',
                    '$T0', '$T1', '$T2', '$T3', '$T4', '$T5', '$T6', '$T7', '$S0', '$S1', '$S2', '$S3', '$S4', '$S5', '$S6', '$S7', '$T8', '$T9', '$K0',
                      '$K1', '$GP', '$SP', '$FP', '$RA']
    for x in check:
        print(x)
        if x not in validlist:
            if x.isnumeric() == False:
                print(False)
                return(False)
    print("correct")
    return

def listmaker():
    lst = []
    finish = 0
    while finish != 1:
        addto = input()
        if addto != "done":
            lst.append(addto.upper())
        else:
            finish = 1
    print(lst)

#codechecker("addi $t0, $t0, 1")
#codechecker("lodsw")
#codechecker("jal $s0, main")
#codechecker("sll $t0, $t1, 3")
codechecker("sw $t0, 0($s0)")