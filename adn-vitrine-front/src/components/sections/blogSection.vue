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
                    <div class="cta-form">
                        <newsletterForm />
                    </div>
                </div>
            </div>
        </div>

        <!-- Articles Grid -->
        <div class="blog-grid-container">
            <div class="blog-grid">
                <!-- Featured Large Article -->
                <article class="article-card featured">
                    <div class="article-card__image">
                        <img src="https://picsum.photos/800/600" alt="Featured article" loading="lazy" />
                        <div class="article-card__badge">Featured</div>
                    </div>
                    <div class="article-card__content">
                        <div class="article-meta">
                            <span class="article-category">Design</span>
                            <span class="article-date">May 15, 2024</span>
                            <span class="article-readtime">8 min read</span>
                        </div>
                        <h3 class="article-title">
                            The Future of UI Design: Emerging Trends for 2024
                        </h3>
                        <p class="article-excerpt">
                            Discover how artificial intelligence, immersive experiences, and sustainable design are shaping the next generation of user interfaces.
                        </p>
                        <div class="article-author">
                            <img src="https://i.pravatar.cc/40" alt="Author" class="author-avatar" />
                            <div class="author-info">
                                <span class="author-name">Sarah Chen</span>
                                <span class="author-role">Lead Designer</span>
                            </div>
                        </div>
                    </div>
                </article>

                <!-- Regular Articles -->
                <article 
                    v-for="article in articles" 
                    :key="article.id"
                    class="article-card"
                >
                    <div class="article-card__image">
                        <img :src="article.image" :alt="article.title" loading="lazy" />
                        <div class="article-card__badge">{{ article.category }}</div>
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

            <!-- Load More -->
            <div class="load-more-container">
                <button class="load-more-btn" @click="loadMoreArticles">
                    <span>Load More Articles</span>
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                        <path d="M12 5V19M12 19L5 12M12 19L19 12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                    </svg>
                </button>
                <p class="load-more-text">Showing {{ displayedArticles }} of {{ totalArticles }} articles</p>
            </div>
        </div>
    </section>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from 'vue';
import newsletterForm from '../forms/newsletterForm.vue';

export default defineComponent({
    name: 'BlogSection',
    components: { newsletterForm },
    setup() {
        const categories = [
            { id: 'all', label: 'All', count: 24 },
            { id: 'design', label: 'Design', count: 8 },
            { id: 'technology', label: 'Technology', count: 6 },
            { id: 'interviews', label: 'Interviews', count: 5 },
            { id: 'resources', label: 'Resources', count: 5 }
        ];

        const activeCategory = ref('all');
        const displayedArticles = ref(6);
        const totalArticles = 24;

        const articles = ref([
            {
                id: 1,
                title: 'Building Accessible Design Systems',
                excerpt: 'Learn how to create design systems that work for everyone, including users with disabilities.',
                image: 'https://picsum.photos/400/300?random=1',
                category: 'Design',
                date: 'May 12, 2024',
                readTime: '6 min read',
                author: {
                    name: 'Alex Johnson',
                    role: 'Accessibility Lead',
                    avatar: 'https://i.pravatar.cc/40?img=1'
                }
            },
            {
                id: 2,
                title: 'The Rise of AI in Product Design',
                excerpt: 'How artificial intelligence is transforming the way we design and build products.',
                image: 'https://picsum.photos/400/300?random=2',
                category: 'Technology',
                date: 'May 10, 2024',
                readTime: '7 min read',
                author: {
                    name: 'Maria Rodriguez',
                    role: 'AI Researcher',
                    avatar: 'https://i.pravatar.cc/40?img=2'
                }
            },
            {
                id: 3,
                title: 'Interview with Figma CEO',
                excerpt: 'An exclusive conversation about the future of collaborative design tools.',
                image: 'https://picsum.photos/400/300?random=3',
                category: 'Interviews',
                date: 'May 8, 2024',
                readTime: '10 min read',
                author: {
                    name: 'David Lee',
                    role: 'Editor-in-Chief',
                    avatar: 'https://i.pravatar.cc/40?img=3'
                }
            },
            {
                id: 4,
                title: 'Free Icon Sets for 2024',
                excerpt: 'A curated collection of the best free icon resources for your next project.',
                image: 'https://picsum.photos/400/300?random=4',
                category: 'Resources',
                date: 'May 5, 2024',
                readTime: '5 min read',
                author: {
                    name: 'Emma Wilson',
                    role: 'Resource Curator',
                    avatar: 'https://i.pravatar.cc/40?img=4'
                }
            },
            {
                id: 5,
                title: 'Mobile UX Best Practices',
                excerpt: 'Essential guidelines for creating exceptional mobile user experiences.',
                image: 'https://picsum.photos/400/300?random=5',
                category: 'Design',
                date: 'May 3, 2024',
                readTime: '8 min read',
                author: {
                    name: 'James Kim',
                    role: 'Mobile UX Specialist',
                    avatar: 'https://i.pravatar.cc/40?img=5'
                }
            }
        ]);

        const loadMoreArticles = () => {
            if (displayedArticles.value < totalArticles) {
                displayedArticles.value += 3;
            }
        };

        const hasMoreArticles = computed(() => {
            return displayedArticles.value < totalArticles;
        });

        return {
            categories,
            activeCategory,
            articles,
            displayedArticles,
            totalArticles,
            hasMoreArticles,
            loadMoreArticles
        };
    }
});
</script>

<style scoped>
/* Variables */
.blog-section {
    --color-bg: #0F172A;
    --color-surface: #1E293B;
    --color-surface-light: #334155;
    --color-primary: #3B82F6;
    --color-primary-light: #60A5FA;
    --color-text: #F8FAFC;
    --color-text-secondary: #94A3B8;
    --color-text-muted: #64748B;
    --color-border: #475569;
    --color-accent: #8B5CF6;
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --radius-xl: 24px;
    --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
    
    background-color: var(--color-bg);
    color: var(--color-text);
    min-height: 100vh;
    padding: 2rem 1.5rem;
}

/* Hero Section */
.blog-hero {
    max-width: 1200px;
    min-height: 100vh;
    margin: 0 auto 4rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 2rem;
    padding: 2rem 0;
    border-bottom: 1px solid var(--color-border);
}

.blog-hero__cta {
    width: 100%;
}


@media (min-width: 1024px) {
    .blog-hero {
        display: grid;
        grid-template-columns: 2fr 1fr;
        gap: 1rem;
    }
}

.blog-hero__badge {
    margin-bottom: 1rem;
}

.blog-hero__badge span {
    background: linear-gradient(135deg, var(--color-primary), var(--color-accent));
    padding: 0.5rem 1rem;
    border-radius: var(--radius-xl);
    font-size: 0.875rem;
    font-weight: 600;
    letter-spacing: 0.05em;
}

.blog-hero__title {
    font-size: clamp(2rem, 5vw, 3.5rem);
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 1.5rem;
    background: linear-gradient(to right, #fff, var(--color-primary-light));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
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
    border-radius: var(--radius-lg);
    padding: 2rem;
    border: 1px solid var(--color-border);
}

.cta-title {
    font-size: 1.25rem;
    font-weight: 700;
    margin-bottom: 0.75rem;
    color: var(--color-text);
}

.cta-description {
    font-size: 0.95rem;
    color: var(--color-text-secondary);
    line-height: 1.6;
    margin-bottom: 1.5rem;
}

/* Navigation */
.blog-navigation {
    max-width: 1200px;
    margin: 0 auto 3rem;
}

.nav-container {
    background: var(--color-surface);
    border-radius: var(--radius-lg);
    padding: 1.5rem;
    border: 1px solid var(--color-border);
}

.nav-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
}

.nav-title {
    font-size: 1.5rem;
    font-weight: 700;
}

.nav-actions {
    display: flex;
    gap: 1rem;
    align-items: center;
}

.nav-filter-btn {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    background: transparent;
    border: 1px solid var(--color-border);
    border-radius: var(--radius-sm);
    color: var(--color-text-secondary);
    font-size: 0.875rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease;
}

.nav-filter-btn:hover {
    border-color: var(--color-primary);
    color: var(--color-primary);
}

.nav-view-toggle {
    display: flex;
    gap: 0.5rem;
    background: var(--color-surface-light);
    padding: 0.25rem;
    border-radius: var(--radius-sm);
}

.view-btn {
    width: 2rem;
    height: 2rem;
    display: flex;
    align-items: center;
    justify-content: center;
    background: transparent;
    border: none;
    border-radius: var(--radius-sm);
    color: var(--color-text-secondary);
    cursor: pointer;
    transition: all 0.2s ease;
}

.view-btn:hover {
    background: var(--color-surface);
    color: var(--color-text);
}

.view-btn.active {
    background: var(--color-surface);
    color: var(--color-primary);
}

/* Category Tabs */
.category-tabs {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
}

.category-tab {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1.25rem;
    background: transparent;
    border: 1px solid var(--color-border);
    border-radius: var(--radius-xl);
    color: var(--color-text-secondary);
    font-size: 0.875rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease;
}

.category-tab:hover {
    border-color: var(--color-primary);
    color: var(--color-text);
}

.category-tab.active {
    background: var(--color-primary);
    border-color: var(--color-primary);
    color: white;
}

.category-count {
    background: rgba(255, 255, 255, 0.1);
    padding: 0.125rem 0.5rem;
    border-radius: 10px;
    font-size: 0.75rem;
}

/* Articles Grid */
.blog-grid-container {
    max-width: 1200px;
    margin: 0 auto;
}

.blog-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 2rem;
    margin-bottom: 3rem;
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
    border-radius: var(--radius-lg);
    overflow: hidden;
    border: 1px solid var(--color-border);
    transition: all 0.3s ease;
    cursor: pointer;
}

.article-card:hover {
    transform: translateY(-4px);
    border-color: var(--color-primary);
    box-shadow: var(--shadow-lg);
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
    border-radius: var(--radius-xl);
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
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
    color: var(--color-text);
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
    color: var(--color-text);
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
    border-radius: var(--radius-xl);
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
    box-shadow: var(--shadow-md);
}

.load-more-btn:active {
    transform: translateY(0);
}

.load-more-text {
    color: var(--color-text-secondary);
    font-size: 0.875rem;
}

/* Featured Article Specific */
.article-card.featured .article-card__image {
    aspect-ratio: 16/9;
}

.article-card.featured .article-title {
    font-size: 1.5rem;
}

/* Mobile Responsive */
@media (max-width: 768px) {
    .blog-section {
        padding: 1.5rem 1rem;
    }
    
    .blog-hero {
        padding: 2rem 0;
        margin-bottom: 2rem;
    }
    
    .nav-header {
        flex-direction: column;
        align-items: flex-start;
        gap: 1rem;
    }
    
    .nav-actions {
        width: 100%;
        justify-content: space-between;
    }
    
    .category-tabs {
        overflow-x: auto;
        padding-bottom: 0.5rem;
        -webkit-overflow-scrolling: touch;
    }
    
    .category-tab {
        flex-shrink: 0;
    }
}
</style>