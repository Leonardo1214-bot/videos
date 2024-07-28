import PIL
from PIL import Image, ImageFilter


IMG_PATH = "image.jpg"

if IMG_PATH:
    IMG = Image.open(IMG_PATH)

    def girar_imagen():
        global IMG
        print("¿Cuántos grados quieres rotar?")
        rotar = int(input())
        IMGROTADA = IMG.rotate(rotar)
        IMG = IMGROTADA
        IMG.show()

    def show_img():
        IMG.show()

    def blur():
        global IMG
        blurred_image = IMG.filter(ImageFilter.BLUR)
        IMG = blurred_image
        IMG.show()

    def save_img():
        IMG.save('LOL.png')
        IMG.show()

    def blanco_y_negro():
        global IMG
        grayscale_image = IMG.convert('L')
        IMG = grayscale_image
        IMG.show()

    def mostrar_comandos():
        print("Comandos disponibles:")
        print("  Girar Imagen")
        print("  Mostrar Imagen")
        print("  Desenfocar Imagen")
        print("  Guardar Imagen")
        print("  Blanco y Negro")
        print("  Salir")

    while True:
        print("¿Qué desea hacer con la imagen? Escriba 'help' para ver la lista de comandos")
        entrada = input().lower()

        if entrada == "help":
            mostrar_comandos()
        elif entrada == "girar imagen":
            girar_imagen()
        elif entrada == "mostrar imagen":
            show_img()
        elif entrada == "desenfocar imagen":
            blur()
        elif entrada == "guardar imagen":
            save_img()
        elif entrada == "blanco y negro":
            blanco_y_negro()
        elif entrada == "salir":
            print("Saliendo del programa...")
            break
        else:
            print("Comando no reconocido")
else:
    print("No se seleccionó ninguna imagen.")
