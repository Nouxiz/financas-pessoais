function adicionarTransacao() {
    let tipo = document.getElementById('tipo').value
    let valor = document.getElementById('valor').value
    let categoria = document.getElementById('categoria').value
    let data = document.getElementById('data').value
    let descricao = document.getElementById('descricao').value

    fetch('/adicionar', {
        method: 'POST',
        headers: {'Content-type': 'application/json' },
        body: JSON.stringify({
            tipo: tipo,
            valor: valor,
            categoria: categoria,
            data: data,
            descricao: descricao
        })
    })

    alert('Transação salva!')
}

function adicionarLimite() {
    let categoria = document.getElementById('categoria_limite').value
    let valor_max = document.getElementById('valor_max').value
    let mes = document.getElementById('mes').value

    fetch('/adicionar', {
        method: 'POST',
        headers: {'Content-type': 'application/json' },
        body: JSON.stringify({
            categoria: categoria,
            valor_max: valor_max,
            mes: mes
        })
    
    })

    alert('Limites salvos!')
}
function listarTransacoes() {
    fetch('/listar')
    .then(response => response.json())
    .then(dados => {
        let tabela = document.getElementById('tabela-transacoes')
        tabela.innerHTML = ''
        dados.forEach(t => {
            tabela.innerHTML += `<tr>
            <td>${t[0]}</td>
            <td>${t[1]}</td>
            <td>${t[2]}</td>
            <td>${t[3]}</td>
            <td>${t[4]}</td>
            <td>${t[5]}</td>
        </tr>`

        })
    })
}