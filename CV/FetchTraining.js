fetch('https://reqres.in/api/users?page=2').then(
    response => response.json()
).then(
    responseJSON => create(responseJSON.data)
).catch(
    err => console.log(err)
);

function create(data){
const curMain = document.querySelector("main");
for (let datum of data){
    const section = document.createElement('Section');
    section.innerHTML=`
        <img src="${datum.avatar}"/>
        <div>
            <span>${datum.first_name} ${datum.last_name}</span> 
        </div>
    `;
    curMain.appendChild(section);
}
}