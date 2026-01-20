<template>
  <section class="newsletter">
    <div class="newsletter__container">
      
      <div class="newsletter__content">
        <h3 class="newsletter__title">
          Soyez au courant <br />
          des dernières nouveautés.
        </h3>
        <p class="newsletter__description">
          Abonnez-vous à notre newsletter pour recevoir les dernières mises à jour,
          des conseils exclusifs et des offres spéciales directement dans votre boîte
          de réception.
        </p>
        <newsletterForm />
      </div>

      <div class="newsletter__visual">
        <div class="visual__glow"></div>
        <div class="visual__image-wrapper">
          <img 
            src="../../assets/pic/undraw_subscriber_whh0.svg" 
            alt="3D Illustration" 
            class="visual__img"
          />
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import newsletterForm from '../forms/newsletterForm.vue';
</script>

<style scoped>
/* Variables de design */
.newsletter {
  
  min-height: 100vh;
  background-color: #0F172A;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 6rem 2rem 1rem 2rem;
  overflow: hidden;
  color:#f8fafc;
}

.newsletter__container {
  max-width: 1200px;
  width: 100%;
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 4rem;
  align-items: center;
}

/* --- COTÉ TEXTE --- */
.newsletter__title {
  color: var(--text-main);
  font-size: clamp(1.5rem, 4vw, 2.5rem);
  font-weight: 700;
  line-height: 1.1;
  margin-bottom: 1.5rem;
  letter-spacing: -0.02em;
}

.newsletter__description {
  color: #94A3B8;
  font-size: 1.15rem;
  line-height: 1.6;
  max-width: 500px;
  margin-bottom: 2.5rem;
}

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

/* --- COTÉ VISUEL & GLOW --- */
.newsletter__visual {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}

.visual__glow {
  position: absolute;
  width: 150%;
  height: 150%;
  background: var(--accent-glow);
  filter: blur(50px);
  z-index: 1;
}

.visual__image-wrapper {
  position: relative;
  z-index: 2;
  width: 100%;
}

.visual__img {
  width: 100%;
  height: auto;
  display: block;
  /* Animation de flottement pour l'aspect 3D */
  animation: floating 5s ease-in-out infinite;
}

@keyframes floating {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-15px); }
}

/* --- RESPONSIVE --- */
@media (max-width: 1024px) {
  .newsletter__container {
    grid-template-columns: 1fr;
    text-align: center;
    gap: 3rem;
  }
  
  .newsletter__content {
    display: flex;
    flex-direction: column;
    align-items: center;
    order: 2;
  }

  .newsletter__visual {
    order: 1;
    max-width: 400px;
    margin: 0 auto;
  }

  .form__group {
    flex-direction: column;
    width: 100%;
    max-width: 400px;
  }
}
</style>