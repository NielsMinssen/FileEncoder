# utils.py
import chardet
import pandas as pd

def convert_file_encoding(uploaded_file, original_encoding, target_encoding='utf-8'):
    # Determine the file type (extension)
    file_name = uploaded_file.name
    extension = file_name.split('.')[-1].lower()

    # Handle text and CSV files
    if extension in ['txt', 'csv']:
        # Decode the content while reading it line by line
        # This is to avoid dealing with newlines incorrectly
        content = uploaded_file.read().decode(original_encoding).splitlines()
        output_filename = f"converted_file.{extension}"
        with open(output_filename, 'w', encoding=target_encoding, newline='\n') as file:
            for line in content:
                # Write each line to the file and add a newline character manually
                file.write(line + '\n')  # Use '\r\n' if you want Windows-style newlines

    # Handle XLS and XLSX files with pandas
    elif extension in ['xls', 'xlsx']:
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(uploaded_file, engine='openpyxl' if extension == 'xlsx' else 'xlrd')

        # Convert DataFrame to the same format (XLS or XLSX)
        output_filename = f"converted_file.{extension}"
        df.to_excel(output_filename, index=False)

    return output_filename