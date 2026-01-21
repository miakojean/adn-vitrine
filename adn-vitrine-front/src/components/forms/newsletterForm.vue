<template>
  <div class="">
    <form v-if="!isSuccess" class="newsletter__form" @submit.prevent="handleSubmit">
      <inputFamily 
        v-model="payload.firstName"
        type="text"
        name="votre prenom"
        label="Votre prenom" 
        placeholder="Entrer votre prenom" 
      />
      <inputFamily 
        v-model="payload.email"
        type="email" 
        name="votre email"
        label="Votre email" 
        placeholder="Entrer votre adresse email" 
      />
      <div class="error__fields">
        <p>
          {{ errorMessage }}
        </p>
      </div>
      <mainButton 
        type="submit" 
        label="S'abonner"
        :is-loading="isLoading"
      />
    </form>

    <transition name="fade-transition">
      <div class="succes__container" v-if="isSuccess">
        <succesCheck :size="80" />
        <h3 class=" text-2xl font-bold">
          Abonnement réussi ! Merci de vous être abonné à notre newsletter.
        </h3>
      </div>
    </transition>
  </div>
</template>

<script lang="ts">
import mainButton from '../button/mainButton.vue';
import inputFamily from '../input/inputFamily.vue';
import succesCheck from '../tools/succesCheck.vue';
import { apiClient } from '../../services/api';
import { reactive, ref } from 'vue';

export default {
    name: 'NewsletterForm',
    components: { mainButton, inputFamily, succesCheck },
    setup() {
      
      // Gestion des etats
      const isLoading = ref(false);
      const errorMessage = ref('')
      const payload = reactive({
        firstName: '',
        email: '',
      })
      const isSuccess = ref(false);
      
      const handleSubmit = async() => {

        if (!payload.firstName || !payload.email) {
          errorMessage.value = '* Tous les champs sont obligatoires.';
          console.log("Champs manquants", payload.firstName, payload.email);
          return;
        }

        isLoading.value = true;
        errorMessage.value = ''

        try {
          const response = await apiClient.post('/newsletter/subscribers/', payload);
          isLoading.value = false;
          isSuccess.value = true;
          console.log('Abonnement réussi:', response.data);
        } catch (error) {
          isLoading.value = false;
          console.error('Erreur lors de l\'abonnement à la newsletter:', error);
          errorMessage.value = '* Une erreur est survenue. Veuillez réessayer.';
        }
        
      };

      return { isLoading, errorMessage, handleSubmit, payload, isSuccess };
    }
}
</script>

<style scoped>
/* --- Mobile first --- */
.newsletter__form {
  margin-bottom: 2rem;
  width: 100%;
  max-width: 500px;
  display: flex;
  flex-direction: column;
  justify-content: start;
  gap: 1rem;
  padding: 2rem 1rem;
  background: #1E293B;
  border-radius: 1rem;
}

input{
  padding: 1rem;
  width: 100%;
  color: var(--placeholder-color);
  border: 1px solid #A7CEFD;
  border-radius: 1.5rem;
  outline: #A7CEFD;
}

.error__fields {
  color: #F87171;
  font-size: 0.9rem;
  font-weight: 600;
  margin-top: -0.5rem;
}

</style>