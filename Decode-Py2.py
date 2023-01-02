import uncompyle6

# Open the compiled Python file
with open('compiled_file.pyc', 'rb') as f:
    # Read the bytecode from the file
    bytecode = f.read()

# Decompile the bytecode
source_code = uncompyle6.decompile_code(bytecode, only_asts=True)

# Print the decompiled source code
print(source_code)
