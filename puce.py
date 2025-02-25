def add_bullet_points(file_path):
    # Read the text from a file
    with open(file_path, 'r') as file:
        text = file.read()

    # Split the text into lines
    lines = text.split('\n')

    # Add a bullet point to each line
    bulleted_lines = ['• ' + line for line in lines]

    # Join the lines back into a single string
    bulleted_text = '\n'.join(bulleted_lines)

    # Write the modified text back to the file
    with open(file_path, 'w') as file:
        file.write(bulleted_text)

# Example usage
file_path = 'fichier.txt'
add_bullet_points(file_path)
