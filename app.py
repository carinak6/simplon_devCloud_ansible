from flask import Flask, request, render_template, jsonify

from bdd_management import *

app = Flask(__name__)

bdd_connecte = ConnectionBDD_PG()
bdd_connecte.create_table()

@app.route('/')
def hello():    
    return 'Hola!'

@app.route('/inc', methods=['GET'])
def plus_un():
    
    reponse = bdd_connecte.incremente()
   
    print('reponse envoyé')
    
    return jsonify(reponse)

@app.route('/id', methods=['GET'])
def affiche():
    reponse = bdd_connecte.afficher()
   
    print('reponse affichée')
    #jsonify
    return jsonify(reponse)

if __name__ == '__main__':
    
    print('hello')
    app.run(host='0.0.0.0', port=3000, debug=True)