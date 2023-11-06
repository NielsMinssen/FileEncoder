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
            uploaded_file = request.FILES['file']
            action = request.POST.get('action')

            if action == 'detect':
                # Read the file content
                content = uploaded_file.read(10000)
                # Detect encoding
                result = chardet.detect(content)
                encoding = result['encoding']
                confidence = result['confidence'] *100
                # Redirect to a new URL or render the same page with the detected encoding
                # You can pass the detected encoding in the context or as a GET parameter
                return render(request, 'FileEncoder/upload.html', {
                    'form': form,
                    'detected_encoding': encoding,
                    'confidence': confidence
                })
            elif action == 'encode':
                if uploaded_file.size > 5 * 1024 * 1024:  # 5 MB limit
                    context = {
                        'form': form,
                        'error_message': "The file size should not exceed 5 MB.",
                    }
                    return render(request, 'FileEncoder/upload.html', context)
                else:
                    file_content = uploaded_file.read()

                    # Use chardet to detect the encoding
                    detected_encoding = chardet.detect(file_content)['encoding']

                    # Assume a default encoding if chardet is not sure
                    original_encoding = detected_encoding if detected_encoding is not None else 'utf-8'

                    # You might want to reset the file read pointer to the start if you'll read it again
                    uploaded_file.seek(0)

                    # Convert the encoding
                    new_file_path = convert_file_encoding(uploaded_file, original_encoding, request.POST['encoding'])

                    # Prepare response to download the new file
                    with open(new_file_path, 'rb') as f:
                        response = HttpResponse(f, content_type='application/octet-stream')
                        response['Content-Disposition'] = f'attachment; filename="{uploaded_file.name}"'
                        return response
    else:
        form = FileUploadForm()

    return render(request, 'FileEncoder/upload.html', {'form': form})
