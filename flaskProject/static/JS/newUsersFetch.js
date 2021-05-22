fetch('https://jsonplaceholder.typicode.com/users').then(
    response1 => response1.json()
).then(
    responseJSON1 => create1(responseJSON1)
).catch(
    err => console.log(err)
);

function create1(data) {
    const curMain = document.querySelector("main");
    for (let datum of data) {
        const section = document.createElement('Section');
        section.innerHTML = `
<div class="col-12">
        <div>
            ID : <span>${datum.id}</span> 
        </div>
        <div>
            Name : <span>${datum.name}</span> 
        </div>
         <div>
            User Name : <span>${datum.username}</span> 
        </div>
         <div>
            E-mail : <span>${datum.email}</span> 
        </div>
        </div>
    `;
        curMain.appendChild(section);
    }
}