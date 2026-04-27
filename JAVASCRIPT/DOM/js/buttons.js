const res = document.querySelector("#res");

// function add() {
//   res.textContent = parseInt(res.textContent) + 1;
// }

// function subtract() {
//   res.textContent = parseInt(res.textContent) - 1;
// }

// let btns = document.getElementsByTagName('button');
for(let btn of document.getElementsByTagName('button')){ btn.addEventListener('click',()=> res.textContent = parseInt(res.textContent) + parseInt(btn.textContent))};
