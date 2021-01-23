import os
import shutil

# Ruta del usuario y carpeta descargas
path = os.environ['USERPROFILE'] + "\\Downloads\\"

# Lista de archivos y carpetas
files = os.listdir(path)

# Posibles extensiones de archivos
docs_ext = ['.pdf','.doc','.docx','.xls', '.xlsx', '.csv', '.txt', '.pptx','.ppt', '.PDF']
img_ext = ['.png', '.jpg', '.jpeg']
audio_ext = ['.mp3', '.wav']
zips_ext = ['.zip', '.rar']
exe_ext = ['.exe']
prog_ext = ['.php', '.sql','.c6bak', '.cf6bak']
iso_ext = ['.iso']
ps4_ext = ['.PUP']
pkt_ext = ['.pkt']
 
# Carpetas donde seran almacenados los archivos
folders = [path + "Documentos", path + "Imagenes",
            path + "Audio", path + "Zips", path + "Ejecutables", 
            path + "Programacion", path + "ISOs", path + "PS4", path + "PacketTracer"]


def check_folders(folders):
    """
    Funcion encargada de revisar si existe las carpetas correspondientes
    Args:
        folders: Rutas de las carpetas a crear o verificar su existencia
    """
    try:
        for folder in folders:
            os.mkdir(folder,777)
    except OSError as e:
        print("No es necesario crear las carpetas, ya existen...")
        pass
    
def sorter(archivo, extension):
    """
    Funcion que se encarga de mover los archivos a la ruta correspondiente de acuerdo a su extension
    Args:
        archivo: Archivo a mover
        extension: extension del archivo .docx, .png, etc.
    """
    for ext in docs_ext:
        if extension == ext:
            shutil.move(path + archivo + extension, folders[0])

    for ext in img_ext:
        if extension == ext:
            shutil.move(path + archivo + extension, folders[1])

    for ext in audio_ext:
        if extension == ext:
            shutil.move(path + archivo + extension, folders[2])

    for ext in zips_ext:
        if extension == ext:
            shutil.move(path + archivo + extension, folders[3])

    for ext in exe_ext:
        if extension == ext:
            shutil.move(path + archivo + extension, folders[4])

    for ext in prog_ext:
        if extension == ext:
            shutil.move(path + archivo + extension, folders[5])

    for ext in iso_ext:
        if extension == ext:
            shutil.move(path + archivo + extension, folders[6])

    for ext in ps4_ext:
        if extension == ext:
            shutil.move(path + archivo + extension, folders[7])

    for ext in pkt_ext:
        if extension == ext:
            shutil.move(path + archivo + extension, folders[8])

def main():
    check_folders(folders)
    for file in files:
        archivo, extension = os.path.splitext(file)
        if extension !='':
            sorter(archivo,extension)

main()