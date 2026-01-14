<template>
  <article class="article-card">
    <div class="article-card__image-container">
      <img 
        :src="imageSrc" 
        :alt="imageAlt" 
        class="article-card__img"
        loading="lazy" 
      />
    </div>

    <div class="article-card__content">
      <h3 class="article-card__title">
        {{ title }}
      </h3>
      
      <p class="article-card__description">
        {{ excerpt }}
      </p>

      <a :href="link" class="article-card__link">
        <span>{{ linkText }}</span>
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="icon">
          <path stroke-linecap="round" stroke-linejoin="round" d="M17.25 8.25 21 12m0 0-3.75 3.75M21 12H3" />
        </svg>
      </a>
    </div>
  </article>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'ArticleCard',
  props: {
    title: { type: String, required: true },
    excerpt: { type: String, required: true },
    imageSrc: { type: String, default: 'https://picsum.photos/800/600' },
    imageAlt: { type: String, default: '' },
    link: { type: String, default: '#' },
    linkText: { type: String, default: "Lire l'article" }
  }
});
</script>

<style scoped>
.article-card {
  --primary-color: #38bdf8;
  --bg-card: #1e293b;
  --border-color: #334155;
  --text-main: #f8fafc;
  --text-muted: #94a3b8;

  display: flex;
  flex-direction: column;
  background-color: var(--bg-card);
  border-radius: 12px;
  overflow: hidden; /* Important pour les coins arrondis de l'image */
  border: 1px solid var(--border-color);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
  height: 100%;
}

.article-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
  border-color: var(--primary-color);
}

.article-card__image-container {
  aspect-ratio: 16 / 9;
  overflow: hidden;
}

.article-card__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.article-card:hover .article-card__img {
  transform: scale(1.05);
}

.article-card__content {
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  flex-grow: 1; /* Pousse le lien vers le bas */
}

.article-card__title {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--text-main);
  margin-bottom: 0.75rem;
  line-height: 1.4;
}

.article-card__description {
  color: var(--text-muted);
  font-size: 0.95rem;
  line-height: 1.6;
  margin-bottom: 1.5rem;
  /* Limite à 3 lignes */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.article-card__link {
  margin-top: auto; /* Aligne le lien en bas */
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--primary-color);
  font-weight: 600;
  text-decoration: none;
  font-size: 0.9rem;
}

/* Astuce UX : Le lien recouvre toute la carte sans casser la sémantique */
.article-card__link::after {
  content: "";
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
}

.icon {
  width: 1.25rem;
  height: 1.25rem;
  transition: transform 0.2s ease;
}

.article-card:hover .icon {
  transform: translateX(4px);
}
</style>