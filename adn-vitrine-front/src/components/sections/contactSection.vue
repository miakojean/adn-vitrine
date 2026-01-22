<template>
    <section>
        <h2>
            Garantissons ensemble votre <span class="highlight">sécurité</span>
        </h2>
        <p>Gardons le contact</p>
        <form @submit.prevent="handleSubmit" class="contact__form">
            <!-- Form content goes here -->
            <inputFamily 
                v-model="payload.name"
                label="Nom et prenoms" 
                name="Nom et prenoms"
                placeholder="Entrer votre nom"
            />
            <inputFamily 
                v-model="payload.email"
                label="Email" 
                name="Email"
                placeholder="Entrer votre email"
            />
            <textAreaFamily 
                v-model="payload.message"
                label="Message" 
                name="Message"
                placeholder="Votre message ici..."
            />
            <mainButton 
                type="submit" 
                label="Envoyer le message"
            />

        </form>
    </section>
</template>

<script lang="ts">
import inputFamily from '../input/inputFamily.vue';
import textAreaFamily from '../input/textAreaFamily.vue';
import mainButton from '../button/mainButton.vue';
import { reactive, ref } from 'vue';
import { apiClient } from '../../services/api';

export default {
    components: { inputFamily, textAreaFamily, mainButton },
    setup() {
        const errorMessage = ref('');
        const isSuccess = ref(false);
        const payload = reactive({
            name: '',
            email: '',
            message: ''
        })

        // Additional logic for form submission can be added here
        const handleSubmit = async () => {
            errorMessage.value = '';
            try {
                // Example API call
                await apiClient.post('/contact', payload);
                isSuccess.value = true;
            } catch (error) {
                errorMessage.value = 'Une erreur est survenue. Veuillez réessayer.';
            }
        }

        return {
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
</style>