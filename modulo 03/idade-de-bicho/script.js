const botao = document.querySelector('.tema');

function trocarTema() {
    document.body.classList.toggle('escuro');

    if (document.body.classList.contains('escuro')) {
        botao.textContent = '☀️ Claro';
    } else {
        botao.textContent = '🌙 Escuro'
    }
}

function calculaIdade(animal, fator, emoji) {
    const idade_usuario = document.querySelector("#idade").value;
    if (!idade_usuario || idade_usuario <=0) {
        document.querySelector('#idade').classList.add('erro')
        return;
    }

    document.querySelector("#idade").classList.remove('erro');
    const idade_final = fator*idade_usuario

    document.querySelector("#resultado").textContent =
    'Você tem ' + idade_final + ' anos de ' + animal + '! ' + emoji;
}
