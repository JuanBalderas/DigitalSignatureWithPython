import hashlib
import random
import sys
from Tkinter import *
import Crypto
from Crypto.PublicKey import RSA
import base64
import ast

#HASH SHA1 ---------------------------------------------------------------------    

def digestFile():
    m=hashlib.sha1()
    archivo=open('message.txt','r')
    linea=archivo.readline()
    m.update(linea) #hash linea
    
    while linea != "":
        #print(linea) 
        linea=archivo.readline()
        m.update(linea) #hash linea por linea
        
    archivo.close()
    return m

#HASH SHA 1---------------------------------------------------------------------



#***SIGNARUTE -------------------------------------
def signature():
    try:
        #File digest
        m=hashlib.sha1()
        m=digestFile() #digesto del archivo
        print("----------------------------------:")
        print("Digest of the File write by A to B:")
        digesto=(m.hexdigest())
        print(digesto)
        
        
        print("----------------------------------:")
        #File digest

        
        
        #RSA
        print("----------------------------------:")
        print("The digital signature of A is\n")
        
        with open('keyA.pvt', 'r') as pvt_file: #cargamos la llave publica
            pvt_key = RSA.importKey(pvt_file.read())#guardamos la llave publica

        encrypted=pvt_key.encrypt(digesto,'None') #cifro digesto
        signature=str(encrypted)
        #print(str(signature))
        print(signature)
        print("----------------------------------:")
        #RSA
        
        fichero=open('ADigitalSign.txt','w')
        fichero.write(str(signature))#se crea la firma en otro archivo
        fichero.close()

        stat1.config(text="Completed!")
    except ValueError:
        stat1.config(text="Please enter the private key")
#***SIGNARUTE -------------------------------------


def check():
    try:
        print("\n-------------The side of B---------------")

        #File digest
        m=hashlib.sha1()
        m=digestFile() #digesto del archivo
        print("----------------------------------:")
        print("Digest of the File write by A to B:")
        digesto=str(m.hexdigest())
        print(digesto)

         #Load private key back from file and we must need private key for decryption
        with open('keyA.pub', 'r') as pub_file:
            pub_key = RSA.importKey(pub_file.read())

        #Decrypt the text back with private key and print to console
        
        print("___________")
        print("Decrypt the Digital Sign of A:")

        archivo=open('ADigitalSign.txt','r')
        lineas=archivo.read()

        decrypted=pub_key.decrypt(ast.literal_eval(str(lineas)))
        
        archivo.close()
                   
        print(decrypted)

        Verify=str(decrypted)

        if digesto==Verify:
            stat2.config(text="Correct Sign! c:")
        else:
            stat2.config(text="Incorrect Sign! :s")
        
    except ValueError:
        stat2.config(text="Please enter the private key")
 

if __name__ == '__main__':
    
    app = Tk()
    app.title("CRYPTOGRAPHY")
     
    #Ventana Principal
    vp = Frame(app)
    vp.grid(column=80, row=80, padx=(50,50), pady=(50,50))
    vp.columnconfigure(50, weight=50)
    vp.rowconfigure(50, weight=50)


     




    etiqueta5 = Label(vp, text="PLEASE SELECT THE OPTION")
    etiqueta5.grid(column=5, row=0,padx=(30,30), pady=(30,30) )


    #Digital Signature
     
    botonDS = Button(vp, text="Digital Signature", command=signature)
    botonDS.grid(column=1, row=5)

    stat1 = Label(vp, text="---")
    stat1.grid(column=1, row=6,pady=(20,20) )

    Names.grid(column=5, row=7,pady=(20,20) )

    #Digital Signature



    botonCS = Button(vp, text="Check Signature",command=check)
    botonCS.grid(column=6, row=5)

    stat2 = Label(vp, text="---")
    stat2.grid(column=6, row=6,pady=(20,20) )

    



    img=PhotoImage(file="ESCOM.gif")
    can=Canvas(app)
    
    can.create_image(10,10,image=img,anchor=NW)
    can.grid(column=0,row=0)

    img2=PhotoImage(file="IPN.gif")
    can2=Canvas(app)
    
    can2.create_image(150,80,image=img2,anchor=CENTER)
    can2.grid(column=100,row=0)

     
    app.mainloop() 
    
    
    
    

    


    

    
