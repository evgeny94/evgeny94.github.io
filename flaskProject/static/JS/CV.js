function downloadCV() {
    window.open('/downloadCV')
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

let obj;

fetch('https://jsonplaceholder.typicode.com/users').then(
    response1 => response1.json()
).then(
    usersData => obj=usersData
).catch(
    err => console.log(err)
);

function getObj(){
    return obj;
}

