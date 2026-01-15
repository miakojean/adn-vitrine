<template>
  <form class="newsletter__form" @submit.prevent="handleSubmit">
    <div class="form__group">
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
    </div>
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
/* --- FORMULAIRE PILL-STYLE --- */
.newsletter__form {
  margin-bottom: 2rem;
  max-width: 500px;
}

.form__group {
  display: flex;
  gap: 1rem;
  background: transparent;
  border:2px solid #3c589a;
  border-radius: 2rem;
  padding: 0.2rem;
}

.form__input {
  flex: 1;
  background-color: var(--input-bg);
  border: none;
  padding: 1.1rem 1.7rem;
  border-radius: 100px;
  color: white;
  font-size: 1rem;
  outline: none;
  transition: box-shadow 0.3s ease;
}

.form__button {
  background-color: white;
  color: black;
  border: none;
  padding: 1.1rem 2rem;
  border-radius: 100px;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  transition: transform 0.2s ease, background-color 0.2s ease;
  white-space: nowrap;
}

.form__button:hover {
  background-color: #e4e4e7;
  transform: translateY(-2px);
}

.newsletter__footer-text {
  color: var(--text-footer);
  font-size: 0.85rem;
  font-style: italic;
  max-width: 400px;
  line-height: 1.4;
}
</style>