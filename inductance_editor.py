def EditInductance(L_k):
    # Get current path
    current_path = os.getcwd()
    # Get the .asc file path
    file_path = os.path.join(current_path, 'spiceModel', 'snspd.asc')

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if 'SYMATTR Value Lind' in line:
            parts = line.split()
            for j, part in enumerate(parts):
                if part.startswith('Lind='):
                    parts[j] = f'Lind={L_k}n'
            lines[i] = ' '.join(parts) + '\n'

    with open(file_path, 'w') as file:
        file.writelines(lines)
