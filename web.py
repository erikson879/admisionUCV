

bufsize = 4048
import socket
import re
from urlparse import urlparse





class Headers(object):
    def __init__(self, headers):
        self.__dict__.update(headers)

    def __getitem__(self, name):
        return getattr(self, name)

    def get(self, name, default=None):
        return getattr(self, name, default)

class Request(object):
    header_re = re.compile(r'([a-zA-Z-]+):? ([^\r]+)', re.M)

    def __init__(self, sock):
        header_off = -1
        data = ''
        while header_off == -1:
            data += sock.recv(bufsize)
            header_off = data.find('\r\n\r\n')
        header_string = data[:header_off]
        self.cabeza = data[:header_off]
        self.content = data[header_off+4:]
        lines = self.header_re.findall(header_string)
        self.method, path = lines.pop(0)
        path, protocol = path.split(' ')
        self.headers = Headers(
            (name.lower().replace('-', '_'), value)
            for name, value in lines
        )

        if self.method in ['POST', 'PUT']:
            content_length = int(self.headers.get('content_length', 0))
            while len(self.content) <  content_length:
                self.content += sock.recv(bufsize)

        self.query = urlparse(path)[4]

acceptor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
acceptor.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_REUSEADDR,
    1,
)

acceptor.bind(('', 2501 ))
acceptor.listen(10)

if __name__ == '__main__':
    while True:
        sock, info = acceptor.accept()
        request = Request(sock)
        #print(request.cabeza)
        metGet = request.cabeza.find('GET ')
        metPost = request.cabeza.find('POST ')
        listaHeader = request.cabeza.split('\r\n')
        #print(listaHeader)
        direccionRequest =''
        if metGet > -1:
            for i in listaHeader: 
                if i.find('GET ')  > -1:
                    direccionRequest = i
                    break
            g = direccionRequest.find('GET ')+len('GET ')
        elif metPost > -1 :
            for i in listaHeader: 
                if i.find('POST ')  > -1:
                    direccionRequest = i
                    break
            g = direccionRequest.find('POST ')+len('POST ')
        h = direccionRequest.find(' HTTP/1.1')
        print('direccionRequest>> '+direccionRequest[g:h])
        direccion = direccionRequest[g:h].replace('?','')
        archivo = 'No existe este recurso'
        print(direccion)
        if direccion == '/':
            f = open("registro.html","r") 
            if f.mode == 'r':
                archivo = f.read()
                f.close()
            sock.send('HTTP/1.1 200 OK\n\n'+(archivo))
        elif direccion == '/bootstrap.min.css':
            f = open("bootstrap.min.css","r") 
            if f.mode == 'r':
                archivo = f.read()
                f.close()
            sock.send('HTTP/1.1 200 OK\n\n'+(archivo))
        elif direccion == '/jquery-3.4.1.min.js':
            f = open("jquery-3.4.1.min.js","r") 
            if f.mode == 'r':
                archivo = bytes(f.read())
                f.close()
            sock.send('HTTP/1.1 200 OK\n\n'+(archivo))
        elif direccion == '/mi.js':
            f = open("mi.js","r") 
            if f.mode == 'r':
                archivo = bytes(f.read())
                f.close()
            sock.send('HTTP/1.1 200 OK\n\n'+(archivo))
        elif direccion == '/examenAdmision':
            try:
                db_sockRes = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                db_sockRes.connect(('127.0.0.1',2503))
                print('12 PASO POR EXAMENADMISION')
                print(request.content)
                db_sockRes.send(request.content)
                print('13 PASO POR EXAMENADMISION')
                datosResumen = db_sockRes.recv(6000)
                print('14 PASO POR EXAMENADMISION')
                print(datosResumen)
                listaMensaje = []
                listaMensaje = datosResumen.split('&')
                print(listaMensaje)
                dicMensaje = {}
                print(dicMensaje)
                for valor in listaMensaje:
                    keyValue = valor.split(":")
                    print(keyValue[0]+'-'+keyValue[1])
                    dicMensaje[keyValue[0]]=keyValue[1]
                    print ("dicMensaje")
                    print (dicMensaje)
                print (dicMensaje)
                index = '''
                        <!DOCTYPE html>
                        <html>
                        <head>
                            <title>Proyecto Sistemas Distribuidos</title>
                            <link type="text/css" rel="stylesheet" href="bootstrap.min.css">
                            <script src="jquery-3.4.1.min.js"></script>
                            <script src="mi.js"></script>
                        </head>
                        <body class = "container" >
                            <div class="card container center-block" style="margin-top: 10%;">
                                    Sr. o Sra. {0}, obtuvo una puntuaci&oacute;n de {1} puntos.
                            </div>
                        </body>
                        </html>
                        '''.format(dicMensaje['nombreCompleto'],dicMensaje['puntuacion'])
            except Error as e:
                print (e)
            finally:
                pass
            sock.send('HTTP/1.1 200 OK\n\n'+(index))
        elif direccion == '/formulario':
            try:
                print('PASO POR FORMULARIO')
                db_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                db_sock.connect(('127.0.0.1',2502))
                db_sock.send(request.content)
                recibo_cliente = db_sock.recv(6000)
                print('==========================================11 PASO POR dicPreguntas \n\n')
                print(recibo_cliente)
                preguntas = recibo_cliente[:recibo_cliente.find(' &&& ')]
                listaPreguntas = preguntas.split('&')
                dicPregunta = {}
                for i in listaPreguntas:
                    iTemp = i.split(':')
                    dicPregunta[iTemp[0]] = iTemp[1]
                print('PASO POR dicPreguntas \n\n')
                #listaPreguntaRespuesta = recibo_cliente.split('&')
                #listaParamtros = []
                #for i in listaPreguntaRespuesta:
                #    listaParamtros.append(i.split(':'))
                #dicParametros = dict(listaParamtros)
                print('+++++++++++++++++++++web como cliente')
                #print(dicParametros)
                #respuestasRaw = db_sock.recv(bufsize)
                #dicPreguntas = dict(recibo_cliente[:' &&& '])
                print(dicPregunta)
                print('//////////////////////////////////////////////////Respuestas')
                respuesta = recibo_cliente[recibo_cliente.find(' &&& ')+5:recibo_cliente.find('###')]
                print(respuesta) 
                idUsuario = recibo_cliente[recibo_cliente.find('###')+3:]
                print('//////////////////////////////////////////////////idUsuario')
                usuario = []
                usuario.append(idUsuario)
                print(usuario) 
                listaRespuestas = respuesta.split('&')
                dicRespuestas = {}
                for i in listaRespuestas:
                    itemp = i.split('=')
                    iTempL = itemp[1].split(',')
                    dicRespuestas[itemp[0]] = iTempL
                dinamica = '''<!DOCTYPE html>
                                <html>
                                <head>
                                    <title>Proyecto Sistemas Distribuidos</title>   
                                    <link type="text/css" rel="stylesheet" href="bootstrap.min.css">
                                    <script src="jquery-3.4.1.min.js"></script>
                                    <script src="mi.js"></script>
                                </head>
                                <body>
                                    <div class="card container">
                                        <div class="card-body" style="padding: 1em 0em;">
                                            <div class="card bg-light mb-12" style="">
                                              <div class="card-header"><strong>Tiempo transcurrido</strong><a id="timer" class="timer" style="margin-left: 1em;
                                                                                                                                    font-size: 2em;
                                                                                                                                    font-weight: bold;
                                                                                                                                    color: #171414;
                                                                                                                                    ">Tiempo restante</a></div>
                                              <div class="card-body">
                                                <h5 class="card-title">Examen de admision Universidad Central de Venezuela</h5>
                                                <p class="card-text">El objetivo de esta prueba es comprobar sus conocimientos en temas comprendidos en el area de estudio. Tiene una duraci&oacute;n de 4 minutos</p>
                                              </div>
                                        </div>
                                    </div>
                                    <div class="card container">
                                        <div class="card-body">
                                            <form action="/examenAdmision" method="post">
                                            <input id="usuario" name="usuario" type="hidden" value="{0}" >'''.format(usuario[0])
                cc = 1
                for i in dicPregunta:
                    dinamica +='''<div class="form-group" >
                                    <label for="exampleInputEmail1"><strong>{0}.</strong>{1}</label>
                                    <input id="{2}" name="{2}" type="hidden" value="{2}">
                                    <select name="{2}" id="{2}" class="custom-select">
                                          <option selected disabled=""> Seleccione una respuesta</option>'''.format(str(cc),str(dicPregunta[i]),i)
                    for k in dicRespuestas:
                        if dicRespuestas[k][1] == i:
                            dinamica += '''<option value="{0}">{1}</option>'''.format(str(k),dicRespuestas[k][0])
                    cc += 1
                    dinamica +='''   </select></div>'''
                dinamica += '''  <button id="envi" type="submit" class="btn btn-primary">Enviar para calificar</button>
                                </form>
                                        </div>
                                    </div>
                                </body>
                                </html>
                                <script type="text/javascript">
                                var d = new Date();
                                var n = d.getMinutes();
                                var start = new Date;
                                var segundos = '00';
                                var minu = 00;
                                window.setInterval(function yourfunction(){ 
                                console.log(n);
                                minu = parseInt(((new Date - start) / 1000)/60);
                                var afueraTemp = ((parseInt(minu) >= 1) ? segundos : parseInt((parseInt((new Date - (start))) / 1000)));
                                if (parseInt(afueraTemp) <= 60){
                                    segundos = afueraTemp;
                                }
                                console.log("afuera "+ segundos);
                                if (parseInt(minu) > 0){
                                    var adentroTemp = parseInt((parseInt((new Date - (start))) / 1000))-(60*(parseInt(parseInt((parseInt((new Date - (start))) / 1000)))%(parseInt(minu)+1)));
                                    if(parseInt(adentroTemp) <= 60 ){
                                        segundos = parseInt(adentroTemp);    
                                    }
                                    console.log((60*(parseInt(parseInt((parseInt((new Date - (start))) / 1000)))%parseInt(minu))));
                                    console.log("adentro "+ segundos);
                                }
                                $('#timer').text(minu+":"+segundos + " Seconds") },500);    
                                if(minu > 3 ){
                                    alert('Boommmm!');
                                    $("#envi").submit();
                                }
                            </script>'''
                print(dicRespuestas)
            except socket.error as error:
                print(error)
            finally:
                db_sock.close()
            sock.send('HTTP/1.1 200 OK\n\n'+(dinamica))
        sock.close()