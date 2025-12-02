from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def template():
    return render_template('index.html')

@app.route('/Consulta')
def aluno():
    pass

@app.route('/Deletar')
def deletar():
    pass

if __name__ == '__main__':
    app.run(debug=True)