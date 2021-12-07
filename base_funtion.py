import sqlite3 as sql

"""Aquí estaran uvicados los codigos para la creacion de las bases de datos y sus respectivas tablas
cuando sean instaladas o iniciado por primera ves el programa"""

class Base:
    def __init__(self):
        """EN ESTE METODO LO UNICO QUE HAGO ES CREAR LA BASE DE DATOS"""
        self.database = 'base datas/data.db'
        try:
            con = sql.connect(self.database)
            con.commit()
            con.close()
        except:
            print('La base ya existe')

    def ejecutar_consulta (self,query,parameters=()):
        #ESTE METODO AUTOMATIZA LAS CONSULTAS Y PARAMETROS EN SQL,
        # CON ESTO EVITO ESTAR ABRIENDO Y CERRANDO LAS TABLAS CADA VEZ QUE LA NECECITE
        with sql.connect(self.database) as conn:
            curs = conn.cursor()
            resultado = curs.execute(query,parameters)
            conn.commit()
        return resultado

    def tabla_clientes(self):
        # CREACION DE TABLA CLIENTES, SU LLAVE PRMARIA PASARÁ A SER FORANEA EN EL RESTO DE TABLAS
        consulta = """CREATE TABLE IF NOT EXISTS clientes (
	        Cod_cliente	INTEGER PRIMARY KEY AUTOINCREMENT,
	        Nombre	TEXT NOT NULL,
	        Apellido	TEXT NOT NULL,
	        Direccion	TEXT,
	        Telefono	TEXT,
	        Cedula	TEXT)"""
        return self.ejecutar_consulta(consulta)

    def cuenta(self,tabla):
        # este modulo es para contar la cantidad de clientes, puede usarce para contar cualquier tabla
        consulta=f"SELECT COUNT(*) FROM {tabla}"    
        return self.ejecutar_consulta(consulta)

    def table_prestamo(self):
        #creacion de tabla prestamos, toma como foranea la id_cliente de la tabla cliente
        consulta ="""CREATE TABLE IF NOT EXISTS prestamo (
	        id_prestamo	INTEGER PRIMARY KEY AUTOINCREMENT,
	        id_cliente INTEGER NOT NULL,
	        fecha_prestamo DATE NOT NULL,
	        monto	REAL NOT NULL,
	        interes	REAL,
	        periodo CHAR(1) NOT NULL,
	        plazo INTEGER NOT NULL,
	        FOREIGN KEY(id_cliente) REFERENCES cliente(Cod_cliente))
            """
        return self.ejecutar_consulta(consulta)

    def tabla_abono(self):
        #Este modulo crea la tabla abono que a su vez tomo como foranea la id_cliente e id_prestamo para referenciar
        consulta ="""CREATE TABLE IF NOT EXISTS abonos(
            id_abonado INTEGER PRIMARY KEY AUTOINCREMENT,
            cod_prestamo INTEGER NOT NULL,
            id_cliente INTEGER NOT NULL,
            fecha_abono DATE NOT NULL,
            monto_abono REAL NOT NULL,
            FOREIGN KEY(id_cliente) REFERENCES cliente(Cod_cliente),
            FOREIGN KEY(cod_prestamo) REFERENCES prestamo(id_prestamo)
            );
            """
        return self.ejecutar_consulta(consulta)

    def inser_data_clinete(self,nombre,apellido,direccion,telefono,cedula):
        #con este modulo inserto datos dentro de la tabla clientes
        parametro =(nombre,apellido,direccion,telefono,cedula)
        query= "INSERT INTO clientes(Nombre,Apellido,Direccion,Telefono,Cedula) VALUES(?,?,?,?,?)"
        return self.ejecutar_consulta(query,parametro)

    def insert_data_prestamo(self,id_cliente,fecha,monto,interes,periodo,plazo):

        consulta = "INSERT INTO prestamo(id_cliente,fecha_prestamo,monto,interes,periodo,plazo) VALUES(?,?,?,?,?,?)"
        parametro = (id_cliente,fecha,monto,interes,periodo,plazo)
        return self.ejecutar_consulta(consulta,parametro)

    def insertar_data_abono(self,id_prestamo,id_cliente,fecha_abono,monto_abon):
        consulta = "INSERT INTO abonos(cod_prestamo,id_cliente,fecha_abono,monto_abono) VALUES(?,?,?,?)"
        parametro = (id_prestamo,id_cliente,fecha_abono,monto_abon)
        return self.ejecutar_consulta(consulta,parametro)

    def consultar_data(self,columnas,tabla,):
        consulta = f"SELECT {columnas} FROM {tabla}"
        return self.ejecutar_consulta(consulta)

    def filtar_nombre(self,filtro):
        consulta= f"SELECT * FROM clientes WHERE Nombre ='{filtro}'"
        return self.ejecutar_consulta(consulta)
    def consulta_prestamo(self):
        consulta = f"SELECT * FROM prestamo INNER JOIN clientes ON prestamo.id_cliente=clientes.Cod_cliente"
        return self.ejecutar_consulta(consulta)

if __name__=='__main__':
    b = Base()
    b.tabla_abono()
    b.tabla_clientes()
    b.table_prestamo()