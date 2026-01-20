<template>
  <form class="newsletter__form" @submit.prevent="handleSubmit">
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
</template>

<script lang="ts">
import mainButton from '../button/mainButton.vue';
import inputFamily from '../input/inputFamily.vue';
import { apiClient } from '../../services/api';
import { reactive, ref } from 'vue';

export default {
    name: 'NewsletterForm',
    components: { mainButton, inputFamily },
    setup() {
      
      // Gestion des etats
      const isLoading = ref(false);
      const errorMessage = ref('')
      const payload = reactive({
        firstName: '',
        email: '',
      })
      
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
          console.log("Formulaire envoyé", response.data);
        } catch (error) {
          isLoading.value = false;
          console.error('Erreur lors de l\'abonnement à la newsletter:', error);
          errorMessage.value = '* Une erreur est survenue. Veuillez réessayer.';
        }
        
      };

      return { isLoading,errorMessage, handleSubmit, payload };
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