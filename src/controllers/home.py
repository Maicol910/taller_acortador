from flask import render_template, request, redirect, url_for, flash, session
from src import app
from random import choice
from src.config.send import mail
from src.models.datos import DatosModel
from flask_mail import Mail, Message

import hashlib

#-----------------------------------------------ACORTADOR--------------------------------------------
@app.route('/', methods=['GET', 'POST'])
def index():
    datosModel = DatosModel()

    if request.method =='GET':  
        return render_template('index.html')

    link = request.form.get('link')
    acortador = request.form.get('acortador')
    usuario_id = request.form.get('usuario_id')

    valores="0123456789abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    acortador=""

    acortador=acortador.join([choice(valores) for i in range(4)])
    acortador = acortador
    link=link

    if session:
        datosModel.crear(link,acortador,session['usuario'][0])
    else:
        datosModel.crear(link,acortador,usuario_id)


    return render_template('index.html', acortador=acortador)

@app.route('/<link>')
def crear_fin(link):
    datosModel = DatosModel()
    lik = datosModel.crearfin(link)
    return redirect(lik[0])

#-----------------------------------------------TRAER DATOS--------------------------------------------

@app.route('/index/datos')
def datos():
    datosModel = DatosModel()
    if session:
        acortador1 = datosModel.traerTodos(session['usuario'][0])
    return render_template('datos.html',acortador1 = acortador1)

#-----------------------------------------------REGISTRO--------------------------------------------

@app.route('/index/registro', methods=['GET', 'POST'])  
def registro():
    if request.method =='GET':
    #mostramos el formulario de creacion
        return render_template('/registro.html')
    # aca es la creacion del usuario
    nombre = request.form.get('nombre')
    email = request.form.get('email')   
    password = request.form.get('password')
    p = hashlib.new('md5',password.encode('utf8'))
    password=p.hexdigest()
    
    datosModel = DatosModel()
    datosModel.registro(nombre, email, password)

    #with app.app_context():
    msg = Message(subject="HOLA!",
                    sender=app.config.get("MAIL_USERNAME"),
                    recipients=[email], # replace with your email for testing
                    html=f"""<p>EL USUARIO REGISTRADO ES: {email}</p>
                    <p>PARA VERIFICAR TU E-MAIL PRECIONA ---> <a href="http://127.0.0.1:5000/index/verificacion/{email}">aqui</a></p>""")               
    mail.send(msg)
    return render_template('login.html')

@app.route('/index/verificacion/<email>', methods=['GET', 'POST'])  
def verificacion(email):

    datosModel = DatosModel()  
    datosModel.confirmarE(email)
    
    return render_template('login.html')

#-----------------------------------------------LOGIN--------------------------------------------

@app.route('/index/login', methods=['GET', 'POST'])  
def login():
    datosModel = DatosModel()  
    
    if request.method =='GET':
        return render_template('login.html')
    
    email = request.form.get('email')
    password = request.form.get('password')    
    p = hashlib.new('md5',password.encode('utf8'))
    password=p.hexdigest()
    #proceso de login, validar que el usuario y contraseña sean correactas        
    user = {
        'email': email,
        'password':password
    }
    usua = datosModel.login1(user)

    if (usua[4] == None):
        flash('Las credenciales no son validas.','error')
        flash('o verifique su E-mail si no lo ha echo','error')
        return render_template('login.html')

    session['usuario'] = usua
    
    return render_template('index.html')
    #crear la sesion del usuario

@app.route('/index/logout')  
def logout():

    session.pop('usuario', None)

    return redirect(url_for('index'))

#----------------------------------------------------- ELIMINAR --------------------------------------------
@app.route('/eliminar/<string:id>')
def eliminar(id):
    datosModel = DatosModel()  

    datosModel.eliminar(id)
        
    return redirect(url_for('datos'))

#----------------------------------------------------- EDITAR --------------------------------------------
@app.route('/editar/<int:id>', methods=['GET','POST'])
def editar(id):
    datosModel = DatosModel()

    if request.method == 'GET':
        datos = datosModel.consulta(id)
        return render_template('editar.html', datos = datos)

    acortador = request.form.get('acortador')   
    link = request.form.get('link') 
    datosModel.editar(id,acortador,link)

    return redirect(url_for('datos'))
    
