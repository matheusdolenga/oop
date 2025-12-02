from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def template():
    return render_template('index.html')

@app.route('/Consulta')
def aluno():
    return render_template('consulta.html')

@app.route('/Deletar')
def deletar():
    return render_template('deletar.html')

@app.route('/processar_consulta', method = ['POST'])
def processar_consulta():
    name = request.form['name']
    email = 
if __name__ == '__main__':
    app.run(debug=True)