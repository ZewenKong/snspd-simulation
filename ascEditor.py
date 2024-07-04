def ascEditor(L_k):
    file_path = r"C:\Users\zewen\Downloads\SNSPDsSim\snspd.asc"

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
