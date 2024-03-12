// Script for displaying/hiding the description button based on screen size
window.onload = function() {
    const descriptionBtnDesk = document.querySelector('.btn-desk');
    const descriptionBtn = document.querySelector('.btn');

    if (window.matchMedia && window.matchMedia('(min-width: 768px)').matches) {
        descriptionBtn.style.display = 'none';
        descriptionBtnDesk.style.display = 'inline-block'
    } else {
        descriptionBtn.style.display = 'inline-block';
        descriptionBtnDesk.style.display = 'none';
    }
}