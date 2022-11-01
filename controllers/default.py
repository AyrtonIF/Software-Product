from pickle import TRUE
from app import app, db
from flask import render_template, request

from app.models.tables import Clientes, Produtos

@app.route("/")
def PaginaInicial():
    return render_template("PaginaInicial.html")

@app.route("/ClienteCRUD")
def ClienteCRUD():
    return render_template("ClienteCRUD.html")

@app.route("/CadastrarCliente", methods=["GET", "POST"])
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

@app.route("/EditarCliente", methods=["GET", "POST"])
def EditarCliente():

    if request.method=="POST":
        id = request.form.get("id_cliente")
        valida_id = db.session.query(db.session.query(Clientes).filter_by(id=id).exists()).scalar()

        if valida_id != True:
            return """
                    <script>
                        alert('Cliente com ID referenciado não encontrado dentro do banco de dados')
                        window.open("http://127.0.0.1:5000/EditarCliente", "_self")
                    </script>
            """

        else:
            id_cliente = Clientes.query.get(id)
            id_cliente.cliente = request.form.get("cliente")
            email = request.form.get("email")
            id_cliente.fone = request.form.get("fone")
            id_cliente.genero = request.form.get("genero")
            id_cliente.nascimento = request.form.get("nascimento")
            id_cliente.cidade = request.form.get("cidade")
            id_cliente.estado = request.form.get("estado")
            id_cliente.endereco = request.form.get("endereco")

            if id_cliente.email == email:
                db.session.commit()
                return """
                    <script>
                        alert('Registro do Cliente atualizado com sucesso!')
                        window.open("http://127.0.0.1:5000/", "_self")
                    </script>
                """

            else:
                valida_email = db.session.query(db.session.query(Clientes).filter_by(email=email).exists()).scalar()

                if valida_email != True:
                    id_cliente.email = request.form.get("email")
                    db.session.commit()
                    return """
                        <script>
                            alert('Registro do Cliente atualizado com sucesso!')
                            window.open("http://127.0.0.1:5000/", "_self")
                        </script>
                    """

                else:
                    return """
                        <script>
                            alert('Usuario já registrado no banco de dados')
                            window.open("http://127.0.0.1:5000/EditarCliente", "_self")
                        </script>
                    """

    return render_template("EditarCliente.html")

@app.route("/DeletarCliente", methods=["GET", "POST"])
def DeletarCliente():
    
    if request.method=="POST":
        id = request.form.get("id_cliente")
        valida_id = db.session.query(db.session.query(Clientes).filter_by(id=id).exists()).scalar()

        if valida_id != True:
            return """
                    <script>
                        alert('Cliente com ID referenciado não encontrado dentro do banco de dados')
                        window.open("http://127.0.0.1:5000/DeletarCliente", "_self")
                    </script>
            """
        
        else:
            cliente = Clientes.query.filter_by(id=id).first()
            db.session.delete(cliente)
            db.session.commit()
            return """
                    <script>
                        alert('Registro do Cliente deletado com sucesso!')
                        window.open("http://127.0.0.1:5000/", "_self")
                    </script>
            """

    return render_template("DeletarCliente.html")

@app.route("/ProdutosCRUD")
def ProdutosCRUD():
    return render_template("ProdutosCRUD.html")

@app.route("/CadastrarProduto", methods=["GET", "POST"])
def CadastrarProduto():
    
    if request.method=="POST":
        nome_produto = request.form.get("nome_produto")
        codigo_produto = request.form.get("codigo_produto")
        data_cadastro = request.form.get("data_cadastro")
        quantidade = request.form.get("quantidade")
        produto = request.form.get("produto")
        cadastrar_produto = Produtos(nome_produto, codigo_produto, data_cadastro,
                quantidade, produto)
        db.session.add(cadastrar_produto)
        db.session.commit()
    return render_template("CadastrarProduto.html")

@app.route("/EditarProduto", methods=["GET", "POST"])
def EditarProduto():

    if request.method=="POST":
        id = request.form.get("id_produto")
        valida_id = db.session.query(db.session.query(Produtos).filter_by(id=id).exists()).scalar()

        if valida_id != True:
            return """
                    <script>
                        alert('Produto com ID referenciado não encontrado dentro do banco de dados')
                    </script>
            """

        else:
            id_produto = Produtos.query.get(id)
            id_produto.nome_produto = request.form.get("nome_produto")
            id_produto.codigo_produto = request.form.get("codigo_produto")
            id_produto.data_cadastro = request.form.get("data_cadastro")
            id_produto.quantidade = request.form.get("quantidade")
            id_produto.produto = request.form.get("produto")
            db.session.commit()
            return """
                    <script>
                        alert('Registro do Produto atualizado com sucesso!')
                        window.open("http://127.0.0.1:5000/", "_self")
                    </script>
                """
    return render_template("EditarProduto.html")

@app.route("/DeletarProduto", methods=["GET", "POST"])
def DeletarProduto():
    
    if request.method=="POST":
        id = request.form.get("id_produto")
        valida_id = db.session.query(db.session.query(Produtos).filter_by(id=id).exists()).scalar()

        if valida_id != True:
            return """
                    <script>
                        alert('Produto com ID referenciado não encontrado dentro do banco de dados')
                        window.open("http://127.0.0.1:5000/DeletarProduto", "_self")
                    </script>
            """
        
        else:
            produto = Produtos.query.filter_by(id=id).first()
            db.session.delete(produto)
            db.session.commit()
            return """
                    <script>
                        alert('Registro do Produto deletado com sucesso!')
                        window.open("http://127.0.0.1:5000/", "_self")
                    </script>
            """

    return render_template("DeletarProduto.html")