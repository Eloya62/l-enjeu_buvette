import json


def saveJson(file_path, new_element):
    with open(file_path, 'a') as file:

        # Check if the file is empty
        file_size = file.tell()
        if file_size == 0:
            # If the file is empty, write the opening bracket
            file.write('[')
        else:
            # If the file is not empty, move back one character
            file.seek(file_size - 2)
            # Remove the closing square bracket
            file.truncate()
            # Add a comma to separate the last element
            file.write(', \n')

        # Write the new element
        json.dump(new_element, file, indent=4)

        # Write the closing bracket
        file.write('\n]')