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
    codigo_produto = db.Column(db.Integer)
    data_cadastro = db.Column(db.Date)
    quantidade = db.Column(db.String)
    produto = db.Column(db.String)

    def __init__(self, nome_produto, codigo_produto, data_cadastro, quantidade, produto):
        self.nome_produto = nome_produto
        self.codigo_produto = codigo_produto
        self.data_cadastro = data_cadastro
        self.quantidade = quantidade
        self.produto = produto