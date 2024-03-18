const footer = document.querySelector('footer');

const colors = ['#000000', '#009688', '#2196F3', '#FF5722', '#97a02f', '#ff00d5']; // Add more colors if needed

let index = 0;

setInterval(() => {
    footer.style.backgroundColor = colors[index];
    index = (index + 1) % colors.length;
}, 1200); // Change color every 2 seconds