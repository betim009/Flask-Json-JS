export async function getAllUsers() {
    const req = await fetch('http://127.0.0.1:5000/usuarios');
    const res = await req.json();

    return res;
};