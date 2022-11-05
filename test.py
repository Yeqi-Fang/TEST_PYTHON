import zipfile


file = '2.txt'
zip = '1.zip'
with zipfile.ZipFile(zip, 'a', compression=zipfile.ZIP_LZMA) as f:
    f.write(file)
