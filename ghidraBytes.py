import ghidra.program.model.mem.Memory;
#################################################################
# km3dg3
# experimenting with byte mods
#################################################################

# Get the beginning address
base_address = currentProgram.getMinAddress ( )

# Get the program memory
memory = currentProgram.getMemory ( )

# Get one byte from base_address
select_1byte = memory.getByte ( base_address )

# Display the first value
print "1 byte value  : ", hex ( select_1byte )

# Get and return / print first and last memory address of highlighted byes (inclusive)
def grabHighlightedBytes():

    if currentSelection is None or currentSelection.isEmpty():
        print "Use your mouse to highlight some data to XOR"
        reutrn
        
    memory = currentProgram.getMemory()
    
    print type(currentSelection)
    print currentSelection
    return currentSelection
    
k = grabHighlightedBytes()
print(k)
