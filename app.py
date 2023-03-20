from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password123'
app.config['MYSQL_DB'] = 'dbproyectofinal'
mysql = MySQL(app)

# Setting
app.secret_key = 'mysecretkey'


@app.route('/libros')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM libros')
    data = cur.fetchall()
    return render_template('index.html', listlibros=data)


@app.route('/agregar', methods=['POST'])
def add_libro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        autor = request.form['autor']
        descripcion = request.form['descripcion']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO libros (nombre,autor,descripcion) VALUES (%s, %s, %s)',
                    (nombre, autor, descripcion))
        mysql.connection.commit()
        flash('Libro Agregado')
        return redirect(url_for('index'))


@app.route('/editar/<id>')
def get_edit_libro(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM libros WHERE id = %s', (id,))
    data = cur.fetchall()
    return render_template('edit_libro.html', listlibro=data[0])


@app.route('/update/<id>', methods=['POST'])
def update_libro(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        autor = request.form['autor']
        descripcion = request.form['descripcion']
        cur = mysql.connection.cursor()
        cur.execute('UPDATE libros SET nombre = %s, autor = %s, descripcion = %s WHERE id = %s',
                    (nombre, autor, descripcion, id))
        mysql.connection.commit()
        flash('Libro Actualizado')
        return redirect(url_for('index'))


@app.route('/eliminar/<string:id>')
def delete_libro(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM libros where id = {0}'.format(id))
    mysql.connection.commit()
    flash('Libro Eliminado')
    return redirect(url_for('index'))


@app.route('/carrito_compras')
def shopping_car():
    return render_template('carrito.html')


@app.route('/inicio')
def inicio():
    return render_template('inicio.html')


@app.route('/acerca_de')
def about():
    return render_template('about.html')


@app.route('/')
def login():
    return render_template('inicio_sesion.html')


@app.route('/404')
def error404():
    return render_template('error404.html')


if __name__ == '__main__':
    app.run(port=3000, debug=True)
