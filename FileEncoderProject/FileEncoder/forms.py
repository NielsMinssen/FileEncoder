from django import forms


COMMON_ENCODINGS = [
    ('utf-8', 'UTF-8'),
    ('ascii', 'ASCII'),
    ('iso-8859-1', 'ISO-8859-1 (Latin-1)'),
    ('iso-8859-2', 'ISO-8859-2 (Latin-2)'),
    ('iso-8859-3', 'ISO-8859-3 (Latin-3)'),
    ('iso-8859-4', 'ISO-8859-4 (Latin-4)'),
    ('iso-8859-5', 'ISO-8859-5 (Cyrillic)'),
    ('iso-8859-6', 'ISO-8859-6 (Arabic)'),
    ('iso-8859-7', 'ISO-8859-7 (Greek)'),
    ('iso-8859-8', 'ISO-8859-8 (Hebrew)'),
    ('iso-8859-9', 'ISO-8859-9 (Latin-5/Turkish)'),
    ('iso-8859-10', 'ISO-8859-10 (Latin-6/Nordic)'),
    ('iso-8859-13', 'ISO-8859-13 (Baltic Rim)'),
    ('iso-8859-14', 'ISO-8859-14 (Celtic)'),
    ('iso-8859-15', 'ISO-8859-15 (Latin-9/Western European with euro)'),
    ('iso-8859-16', 'ISO-8859-16 (South-Eastern European)'),
    ('windows-1250', 'Windows-1250 (Central European languages)'),
    ('windows-1251', 'Windows-1251 (Cyrillic)'),
    ('windows-1252', 'Windows-1252 (Western languages)'),
    ('windows-1253', 'Windows-1253 (Greek)'),
    ('windows-1254', 'Windows-1254 (Turkish)'),
    ('windows-1255', 'Windows-1255 (Hebrew)'),
    ('windows-1256', 'Windows-1256 (Arabic)'),
    ('windows-1257', 'Windows-1257 (Baltic languages)'),
    ('windows-1258', 'Windows-1258 (Vietnamese)'),
    ('big5', 'Big5 (Traditional Chinese)'),
    ('gb2312', 'GB2312 (Simplified Chinese)'),
    ('euc-jp', 'EUC-JP (Japanese)'),
    ('shift_jis', 'Shift_JIS (Japanese)'),
    ('euc-kr', 'EUC-KR (Korean)'),
    ('utf-16', 'UTF-16 (16-bit Unicode)'),
    ('utf-32', 'UTF-32 (32-bit Unicode)'),
]

class FileUploadForm(forms.Form):
    file = forms.FileField()
    encoding = forms.ChoiceField(choices=COMMON_ENCODINGS)
