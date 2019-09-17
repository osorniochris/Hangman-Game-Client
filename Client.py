from socket import  *

#function to print the hanged guy
def printBody(num):
    print("Vidas restantes: "+str(5-num))
    if( num == 1 ):
        print("  -----\n")
        print(" |     |\n")
        print(" |\n")
        print(" |\n")
        print(" |\n")
        print(" |\n")
        print("- -\n")
    elif( num == 2):
        print("  -----\n")
        print(" |     |\n")
        print(" |   (._.)\n")
        print(" |\n")
        print(" |\n")
        print(" |\n")
        print("- -\n")
    elif( num == 3):
        print("  -----\n")
        print(" |     |\n")
        print(" |   (._.)\n")
        print(" |     |\n")
        print(" |\n")
        print(" |\n")
        print("- -\n")
    elif( num == 4 ):
        print("  -----\n")
        print(" |     |\n")
        print(" |   (.o.)\n")
        print(" |    /|\ \n")
        print(" |\n")
        print(" |\n")
        print("- -\n")
    elif( num == 5):
        print("  -----\n")
        print(" |     |\n")
        print(" |   (x_x)\n")
        print(" |    /|\ \n")
        print(" |    / \ \n")
        print(" |\n")
        print("- -\n")
        print("P E R D I S T E\n")

#variables
ip = "127.0.0.1"
port = 9600
word = ""
opc = ""
mistakes = "0"

#start connection
cl = socket(AF_INET, SOCK_STREAM)
cl.connect( ( ip, port ) )

#select difficulty
print( "----- AHORCADO -----" )
print( "Elija una dificultad" )
print( "(1) Fácil")
print( "(2) Media")
print( "(3) Imposible\n")
opc = str(input(">>"))
print("\n")

#send selected difficulty
cl.send((opc+"\n").encode('utf-8'))

#receives new word to start game
word = cl.recv(1024).decode('utf-8')

#start game
while word != "<end>\r\n":
    mistakes = cl.recv(1024).decode('utf-8')
    printBody(int(mistakes))
    print("PALABRA/ORACIÓN: "+word)
    print("\nSelecciona una letra")
    opc = str(input(">>"))
    print("\n")

    if( len(opc) > 1 ):
        cl.send("-1\n".encode('utf-8'))
        print("Solo se permite una letra")
    else:
        cl.send((opc+"\n").encode('utf-8'))

    word = cl.recv(1024).decode('utf-8')


word = cl.recv(1024).decode('utf-8')

if( word == "<win>\r\n"):
    print("PALABRA / ORACIÓN CORRECTA: " + word)
    print("  -----\n")
    print(" |     |\n")
    print(" |\n")
    print(" |\n")
    print(" |      (uwu)\n")
    print(" |       \|/\n")
    print("- -      / \ \n")
    print("G A N A S T E")
    word = cl.recv(1024).decode('utf-8')
    print("PALABRA / ORACIÓN CORRECTA: " +word)
elif ( word == "<fail>\r\n" ):

    word = cl.recv(1024).decode('utf-8')
    printBody(5)
    print("PALABRA / ORACIÓN CORRECTA: " + word)

cl.close()


