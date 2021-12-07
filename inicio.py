#from ventanas import  mod_cliente,nuevo_prestamo,mod_prestamo,abonado,mod_abono
import base_funtion as bd
from tkinter.constants import CENTER
import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk, messagebox,Menu



def destruir(ventana1, max2 = None):
    ventana1.destroy()
    max2.deiconify()

def limpiar(*args):
    for i in args:
        i.delete(0, 'end')
    
class Principal:

    def __init__(self) -> None:
      ################################# decorador de imagenes
        self.root = tk.Tk()
        self.root.geometry('580x300')
        #self.root.config(bg='red')
        self.root.title("Registros de prestamos (Pantalla principal)")
        self.root.iconbitmap("imagenes/principal.ico")
        self.root.resizable(0,0)
        
        
        self.im_bruck = tk.PhotoImage(file = 'imagenes/LOGOBRUK.png').subsample(1)
        self.fuente = tkfont.Font(family="Arial", size=10, weight="bold", slant="italic")
        self.im_borrar = tk.PhotoImage(file='imagenes/borrar.png')
        self.im_borr_cliente = tk.PhotoImage(file='imagenes/BorrarCliente.png').subsample(15)
        self.im_buscar = tk.PhotoImage(file='imagenes/buscar.png').subsample(7)
        self.im_check = tk.PhotoImage(file='imagenes/buscar.png').subsample(15)
        self.im_cobro = tk.PhotoImage(file='imagenes/cobro.png').subsample(15)
        self.im_nuevo_cliente = tk.PhotoImage(file='imagenes/nuevoCliente.png').subsample(15)
        self.im_nuevo_prestamo = tk.PhotoImage(file='imagenes/nuevoPrestamo.png').subsample(15)
        self.im_salir = tk.PhotoImage(file='imagenes/salir.png').subsample(15)
        self.im_ayuda = tk.PhotoImage(file='imagenes/ayuda.png').subsample(15)
        self.im_relod = tk.PhotoImage(file='imagenes/reloded.png')
        self.im_filter = tk.PhotoImage(file='imagenes/Filter.png')
        #self.im_logobru = tk.PhotoImage(file='imagenes/LOGOBRUK.png').subsample(115)
        #self.menus()
        self.periodo =''  
        self.b = bd.Base()
        self.decorar()
        self.root.mainloop()
        #self.decorar()
        #self.root.mainloop()
        ############################## imagenes##########################################################

    def decorar(self):
      ######################################## botones
        frame_botons = ttk.Frame(self.root)
        frame_botons.grid(padx = 1, pady = 1, row = 0, column = 0,columnspan=5, sticky = 'EW')

        b_client = ttk.Button(frame_botons,text = 'N cliente', image = self.im_nuevo_cliente,compound = tk.TOP,
        command = lambda: self.nuevo_cliente(self.root))
        b_client.grid(padx = 10, pady = 5,row = 1, column = 0)

        b_nuevo_prestamo = ttk.Button(
            frame_botons, text='N Pestamo', image= self.im_nuevo_prestamo,compound = tk.TOP, command = self.clientes_tap)
        b_nuevo_prestamo.grid(padx=10, pady=5, row=1, column=1)

        b_cobro = ttk.Button(frame_botons, text='Cobro', image= self.im_cobro,compound = tk.TOP, command = self.abonos)
        b_cobro.grid(padx=10, pady=5, row=1, column=2)
        b_buscar = ttk.Button(frame_botons, text='Buscar', image= self.im_buscar,compound = tk.TOP)
        b_buscar.grid(padx=10, pady=5, row=1, column=3)

        b_ayuda = ttk.Button(frame_botons, text='Ayuda', image= self.im_ayuda,compound = tk.TOP, command = lambda :
        messagebox.showinfo('Ayuda','Escríbeme : cristiancortez776@gmail.com'))
        b_ayuda.grid(padx=10, pady=5, row=1, column=4)

        b_salir = ttk.Button(frame_botons, text='salir', image= self.im_salir,compound = tk.TOP, command = self.root.destroy)
        b_salir.grid(padx=10, pady=5, row=1, column=5)

      #################################################################################cuerpo de informacion
        s = ttk.Separator(self.root, orient='horizontal')
        s.grid(row = 1, column = 0, columnspan = 5, sticky='we')
        
        fram_id = tk.Frame(self.root,borderwidth=3, relief="ridge")
        fram_id.grid(row=2,column=0,sticky='nws')

        self.logo= ttk.Label(fram_id, image=self.im_bruck, text='Creador')
        self.logo.grid(row = 0, column = 0,sticky = 'w')
    
        ttk.Label(fram_id, text = 'Cuenta_Registro V1.0.0', font=tkfont.Font(family="Arial", size=7, weight="bold", slant="italic")).grid(row=1, column=0, sticky='ws')
        ttk.Label(fram_id, text= 'cristiancortez776@gmail.com').grid(row = 2, column = 0, sticky = 'ws')
        
        fra_data = tk.Frame(self.root,borderwidth=3, relief="ridge")
        fra_data.grid(ipady = 97, ipadx = 205, row = 2, column = 1, sticky='nsew')
        
        ttk.Label(fra_data, text='Clientes Registrados: ', font=self.fuente).grid(row = 0, column = 0, sticky='w')

        self.la_data_client=ttk.Label(fra_data, font=self.fuente)
        self.la_data_client.grid(row = 0, column = 1, sticky='w')
        ttk.Label(fra_data, text='Prestamos realizados: ', font=self.fuente).grid(row = 1, column = 0, sticky='w')
        self.lab_presta = ttk.Label(fra_data, text='Prestamos realizados: ', font=self.fuente)
        self.lab_presta.grid(row = 1, column = 1, sticky='w')

        self.Info_total(self.la_data_client,'clientes')
        self.Info_total(self.lab_presta,'prestamo')

    def Info_total(self,etiqueta,tabla):
        for row in self.b.cuenta(tabla):
            etiqueta.config(text = row)

    def select(self,frame,r):
        pla = ['Quincenal', ' Mensual ']
        seleccion = r.get()
        lab = ttk.Label(frame)
        lab.grid(row=0, column=6)
        lab.config(text=pla[seleccion])
        if pla[seleccion]=='Quincenal':
            self.periodo = 'Q'
        elif pla[seleccion] == ' Mensual ':
            self.periodo = 'M'

    def nuevo_cliente(self,madre):
        madre.iconify()
        #destruir(self.root) 
        def guardar_cliete(nom, ape, dire, tele, cedu):
            self.b.inser_data_clinete(nom, ape, dire, tele, cedu)
            self.Info_total(self.la_data_client,'clientes')

        root_cliente = tk.Toplevel(self.root)
        root_cliente.title('Registro de nuevo cliente')
        root_cliente.iconbitmap('imagenes/cliente.ico')
        # root.geometry('400x300')
        root_cliente.transient() # este metodo dibuja la ventana por encima de la ventana madre
        root_cliente.grab_set() # este metodo evita que haya eventos en la ventana madre
        root_cliente.resizable(0,0)
        direccion = tk.StringVar()
        telefono = tk.StringVar()
        cedula = tk.StringVar()
        deuda = tk.IntVar()
        apellido = tk.StringVar()
        nombre = tk.StringVar()

        frame_central = ttk.Frame(root_cliente )
        frame_central.grid(padx=30, pady=30, row=0, column=0)

        l_nombre = ttk.Label(frame_central, text='Nombre')
        l_nombre.grid(row=0, column=0, sticky='w')

        l_apellido = ttk.Label(frame_central, text='   Apellido')
        l_apellido.grid(padx=10, row=0, column=1, sticky='w')

        e_nombre = ttk.Entry(frame_central, textvariable=nombre)
        e_nombre.grid(ipadx=10, row=2, column=0)
        e_nombre.focus()

        e_apellido = ttk.Entry(frame_central, textvariable=apellido)
        e_apellido.grid(ipadx=10, padx=10, row=2, column=1)

        frame_direccion = ttk.Frame(frame_central)
        frame_direccion.grid(pady=20, row=3, column=0, columnspan=2, sticky='nsew')

        l_direccion = ttk.Label(frame_direccion, text='Dirección')
        l_direccion.grid(row=0, column=0, sticky='w')

        e_direccion = ttk.Entry(frame_direccion, textvariable=direccion)
        e_direccion.grid(ipadx=93, row=1, column=0, columnspan=2, sticky='ew')

        l_telefono = ttk.Label(frame_central, text='Telefono')
        l_telefono.grid(row=4, column=0, sticky='w')

        l_cedula = ttk.Label(frame_central, text='Cedula')
        l_cedula.grid(row=4, column=1, padx=10, sticky='w')

        e_telefono = ttk.Entry(frame_central, textvariable=telefono)
        e_telefono.grid(row=5, column=0, sticky='w')

        e_cedula = ttk.Entry(frame_central, textvariable=cedula)
        e_cedula.grid(row=5, column=1, padx=10, ipadx=15)

        f_deuda = ttk.LabelFrame(frame_central)
        f_deuda.grid(row=6, column=0, columnspan=2, sticky='ew')

        f_cen = ttk.Frame(f_deuda)
        f_cen.grid(row=0, column=0, padx=50, pady=5)

        l_deuda = ttk.Label(f_cen, text='Deuda actual')
        l_deuda.grid(row=0, column=0)

        e_deuda = ttk.Entry(f_cen, state='disable')
        e_deuda.grid(row=0, column=1, ipadx=5, sticky='w')

        f_botones = ttk.Frame(root_cliente)
        f_botones.grid(row=1, column=0, columnspan=2, sticky='w')

        b_limpiar = ttk.Button(f_botones, text='Limpiar', command=lambda: limpiar(e_nombre,e_apellido,
            e_deuda,e_cedula,e_telefono,e_direccion))
        b_limpiar.grid(column=0, row=0, padx=10)

        b_guardar = ttk.Button(f_botones, text='Guardar', command= lambda :guardar_cliete(nombre.get(), apellido.get(),
            direccion.get(), telefono.get(), cedula.get()))
        b_guardar.grid(column=1, row=0)

        b_cancelar = ttk.Button(f_botones, text='Cancelar', command=lambda: destruir( root_cliente, madre))
        b_cancelar.grid(column=2, row=0, padx=10)
        # #######################################################################################################################
    
    def guardar_prestamo(self,client_id,fecha,monto,interes,periodo,plazo):
            interes*=0.01
            self.id_cliente.config(state = 'normal')
            self.b.insert_data_prestamo(client_id,fecha,monto,interes,periodo,plazo)
            self.id_cliente.config(state = 'disable')
            limpiar(self.entry_nombre,self.entry_deuda,self.entry_plazo,self.entry_monto,self.entry_interes,
            self.entry_detalle,self.entry_fecha)
            self.Info_total(self.lab_presta,'prestamo')

    def nuevo_prestamo(self):  
      ############################################### entrys no grap
        self.root_n_prestamo = tk.Toplevel(self.root)
        self.root_n_prestamo.title('Registro de nuevo préstamo')
        #self.root_n_prestamo.geometry('400x300')
        self.root_n_prestamo.resizable(0, 0)
        #self.root_n_prestamo.transient()  # este metodo dibuja la ventana por encima de la ventana madre
        # self.root_n_prestamo.grab_set()
        deuda = tk.IntVar()
        self.id = tk.IntVar()
        fecha = tk.StringVar()
        monto = tk.IntVar()
        interes = tk.IntVar()
        plazo = tk.IntVar()
        Frame_dev_prin = ttk.Frame(self.root_n_prestamo)
        Frame_dev_prin.grid(row=0, column=0)

        radio = tk.IntVar()
        frame_datos = ttk.Frame(Frame_dev_prin)
        frame_datos.grid(padx=10, pady=10, row=0, column=0, sticky='nsew')

        ttk.Label(frame_datos, text='Nombre completo').grid(row=0, column=0)
        self.nombre = tk.StringVar()
        self.entry_nombre = ttk.Entry(frame_datos,textvariable=self.nombre)
        self.entry_nombre.grid(ipadx=150, row=0, column=1, columnspan=6, sticky='ew')

        ttk.Label(frame_datos, text='Deuda actual').grid(row=1, column=0)

        self.entry_deuda = ttk.Entry(frame_datos)
        self.entry_deuda.grid(pady=5, row=1, column=1, columnspan=2, sticky='ew')

        ttk.Label(frame_datos, text='Cod. Cliente:').grid(row = 2, column = 0)
        
        self.id_cliente = ttk.Entry(frame_datos,textvariable=self.id)
        self.id_cliente.grid(column=1,row = 2)
      ###################################################################### entris fecha monto
        ttk.Separator(Frame_dev_prin, orient='horizontal').grid(pady=20, padx=20, row=2, column=0, columnspan=7, sticky='ew')

        frame_fecha = ttk.Frame(Frame_dev_prin)
        frame_fecha.grid(padx=70, pady=20, row=3, column=0)

        ttk.Label(frame_fecha, text='Fecha desembolso').grid(row=0, column=0)

        ttk.Label(frame_fecha, text='Monto').grid(padx=10, row=0, column=2)

        self.entry_fecha = ttk.Entry(frame_fecha,textvariable=fecha)
        self.entry_fecha.grid(row=0, column=1)

        self.entry_monto = ttk.Entry(frame_fecha, width=10,textvariable=monto)
        self.entry_monto.grid(row=0, column=3)

      ###################################################################### radiobutons

        frame_radio = ttk.LabelFrame(Frame_dev_prin, text='Periodo de cuotas')
        frame_radio.grid(ipady=5, padx=50, pady=10, row=5, column=0, columnspan=6, sticky='nsew')

        r_quince = ttk.Radiobutton(frame_radio, text='Quincenal', variable=radio,
                 value=0, command= lambda : self.select( frame_interes,radio))
        r_quince.grid(padx=120, row=0, column=0)
        
        r_mes = ttk.Radiobutton(frame_radio, text='Mensual',
                 variable=radio, value=1, command=lambda : self.select(frame_interes,radio))
        r_mes.grid(padx=10, row=0, column=1)

      ##################################################################### Caja tipo periodo
        frame_interes = ttk.Frame(Frame_dev_prin)
        frame_interes.grid(padx=50, pady=20, row=6, column=0, columnspan=6, sticky='nsew')

        ttk.Label(frame_interes, text='Interés Mensual').grid(row=0, column=0)

        self.entry_interes = ttk.Entry(frame_interes, width=10, textvariable=interes)
        self.entry_interes.grid(row=0, column=1)

        ttk.Label(frame_interes, text='%').grid(row=0, column=2)


        ttk.Label(frame_interes, text='Plazo').grid(row=0, column=4)
        self.entry_plazo = ttk.Entry(frame_interes, width=10,textvariable=plazo)
        self.entry_plazo.grid(row=0, column=5)
        ttk.Label(frame_interes, text='Detalles').grid(row=1, column=0)
        self.entry_detalle = ttk.Entry(frame_interes)
        self.entry_detalle.grid(pady=10, ipady=10, row=1, column=1, columnspan=5, rowspan=2,sticky='ewns')

      ##################################################################### botones n-PRESTAMO|
        style = ttk.Style()
        style.configure('N.TFrame', background='light blue')
        frame_botone = ttk.Frame(Frame_dev_prin, style='N.TFrame')
        frame_botone.grid(padx=15, pady=4, row=7, column=0, columnspan=6, sticky='nsew')

        boton_limpiar = ttk.Button(frame_botone, text='Limpiar', command = lambda : limpiar(self.entry_nombre,self.entry_deuda,self.entry_plazo,
            self.entry_monto,self.entry_interes,self.entry_detalle,self.entry_fecha))

        boton_limpiar.grid(padx=8, pady=5, row=0, column=0)

        boton_contrato = ttk.Button(frame_botone, text='Contrato')
        boton_contrato.grid(padx=8, pady=5, row=0, column=1)

        boton_Imprimir = ttk.Button(frame_botone, text='Imprimir')
        boton_Imprimir.grid(padx=8, pady=5, row=0, column=2)

        boton_tabla = ttk.Button(frame_botone, text='Tabla', command = self.clientes_tap)
        boton_tabla.grid(padx=8, pady=5, row=0, column=3)

        boton_guardar = ttk.Button(frame_botone, text='Guardar',command =lambda: self.guardar_prestamo(
              self.id.get(),fecha.get(),monto.get(),interes.get(),self.periodo,plazo.get()))
        boton_guardar.grid(padx=8, pady=5, row=0, column=4)

        boton_cancelar = ttk.Button(frame_botone, text='Cancelar', comman =lambda: destruir(self.root_n_prestamo,self.root))
        boton_cancelar.grid(padx=8, pady=5, row=0, column=5)

    def capturando_datos(self,nomb,id_cl):
        #Este metodo captura los datos de la lista cuando se le da un clic y los inserta en el arbol
        id_cl.delete(0,'end')
        id_cl.insert(0,self.lista.item(self.lista.focus())['values'][0]) # capturo el valor 0 de la linea selccionada
        for valor in self.lista.item(self.lista.focus())['values'][1:]: # # capturo los ultimos valores de la linea selccionada
            nomb.insert('end',valor)
            nomb.insert('end',' ')
        nomb.config(state='disable')
        id_cl.config(state='disable')
        self.root_en_pantalla.destroy()
        self.root_n_prestamo.deiconify()

    def clientes_tap(self):
        self.root.iconify()
        self.nuevo_prestamo()
        self.root_n_prestamo.iconify()
        nomb = tk.StringVar()

        self.root_en_pantalla = tk.Toplevel(self.root)
        self.root_en_pantalla.title('Lista de clientes')
        #self.root_en_pantalla.geometry('400x300')

        tk.Label(self.root_en_pantalla, text = 'Nombre').grid(row = 0, column = 0)
        e_nombre = tk.Entry(self.root_en_pantalla,textvariable = nomb)
        e_nombre.grid(row = 1, column = 0)
        ttk.Button(self.root_en_pantalla,image=self.im_filter,compound=CENTER,command=lambda:self.mostra_en_tabla(
            nomb.get().upper())).grid(
            column = 1, row = 1)
        ttk.Button(self.root_en_pantalla,image=self.im_relod,compound=tk.CENTER, command= self.reload).grid(
            column=2, row = 1)
        
        self.lista = ttk.Treeview(self.root_en_pantalla, columns=(1, 2, 3), show='headings', height='25')#, height='15'
        self.lista.heading(1, text='ID', anchor=CENTER)
        self.lista.heading(2, text='Nombre', anchor=CENTER)
        self.lista.heading(3, text='Apellido', anchor=CENTER)
        self.lista.grid(padx=10, column=0, row=2,columnspan=5)
        ttk.Button(self.root_en_pantalla,text ='Nuevo prestamo',command=lambda:self.capturando_datos(
            self.entry_nombre,self.id_cliente)).grid(column=0,row=3,sticky='we')
        
        elemnt = self.b.consultar_data('Cod_cliente,Nombre,Apellido','clientes') # llamando al metodo consutar de la  clase Base
        # este codigo pasa linea por linea del Tree para insertar los valores del elemnt
        for row in elemnt: 
            self.lista.insert('', 'end', values=row)
        
    def reload(self):
        elemnt = self.b.consultar_data('Cod_cliente,Nombre,Apellido','clientes')
        self.lista.delete(*self.lista.get_children()) 
        for row in elemnt: 
            self.lista.insert('', 'end', values=row)

    def menus(self):
      # menú bar para obciones
      # ARCHIVOS
        menu = Menu(self.root)
        menu_archivos = Menu(menu, tearoff=0)
        menu_archivos.add_command(label='Tabla', command=self.clientes_tap)
        menu_archivos.add_command(label='Nuevo')
        menu.add_cascade(label='Archivo', menu=menu_archivos)
      # CLIENTE
        menu_cliente = Menu(menu, tearoff=0)
        menu_cliente.add_command(label='Nuevo cliente', command = None ) #nuevo_cliente
        menu_cliente.add_command(label='Modificar cliente')
        menu.add_cascade(label='Clientes', menu=menu_cliente)
      # PRESTAMOS
        m_prestamo = Menu(menu, tearoff=0)
        m_prestamo.add_command(label='Nuevo préstamo', command =None )# nuevo_prestamo
        m_prestamo.add_command(label='Modificar Préstamo')
        m_prestamo.add_command(label='Abonados', command=self.abonos) #abonado
        m_prestamo.add_command(label='Modificar abono',command=None) #mod_abono
        menu.add_cascade(label='Préstamos', menu=m_prestamo)
      # AYUDA
        m_ayuda = Menu(menu, tearoff=0)
        m_ayuda.add_command(label='Acerca de')
        m_ayuda.add_command(label='Contacto')
        
        self.root.config(menu=menu)

    def abonos(self):
      ############################################# Config de ventana
        self.root.iconify()
        root_Devolucion = tk.Toplevel(self.root)
        root_Devolucion.title('Registro de devolucion')
        #root_Devolucion.geometry('400x300')
        root_Devolucion.resizable(0, 0)
        root_Devolucion.transient()  # este metodo dibuja la ventana por encima de la ventana madre
        root_Devolucion.grab_set()

        id_cliente_abo = tk.IntVar()
        id_prestamo_abo = tk.IntVar()
        fecha_abono = tk.StringVar()
        monto_abono = tk.IntVar()
        interes = tk.IntVar()

        Frame_dev_prin = ttk.Frame(root_Devolucion)
        Frame_dev_prin.grid(row=0, column=0)

        frame_datos = ttk.Frame(Frame_dev_prin)
        frame_datos.grid(padx=10, pady=10, row=0, column=0, sticky='nsew')
      ################################################################################ seccion datos cliente
        ttk.Label(frame_datos, text='Nombre completo').grid(row=0, column=0)
        self.entry_nombre_abono = ttk.Entry(frame_datos, state='normal')                       
        self.entry_nombre_abono.grid(ipadx=150, row=0, column=1, columnspan=6, sticky='ew')
      ################################################################################ seccion deuda
        ttk.Label(frame_datos, text='Deuda actual').grid(row=1, column=0,sticky='ew')
        self.entry_deuda_abono = ttk.Entry(frame_datos)                          
        self.entry_deuda_abono.grid(pady=5, row=1, column=1, columnspan=2, sticky='ew')
      ################################################################################ seccion codigo cliente
        ttk.Label(frame_datos, text='Cod. Cliente:').grid(row = 2, column = 2)
        self.entry_id_cliente_abono = ttk.Entry(frame_datos,textvariable=id_cliente_abo)                            
        self.entry_id_cliente_abono.grid(column=3,row = 2)
      ################################################################################ seccion codigo prestamo
        ttk.Label(frame_datos, text='Cod. Prestamo:').grid(row = 2, column = 0, sticky='w')
        self.entry_id_prestamo_abono = ttk.Entry(frame_datos, textvariable=id_prestamo_abo)                                   
        self.entry_id_prestamo_abono.grid(column=1,row = 2,sticky='w')
      ###################################################################### Seccion de amortizacion
        ttk.Separator(Frame_dev_prin, orient='horizontal').grid(pady=20, padx=20, row=2, column=0, columnspan=7, sticky='ew')

        # frame_fecha = ttk.Frame(Frame_dev_prin)
        # frame_fecha.grid(padx=70, pady=20, row=3, column=0)

        # ttk.Label(frame_fecha, text='Fecha amortizacion').grid(row=0, column=0)
        # self.entry_fecha_abono = ttk.Entry(frame_fecha,textvariable = fecha_abono)
        # self.entry_fecha_abono.grid(row=0, column=1)

        # ttk.Label(frame_fecha, text='Monto de cuota').grid(padx=10, row=0, column=2)
        # self.entry_monto_abono = ttk.Entry(frame_fecha, width=10,textvariable=monto_abono)
        # self.entry_monto_abono.grid(row=0, column=3)
      ######################################################################  datos de cuota esperada

        frame_cuo = ttk.LabelFrame(Frame_dev_prin, text='Cuotas')
        frame_cuo.grid(ipady=5, padx=50, pady=10, row=5,
                 column=0, columnspan=6, sticky='nsew')
        
        ttk.Label(frame_cuo, text = 'Monto a bonar').grid(padx=30,row=0, column=0)
        self.En_Cuota_abono = ttk.Entry(frame_cuo, textvariable= monto_abono)
        self.En_Cuota_abono.grid(row=0, column=1)
        
        ttk.Label(frame_cuo, text = 'Interes').grid(row=0, column=2)
        self.En_Cuota_abono = ttk.Entry(frame_cuo, textvariable= interes)
        self.En_Cuota_abono.grid(row=0, column=3)
      ##################################################################### detalles de amortizacion
        frame_interes = ttk.Frame(Frame_dev_prin)
        frame_interes.grid(padx=50, pady=20, row=6, column=0, columnspan=6, sticky='nsew')

        ttk.Label(frame_interes, text='Detalles',font = self.fuente).grid(row=0, column=0, sticky='w')
        self.entry_detalle_abono = tk.Text(frame_interes, height=3, width= 30)
        self.entry_detalle_abono.grid(row=1, column=0)
      ##################################################################### botones finales
        style = ttk.Style()
        style.configure('N.TFrame', background='light gray')
        frame_botone = ttk.Frame(Frame_dev_prin, style='N.TFrame')
        frame_botone.grid(padx=15, pady=4, row=7, column=0, columnspan=6, sticky='nsew')

        boton_limpiar = ttk.Button(frame_botone, text='Limpiar', command = lambda : limpiar(self.entry_nombre_abono,self.entry_deuda_abono,
                                                                                entry_monto,entry_detalle,entry_fecha))
        boton_limpiar.grid(padx=100, pady=5, row=0, column=0)

        boton_guardar = ttk.Button(frame_botone, text='Guardar')
        boton_guardar.grid(padx=50, pady=5, row=0, column=4)

        boton_cancelar = ttk.Button(frame_botone, text='Cancelar', comman =lambda: destruir(root_Devolucion,self.root))
        boton_cancelar.grid(padx=8, pady=5, row=0, column=5)

    def mostra_en_tabla(self,valor):
        self.lista.delete(*self.lista.get_children())
        for i in self.b.filtar_nombre(valor):
            self.lista.insert('', 'end', values=i)

    def insert_data_amortizacion(self,cod_prestamo,id_cliente,fecha_abono,monto_abono):

        self.b.insertar_data_abono(cod_prestamo,id_cliente,fecha_abono,monto_abono)
    
   
if __name__ == '__main__':
    venta = Principal()
    