from src.config.db import DB

class DatosModel():
    def traerTodos(self, usuario_id):
        cursor = DB.cursor()
        cursor.execute('select * from acortador_base WHERE usuario_id = ?',(usuario_id,))
        acortador1 = cursor.fetchall()
        cursor.close()
        return acortador1

    def crear(self, link, acortador, usuario_id):
        cursor = DB.cursor()
        cursor.execute('insert into acortador_base(link, acortador, usuario_id) values(?,?,?)', (link, acortador,usuario_id,))
        cursor.close()

    def crearfin(self, acortador):
        cursor = DB.cursor()
        cursor.execute('select link from acortador_base where acortador = ?',(acortador,))
        lik = cursor.fetchone()
        cursor.close()
        return lik

    def registro(self, nombre, email, password):
        cursor = DB.cursor()
        cursor.execute('insert into usuario(nombre, email, password) values(?,?,?)', (nombre, email, password,))
        cursor.close()

    def confirmarE(self, email):
        cursor = DB.cursor()
        cursor.execute('update usuario set verificacion = curdate() where email = ?',(email,))
        cursor.close

    def login1(self, user):
        cursor = DB.cursor()
        cursor.execute('select * from usuario where email = ? and password = ?', (user['email'],user['password'],))
        usua = cursor.fetchone()
        cursor.close()
        print(usua)
        return usua

    def eliminar(self,id):
        cursor = DB.cursor()
        cursor.execute('delete from acortador_base where id=?',(id,))
        cursor.close()

    def editar(self,id,acortador,link):
        cursor = DB.cursor()
        cursor.execute(""" update acortador_base set acortador=?, link=? where id=? """,(acortador,link,id,))
        cursor.close()

    def consulta(self,id):
        cursor = DB.cursor()
        cursor.execute("""select * from acortador_base where id = ?""",(id,))
        datos = cursor.fetchone()
        cursor.close()
        return datos

        
