<template>
    <section class="blog-section">
        <!-- Hero Header -->
        <div class="blog-hero">
            <div class="blog-hero__content">
                <h1 class="blog-hero__title">
                    Découvrez nos derniers articles de blog.
                </h1>
                <p class="blog-hero__subtitle">
                    Restez informé des dernières idées, tendances et innovations au sein du cabinet ADN consulting.
                </p>
            </div>
            
            <div class="blog-hero__cta">
                <div class="cta-content">
                    <h3 class="cta-title">Rejoignez notre communauté</h3>
                    <p class="cta-description">
                        Abonnez-vous pour découvrir les nouvelles fonctionnalités produits, les dernières technologies, solutions et mises à jour.
                    </p>
                    <newsletterForm />
                </div>
            </div>
        </div>

        <!-- État "Aucun article" -->
        <div v-if="!hasArticles" class="empty-state">
            <div class="empty-state__icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 7.5h1.5m-1.5 3h1.5m-7.5 3h7.5m-7.5 3h7.5m3-9h3.375c.621 0 1.125.504 1.125 1.125V18a2.25 2.25 0 0 1-2.25 2.25M16.5 7.5V18a2.25 2.25 0 0 0 2.25 2.25M16.5 7.5V4.875C16.5 4.253 15.996 3.75 15.375 3.75h-1.5a1.125 1.125 0 0 0-1.125 1.125V7.5m-6 3.75H3.375c-.621 0-1.125.504-1.125 1.125v9c0 .621.504 1.125 1.125 1.125h9c.621 0 1.125-.504 1.125-1.125v-9c0-.621-.504-1.125-1.125-1.125H10.5" />
                </svg>
            </div>
            <h3 class="empty-state__title">Aucun article disponible pour le moment</h3>
            <p class="empty-state__message">
                Notre équipe est en train de préparer du contenu de qualité pour vous.
                Revenez bientôt pour découvrir nos premiers articles !
            </p>
        </div>

        <!-- Articles Grid (uniquement si hasArticles = true) -->
        <div v-else class="blog-grid-container">
            <div class="blog-grid">
                <!-- Featured Large Article -->
                <article class="article-card featured">
                    <div class="article-card__image">
                        <img src="https://picsum.photos/800/600" alt="Featured article" loading="lazy" />
                        <span class="article-card__badge">À la une</span>
                    </div>
                    <div class="article-card__content">
                        <div class="article-meta">
                            <span class="article-category">Design</span>
                            <span class="article-date">15 Mai 2024</span>
                            <span class="article-readtime">8 min</span>
                        </div>
                        <h3 class="article-title">
                            L'avenir du design UI : tendances émergentes pour 2024
                        </h3>
                        <p class="article-excerpt">
                            Découvrez comment l'intelligence artificielle, les expériences immersives et le design durable façonnent la nouvelle génération d'interfaces.
                        </p>
                        <div class="article-author">
                            <img src="https://i.pravatar.cc/40" alt="Auteur" class="author-avatar" />
                            <div class="author-info">
                                <span class="author-name">Sarah Chen</span>
                                <span class="author-role">Designer principale</span>
                            </div>
                        </div>
                    </div>
                </article>

                <!-- Regular Articles -->
                <article 
                    v-for="article in displayedArticles" 
                    :key="article.id"
                    class="article-card"
                >
                    <div class="article-card__image">
                        <img :src="article.image" :alt="article.title" loading="lazy" />
                        <span class="article-card__badge">{{ article.category }}</span>
                    </div>
                    <div class="article-card__content">
                        <div class="article-meta">
                            <span class="article-category">{{ article.category }}</span>
                            <span class="article-date">{{ article.date }}</span>
                            <span class="article-readtime">{{ article.readTime }}</span>
                        </div>
                        <h3 class="article-title">{{ article.title }}</h3>
                        <p class="article-excerpt">{{ article.excerpt }}</p>
                        <div class="article-author">
                            <img :src="article.author.avatar" :alt="article.author.name" class="author-avatar" />
                            <div class="author-info">
                                <span class="author-name">{{ article.author.name }}</span>
                                <span class="author-role">{{ article.author.role }}</span>
                            </div>
                        </div>
                    </div>
                </article>
            </div>

        </div>
    </section>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import newsletterForm from '../forms/newsletterForm.vue'

// Changement ici : mettre à false pour voir l'état "Aucun article"
const hasArticles = ref(false)

const pageSize = 6
const currentPage = ref(1)

const articles = ref([
    {
        id: 1,
        title: 'Création de systèmes de design accessibles',
        excerpt: 'Apprenez à créer des systèmes de design qui fonctionnent pour tous, y compris les utilisateurs en situation de handicap.',
        image: 'https://picsum.photos/400/300?random=1',
        category: 'Design',
        date: '12 Mai 2024',
        readTime: '6 min',
        author: { name: 'Alex Johnson', role: 'Responsable accessibilité', avatar: 'https://i.pravatar.cc/40?img=1' }
    },
    {
        id: 2,
        title: "L'essor de l'IA dans le design produit",
        excerpt: "Comment l'intelligence artificielle transforme notre façon de concevoir et de construire des produits.",
        image: 'https://picsum.photos/400/300?random=2',
        category: 'Technologie',
        date: '10 Mai 2024',
        readTime: '7 min',
        author: { name: 'Maria Rodriguez', role: 'Chercheuse IA', avatar: 'https://i.pravatar.cc/40?img=2' }
    },
    {
        id: 3,
        title: 'Interview avec le CEO de Figma',
        excerpt: "Une conversation exclusive sur l'avenir des outils de design collaboratif.",
        image: 'https://picsum.photos/400/300?random=3',
        category: 'Interviews',
        date: '8 Mai 2024',
        readTime: '10 min',
        author: { name: 'David Lee', role: 'Rédacteur en chef', avatar: 'https://i.pravatar.cc/40?img=3' }
    }
])

const displayedArticles = computed(() => 
    articles.value.slice(0, currentPage.value * pageSize)
)


</script>

<style scoped>
.blog-section {
    --color-bg: #0F172A;
    --color-surface: #1E293B;
    --color-primary: #3B82F6;
    --color-accent: #8B5CF6;
    --color-text: #F8FAFC;
    --color-text-secondary: #94A3B8;
    --color-border: #475569;
    
    background-color: var(--color-bg);
    color: var(--color-text);
    min-height: 100vh;
    padding: 2rem 1.5rem;
}

/* Hero Section */
.blog-hero {
    max-width: 1200px;
    margin: 0 auto 4rem;
    display: flex;
    align-items: center;
    flex-direction: column;
    gap: 3rem;
    padding: 4rem 0;
    border-bottom: 1px solid var(--color-border);
}

@media (min-width: 1024px) {
    .blog-hero {
        flex-direction: row;
        gap: 4rem;
    }
    
    .blog-hero__content { flex: 2; }
    .blog-hero__cta { flex: 1; }
}

.blog-hero__title {
    font-size: clamp(2rem, 5vw, 3.5rem);
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 1.5rem;
    background: linear-gradient(to right, #fff, var(--color-primary));

    -webkit-text-fill-color: transparent;
}

.blog-hero__subtitle {
    font-size: 1.125rem;
    color: var(--color-text-secondary);
    line-height: 1.6;
    max-width: 600px;
}

/* CTA Section */
.cta-content {
    background: var(--color-surface);
    border-radius: 16px;
    padding: 2rem;
    border: 1px solid var(--color-border);
}

.cta-title {
    font-size: 1.25rem;
    font-weight: 700;
    margin-bottom: 0.75rem;
}

.cta-description {
    font-size: 0.95rem;
    color: var(--color-text-secondary);
    line-height: 1.6;
    margin-bottom: 1.5rem;
}

/* Empty State */
.empty-state {
    max-width: 600px;
    margin: 4rem auto;
    padding: 4rem 2rem;
    text-align: center;
    background: var(--color-surface);
    border-radius: 24px;
    border: 1px solid var(--color-border);
}

.empty-state__icon {
    margin-bottom: 2rem;
}

.empty-state__icon svg {
    color: var(--color-primary);
    opacity: 0.7;
}

.empty-state__title {
    font-size: 1.75rem;
    font-weight: 700;
    margin-bottom: 1rem;
    color: var(--color-text);
}

.empty-state__message {
    font-size: 1.125rem;
    line-height: 1.6;
    color: var(--color-text-secondary);
    margin-bottom: 2rem;
    max-width: 500px;
    margin-left: auto;
    margin-right: auto;
}

.empty-state__cta {
    display: inline-flex;
    align-items: center;
    gap: 0.75rem;
    padding: 1rem 2rem;
    background: linear-gradient(135deg, var(--color-primary), var(--color-accent));
    border: none;
    border-radius: 12px;
    color: white;
    font-weight: 600;
    cursor: pointer;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.empty-state__cta:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(59, 130, 246, 0.3);
}

.empty-state__cta svg {
    width: 20px;
    height: 20px;
}

/* Articles Grid */
.blog-grid-container {
    max-width: 1200px;
    margin: 0 auto;
}

.blog-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 2rem;
    margin-bottom: 3rem;
}

@media (min-width: 1024px) {
    .blog-grid {
        grid-template-columns: repeat(3, 1fr);
    }
    
    .article-card.featured {
        grid-column: 1 / -1;
        display: grid;
        grid-template-columns: 2fr 1fr;
        gap: 2rem;
    }
}

/* Article Cards */
.article-card {
    background: var(--color-surface);
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid var(--color-border);
    transition: all 0.3s ease;
    cursor: pointer;
}

.article-card:hover {
    transform: translateY(-4px);
    border-color: var(--color-primary);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}

.article-card__image {
    position: relative;
    aspect-ratio: 16/9;
    overflow: hidden;
}

.article-card__image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
}

.article-card:hover .article-card__image img {
    transform: scale(1.05);
}

.article-card__badge {
    position: absolute;
    top: 1rem;
    left: 1rem;
    background: var(--color-primary);
    color: white;
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
}

.article-card__content {
    padding: 1.5rem;
}

.article-meta {
    display: flex;
    gap: 0.75rem;
    margin-bottom: 1rem;
    font-size: 0.75rem;
    color: var(--color-text-secondary);
}

.article-category {
    color: var(--color-primary);
    font-weight: 600;
}

.article-title {
    font-size: 1.25rem;
    font-weight: 700;
    line-height: 1.4;
    margin-bottom: 0.75rem;
}

.article-excerpt {
    font-size: 0.95rem;
    line-height: 1.6;
    color: var(--color-text-secondary);
    margin-bottom: 1.5rem;
}

.article-author {
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.author-avatar {
    width: 2.5rem;
    height: 2.5rem;
    border-radius: 50%;
    object-fit: cover;
}

.author-info {
    display: flex;
    flex-direction: column;
}

.author-name {
    font-size: 0.875rem;
    font-weight: 600;
}

.author-role {
    font-size: 0.75rem;
    color: var(--color-text-secondary);
}

/* Load More */
.load-more-container {
    text-align: center;
    padding: 3rem 0;
}

.load-more-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.75rem;
    padding: 1rem 2.5rem;
    background: var(--color-surface);
    border: 1px solid var(--color-primary);
    border-radius: 20px;
    color: var(--color-primary);
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    margin-bottom: 1rem;
}

.load-more-btn:hover {
    background: var(--color-primary);
    color: white;
    transform: translateY(-2px);
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.load-more-text {
    color: var(--color-text-secondary);
    font-size: 0.875rem;
}

/* Responsive */
@media (max-width: 768px) {
    .blog-section {
        padding: 1.5rem 1rem;
    }
    
    .blog-hero {
        padding: 2rem 0;
        margin-bottom: 2rem;
    }
    
    .empty-state {
        margin: 2rem auto;
        padding: 2rem 1.5rem;
    }
    
    .empty-state__title {
        font-size: 1.5rem;
    }
    
    .article-card.featured {
        grid-template-columns: 1fr;
    }
}
</style>