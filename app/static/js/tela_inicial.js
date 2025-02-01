document.addEventListener('DOMContentLoaded', function() {
    const button = document.querySelector('.agendar-button');

    
    button.addEventListener('click', function() {
        
        window.location.href = '/agenda/funcionario';
    });
});
