import os

def EditInductance(L_k):
    # Get current path
    current_path = os.getcwd()

    # Get the .asc file path
    file_path = os.path.join(current_path, 'spiceModel', 'snspd.asc')

    # Read the file contents
    with open(file_path, 'r') as file:
        lines = file.readlines()

    line_found = False

    for i, line in enumerate(lines):
        if 'SYMATTR Value Lind=' in line:
            parts = line.split()
            for j, part in enumerate(parts):
                if part.startswith('Lind='):
                    parts[j] = f'Lind={L_k}n'
                    line_found = True
            lines[i] = ' '.join(parts) + '\n'
    
    if not line_found:
        lines.append(f"SYMATTR Value Lind={L_k}n\n")
        lines.append(f"SYMATTR SpiceModel nanowireBCF\n")

    with open(file_path, 'w') as file:
        file.writelines(lines)
