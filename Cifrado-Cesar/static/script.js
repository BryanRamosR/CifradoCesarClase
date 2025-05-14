document.addEventListener('DOMContentLoaded', function() {
    const encryptedText = document.getElementById('encrypted-text');
    if (encryptedText) {
        setTimeout(function() {
             encryptedText.classList.add('show');}, 100); 
    }
});
