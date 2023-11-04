const header = document.getElementById('header');
const colorForm = document.getElementById('colorForm');
const colorInput = document.getElementById('colorInput');


function changeTextColor(event) {
    event.preventDefault();
    const userColor = colorInput.value;
    header.style.color = userColor;
    colorInput.value = '';
}


colorForm.addEventListener('submit', changeTextColor);