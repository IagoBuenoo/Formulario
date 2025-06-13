let feira = document.getElementsByName('feira')
let dias = document.getElementById('dias-feira')

function verificar() {
    if (feira[0].checked) {
    dias.style.display = 'flex'
    } else {
        dias.style.display = 'none'
    }  
}