from tkinter import Entry, Label, Frame, Tk, Button,ttk, Scrollbar, VERTICAL, HORIZONTAL,StringVar,END
import tkinter as tk
from tkinter import ttk
from conexion import*
from analitico import *
from tkinter import * 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from pandas import DataFrame

class Registro(Frame):

    def __init__(self, master):
        super().__init__(master)

        self.cuaderno1 = ttk.Notebook(self.master)

        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Sucursal") 
        self.cuaderno1.add(self.pagina2, text="Empleado")
        self.cuaderno1.add(self.pagina3, text="Usuarios")
        self.cuaderno1.add(self.pagina4, text="Vehiculos")

        self.frame1 = Frame(self.pagina1)
        self.frame1.grid(columnspan=2, column=0,row=0)
        self.frame2 = Frame(self.pagina1, bg='navy')
        self.frame2.grid(column=0, row=1)
        self.frame3 = ttk.Frame(self.pagina1)
        self.frame3.grid(rowspan=2, column=1, row=1)

        self.frame4 = Frame(self.pagina1, bg='black')
        self.frame4.grid(column=0, row=2)

        self.frame5 = Frame(self.pagina2)
        self.frame5.grid(columnspan=2, column=0,row=0)
        self.frame6 = Frame(self.pagina2, bg='navy')
        self.frame6.grid(column=0, row=1)
        self.frame7 = ttk.Frame(self.pagina2)
        self.frame7.grid(rowspan=2, column=1, row=1)

        self.frame8 = Frame(self.pagina2, bg='black')
        self.frame8.grid(column=0, row=2)

        self.frame9 = Frame(self.pagina3)
        self.frame9.grid(columnspan=2, column=0,row=0)
        self.frame10 = Frame(self.pagina3, bg='navy')
        self.frame10.grid(column=0, row=1)
        self.frame11 = ttk.Frame(self.pagina3)
        self.frame11.grid(rowspan=2, column=1, row=1)

        self.frame12 = Frame(self.pagina3, bg='black')
        self.frame12.grid(column=0, row=2)

        self.frame13 = Frame(self.pagina4)
        self.frame13.grid(columnspan=2, column=0,row=0)
        self.frame14 = Frame(self.pagina4, bg='navy')
        self.frame14.grid(column=0, row=1)
        self.frame15 = ttk.Frame(self.pagina4)
        self.frame15.grid(rowspan=2, column=1, row=1)

        self.frame16 = Frame(self.pagina4, bg='black')
        self.frame16.grid(column=0, row=2)

        self.codigo_sucur = StringVar()
        self.nombre_sucur = StringVar()
        self.modelo_sucur = StringVar()
        self.precio_sucur = StringVar()
        self.cantidad_sucur = StringVar()
        self.buscar_sucur = StringVar()

        self.codigo_emple = StringVar()
        
        #####
        self.nombre_emple = StringVar()
        self.cargo_emple = StringVar()
        self.sueldo_emple = StringVar()
        self.idsucursal_emple = StringVar()
        self.telefono_emple = StringVar()
        self.direccion_emple = StringVar()
        self.cedula_emple = StringVar()
        self.buscar_emple = StringVar()
        #####
        self.nombre_usua = StringVar()
        self.td_usua = StringVar()
        self.nd_usua = StringVar()
        self.ciudad_usua = StringVar()
        self.telefono_usua = StringVar()
        self.direccion_usua = StringVar()
        self.buscar_usua = StringVar()
        #####
        self.placa_vehi = StringVar()
        self.tipo_vehi = StringVar()
        self.idempleado_vehi = StringVar()
        self.modelo_vehi = StringVar()
        self.buscar_vehi = StringVar()
        #####
        self.base_datos = Registro_datos()

        self.create_wietgs_page1()
        self.create_wietgs_page2()
        self.create_wietgs_page3()
        self.create_wietgs_page4()

        # Añadirlas al panel con su respectivo texto.
        #self.notebook.add(self, text="Sucursal", padding=20)
        #self.notebook.add(self.forum_label, text="Foro", padding=20)

        #self.notebook.pack(padx=10, pady=10)
        #self.pack()

        self.cuaderno1.grid(column=0, row=0)

    def create_wietgs_page1(self):

        Label(self.frame1, text = 'R E G I S T R O \t D E \t D A T O S\t S U C U R S A L E S',bg='gray22',fg='white', font=('Orbitron',15,'bold')).grid(column=0, row=0)
        
        Label(self.frame2, text = 'Agregar Nuevos Datos',fg='white', bg ='navy', font=('Rockwell',12,'bold')).grid(columnspan=2, column=0,row=0, pady=5)
        Label(self.frame2, text = 'Ciudad',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=1, pady=15)
        Label(self.frame2, text = 'Dirección',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=15)
        Label(self.frame2, text = 'Telefono',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=15)
        #Label(self.frame2, text = 'Responsable', fg='white',bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=15)
        Label(self.frame2, text = 'ID_Sucursal',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)

        Entry(self.frame2,textvariable=self.codigo_sucur , font=('Arial',12)).grid(column=1,row=1, padx =5)
        Entry(self.frame2,textvariable=self.nombre_sucur , font=('Arial',12)).grid(column=1,row=2)
        Entry(self.frame2,textvariable=self.modelo_sucur , font=('Arial',12)).grid(column=1,row=3)
        #Entry(self.frame2,textvariable=self.precio_sucur , font=('Arial',12)).grid(column=1,row=4)
        Entry(self.frame2,textvariable=self.cantidad_sucur , font=('Arial',12)).grid(column=1,row=5)
       
        Label(self.frame4, text = 'Consultas',fg='white', bg ='black', font=('Rockwell',12,'bold')).grid(columnspan=3, column=0,row=0, pady=1, padx=4)         
        Button(self.frame4,command= self.agregar_datos_sucur, text='REGISTRAR', font=('Arial',10,'bold'), bg='magenta2').grid(column=0,row=1, pady=10, padx=4)
        Button(self.frame4,command = self.limpiar_datos_sucur, text='LIMPIAR', font=('Arial',10,'bold'), bg='orange red').grid(column=1,row=1, padx=10)        
        Button(self.frame4,command = self.eliminar_fila_sucur, text='ELIMINAR', font=('Arial',10,'bold'), bg='yellow').grid(column=2,row=1, padx=4)
        Button(self.frame4,command = self.buscar_nombre_sucur, text='BUSCAR POR CIUDAD', font=('Arial',8,'bold'), bg='orange').grid(columnspan=2,column = 1, row=2)
        Entry(self.frame4,textvariable=self.buscar_sucur , font=('Arial',12), width=10).grid(column=0,row=2, pady=1, padx=8)
        Button(self.frame4,command = self.mostrar_todo_sucur, text='MOSTRAR TODOS LOS DATOS', font=('Arial',10,'bold'), bg='green2').grid(columnspan=3,column=0,row=3, pady=8)

        self.tabla_sucur = ttk.Treeview(self.frame3, height=21)
        self.tabla_sucur.grid(column=0, row=0)

        ladox_sucur = Scrollbar(self.frame3, orient = HORIZONTAL, command= self.tabla_sucur.xview)
        ladox_sucur.grid(column=0, row = 1, sticky='ew') 
        ladoy_sucur = Scrollbar(self.frame3, orient =VERTICAL, command = self.tabla_sucur.yview)
        ladoy_sucur.grid(column = 1, row = 0, sticky='ns')

        self.tabla_sucur.configure(xscrollcommand = ladox_sucur.set, yscrollcommand = ladoy_sucur.set)
       
        self.tabla_sucur['columns'] = ('Ciudad','Nombre', 'Precio')

        self.tabla_sucur.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla_sucur.column('Ciudad', minwidth=100, width=130 , anchor='center')
        self.tabla_sucur.column('Nombre', minwidth=100, width=130 , anchor='center')
        #self.tabla_sucur.column('Modelo', minwidth=100, width=120, anchor='center' )
        self.tabla_sucur.column('Precio', minwidth=100, width=120 , anchor='center')
        #self.tabla_sucur.column('Cantidad', minwidth=100, width=105, anchor='center')

        self.tabla_sucur.heading('#0', text='idSucursal', anchor ='center')
        self.tabla_sucur.heading('Ciudad', text='Ciudad', anchor ='center')
        self.tabla_sucur.heading('Nombre', text='Dirección', anchor ='center')
        #self.tabla_sucur.heading('Modelo', text='Telefono', anchor ='center')
        self.tabla_sucur.heading('Precio', text='Telefono', anchor ='center')
        #self.tabla_sucur.heading('Cantidad', text='SucursalCol', anchor ='center')

        estilo_sucur = ttk.Style(self.frame3)
        estilo_sucur.theme_use('alt') #  ('clam', 'alt', 'default', 'classic')
        estilo_sucur.configure(".",font= ('Helvetica', 12, 'bold'), foreground='red2')        
        estilo_sucur.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black',  background='white')
        estilo_sucur.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

        self.tabla_sucur.bind("<<TreeviewSelect>>", self.obtener_fila_sucur)  # seleccionar  fila

    def create_wietgs_page2(self):

        Label(self.frame5, text = 'R E G I S T R O \t D E \t D A T O S\t E M P L E A D O S',bg='gray22',fg='white', font=('Orbitron',15,'bold')).grid(column=0, row=0)
        
        Label(self.frame6, text = 'Agregar Nuevos Datos',fg='white', bg ='navy', font=('Rockwell',12,'bold')).grid(columnspan=2, column=0,row=0, pady=5)
        Label(self.frame6, text = 'Nombre',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=1, pady=15)
        Label(self.frame6, text = 'Cargo',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=15)
        Label(self.frame6, text = 'Sueldo',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=15)
        Label(self.frame6, text = 'idSucursal', fg='white',bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=15)
        Label(self.frame6, text = 'Telefono',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)
        Label(self.frame6, text = 'Direccion',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=6, pady=15)
        Label(self.frame6, text = 'Cedula',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=7, pady=15)

        Entry(self.frame6,textvariable=self.nombre_emple , font=('Arial',12)).grid(column=1,row=1, padx =5)
        Entry(self.frame6,textvariable=self.cargo_emple , font=('Arial',12)).grid(column=1,row=2)
        Entry(self.frame6,textvariable=self.sueldo_emple , font=('Arial',12)).grid(column=1,row=3)
        Entry(self.frame6,textvariable=self.idsucursal_emple , font=('Arial',12)).grid(column=1,row=4)
        Entry(self.frame6,textvariable=self.telefono_emple , font=('Arial',12)).grid(column=1,row=5)
        Entry(self.frame6,textvariable=self.direccion_emple , font=('Arial',12)).grid(column=1,row=6)
        Entry(self.frame6,textvariable=self.cedula_emple , font=('Arial',12)).grid(column=1,row=7)
       
        Label(self.frame8, text = 'Consultas',fg='white', bg ='black', font=('Rockwell',12,'bold')).grid(columnspan=3, column=0,row=0, pady=1, padx=4)         
        Button(self.frame8,command= self.agregar_datos_emple, text='REGISTRAR', font=('Arial',10,'bold'), bg='magenta2').grid(column=0,row=1, pady=10, padx=4)
        Button(self.frame8,command = self.limpiar_datos_emple, text='LIMPIAR', font=('Arial',10,'bold'), bg='orange red').grid(column=1,row=1, padx=10)        
        Button(self.frame8,command = self.eliminar_fila_emple, text='ELIMINAR', font=('Arial',10,'bold'), bg='yellow').grid(column=2,row=1, padx=4)
        Button(self.frame8,command = self.buscar_nombre_emple, text='BUSCAR POR Id Empleado', font=('Arial',8,'bold'), bg='orange').grid(columnspan=2,column = 1, row=2)
        Entry(self.frame8,textvariable=self.buscar_emple , font=('Arial',12), width=10).grid(column=0,row=2, pady=1, padx=8)
        Button(self.frame8,command = self.mostrar_todo_emple, text='MOSTRAR TODOS LOS DATOS', font=('Arial',10,'bold'), bg='green2').grid(columnspan=3,column=0,row=3, pady=8)
        Button(self.frame8,command = self.analitica_emple, text='GRAFICA DE LOS DATOS', font=('Arial',10,'bold'), bg='orange red').grid(columnspan=3,column=0,row=4, pady=8)

        self.tabla_emple = ttk.Treeview(self.frame7, height=21)
        self.tabla_emple.grid(column=0, row=0)

        ladox_emple = Scrollbar(self.frame7, orient = HORIZONTAL, command= self.tabla_emple.xview)
        ladox_emple.grid(column=0, row = 1, sticky='ew') 
        ladoy_emple = Scrollbar(self.frame7, orient =VERTICAL, command = self.tabla_emple.yview)
        ladoy_emple.grid(column = 1, row = 0, sticky='ns')

        self.tabla_emple.configure(xscrollcommand = ladox_emple.set, yscrollcommand = ladoy_emple.set)
       
        self.tabla_emple['columns'] = ('Nombre', 'Cargo', 'Sueldo', 'idSucursal', 'Telefono', 'Direccion', 'Cedula')

        self.tabla_emple.column('#0', minwidth=100, width=120, anchor='center')
        #self.tabla.column('idEmpleado', minwidth=100, width=130 , anchor='center')
        self.tabla_emple.column('Nombre', minwidth=100, width=130 , anchor='center')
        self.tabla_emple.column('Cargo', minwidth=100, width=120, anchor='center' )
        self.tabla_emple.column('Sueldo', minwidth=100, width=120 , anchor='center')
        self.tabla_emple.column('idSucursal', minwidth=100, width=105, anchor='center')
        self.tabla_emple.column('Telefono', minwidth=100, width=120, anchor='center' )
        self.tabla_emple.column('Direccion', minwidth=100, width=120 , anchor='center')
        self.tabla_emple.column('Cedula', minwidth=100, width=105, anchor='center')

        self.tabla_emple.heading('#0', text='idEmpleado', anchor ='center')
        #self.tabla.heading('idEmpleado', text='Ciudad', anchor ='center')
        self.tabla_emple.heading('Nombre', text='Nombre', anchor ='center')
        self.tabla_emple.heading('Cargo', text='Cargo', anchor ='center')
        self.tabla_emple.heading('Sueldo', text='Sueldo', anchor ='center')
        self.tabla_emple.heading('idSucursal', text='idSucursal', anchor ='center')
        self.tabla_emple.heading('Telefono', text='Telefono', anchor ='center')
        self.tabla_emple.heading('Direccion', text='Direccion', anchor ='center')
        self.tabla_emple.heading('Cedula', text='Cedula', anchor ='center')

        estilo_emple = ttk.Style(self.frame7)
        estilo_emple.theme_use('alt') #  ('clam', 'alt', 'default', 'classic')
        estilo_emple.configure(".",font= ('Helvetica', 12, 'bold'), foreground='red2')        
        estilo_emple.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black',  background='white')
        estilo_emple.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

        self.tabla_emple.bind("<<TreeviewSelect>>", self.obtener_fila_emple)  # seleccionar  fila
        
    def create_wietgs_page3(self):

        Label(self.frame9, text = 'R E G I S T R O \t D E \t D A T O S\t U S U A R I O S',bg='gray22',fg='white', font=('Orbitron',15,'bold')).grid(column=0, row=0)
        
        Label(self.frame10, text = 'Agregar Nuevos Datos',fg='white', bg ='navy', font=('Rockwell',12,'bold')).grid(columnspan=2, column=0,row=0, pady=5)
        Label(self.frame10, text = 'Nombre',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=1, pady=15)
        Label(self.frame10, text = 'Tipo Doc',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=15)
        Label(self.frame10, text = 'Num Doc',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=15)
        Label(self.frame10, text = 'Ciudad', fg='white',bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=15)
        Label(self.frame10, text = 'Telefono',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)
        Label(self.frame10, text = 'Direccion',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=6, pady=15)
        #Label(self.frame10, text = 'Cedula',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=7, pady=15)

        Entry(self.frame10,textvariable=self.nombre_usua , font=('Arial',12)).grid(column=1,row=1, padx =5)
        Entry(self.frame10,textvariable=self.td_usua , font=('Arial',12)).grid(column=1,row=2)
        Entry(self.frame10,textvariable=self.nd_usua , font=('Arial',12)).grid(column=1,row=3)
        Entry(self.frame10,textvariable=self.ciudad_usua , font=('Arial',12)).grid(column=1,row=4)
        Entry(self.frame10,textvariable=self.telefono_usua , font=('Arial',12)).grid(column=1,row=5)
        Entry(self.frame10,textvariable=self.direccion_usua , font=('Arial',12)).grid(column=1,row=6)
        #Entry(self.frame10,textvariable=self.cedula_usua , font=('Arial',12)).grid(column=1,row=7)
       
        Label(self.frame12, text = 'Consultas',fg='white', bg ='black', font=('Rockwell',12,'bold')).grid(columnspan=3, column=0,row=0, pady=1, padx=4)         
        Button(self.frame12,command= self.agregar_datos_usua, text='REGISTRAR', font=('Arial',10,'bold'), bg='magenta2').grid(column=0,row=1, pady=10, padx=4)
        Button(self.frame12,command = self.limpiar_datos_usua, text='LIMPIAR', font=('Arial',10,'bold'), bg='orange red').grid(column=1,row=1, padx=10)        
        Button(self.frame12,command = self.eliminar_fila_usua, text='ELIMINAR', font=('Arial',10,'bold'), bg='yellow').grid(column=2,row=1, padx=4)
        Button(self.frame12,command = self.buscar_nombre_usua, text='BUSCAR POR #DOCUMENTO', font=('Arial',8,'bold'), bg='orange').grid(columnspan=2,column = 1, row=2)
        Entry(self.frame12,textvariable=self.buscar_usua , font=('Arial',12), width=10).grid(column=0,row=2, pady=1, padx=8)
        Button(self.frame12,command = self.mostrar_todo_usua, text='MOSTRAR TODOS LOS DATOS', font=('Arial',10,'bold'), bg='green2').grid(columnspan=3,column=0,row=3, pady=8)
        Button(self.frame12,command = self.analitica_usua, text='GRAFICA DE LOS DATOS', font=('Arial',10,'bold'), bg='orange red').grid(columnspan=3,column=0,row=4, pady=8)

        self.tabla_usua = ttk.Treeview(self.frame11, height=21)
        self.tabla_usua.grid(column=0, row=0)

        ladox_usua = Scrollbar(self.frame11, orient = HORIZONTAL, command= self.tabla_usua.xview)
        ladox_usua.grid(column=0, row = 1, sticky='ew') 
        ladoy_usua = Scrollbar(self.frame11, orient =VERTICAL, command = self.tabla_usua.yview)
        ladoy_usua.grid(column = 1, row = 0, sticky='ns')

        self.tabla_usua.configure(xscrollcommand = ladox_usua.set, yscrollcommand = ladoy_usua.set)
       
        self.tabla_usua['columns'] = ('Tipo de Documento', 'Nombre', 'Ciudad', 'Direccion', 'Telefono')

        self.tabla_usua.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla_usua.column('Tipo de Documento', minwidth=100, width=130 , anchor='center')
        self.tabla_usua.column('Nombre', minwidth=100, width=120, anchor='center' )
        self.tabla_usua.column('Ciudad', minwidth=100, width=120 , anchor='center')
        self.tabla_usua.column('Direccion', minwidth=100, width=120 , anchor='center')
        self.tabla_usua.column('Telefono', minwidth=100, width=120, anchor='center' )

        self.tabla_usua.heading('#0', text='No Documento', anchor ='center')
        self.tabla_usua.heading('Tipo de Documento', text='Tipo de Documento', anchor ='center')
        self.tabla_usua.heading('Nombre', text='Nombre', anchor ='center')
        self.tabla_usua.heading('Ciudad', text='Ciudad', anchor ='center')
        self.tabla_usua.heading('Direccion', text='Direccion', anchor ='center')
        self.tabla_usua.heading('Telefono', text='Telefono', anchor ='center')

        estilo_usua = ttk.Style(self.frame11)
        estilo_usua.theme_use('alt') #  ('clam', 'alt', 'default', 'classic')
        estilo_usua.configure(".",font= ('Helvetica', 12, 'bold'), foreground='red2')        
        estilo_usua.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black',  background='white')
        estilo_usua.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

        self.tabla_usua.bind("<<TreeviewSelect>>", self.obtener_fila_usua)  # seleccionar  fila

    def create_wietgs_page4(self):

        Label(self.frame13, text = 'R E G I S T R O \t D E \t D A T O S\t V E H I C U L O S',bg='gray22',fg='white', font=('Orbitron',15,'bold')).grid(column=0, row=0)
        
        Label(self.frame14, text = 'Agregar Nuevos Datos',fg='white', bg ='navy', font=('Rockwell',12,'bold')).grid(columnspan=2, column=0,row=0, pady=5)
        Label(self.frame14, text = 'Placa',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=1, pady=15)
        Label(self.frame14, text = 'Tipo',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=15)
        Label(self.frame14, text = 'idEmpleados',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=15)
        Label(self.frame14, text = 'Modelo', fg='white',bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=15)
        #Label(self.frame14, text = 'Telefono',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)
        #Label(self.frame14, text = 'Direccion',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=6, pady=15)
        #Label(self.frame10, text = 'Cedula',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=7, pady=15)

        Entry(self.frame14,textvariable=self.placa_vehi , font=('Arial',12)).grid(column=1,row=1, padx =5)
        Entry(self.frame14,textvariable=self.tipo_vehi , font=('Arial',12)).grid(column=1,row=2)
        Entry(self.frame14,textvariable=self.idempleado_vehi , font=('Arial',12)).grid(column=1,row=3)
        Entry(self.frame14,textvariable=self.modelo_vehi , font=('Arial',12)).grid(column=1,row=4)
        #Entry(self.frame14,textvariable=self.telefono_usua , font=('Arial',12)).grid(column=1,row=5)
        #Entry(self.frame14,textvariable=self.direccion_usua , font=('Arial',12)).grid(column=1,row=6)
        #Entry(self.frame10,textvariable=self.cedula_usua , font=('Arial',12)).grid(column=1,row=7)
       
        Label(self.frame16, text = 'Consultas',fg='white', bg ='black', font=('Rockwell',12,'bold')).grid(columnspan=3, column=0,row=0, pady=1, padx=4)         
        Button(self.frame16,command= self.agregar_datos_vehi, text='REGISTRAR', font=('Arial',10,'bold'), bg='magenta2').grid(column=0,row=1, pady=10, padx=4)
        Button(self.frame16,command = self.limpiar_datos_vehi, text='LIMPIAR', font=('Arial',10,'bold'), bg='orange red').grid(column=1,row=1, padx=10)        
        Button(self.frame16,command = self.eliminar_fila_vehi, text='ELIMINAR', font=('Arial',10,'bold'), bg='yellow').grid(column=2,row=1, padx=4)
        Button(self.frame16,command = self.buscar_nombre_vehi, text='BUSCAR POR PLACA', font=('Arial',8,'bold'), bg='orange').grid(columnspan=2,column = 1, row=2)
        Entry(self.frame16,textvariable=self.buscar_vehi , font=('Arial',12), width=10).grid(column=0,row=2, pady=1, padx=8)
        Button(self.frame16,command = self.mostrar_todo_vehi, text='MOSTRAR TODOS LOS DATOS', font=('Arial',10,'bold'), bg='green2').grid(columnspan=3,column=0,row=3, pady=8)
        #Button(self.frame16,command = self.analitica_usua, text='GRAFICA DE LOS DATOS', font=('Arial',10,'bold'), bg='orange red').grid(columnspan=3,column=0,row=4, pady=8)

        self.tabla_vehi = ttk.Treeview(self.frame15, height=21)
        self.tabla_vehi.grid(column=0, row=0)

        ladox_vehi = Scrollbar(self.frame15, orient = HORIZONTAL, command= self.tabla_vehi.xview)
        ladox_vehi.grid(column=0, row = 1, sticky='ew') 
        ladoy_vehi = Scrollbar(self.frame15, orient =VERTICAL, command = self.tabla_vehi.yview)
        ladoy_vehi.grid(column = 1, row = 0, sticky='ns')

        self.tabla_usua.configure(xscrollcommand = ladox_vehi.set, yscrollcommand = ladoy_vehi.set)
       
        self.tabla_vehi['columns'] = ( 'Tipo', 'idEmpleado', 'Modelo')

        self.tabla_vehi.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla_vehi.column('Tipo', minwidth=100, width=130 , anchor='center')
        self.tabla_vehi.column('idEmpleado', minwidth=100, width=120, anchor='center' )
        self.tabla_vehi.column('Modelo', minwidth=100, width=120 , anchor='center')

        self.tabla_vehi.heading('#0', text='Placa', anchor ='center')
        self.tabla_vehi.heading('Tipo', text='Tipo', anchor ='center')
        self.tabla_vehi.heading('idEmpleado', text='idEmpleado', anchor ='center')
        self.tabla_vehi.heading('Modelo', text='Modelo', anchor ='center')

        estilo_vehi = ttk.Style(self.frame15)
        estilo_vehi.theme_use('alt') #  ('clam', 'alt', 'default', 'classic')
        estilo_vehi.configure(".",font= ('Helvetica', 12, 'bold'), foreground='red2')        
        estilo_vehi.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black',  background='white')
        estilo_vehi.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

        self.tabla_vehi.bind("<<TreeviewSelect>>", self.obtener_fila_vehi)  # seleccionar  fila

    def grafica_barras_circular(self, x, y, t):

        # Crear una ventana secundaria.
        ventana_secundaria = tk.Toplevel()
        ventana_secundaria.title("Graficos")
        ventana_secundaria.config(width=700, height=425)

        framegraficos = ttk.Frame(ventana_secundaria, width="600", height="600")
        framegraficos.place(x=10,y=10)

        Data1 = {'Ciudades': x, t: y}
        df1 = DataFrame(Data1, columns= ['Ciudades', t])
        df1 = df1[['Ciudades', t]].groupby('Ciudades').sum()

        #Crear Gráfico de barras:
        grafico1 = plt.Figure(figsize=(8,8), dpi=50)
        barras = grafico1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(grafico1, framegraficos)
        bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
        df1.plot(kind='bar', legend=True, ax=barras)
        barras.set_title('Cantidad Por Ciudad')

        #crear grafico circular/pastel
        grafico2 = plt.Figure(figsize=(6,6), dpi=50)
        circulo = grafico2.add_subplot(111)
        circulo.pie(y, labels=x, autopct='%1.1f%%', shadow=True, startangle=90)
        pie1 = FigureCanvasTkAgg(grafico2, framegraficos) 
        pie1.get_tk_widget().pack()
        circulo.set_title("Porcentaje Nacional")

#####################################

    def agregar_datos_sucur(self):
        self.tabla_sucur.get_children()
        codigo = self.codigo_sucur.get()
        id_sucur= self.cantidad_sucur.get()
        nombre = self.nombre_sucur.get()
        precio = self.modelo_sucur.get()
        datos = (  codigo, nombre, precio)
        if codigo and id_sucur and nombre and precio !='':        
            self.tabla_sucur.insert('',0, text = id_sucur, values=datos)
            self.base_datos.inserta_producto( codigo, id_sucur, nombre, precio)

    def limpiar_datos_sucur(self):
        self.tabla_sucur.delete(*self.tabla_sucur.get_children())
        self.codigo_sucur.set('')
        self.nombre_sucur.set('')
        self.modelo_sucur.set('')
        self.precio_sucur.set('')
        self.cantidad_sucur.set('')

    def buscar_nombre_sucur(self):
        nombre_producto = self.buscar_sucur.get()
        nombre_producto = str("'" + nombre_producto + "'")
        nombre_buscado = self.base_datos.busca_producto(nombre_producto)
        self.tabla_sucur.delete(*self.tabla_sucur.get_children())
        i = -1
        for dato in nombre_buscado:
            i= i+1                       
            self.tabla_sucur.insert('',i, text = nombre_buscado[i][0:1], values=nombre_buscado[i][1:4])

    def mostrar_todo_sucur(self):
        self.tabla_sucur.delete(*self.tabla_sucur.get_children())
        registro = self.base_datos.mostrar_productos()
        i = -1
        for dato in registro:
            i= i+1                       
            self.tabla_sucur.insert('',i, text = registro[i][0:1], values=registro[i][1:4])

    def eliminar_fila_sucur(self):
        fila = self.tabla_sucur.selection()
        if len(fila) !=0:        
            self.tabla_sucur.delete(fila)
            nombre = (self.nombre_borar)       
            self.base_datos.elimina_productos(nombre)

    def obtener_fila_sucur(self, event):
        current_item = self.tabla_sucur.focus()
        if not current_item:
            return
        #print(current_item)
        data = self.tabla_sucur.item(current_item)
        print(data['text'])
        self.nombre_borar = data['text']
        #['values'][0]

########################

    def agregar_datos_emple(self):
        self.tabla_emple.get_children()
        nombre_emple = self.nombre_emple.get()
        cargo_emple = self.cargo_emple.get()
        sueldo_emple = self.sueldo_emple.get()
        idsucursal_emple = self.idsucursal_emple.get()
        telefono_emple = self.telefono_emple.get()
        direccion_emple = self.direccion_emple.get()
        cedula_emple = self.cedula_emple.get()
        datos = ( nombre_emple, cargo_emple, sueldo_emple, idsucursal_emple, telefono_emple, direccion_emple, cedula_emple)
        if nombre_emple and cargo_emple and sueldo_emple and idsucursal_emple and telefono_emple and direccion_emple and cedula_emple !='':        
            self.base_datos.inserta_producto2(nombre_emple, cargo_emple, sueldo_emple, idsucursal_emple, telefono_emple, direccion_emple, cedula_emple)
            self.tabla_emple.delete(*self.tabla_emple.get_children())
            registro = self.base_datos.mostrar_productos2()
            i = -1
            for dato in registro:
                i= i+1                       
                self.tabla_emple.insert('',i, text = registro[i][0:1], values=registro[i][1:8])
            #self.tabla_emple.insert('',0, text = id_emple, values=datos)

    def limpiar_datos_emple(self):
        self.tabla_emple.delete(*self.tabla_emple.get_children())
        self.codigo_sucur.set('')
        self.nombre_sucur.set('')
        self.modelo_sucur.set('')
        self.precio_sucur.set('')
        self.cantidad_sucur.set('')

    def buscar_nombre_emple(self):
        nombre_producto = self.buscar_emple.get()
        nombre_producto = str("'" + nombre_producto + "'")
        nombre_buscado = self.base_datos.busca_producto2(nombre_producto)
        self.tabla_emple.delete(*self.tabla_emple.get_children())
        i = -1
        for dato in nombre_buscado:
            i= i+1                       
            self.tabla_emple.insert('',i, text = nombre_buscado[i][0:1], values=nombre_buscado[i][1:8])

    def mostrar_todo_emple(self):
        self.tabla_emple.delete(*self.tabla_emple.get_children())
        registro = self.base_datos.mostrar_productos2()
        i = -1
        for dato in registro:
            i= i+1                       
            self.tabla_emple.insert('',i, text = registro[i][0:1], values=registro[i][1:8])

    def eliminar_fila_emple(self):
        fila = self.tabla_emple.selection()
        if len(fila) !=0:        
            self.tabla_emple.delete(fila)
            nombre = ("'"+ str(self.nombre_borar) + "'")       
            self.base_datos.elimina_productos2(nombre)

    def obtener_fila_emple(self, event):
        current_item = self.tabla_emple.focus()
        if not current_item:
            return
        data = self.tabla_emple.item(current_item)
        #print(data['values'][0])
        self.nombre_borar = data['text']

    def analitica_emple(self):
        data=self.base_datos.grafica_empleados()
        i=-1
        label_graf = []
        dato_graf = []
        tipo='Empleados'
        for x in data:
            i=i+1
            label_graf.append(data[i][0])
            dato_graf.append(data[i][1])
        print(label_graf)
        print(dato_graf)
        self.grafica_barras_circular(label_graf, dato_graf, tipo)    

########################

    def agregar_datos_usua(self):
        self.tabla_usua.get_children()
        nombre_usua=self.nombre_usua.get()
        td_usua=self.td_usua.get()
        nd_usua=self.nd_usua.get()
        ciudad_usua=self.ciudad_usua.get()
        telefono_usua=self.telefono_usua.get()
        direccion_usua=self.direccion_usua.get()
        
        datos = ( td_usua, nombre_usua, ciudad_usua, direccion_usua , telefono_usua)
        if td_usua and nd_usua and nombre_usua and ciudad_usua and direccion_usua and telefono_usua !='':        
            self.base_datos.inserta_producto3(nd_usua, td_usua, nombre_usua, ciudad_usua, direccion_usua, telefono_usua)
            self.tabla_usua.insert('',0, text = nd_usua, values=datos)

    def limpiar_datos_usua(self):
        self.tabla_emple.delete(*self.tabla_emple.get_children())
        self.codigo_sucur.set('')
        self.nombre_sucur.set('')
        self.modelo_sucur.set('')
        self.precio_sucur.set('')
        self.cantidad_sucur.set('')

    def buscar_nombre_usua(self):
        nombre_producto = self.buscar_usua.get()
        nombre_producto =  nombre_producto 
        nombre_buscado = self.base_datos.busca_producto3(nombre_producto)
        self.tabla_usua.delete(*self.tabla_usua.get_children())
        i = -1
        for dato in nombre_buscado:
            i= i+1                       
            self.tabla_usua.insert('',i, text = nombre_buscado[i][0:1], values=nombre_buscado[i][1:7])

    def mostrar_todo_usua(self):
        self.tabla_usua.delete(*self.tabla_usua.get_children())
        registro = self.base_datos.mostrar_productos3()
        i = -1
        for dato in registro:
            i= i+1                       
            self.tabla_usua.insert('',i, text = registro[i][0:1], values=registro[i][1:7])

    def eliminar_fila_usua(self):
        fila = self.tabla_usua.selection()
        if len(fila) !=0:        
            self.tabla_usua.delete(fila)
            nombre = (self.nombre_borar)       
            self.base_datos.elimina_productos3(nombre)

    def obtener_fila_usua(self, event):
        current_item = self.tabla_usua.focus()
        if not current_item:
            return
        data = self.tabla_usua.item(current_item)
        #print(data['values'][0])
        print(data['text'])
        self.nombre_borar = data['text']

    def analitica_usua(self):
        data=self.base_datos.grafica_usuarios()
        i=-1
        label_graf = []
        dato_graf = []
        tipo='Usuarios'
        for x in data:
            i=i+1
            label_graf.append(data[i][0])
            dato_graf.append(data[i][1])
        print(label_graf)
        print(dato_graf)
        self.grafica_barras_circular(label_graf, dato_graf, tipo)
        
#########################

    def agregar_datos_vehi(self):
        self.tabla_vehi.get_children()
        placa_vehi = self.placa_vehi.get()
        tipo_vehi = self.tipo_vehi.get()
        idempleado_vehi = self.idempleado_vehi.get()
        modelo_vehi = self.modelo_vehi.get()
        
        datos = ( tipo_vehi, idempleado_vehi, modelo_vehi)
        if placa_vehi and tipo_vehi and idempleado_vehi and modelo_vehi !='':        
            self.base_datos.inserta_producto4(placa_vehi, tipo_vehi, idempleado_vehi, modelo_vehi)
            self.tabla_vehi.insert('',0, text = placa_vehi, values=datos)

    def limpiar_datos_vehi(self):
        self.tabla_vehi.delete(*self.tabla_vehi.get_children())
        self.placa_vehi.set('')
        self.tipo_vehi.set('')
        self.idempleado_vehi.set('')
        self.modelo_vehi.set('')

    def buscar_nombre_vehi(self):
        nombre_producto = self.buscar_vehi.get()
        nombre_producto =  nombre_producto 
        nombre_buscado = self.base_datos.busca_producto4(nombre_producto)
        self.tabla_vehi.delete(*self.tabla_vehi.get_children())
        i = -1
        for dato in nombre_buscado:
            i= i+1                       
            self.tabla_vehi.insert('',i, text = nombre_buscado[i][0:1], values=nombre_buscado[i][1:5])

    def mostrar_todo_vehi(self):
        self.tabla_vehi.delete(*self.tabla_vehi.get_children())
        registro = self.base_datos.mostrar_productos4()
        i = -1
        for dato in registro:
            i= i+1                       
            self.tabla_vehi.insert('',i, text = registro[i][0:1], values=registro[i][1:5])

    def eliminar_fila_vehi(self):
        fila = self.tabla_vehi.selection()
        if len(fila) !=0:        
            self.tabla_vehi.delete(fila)
            nombre = (self.nombre_borar)       
            self.base_datos.elimina_productos4(nombre)

    def obtener_fila_vehi(self, event):
        current_item = self.tabla_vehi.focus()
        if not current_item:
            return
        data = self.tabla_vehi.item(current_item)
        #print(data['values'][0])
        print(data['text'])
        self.nombre_borar = data['text']

#########################

def main():
    ventana = Tk()
    ventana.wm_title("Datos Servientrega")
    ventana.config(bg='gray22')
    ventana.geometry('1150x650')
    ventana.resizable(0.1,0.1)
    app = Registro(ventana)
    app.mainloop()

if __name__=="__main__":
    main()        


