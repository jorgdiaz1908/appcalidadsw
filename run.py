# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key='some_secret'
app.debug=True


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route(r'/addTriangulo', methods=['GET', 'POST'])
def eval_Triangulo():
    error= None
    msg=""
    if request.method=='POST':
        lado_1=int(request.form['lado1'])
        lado_2=int(request.form['lado2'])
        lado_3=int(request.form['lado3'])
        if ((lado_1 + lado_2 > lado_3) and (lado_1 + lado_3 > lado_2) and (lado_2 + lado_3 > lado_1)):
            if(lado_1 == lado_2 and lado_2 == lado_3):
                msg=('El triangulo es equilatero.')
            elif(lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3):
                msg=('El triangulo es isosceles.')
            else:
                msg=('El triangulo es escaleno.')
        else:
            error=('Las medidas no corresponde')
    return render_template('triangulo.html', msg=msg, error=error)

@app.route(r'/addCuadrilatero', methods=['GET', 'POST'])
def eval_Cuadrilatero():
    msg=""
    if request.method=='POST':
        lado_1=request.form['lado1']
        lado_2=request.form['lado2']
        lado_3=request.form['lado3']
        lado_4=request.form['lado4']
        if (lado_1 == lado_2 and lado_3 == lado_4 and lado_1 == lado_3):
            msg=('La figura es un cuadrado')
        elif ((lado_1 == lado_2 and lado_3 == lado_4) or (lado_1 == lado_3 and lado_2 == lado_4) or (lado_1 == lado_4 and lado_2 == lado_3)):
            msg=('La figura es un rectangulo')
        else:
            msg=('La figura es un trapecio')
    return render_template('cuadrilatero.html',msg=msg)

if __name__=='__main__':
    app.run()
