# utils.py
import chardet
import pandas as pd

def convert_file_encoding(uploaded_file, original_encoding, target_encoding):
    # Determine the file type (extension)
    file_name = uploaded_file.name
    extension = file_name.split('.')[-1].lower()

    # Decode the content while reading it line by line
    # This is to avoid dealing with newlines incorrectly
    content = uploaded_file.read().decode(original_encoding).splitlines()
    output_filename = f"converted_file.{extension}"
    with open(output_filename, 'w', encoding=target_encoding, newline='\n', errors='replace') as file:
        for line in content:
            # Write each line to the file and add a newline character manually
            file.write(line + '\n')  # Use '\r\n' if you want Windows-style newlines

    return output_filename