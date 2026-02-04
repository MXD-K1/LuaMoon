import zipfile
import tarfile

def extract_zip(pkg_zip_file, extraction_path):
    with zipfile.ZipFile(pkg_zip_file + '.zip', "r") as z:
        z.extractall(extraction_path)

def extract_tar(pkg_tar_file, extraction_path):
    with tarfile.open(pkg_tar_file , "r:*") as t:
        t.extractall(extraction_path)
