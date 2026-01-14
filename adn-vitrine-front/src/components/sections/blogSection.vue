<template>
    <section class="blog-section">
        <header class="blog-header">
            <span class="blog-header__badge">Actualités</span>
            <h2 class="blog-header__title">Blog & Articles</h2>
            <p class="blog-header__subtitle">
                Restez à l'affût des dernières innovations juridiques et technologiques.
            </p>
            
            <div class="blog-header__action">
                <newsletterForm />
            </div>
        </header>

        <div class="blog-content">
            <div class="blog-content__top">
                <h3 class="blog-content__title">Dernières publications</h3>
                <navCategory
                    :tabs="categories"
                    variant="minimal"
                />
            </div>

            <div class="blog-grid">
                <articleCards 
                    v-for="i in 3" :key="i"
                    title="Transformation numérique dans le droit"
                    excerpt="Découvrez comment la transformation numérique révolutionne le secteur juridique en améliorant l'efficacité."
                    imageSrc="https://picsum.photos/400/300"
                    link="#"
                />
            </div>

            <button class="blog-load-more">Voir tous les articles</button>
        </div>
    </section>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import newsletterForm from '../forms/newsletterForm.vue';
import navCategory from '../navigation/navCategory.vue';
import articleCards from '../cards/articleCards.vue';

export default defineComponent({
    name: 'BlogSection',
    components: { newsletterForm, navCategory, articleCards },
    setup() {
        const categories = [
            { id: 'all', label: 'Tous', count: 12 },
            { id: 'legal', label: 'Juridique', count: 5 },
            { id: 'tech', label: 'Technologie', count: 4 },
            { id: 'business', label: 'Business', count: 3 }
        ];
        return { categories };
    }
});
</script>

<style scoped>
/* Variables locales pour la cohérence */
.blog-section {
    --primary: #38bdf8;
    --bg-dark: #0f172a;
    --bg-card: #1e293b;
    --text-muted: #94a3b8;
    
    width: 100%;
    padding: 100px 1.5rem;
    background-color: var(--bg-dark);
    color: #f8fafc;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.blog-header {
    max-width: 800px;
    text-align: center;
    margin-bottom: 5rem;
}

.blog-header__badge {
    color: var(--primary);
    text-transform: uppercase;
    letter-spacing: 0.1rem;
    font-size: 0.8rem;
    font-weight: 700;
    margin-bottom: 1rem;
    display: inline-block;
}

.blog-header__title {
    font-size: clamp(2.5rem, 5vw, 3.5rem);
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 1.5rem;
    background: linear-gradient(to bottom, #fff, #94a3b8);
    -webkit-text-fill-color: transparent;
}

.blog-header__subtitle {
    font-size: 1.2rem;
    color: var(--text-muted);
    max-width: 600px;
    margin: 0 auto 2.5rem;
}

.blog-content {
    max-width: 1240px;
    width: 100%;
}

.blog-content__top {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    margin-bottom: 3rem;
    border-bottom: 1px solid #334155;
    padding-bottom: 1rem;
    gap: 2rem;
}

.blog-content__title {
    font-size: 1.5rem;
    font-weight: 600;
    white-space: nowrap;
}

/* Grille Responsive */
.blog-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 2rem;
}

@media (min-width: 768px) {
    .blog-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (min-width: 1024px) {
    .blog-grid {
        grid-template-columns: repeat(3, 1fr);
    }
}

.blog-load-more {
    margin: 4rem auto 0;
    display: block;
    padding: 1rem 2.5rem;
    background: transparent;
    border: 1px solid #334155;
    color: white;
    border-radius: 99px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
}

.blog-load-more:hover {
    background: #f8fafc;
    color: var(--bg-dark);
}

/* Ajustement mobile pour le header de section */
@media (max-width: 768px) {
    .blog-content__top {
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
}
</style>