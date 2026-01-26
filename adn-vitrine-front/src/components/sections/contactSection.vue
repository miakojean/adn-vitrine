<template>
    <section>
        <h2>
            Garantissons ensemble votre <span class="highlight">sécurité</span>
        </h2>
        <p>Nous contacter</p>
        <form @submit.prevent="handleSubmit" class="contact__form" v-if="!isSuccess">
            <!-- Form content goes here -->
            <inputFamily 
                v-model="payload.name"
                label="Nom et prenoms" 
                name="Nom et prenoms"
                placeholder="Entrer votre nom"
            />
            <inputFamily 
                v-model="payload.phone_number"
                label="Téléphone" 
                name="Téléphone"
                placeholder="Entrer votre numéro de téléphone"
            />
            <inputFamily 
                v-model="payload.email"
                label="Email" 
                name="Email"
                placeholder="Entrer votre adresse email"
            />
            <inputFamily 
                v-model="payload.subject"
                label="Sujet" 
                name="Sujet"
                placeholder="Sujet de votre message"
            />
            <textAreaFamily 
                v-model="payload.message"
                label="Message" 
                name="Message"
                placeholder="Votre message ici..."
            />
            <p class="error-message">{{ errorMessage }}</p>
            <mainButton 
                type="submit" 
                label="Envoyer le message"
                :is-loading="isLoading"
            />
        </form>
        <succesCheck v-if="isSuccess" />
    </section>
</template>

<script lang="ts">
import inputFamily from '../input/inputFamily.vue';
import textAreaFamily from '../input/textAreaFamily.vue';
import mainButton from '../button/mainButton.vue';
import succesCheck from '../tools/succesCheck.vue';
import { reactive, ref } from 'vue';
import { apiClient } from '../../services/api';

interface ContactPayload {
    name: string;
    phone_number: string;
    email: string;
    subject: string;
    message: string;
}

export default {
    components: { 
        inputFamily, 
        textAreaFamily, 
        mainButton,
        succesCheck
    },
    setup() {

        // State
        const isLoading = ref<boolean>(false);
        const errorMessage = ref('');
        const isSuccess = ref(false);
        const payload = reactive<ContactPayload>({
            name: '',
            phone_number: '',
            email: '',
            subject: '',
            message: '',
        });



        // Action of the compnent.
        const handleSubmit = async () => {
            if (payload.name === '' || payload.email === '' || payload.message === '') {
                errorMessage.value = 'Veuillez remplir tous les champs obligatoires.';
                console.log("Champs manquants", payload.name, payload.email, payload.message);
                return;
            }
            isLoading.value = true;
            try {
                // Example API call
                await apiClient.post('/contact/messages/', payload);
                isSuccess.value = true;
                isLoading.value = false;
                console.log('Message envoyé avec succès');
            } catch (error) {
                errorMessage.value = 'Une erreur est survenue. Veuillez réessayer.';
            } finally {
                isLoading.value = false;
            }
        }

        return {
            isLoading,
            errorMessage,
            isSuccess,
            payload,
            handleSubmit,
        }
    }
}

</script>

<style scoped>
section {
  position: relative;
  background-color: #0f172a;
  padding: 6rem 1.5rem;
  overflow: hidden;
  min-height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

section h2{
    font-size: 3rem;
    font-weight: 600;
    color: aliceblue;
}

section p{
    font-size: 1.3rem;
    font-weight: 600;
    color: white;
}

.highlight {
    color: #3b82f6;
    font-weight: bold;
}

.contact__form {
    margin-top: 2rem;
    width: 100%;
    max-width: 500px;
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}
.error-message {
    color: #f87171;
    font-size: 0.9rem;
    font-weight: 600;
    margin-top: -0.5rem;
}
</style>