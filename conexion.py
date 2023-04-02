# Registro de datos en MySQL desde una GUI en TkInter
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren

import mysql.connector  #pip install mysql-connector-python
 
class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost',
                                            database ='parcial1_bases', 
                                            user = 'root')
                                            #password ='')



    def inserta_producto(self, codigo, id_sucur, nombre, precio):
        cur = self.conexion.cursor()
        sql='''INSERT INTO sucursal (idSucursal, Ciudad, Direccion, Telefono)
        VALUES ('{}','{}', '{}','{}')'''.format( id_sucur, codigo, nombre, precio)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()

    def inserta_producto2(self, Nombre, Cargo, Sueldo, idSucursal, Telefono, Direccion, cedula):
        cur = self.conexion.cursor()
        sql='''INSERT INTO empleados (Nombre, Cargo, Sueldo, idSucursal, Telefono, Direccion, cedula)
        VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format( Nombre, Cargo, Sueldo, idSucursal, Telefono, Direccion, cedula)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()

    def inserta_producto3(self, No_doc, Tipo_id, Nombre, Ciudad, Direccion, Telefono):
        cur = self.conexion.cursor()
        sql='''INSERT INTO usuarios (No_doc, Tipo_id, Nombre, Ciudad, Direccion, Telefono) 
        VALUES ('{}','{}','{}','{}','{}','{}')'''.format(No_doc, Tipo_id, Nombre, Ciudad, Direccion, Telefono) 
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()

    def inserta_producto4(self, Placa, Tipo, idEmpleado, Modelo):
        cur = self.conexion.cursor()
        sql='''INSERT INTO vehiculos (Placa, Tipo, idEmpleado, Modelo) 
        VALUES ('{}','{}','{}','{}')'''.format(Placa, Tipo, idEmpleado, Modelo) 
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()

    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM sucursal " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def mostrar_productos2(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM empleados " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def mostrar_productos3(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM usuarios " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        print(type(registro))
        print(registro)
        return registro

    def mostrar_productos4(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM vehiculos " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_producto(self, nombre_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM sucursal WHERE Ciudad = {}".format(nombre_producto)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX 

    def busca_producto2(self, nombre_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM empleados WHERE idEmpleados = {}".format(nombre_producto)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX 

    def busca_producto3(self, nombre_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM usuarios WHERE No_doc = {}".format(nombre_producto)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX

    def busca_producto4(self, nombre_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM vehiculos WHERE Placa = {}".format(nombre_producto)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX

    def elimina_productos(self,nombre):
        cur = self.conexion.cursor()
        sql='''DELETE FROM sucursal WHERE idSucursal = {}'''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()

    def elimina_productos2(self,nombre):
        cur = self.conexion.cursor()
        sql='''DELETE FROM empleados WHERE idEmpleados = {}'''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()

    def elimina_productos3(self,nombre):
        cur = self.conexion.cursor()
        sql='''DELETE FROM usuarios WHERE No_doc = {}'''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()

    def elimina_productos4(self,nombre):
        cur = self.conexion.cursor()
        sql='''DELETE FROM vehiculos WHERE Placa = {}'''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()

    def grafica_usuarios(self):
        cur = self.conexion.cursor()
        sql='''select Ciudad , count(*) as usuarios
            from usuarios
            group by Ciudad'''
        cur.execute(sql)
        cantidad_city = cur.fetchall()   
        return cantidad_city

    def grafica_empleados(self):
        cur = self.conexion.cursor()
        sql='''SELECT Ciudad , count(*) as sucursal
            FROM sucursal C, empleados O
            WHERE C.idSucursal = O.idSucursal
            group by Ciudad'''
        cur.execute(sql)
        cantidad_city = cur.fetchall()   
        return cantidad_city