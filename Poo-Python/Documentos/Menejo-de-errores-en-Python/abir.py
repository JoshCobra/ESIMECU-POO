def main():
    open("/path/to/mars.jpg")

if __name__ == '__main__':
    main()

"""
Traceback (most recent call last):
  File "\ESIMECU-POO\Poo-Python\Documentos\Menejo-de-errores-en-Python\abir.py", line 5, in <module>
    main()
    ~~~~^^
  File "c:\ESIMECU-POO\Poo-Python\Documentos\Menejo-de-errores-en-Python\abir.py", line 2, in main
    open("/path/to/mars.jpg")
    ~~~~^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '/path/to/mars.jpg'
"""