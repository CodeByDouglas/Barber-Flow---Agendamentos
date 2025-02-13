document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.barber-card');

    cards.forEach(function(card) {  // Corrigido: função dentro do forEach
        card.addEventListener('click', function() {
            window.location.href = '/agenda/funcionario/servico';
        });
    });
});
