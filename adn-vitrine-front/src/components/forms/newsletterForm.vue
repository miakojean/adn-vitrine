<template>
  <form class="newsletter__form" @submit.prevent="handleSubmit">
    <input 
      type="email" 
      class="form__input" 
      placeholder="email@exemple.com" 
      required
    />
    <mainButton 
      type="submit" 
      label="S'abonner" 
    />
  </form>
</template>

<script lang="ts">
import mainButton from '../button/mainButton.vue';

export default {
    name: 'NewsletterForm',
    components: { mainButton },
    setup() {
      const handleSubmit = () => {
        console.log("Formulaire envoyé");
      };

      return { handleSubmit };
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
}

input{
  padding: 1rem;
  width: 100%;
  color: var(--placeholder-color);
  border: 1px solid #A7CEFD;
  border-radius: 1.5rem;
  outline: #A7CEFD;
}

</style>