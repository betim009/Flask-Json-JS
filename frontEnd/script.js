import { getAllUsers } from "./src/services/fetchApi.js";

let data = null;
const nome = document.getElementById('nome');




window.addEventListener('DOMContentLoaded', async function () {
    data = await getAllUsers();



    this.window.handleSubmit = function (event) {
        event.preventDefault();
        alert(nome.value);
    };

    console.log(data);
});