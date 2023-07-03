window.addEventListener("scroll", function(){
    var header = document.querySelector("header");
    header.classList.toggle("abajo",window.scrollY>0);
})

// Codigo API sheetDB
var form = document.getElementById('contact-form');
  form.addEventListener("submit", e => {
    e.preventDefault();
    fetch(form.action, {
        method : "POST",
        body: new FormData(document.getElementById("contact-form")),
    }).then(
        response => response.json()
    ).then((html) => {
      // you can put any JS code here
      
      form.reset();
      alert('Mensaje enviado. Nos contactaremos a la brevedad')
    });
  });



const button = document.getElementById("my-button");
const nav = document.getElementById("mynav");

button.addEventListener('click', () => {
  nav.classList.toggle('show');
});