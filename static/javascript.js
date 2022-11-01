function myalert_clientes() {
    var cliente = document.getElementById("cliente");
    var email = document.getElementById("email");
    var fone = document.getElementById("fone");
    var genero = document.getElementsByName("genero");
    var nascimento = document.getElementById("nascimento");
    var cidade = document.getElementById("cidade");
    var estado = document.getElementById("estado");
    var endereco = document.getElementById("endereco");

    if(endereco.value==""){
        alert('Preencha todos os campos')
    }

    else{
        for (var i = 0, length = genero.length; i < length; i++) {
            if (genero[i].checked) {
                if(cliente.value != "" && email.value != "" && fone.value != "" && genero.value != "" 
                && cidade.value != "" && estado.value != "" && endereco.value != "") {
                    alert('Os dados do(a) cliente foram registrados com sucesso! \n'
                    + cliente.value + '\n'
                    + email.value + '\n'
                    + fone.value + '\n'
                    + genero[i].value + '\n'
                    + cidade.value + '\n'
                    + estado.value + '\n'
                    + endereco.value);
                }
                break;
            }
        }
    }
}

function myalert_produtos() {
    var nome_produto = document.getElementById("nome_produto");
    var id_produto = document.getElementById("id_produto");
    var data_cadastro = document.getElementById("data_cadastro");
    var quantidade = document.getElementsById("quantidade");
    var produto = document.getElementByName("produto");

    if(nome_produto.value==""){
        alert('Preencha todos os campos')
    }

    else{
        for (var i = 0, length = produto.length; i < length; i++) {
            if (produto[i].checked) {
                if(nome_produto.value != "" && id_produto.value != "" && data_cadastro.value != "" 
                && quantidade.value != "" && produto.value != "") {
                    alert('Os dados do produto foram registrados com sucesso! \n'
                    + nome_produto.value + '\n'
                    + id_produto.value + '\n'
                    + data_cadastro.value + '\n'
                    + quantidade.value + '\n'
                    + produto[i].value);
                }
                break;
            }
        }
    }
}

function clienteCRUD() {
    window.open("http://127.0.0.1:5000/ClienteCRUD", "_self");
}

function adicionar_cliente() {
    window.open("http://127.0.0.1:5000/CadastrarCliente", "_self");
}

function editar_cliente() {
    window.open("http://127.0.0.1:5000/EditarCliente", "_self");
}

function produtosCRUD() {
    window.open("http://127.0.0.1:5000/ProdutosCRUD", "_self");
}