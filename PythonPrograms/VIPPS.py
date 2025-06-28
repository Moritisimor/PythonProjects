# Virtual Imperative Python Processor Simulator

simRegisters = { # Dictionary which holds registers. You can change values by adressing the "rgx" keys
"rg1" : None,
"rg2" : None,
"rg3" : None,
"rg4" : None
}

RAM = [] # A (for now) empty list simulates the RAM

# INSTRUCTION SET REGION

def LOADRG(value, simReg): # Load the value into selected register
    simRegisters[simReg] = value

def LOADRAM(value): # Loads the value into RAM and prints its adress to console
    RAM.append(value)
    print(f"SUCCESFULLY LOADED VALUE: {value} INTO RAM AT ADRESS: {RAM.index(value)}")

def LOADRGRAM(simReg): # Loads the value of a register into RAM instead of a value on its own
    RAM.append(simRegisters[simReg])
    print(f"SUCCESFULLY LOADED VALUE OF REGISTER: {simReg} INTO RAM AT ADRESS: {RAM.index(simRegisters[simReg])}")

def SHOWRAM(): # Shows the value every adress holds in RAM
    if RAM: # RAM returns True if it's not empty, else False
        for value in RAM:
            print(f"ADRESS: {RAM.index(value)} HOLDS VALUE: {value}")
    else:
        print("RAM IS EMPTY")

def SHOWRAMAD(adress): # Shows the value a RAM adress holds. Adressing a non-existent adress throws an error
    print(f"ADRESS: {adress} HOLDS VALUE: {RAM[adress]}")

def CLRRAM(): # Removes all Adresses and their values
    RAM.clear()

def CLRALL(): # Clears both registers and RAM
    for simReg in simRegisters:
        UNLOADRG(simReg)
    CLRRAM()

def UNLOADRG(simReg): # Set selected register's value back to None
    simRegisters[simReg] = None

def ADD(simReg1, simReg2): # Takes two registers and prints their sum to console. Can also be used for string concatenation
    print(simRegisters[simReg1] + simRegisters[simReg2])

def ADDOUT(simReg1, simReg2, simReg3): # Like the ADD instruction, but puts output into a third register
    simRegisters[simReg3] = simRegisters[simReg1] + simRegisters[simReg2]

def SUB(simReg1, simReg2): # Takes two registers and prints their difference to console
    print(simRegisters[simReg1] - simRegisters[simReg2])

def SUBOUT(simReg1, simReg2, simReg3): # Like the SUB instruction, but puts output into a third register
    simRegisters[simReg3] = simRegisters[simReg1] - simRegisters[simReg2]

def MULT(simReg1, simReg2): # Takes two registers and prints their product
    print(simRegisters[simReg1] * simRegisters[simReg2])

def MULTOUT(simReg1, simReg2, simReg3): # Like the MULT instruction, but puts output into a third register
    simRegisters[simReg3] = simRegisters[simReg1] * simRegisters[simReg2]

def DIV(simReg1, simReg2): # Takes two registers and prints their quotient
    print(simRegisters[simReg1] / simRegisters[simReg2])

def DIVOUT(simReg1, simReg2, simReg3): # Like the DIV instruction but puts output into a third register
    simRegisters[simReg3] = simRegisters[simReg1] / simRegisters[simReg2]

def CMP(simReg1, simReg2): # A simple instruction which tells you if two registers hold the same value
    if simRegisters[simReg1] == simRegisters[simReg2]:
        print("SAME")
    else:
        print("NOT SAME")

def SHOWRG(simReg): # Prints the current value of selected register to console
    print(simRegisters[simReg])

# EXECUTE REGION

try:
    LOADRG(100, "rg1"),
    LOADRG(200, "rg2"),
    LOADRG(300, "rg3"),
    ADDOUT("rg1", "rg2", "rg4"),
    LOADRGRAM("rg4"),
    SHOWRAMAD(0),
    CLRALL(),
    SHOWRG("rg1"),
    SHOWRG("rg2"),
    SHOWRG("rg3"),
    SHOWRG("rg4"),
    SHOWRAM()
except Exception as error:
    print(f"THE FOLLOWING ERROR HAS OCCURRED: {error} AND THE PROGRAM WILL SHUT DOWN NOW.")