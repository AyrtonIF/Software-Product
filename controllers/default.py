from pickle import TRUE
from app import app, db
from flask import render_template, request

from app.models.tables import Clientes, Produtos

@app.route("/", methods=["GET", "POST"])
def CadastrarCliente():
    if request.method=="POST":
        cliente = request.form.get("cliente")
        email = request.form.get("email")
        fone = request.form.get("fone")
        genero = request.form.get("genero")
        nascimento = request.form.get("nascimento")
        cidade = request.form.get("cidade")
        estado = request.form.get("estado")
        endereco = request.form.get("endereco")
        cadastrar_cliente = Clientes(cliente, email, fone, genero, 
                nascimento, cidade, estado, endereco)
        valida_email = db.session.query(db.session.query(Clientes).filter_by(email=email).exists()).scalar()
        if valida_email != True:    
            db.session.add(cadastrar_cliente)
            db.session.commit()
        else:
            return """
                <script>
                    alert('Usuario já registrado no banco de dados')
                </script>
            """
    return render_template("CadastrarCliente.html")

@app.route("/delete")
def delete():
    return "<h1>Digite no endereço do site o nome do cliente a ser deletado</h1>"

@app.route("/DeletarCliente/<id>")
def deletar_cliente(id):
    cliente = Clientes.query.filter_by(id=id).first()
    db.session.delete(cliente)
    db.session.commit()
    return """
                <script>
                    alert('Cliente removido do Banco de Dados com sucesso!')
                </script>
            """

@app.route("/CadastrarProduto", methods=["GET", "POST"])
def CadastrarProduto():
    if request.method=="POST":
        nome_produto = request.form.get("nome_produto")
        id_produto = request.form.get("id_produto")
        data_cadastro = request.form.get("data_cadastro")
        tipo_produto = request.form.get("tipo_produto")
        produto = request.form.get("produto")
        cadastrar_produto = Produtos(nome_produto, id_produto, data_cadastro,
                tipo_produto, produto)
        db.session.add(cadastrar_produto)
        db.session.commit()
    return render_template("CadastrarProduto.html")

@app.route("/DeletarProduto/<id>")
def deletar_produto(id):
    produto = Produtos.query.filter_by(id=id).first()
    db.session.delete(produto)
    db.session.commit()
    return """
                <script>
                    alert('Produto removido do Banco de Dados com sucesso!')
                </script>
            """