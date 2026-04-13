async function generate() {

let data = {
age: document.getElementById("age").value,
height: document.getElementById("height").value,
weight: document.getElementById("weight").value,
goal: document.getElementById("goal").value,
days: document.getElementById("days").value,
equipment: document.getElementById("equipment").value
}

let response = await fetch("http://127.0.0.1:8000/generate-plan",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify(data)
})

let result = await response.json()

document.getElementById("result").innerText =
JSON.stringify(result,null,2)

}