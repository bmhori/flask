# Importando o módulo flask no projeto
from flask import Flask, render_template

# Criando um objeto da classe Flask
app = Flask(__name__)

# A função route() da classe Flask
@app.route("/")
# A URL ‘/’ é ligada à função first_webpage.
def first_webpage():
    
    return render_template('index.html')
#app.run(debug=True)
# Execute a aplicação no servidor local
app.run()
