# views.py
from django.shortcuts import render
from .forms import FileUploadForm
from .utils import convert_file_encoding
from django.http import HttpResponse
from django.core.files import File
import chardet  # Make sure chardet is imported

def file_upload_view(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the uploaded file
            uploaded_file = request.FILES['file']
            file_content = uploaded_file.read()

            # Use chardet to detect the encoding
            detected_encoding = chardet.detect(file_content)['encoding']

            # Assume a default encoding if chardet is not sure
            original_encoding = detected_encoding if detected_encoding is not None else 'utf-8'

            # You might want to reset the file read pointer to the start if you'll read it again
            uploaded_file.seek(0)

            # Convert the encoding
            new_file_path = convert_file_encoding(uploaded_file, original_encoding)

            # Prepare response to download the new file
            with open(new_file_path, 'rb') as f:
                response = HttpResponse(f, content_type='application/octet-stream')
                response['Content-Disposition'] = f'attachment; filename="{uploaded_file.name}"'
                return response
    else:
        form = FileUploadForm()

    return render(request, 'FileEncoder/upload.html', {'form': form})
