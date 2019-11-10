bufsize = 4048
import socket
import re
from urlparse import urlparse
import psycopg2
import random


def validaRespuesta(codigo_respuesta):
    respuesta_correcta = ''
    try:
        conn = psycopg2.connect(host='localhost',port='5432',user='projuser',password='secret',database='sistemadistribuido')
        cursor = conn.cursor()
        postgreSQL_select_Query = ("select respuesta_correcta from admisionucv.respuesta where id_respuesta = {0};".format(codigo_respuesta))
        print (postgreSQL_select_Query)
        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        mobile_records = cursor.fetchall() 
        print("Print each row and it's columns values")
        for row in mobile_records:
            respuesta_correcta += codigo_respuesta+':'+str(row[0])
        print(respuesta_correcta)
    except (Exception, psycopg2.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)
    finally:
        #closing database connection.
        if(conn):
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")    
    return respuesta_correcta

def getNombreUsuario(id):
    nombreCompleto = ''
    try:
        conn = psycopg2.connect(host='localhost',port='5432',user='projuser',password='secret',database='sistemadistribuido')
        cursor = conn.cursor()
        postgreSQL_select_Query = ("select nombre1, nombre2,apellido1,apellido2 from admisionucv.aspirante where id_aspirante = {0};".format(id))
        print (postgreSQL_select_Query)
        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        mobile_records = cursor.fetchall() 
        print("Print each row and it's columns values")
        for row in mobile_records:
            nombreCompleto += str(row[0])+' '+str(row[1])+' '+str(row[2])+' '+str(row[3])
    except (Exception, psycopg2.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)
    finally:
        if(conn):
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")
    return nombreCompleto

def guardaResultado(puntuacion,id):
    try:
        conn = psycopg2.connect(host='localhost',port='5432',user='projuser',password='secret',database='sistemadistribuido')
        print('Conecto')
        cursor = conn.cursor()
        cursor.execute("""UPDATE admisionucv.aspirante SET calificacion = {0} WHERE id_aspirante = {1};""".format(round(float(puntuacion), 2),int(id)))
        conn.commit() # <- We MUST commit to reflect the inserted data
        print('Luego de commit')
    except psycopg2.Error as e:
        print('Mi error: '+str(e.pgcode))
        print('Mi error: '+str(e))
    finally:
        cursor.close()
        conn.close()
        print('Luego de cerrar cursor y conexion')

acceptor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
acceptor.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_REUSEADDR,
    1,
)

acceptor.bind(('', 2503 ))
acceptor.listen(10)
while True:
    piv = []
    sock, info = acceptor.accept()
    data = sock.recv(bufsize)
    print(data)
    listaDatos = data.split('&')
    listaParamtros = []
    for i in listaDatos:
        listaParamtros.append(i.split('='))
    dicParametros = dict(listaParamtros)
    print(dicParametros)
    try:
        usuario = dicParametros.pop('usuario') 
    except:
        usuario = None
    for i in dicParametros:
        if i == dicParametros[i]:
            piv.append(i)
    for i in piv:
        dicParametros.pop(i)
    puntuacion = 0 
    for i in dicParametros:
        val = validaRespuesta(dicParametros[i]).split(':')
        print('+++++++++++++++++++++++val+++++++++++++++++++++++++++++++++++++VAL')
        print(val)
        if  val[1] == 'X':
            puntuacion += 4
    guardaResultado(puntuacion,usuario)
    infoSend = 'nombreCompleto:'+getNombreUsuario(usuario)+'&puntuacion:'+str(puntuacion)
    print(infoSend)
    sock.send(infoSend)
    print('DESPUES DE ENVIAR')
    sock.close()