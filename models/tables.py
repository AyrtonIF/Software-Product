from app import db

class Clientes(db.Model):
    __tablename__ = "Clientes"

    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    genero = db.Column(db.String)
    nascimento = db.Column(db.Date)
    fone = db.Column(db.Integer)
    cidade = db.Column(db.String)
    estado = db.Column(db.String)
    endereco = db.Column(db.String)

    def __init__(self, cliente, email, fone, genero, nascimento, cidade, estado, endereco):
        self.cliente = cliente
        self.email = email
        self.fone = fone
        self.genero = genero
        self.nascimento = nascimento
        self.cidade = cidade
        self.estado = estado
        self.endereco = endereco

class Produtos(db.Model):
    __tablename__ = "Produtos"

    id = db.Column(db.Integer, primary_key=True)
    nome_produto = db.Column(db.String)
    id_produto = db.Column(db.Integer)
    data_cadastro = db.Column(db.Date)
    tipo_produto = db.Column(db.String)
    produto = db.Column(db.String)

    def __init__(self, nome_produto, id_produto, data_cadastro, tipo_produto, produto):
        self.nome_produto = nome_produto
        self.id_produto = id_produto
        self.data_cadastro = data_cadastro
        self.tipo_produto = tipo_produto
        self.produto = produto