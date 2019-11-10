bufsize = 4048
import socket
import re
from urlparse import urlparse
import psycopg2
import random

def getIndiceAleatorioPreguntas():
    listaDePreguntas = []
    for i in range(1,100):
        indiceSeleccion = random.randrange(1, 11)
        if not listaDePreguntas:
            listaDePreguntas.append(indiceSeleccion)
        else:
            existe = 0
            for i in listaDePreguntas:
                if i == indiceSeleccion:
                    existe = 1
            if existe == 0:
                listaDePreguntas.append(indiceSeleccion)
        if len(listaDePreguntas) == 5:
            break
    print(listaDePreguntas)
    return tuple(listaDePreguntas)


acceptor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
acceptor.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_REUSEADDR,
    1,
)
acceptor.bind(('', 2502 ))
acceptor.listen(10)
codido_documento = ''
documento = ''
while True:
    
    sock, info = acceptor.accept()
    data = sock.recv(bufsize)
    print('+++++++++++++++++++++web_db')
    listaDatos = data.split('&')
    listaParamtros = []
    for i in listaDatos:
        listaParamtros.append(i.split('='))
    dicParametros = dict(listaParamtros)
    print(dicParametros)
    nombre1 = dicParametros['nombre1']
    nombre2 = dicParametros['nombre2']
    apellido1 = dicParametros['apellido1']
    apellido2 = dicParametros['apellido2']
    codido_documento = dicParametros['codigo_identificacion']
    documento = dicParametros['identificacion']
    fecha_nacimiento = dicParametros['fecha_nacimiento']
    pais_nacimiento = dicParametros['pais_nacimiento']
    fecha_bachiller = dicParametros['fecha_graduacion_bachiller']
    sexo = dicParametros['sexo']
    try:
        print('Antes de Conectar')
        conn = psycopg2.connect(host='localhost',port='5432',user='projuser',password='secret',database='sistemadistribuido')
        print('Conecto')
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO admisionucv.aspirante (nombre1,nombre2,apellido1,apellido2,codido_documento,documento,fecha_nacimiento,pais_nacimiento,sexo,fecha_bachiller)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",(nombre1,nombre2,apellido1,apellido2,codido_documento,documento,fecha_nacimiento,pais_nacimiento,sexo,fecha_bachiller))
        conn.commit() # <- We MUST commit to reflect the inserted data
        print('Luego de commit')
    except psycopg2.Error as e:
        print('Mi error: '+str(e.pgcode))
        print('Mi error: '+str(e))
    finally:
        cursor.close()
        conn.close()
        print('Luego de cerrar cursor y conexion')
    #enviar informacion de prueba de admisions
    #inicio
    pre =''
    try:
        conn = psycopg2.connect(host='localhost',port='5432',user='projuser',password='secret',database='sistemadistribuido')
        cursor = conn.cursor()
        pre = getIndiceAleatorioPreguntas()
        print (pre)
        postgreSQL_select_Query = ("select id_pregunta,pregunta from admisionucv.pregunta where id_pregunta in ({},{},{},{},{});".format(pre[0],pre[1],pre[2],pre[3],pre[4]))
        print (postgreSQL_select_Query)
        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        mobile_records = cursor.fetchall() 
        print("Print each row and it's columns values")
        preguntasLista = []
        for row in mobile_records:
            preguntasLista.append(str(row[0])+':'+row[1])
        preguntaString=''
        longitud = len(preguntasLista)-1
        contador = 0
        for tup in preguntasLista:
            if contador == longitud:
                preguntaString += tup
            else:
                preguntaString += tup+'&'
            contador += 1
        print(preguntaString)
    except (Exception, psycopg2.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)
    finally:
        #closing database connection.
        if(conn):
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")
    #fin 
    #inicio
    try:
        print('Antes de Conectar')
        conn = psycopg2.connect(host='localhost',port='5432',user='projuser',password='secret',database='sistemadistribuido')
        print('Conecto')
        cursor = conn.cursor()
        postgreSQL_select_Query = ("select id_aspirante from admisionucv.aspirante where calificacion is null and codido_documento = '{}' and documento = '{}';".format(codido_documento,documento))
        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall() 
        idUsuario =''
        for row in mobile_records:
            idUsuario += str(row[0])
        print('USUARIO ID-----------------------------------------------')
        print(idUsuario)
    except psycopg2.Error as e:
        print('Mi error: '+str(e.pgcode))
        print('Mi error: '+str(e))
    finally:
        cursor.close()
        conn.close()
        print('Luego de cerrar cursor y conexion')
    #enviar informacion de prueba de admisions
    #inicio documento clave
    try:
        conn = psycopg2.connect(host='localhost',port='5432',user='projuser',password='secret',database='sistemadistribuido')
        cursor = conn.cursor()
        pre = getIndiceAleatorioPreguntas()
        print (pre)
        postgreSQL_select_Query = ("select id_pregunta,pregunta from admisionucv.pregunta where id_pregunta in ({},{},{},{},{});".format(pre[0],pre[1],pre[2],pre[3],pre[4]))
        print (postgreSQL_select_Query)
        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        mobile_records = cursor.fetchall() 
        print("Print each row and it's columns values")
        preguntasLista = []
        for row in mobile_records:
            preguntasLista.append(str(row[0])+':'+row[1])
        preguntaString=''
        longitud = len(preguntasLista)-1
        contador = 0
        for tup in preguntasLista:
            if contador == longitud:
                preguntaString += tup
            else:
                preguntaString += tup+'&'
            contador += 1
        print(preguntaString)
    except (Exception, psycopg2.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)
    finally:
        #closing database connection.
        if(conn):
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")
    #fin documento clave
    #enviar respuestas a las preguntas seleccionadas
    #inicio
    try:
        conn = psycopg2.connect(host='localhost',port='5432',user='projuser',password='secret',database='sistemadistribuido')
        cursor = conn.cursor()
        print (pre)
        postgreSQL_select_Query = ("select id_respuesta,respuesta,id_pregunta,respuesta_correcta from admisionucv.respuesta where id_pregunta in ({},{},{},{},{});".format(pre[0],pre[1],pre[2],pre[3],pre[4]))
        print (postgreSQL_select_Query)
        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        mobile_records = cursor.fetchall() 
        print("Print each row and it's columns values")
        stringRespuestas = ''
        print('+++++++++++++++++++++++++++++++++++++++++mobile_records++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print(mobile_records)
        respuestaLen = len(mobile_records)-1
        c = 0
        for row in mobile_records:
            if c == respuestaLen:
                stringRespuestas += str(row[0])+'='+row[1]+','+str(row[2])+','+('0' if (row[3] == None) else row[3])
            else:
                stringRespuestas += str(row[0])+'='+row[1]+','+str(row[2])+','+('0' if (row[3] == None) else row[3])+'&'
            c += 1
        print(stringRespuestas)
    except (Exception, psycopg2.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)
    finally:
        #closing database connection.
        if(conn):
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")
    #fin
    variable = preguntaString+' &&& '+stringRespuestas +'###'+ idUsuario
    print(variable)
    print('ANTES DE ENVIAR')
    sock.send(variable)
    print('DESPUES DE ENVIAR')
    sock.close()
    print('Despues de enviar desde socket')
    
