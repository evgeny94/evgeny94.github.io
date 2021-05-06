function downloadCV() {
    window.open('Evgeny%20Musatov-CV.docx');
}

let upperTxt = "I say... Will > Skill :)";
let i = 0;

function introFunction() {
    if (i < upperTxt.length) {
        document.getElementById("legacy").innerHTML += upperTxt.charAt(i);
        i++;
        setTimeout(introFunction, 200);
    }
}
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

