# Exemple d'utilisation
def remove_newlines_even_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for i, line in enumerate(lines):
            if i % 2 != 1:  # Even-numbered lines (0-based index)
                file.write(line.replace('\n', ' : '))
            else: 
                file.write(line)

remove_newlines_even_lines('fichier.txt')