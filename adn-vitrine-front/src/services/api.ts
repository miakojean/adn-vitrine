import axios from "axios";

const apiClient = axios.create({
    baseURL: 'http://localhost:8000/',
    timeout: 7000,
    headers: {
        'Content-Type': 'application/json',
    },
})

axios.interceptors.response.use(
    function (response){

        console.log('Mauvaise reponse du serveur')
        return response;
    }, function (error){
        console.log('Erreur reseau')
        return Promise.reject(error);
    }
)

export {apiClient}