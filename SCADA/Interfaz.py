import tkinter as tk
from tkinter import  Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkinter import font
import firebase_admin
from firebase_admin import credentials, db
from PIL import Image, ImageTk
import time
import threading
from tkinter import scrolledtext



cred = credentials.Certificate("usuarios-47379-firebase-adminsdk-fbsvc-a429e91049.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://usuarios-47379-default-rtdb.firebaseio.com/"})


running = True
flujo_file = "flujo.txt"  
last_line_F = ""
flujo_line=''
estado = "estado.txt"  
last_line_E = ""
estado_line=''
temperatura_file = "temperatura.txt"  
last_line_T = ""
temp_line=''
nivel_file='nivel.txt'
last_line_N=''
nivel_line=''


##crear una ventana principal
ventana = tk.Tk()
ventana.title("ventana inicio")
##definir tamaño de la ventana a tamaño completo
ventana.attributes('-fullscreen',1)
##definir el color del fondo de la ventana
ventana.config(bg='white')
#"definir la fuente para botones y titulo"
fuentebotones=font.Font(family="Arcade Classic", size=30, weight="bold")
fuentetitulo=font.Font(family="Arcade Classic", size=75, weight="bold")
fuentebotonesventanas=font.Font(family="Arcade Classic", size=15, weight="bold")
fuentetitbrick=font.Font(family="Arcade Classic", size=125, weight="bold")
fuenteusucontra=font.Font(family="Arcade Classic", size=55, weight="bold")
fuentescada=font.Font(family="Arcade Classic", size=20,weight="bold")

#configuracion de listas para para las graficas
eje_x_grafica_temp = []
for i in range(0,11):
    eje_x_grafica_temp.append(i) # eje x

eje_y_grafica_temp = [None,None,None,None,None] #eje y 
for i in range((len(eje_x_grafica_temp)-len(eje_y_grafica_temp))):
    eje_y_grafica_temp.append(None)
    
eje_x_grafica_nivel = []
for i in range(0,11):
    eje_x_grafica_nivel.append(i) # eje x

eje_y_grafica_nivel = [None,None,None,None,None] #eje y 
for i in range((len(eje_x_grafica_nivel)-len(eje_y_grafica_nivel))):
    eje_y_grafica_nivel.append(None)

# Variables globales para widgets de entrada
caja_texto_usuario = None
caja_texto_contraseña = None
text_area = None
variable_bool=None
#funcion para cambiar el tamaño de las IMG
def redimensionar_imagen(imagen, nuevo_ancho, nuevo_alto):
    return imagen.resize((nuevo_ancho, nuevo_alto), Image.LANCZOS)





def Scada():
    
    def historico():
        cerrar()
        ventana_historico=tk.Toplevel(ventana)
        ventana_historico.attributes('-fullscreen',1)
        ventana_historico.config(bg='white')
        LDAtos= tk.Label(ventana_historico,text='Datos historicos de sensores',font=(fuenteusucontra),bg='white',fg='black')
        LDAtos.place(x=150,y=35)
        boton_volver=tk.Button(ventana_historico,text='volver',font=(fuentebotonesventanas),bg='#000000',fg='white',relief='raised',command=ventana_historico.destroy)
        boton_volver.place(x=1180,y=20)
        canvas_camptext_histo =tk.Canvas(ventana_historico,width=500,height=500,bg='white') 
        canvas_camptext_histo.place(x=450,y=200)
        histo_area = scrolledtext.ScrolledText(ventana_historico, width=60, height=18)
        histo_area.pack()
        canvas_camptext_histo.create_window(250,250, window=histo_area)
        
        def lectura_estado():
            global estado_line
            with open(estado, 'r')as f:
                for i in f:
                    estado_line=i
        def lectura_flujo():
            with open(flujo_file, 'r')as f:
                global flujo_line
                for i in f:
                    flujo_line=i
        def lectura_nivel():
            global nivel_line
            a=0
            with open(nivel_file, 'r')as f:
                for i in f:
                    a+=1
                    nivel_line=i
                    histo_area.insert(tk.END,f'Datos Registrados: {a}Temp={temp_line} /// Flujo={flujo_line} /// Nivel={nivel_line} /// Estado={estado_line}\n')
        def lectura_temp():
            with open(temperatura_file, 'r')as f:
                global temp_line
                for i in f:
                    temp_line=i
        Lectemphilo=threading.Thread(target=lectura_temp)
        Lectemphilo.start()
        Lec_Est_hilo=threading.Thread(target=lectura_estado)
        Lec_Est_hilo.start()
        Lec_Flujo_hilo=threading.Thread(target=lectura_flujo)
        Lec_Flujo_hilo.start()
        Lec_Nivel_hilo=threading.Thread(target=lectura_nivel)
        Lec_Nivel_hilo.start()    

    def read_file_nivel():
        global last_line_N, running
        while running:
            try:
                with open(nivel_file, 'r') as file:
                    lines = file.readlines()
                    if lines:
                        last_line_N = float(lines[-1].strip())  # Leer la última línea                
            except Exception as e:
                print(f"Error al leer el archivo: {e}")
            time.sleep(1)  # Esperar 1 segundo antes de volver a leer
            
    
    def read_file_temp():
        global last_line_T, running
        while running:
            try:
                with open(temperatura_file, 'r') as file:
                    lines = file.readlines()
                    if lines:
                        last_line_T= int(lines[-1].strip())  # Leer la última línea
                        
                        
            except Exception as e:
                print(f"Error al leer el archivo: {e}")
            time.sleep(1)  # Esperar 1 segundo antes de volver a leer

    def read_file_flujo():
        global last_line_F, running
        while running:
            try:
                with open(flujo_file, 'r') as file:
                    lines = file.readlines()
                    if lines:
                        last_line_F= float(lines[-1].strip())  # Leer la última línea
                                
            except Exception as e:
                print(f"Error al leer el archivo: {e}")
            time.sleep(1)  # Esperar 1 segundo antes de volver a leer
    def read_file_estado():
        global last_line_E, running
        while running:
            try:
                with open(estado, 'r') as file:
                    lines = file.readlines()
                    if lines:
                        last_line_E= lines[-1].strip()  # Leer la última línea
                                
            except Exception as e:
                print(f"Error al leer el archivo: {e}")
            time.sleep(1)  # Esperar 1 segundo antes de volver a leer

    def cerrar():
        global running
        running = False  # Detener el hilo
        ventana_SCADA.destroy()  # Cerrar la ventana


    # Iniciar el hilo para leer el archivo
    
    temphilo=threading.Thread(target=read_file_temp)
    temphilo.start()
    nivelhilo=threading.Thread(target=read_file_nivel)
    nivelhilo.start()
    estadohilo=threading.Thread(target=read_file_estado)
    estadohilo.start()
    flujohilo=threading.Thread(target=read_file_flujo)
    flujohilo.start()

    
    """Abre la ventana SCADA después del registro."""
    ventana_SCADA = tk.Toplevel(ventana)
    ventana_SCADA.attributes('-fullscreen', 1)
    ventana_SCADA.config(bg='white')


    def Parar():
        with open('abrir_parar.txt', 'w') as f:
        # Escribir datos en el archivo
            f.write("0")
    def Start():
        with open('abrir_parar.txt', 'w') as f:
        # Escribir datos en el archivo
            f.write("1")




    # Crear el Canvas
    canvas_botones = tk.Canvas(ventana_SCADA, width=300, height=800, bg="white")
    canvas_botones.place(x=975,y=0)
    canvas_animacion =tk.Canvas(ventana_SCADA,width=600,height=400,bg='lightblue') 
    canvas_animacion.place(x=0,y=0)
    canvas_camptext =tk.Canvas(ventana_SCADA,width=368,height=400,bg='white') 
    canvas_camptext.place(x=602,y=0)
    canvas_graficas =tk.Canvas(ventana_SCADA,width=970,height=400,bg='lightblue') 
    canvas_graficas.place(x=0,y=400)

    #imagenes a usar
    Tierra= Image.open("tierra.jpg")
    Agua= Image.open("Agua.png")
    Bomba= Image.open("bomba.png")
    Flecha= Image.open("Flecha.png")
    Tanque= Image.open("tanque.png")
    Tubo=Image.open("tubo.png")

    # Redimensionar las imágenes
    tierra_redimensionada = redimensionar_imagen(Tierra, 600, 400)  # Cambia las dimensiones según sea necesario
    agua_redimensionada = redimensionar_imagen(Agua, 600, 350)
    flecha_redimensionada = redimensionar_imagen(Flecha, 30, 50)
    bomba_redimensionada = redimensionar_imagen(Bomba, 150, 150)
    tanque_redimensionado = redimensionar_imagen(Tanque, 600, 400)
    tubo_redimensionado = redimensionar_imagen(Tubo, 475, 400)
    # Convertir las imágenes a PhotoImage para que sea complatible con tkinter
    tierra_tk=ImageTk.PhotoImage(tierra_redimensionada)
    agua_tk=ImageTk.PhotoImage(agua_redimensionada)
    bomba_tk=ImageTk.PhotoImage(bomba_redimensionada)
    flecha_tk=ImageTk.PhotoImage(flecha_redimensionada)
    tanque_tk=ImageTk.PhotoImage(tanque_redimensionado)
    tubo_tk=ImageTk.PhotoImage(tubo_redimensionado)

    # Mantener referencias a las imágenes
    canvas_animacion.image_refs = [tierra_tk, agua_tk, bomba_tk, flecha_tk, tanque_tk, tubo_tk]


    #widgets camnv_animacion
    canvas_animacion.create_image(0,0,anchor=tk.NW, image=tierra_tk)
    canvas_animacion.create_image(0,0,anchor=tk.NW, image=tanque_tk)
    canvas_animacion.create_image(0,40,anchor=tk.NW, image=agua_tk)
    canvas_animacion.create_image(260,115,anchor=tk.NW, image=bomba_tk)
    canvas_animacion.create_image(75,-100,anchor=tk.NW, image=tubo_tk)
    flechaid1=canvas_animacion.create_image(300,120,anchor=tk.NW, image=flecha_tk)#posicion inicial flecha= x=300 y=120
    
    def iniciar_animacion():
        global variable_bool
        variable_bool = True
        
    def detener_animacion():
        global variable_bool
        variable_bool = False
            
    def anima():
        global variable_bool

        if variable_bool == True:
            canvas_animacion.move(flechaid1,0,-10)
            if (canvas_animacion.coords(flechaid1)) == [300.0, 10.0]:
                canvas_animacion.moveto(flechaid1,300.0, 110.0)
        else:
            canvas_animacion.moveto(flechaid1,300.0, 110.0)   
        ventana_SCADA.after(100,anima)
    ventana_SCADA.after(100,anima)
    def animacion():
        global last_line_E
        if (last_line_E=='Encendido'):
            ventana_SCADA.after(100,iniciar_animacion)
        else:
            ventana_SCADA.after(100,detener_animacion)
        ventana_SCADA.after(100,animacion)
        
    ventana_SCADA.after(100,animacion)
    
    #Botones Scada
    boton_volver=tk.Button(ventana_SCADA,text='volver',font=(fuentescada),bg='#000000',fg='white',relief='raised',command=cerrar,width=16)
    canvas_botones.create_window(150,100,window=boton_volver)
    boton_historico=tk.Button(ventana_SCADA,text='Historico',font=(fuentescada),bg='#000000',fg='white',relief='raised',command=historico,width=16)
    canvas_botones.create_window(150,250,window=boton_historico)
    boton_Parar=tk.Button(ventana_SCADA,text='Parar Bomba',font=(fuentescada),bg='#000000',fg='white',relief='raised',command=Parar,width=16)
    canvas_botones.create_window(150,400,window=boton_Parar)
    boton_Start=tk.Button(ventana_SCADA,text='Bomba Start',font=(fuentescada),bg='#000000',fg='white',relief='raised',width=16,command=Start)
    canvas_botones.create_window(150,550,window=boton_Start)
    
    
    #widgets camp text
    Titulo_advertencia = tk.Label(ventana_SCADA,text='¡Advertencias!',font=(fuentescada,40),bg='white',fg='red',)
    canvas_camptext.create_window(200,50,window=Titulo_advertencia)
    Advertencia = tk.Label(ventana_SCADA,text='aqui se presentaran las\nadvertencias presentadas por el \nsistema',font=(fuentescada,15),bg='white',fg='black',)
    canvas_camptext.create_window(200,150,window=Advertencia)
    Advertencia_2 = tk.Label(ventana_SCADA,font=(fuentescada,15),bg='white',fg='black',text='soy la prueba de que existo')
    canvas_camptext.create_window(200,250,window=Advertencia_2)

    #graficas
    frame_temperatura = Frame(canvas_graficas,  bg='blue',pady=20,padx=20)
    frame_temperatura.grid(column=0,row=0, sticky='nsew')
    def cambios_de_valores_temperatura():
        plt.cla()
        if None in eje_y_grafica_temp:
            eje_y_grafica_temp.remove(None)
            eje_y_grafica_temp.append(last_line_T)
        else:
            eje_y_grafica_temp.pop(0)
            eje_y_grafica_temp.append(last_line_T)
        figura, axs = plt.subplots( dpi=80, figsize=(5,4), 
	    sharey=True, facecolor='#00f9f844')
        figura.suptitle('Grafica de Temperatura')
        axs.plot(eje_x_grafica_temp, eje_y_grafica_temp, color = 'm')
        canvas = FigureCanvasTkAgg(figura, master = frame_temperatura)  # Crea el area de dibujo en Tkinter
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=0)
        ventana.after(1000,cambios_de_valores_temperatura)
        plt.close(figura)
    frame_temperatura.after(100,cambios_de_valores_temperatura)
    
    frame_nivel = Frame(canvas_graficas,  bg='blue',pady=20,padx=20)
    frame_nivel.grid(column=1,row=0, sticky='nsew')
    def cambios_de_valores_nivel():
        if None in eje_y_grafica_nivel:
            eje_y_grafica_nivel.remove(None)
            eje_y_grafica_nivel.append(last_line_N)
        else:
            eje_y_grafica_nivel.pop(0)
            eje_y_grafica_nivel.append(last_line_N)
        figura, axs = plt.subplots( dpi=80, figsize=(5,4), 
        sharey=True, facecolor='#00f9f844')
        figura.suptitle('Grafica de Nivel del Agua')
        axs.plot(eje_x_grafica_nivel, eje_y_grafica_nivel, color = 'm')
        canvas = FigureCanvasTkAgg(figura, master = frame_nivel)  # Crea el area de dibujo en Tkinter
        canvas.draw()
        canvas.get_tk_widget().grid(column=1, row=0)
        ventana.after(1000,cambios_de_valores_nivel)
        plt.close(figura)
    frame_nivel.after(100,cambios_de_valores_nivel)
#advertencias
    def advertencia_de_temperatura():
        if (last_line_T >27):
            Advertencia_2.config(text='¡¡¡ADVETENCIA!!!\n La temperatura  actual\nsobrepasa la temperatura\noptima',fg='red')
        else:
            Advertencia_2.config(text='')
        ventana.after(100,advertencia_de_temperatura)
    ventana.after(100,advertencia_de_temperatura)
    def advertencia_de_flujo():
        if ((last_line_N<10) and (last_line_F==1)):
            Advertencia.config(text='¡¡¡ADVETENCIA!!!\n El flujo de agua actual\nes menor al flujo\noptimo recomendado',fg='red')
        else:
            Advertencia.config(text='aqui se presentaran las\nadvertencias presentadas por el \nsistema',font=(fuentescada,15),bg='white',fg='black')
        ventana.after(100,advertencia_de_flujo)
    ventana.after(100,advertencia_de_flujo)


#funcion ventana de registro 
def registro():
    ventana_registro=tk.Toplevel(ventana)
    ventana_registro.attributes('-fullscreen',1)
    ventana_registro.config(bg='white')
    registrar= tk.Label(ventana_registro,text='registro',font=(fuentetitbrick),bg='white',fg='black')
    registrar.place(x=300,y=0)
    boton_volver=tk.Button(ventana_registro,text='volver',font=(fuentebotonesventanas),bg='#000000',fg='white',relief='raised',command=ventana_registro.destroy)
    boton_volver.place(x=1180,y=20) 
    usuario=tk.Label(ventana_registro,text='usuario',font=(fuenteusucontra),bg='white',fg='black')
    usuario.place(x=500,y=200)
    caja_texto_usuario = tk.Text(ventana_registro, height=1, width=40)
    caja_texto_usuario.place(x=475,y=290)
    contraseña=tk.Label(ventana_registro,text='contraseña',font=(fuenteusucontra),bg='white',fg='black')
    contraseña.place(x=450,y=330)
    caja_texto_contraseña = tk.Text(ventana_registro, height=1, width=40)
    caja_texto_contraseña.place(x=475,y=425)
    text_area = tk.Text(ventana_registro,height=3,width=50)
    text_area.place(x=500,y=480)
        
    def dataregist():
        texto_usuario=caja_texto_usuario.get("1.0", tk.END).strip()
        texto_contraseña=caja_texto_contraseña.get("1.0", tk.END).strip()
        referencia= db.reference(f'usuarios/{texto_usuario}')
        name=caja_texto_usuario.get("1.0", tk.END).strip()
        if referencia.get():
                text_area.delete("1.0", tk.END) 
                text_area.insert(tk.END,f'El Usuario {name}, ya se encuentra registrado')
        else:        
            text_area.delete("1.0", tk.END)    
            referencia.set({'contraseña':texto_contraseña})
            def destruir_regist():
                 ventana_registro.destroy
            text_area.insert(tk.END,f'Hola {name}, Bienvenido desde la siguiente pestaña podrá observar lo referente a su sistema de alcantalillado')
            ventana_registro.after(100000,destruir_regist)
            Scada()
    boton_registro=tk.Button(ventana_registro,text='registrarse',font=(fuentebotones),bg='#000000',fg='white',relief='raised',command=dataregist)
    boton_registro.place(x=500,y=600)


                

def inicio_sesion():
    ventana_inicio=tk.Toplevel(ventana)
    ventana_inicio.attributes('-fullscreen',1)
    ventana_inicio.config(bg='white')
    iniciar= tk.Label(ventana_inicio,text='inicie sesión',font=(fuentetitbrick),bg='white',fg='black')
    iniciar.place(x=200,y=20)
    boton_volver=tk.Button(ventana_inicio,text='volver',font=(fuentebotonesventanas),bg='#000000',fg='white',relief='raised',command=ventana_inicio.destroy)
    boton_volver.place(x=1180,y=20)
    usuario=tk.Label(ventana_inicio,text='usuario',font=(fuenteusucontra),bg='white',fg='black')
    usuario.place(x=500,y=220)
    caja_texto_usuario = tk.Text(ventana_inicio, height=1, width=40)
    caja_texto_usuario.place(x=475,y=310)
    contraseña=tk.Label(ventana_inicio,text='contraseña',font=(fuenteusucontra),bg='white',fg='black')
    contraseña.place(x=450,y=350)
    caja_texto_contraseña = tk.Text(ventana_inicio, height=1, width=40)
    caja_texto_contraseña.place(x=475,y=425)
    
    text_area = tk.Text(ventana_inicio,height=3,width=50)
    text_area.place(x=500,y=450)    
    def inicio():
        texto_usuario=caja_texto_usuario.get("1.0", tk.END).strip()
        texto_contraseña=caja_texto_contraseña.get("1.0", tk.END).strip()
        referencia= db.reference(f'usuarios/{texto_usuario}')
        name=caja_texto_usuario.get("1.0", tk.END).strip()
        dato_usuario=referencia.get()
        contr_usua=dato_usuario.get('contraseña')
        print(contr_usua)
        print(texto_contraseña)
        if (contr_usua== texto_contraseña):

             text_area.insert(tk.END,f'Hola {name}, Bienvenido desde la siguiente pestaña podrá observar lo referente a su sistema de alcantalillado')
             
             Scada()
        else:
             text_area.insert(tk.END,f'Hola {name}, el usuario o la contraseñaa estan incorrectos')
    boton_sesion=tk.Button(ventana_inicio,text='iniciar sesion',font=(fuentebotones),bg='#000000',fg='white',relief='raised',command=inicio)
    boton_sesion.place(x=500,y=550)    


titulo = tk.Label(ventana,text='SCADA SISTEMA INTERNO\nDE ALCANTARILLADO',font=(fuentetitulo),bg='white',fg='black')
titulo.place(x=0,y=40)
registrarse= tk.Button(ventana,text='registrarse',font=fuentebotones,bg='#000000',fg='white',relief='raised',command=registro)
registrarse.place(x=530,y=350)
but_inicio= tk.Button(text='Inicio de Sesión',font=(fuentebotones),bg='#000000',fg='white',relief='raised',command=inicio_sesion)
but_inicio.place(x=480,y=440)
#brick_Breaker= tk.Button(text='Brick Breacker',font=(fuentebotones),bg='#000000',fg='white',relief='raised',command=crear_ventana_brick)
#brick_Breaker.place(x=490,y=530)
salir= tk.Button(text='Salir',font=(fuentebotones),bg='#000000',fg='white',relief='raised',command=ventana.quit)
salir.place(x=600,y=620)
ventana.mainloop()  
