const form = document.querySelector('#calc');
const n1 = document.querySelector('#n1');
const n2 = document.querySelector('#n2');
const op = document.querySelector('#op');
const resultado = document.querySelector('#resultado');
const erro = document.querySelector('#erro')

form.addEventListener('submit' , function (event) {
    event.preventDefault();
    const a = Number(n1.value);
    const b = Number(n2.value);
    let conta;

    if (op.value === '+') conta =  a + b;
    if (op.value === '-') conta = a - b;
    if (op.value === '*') conta = a * b;
    if (op.value === '/') conta = a / b;

    if (n1.value, n2.value === "0") {
        erro.textContent = ('Não dá pra dividir por zero!!!');
    }

    resultado.textContent = conta;
})