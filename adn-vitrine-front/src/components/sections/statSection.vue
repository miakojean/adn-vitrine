<template>
    <section class="stat-section" ref="statsSection">
        <div class="stats-background">
            <div class="particle" v-for="(particle, index) in particles" :key="index" :style="particle.style"></div>
        </div>
        
        <div class="stats-container">
            <!-- Titre avec effet de révélation -->
            <div class="section-header">
                <h2 class="section-title">
                    <span class="title-line">Des chiffres qui</span>
                    <span class="title-line highlight">parlent d'eux-mêmes</span>
                </h2>
                <p class="section-subtitle">
                    Plus de 9 ans d'excellence et d'engagement à vos côtés
                </p>
            </div>

            <!-- Conteneur des statistiques -->
            <div class="stats-grid">
                <div 
                    v-for="(stat, index) in stats" 
                    :key="index"
                    :class="['stat-item', { 'animated': stat.animated }]"
                >
                    <!-- Valeur animée principale -->
                    <div class="stat-number">
                        <span>{{ stat.displayValue.toLocaleString() }}</span>
                        <span class="plus" v-if="stat.hasPlus">+</span>
                    </div>
                    
                    <!-- Contenu texte -->
                    <div class="stat-content">
                        <h3 class="stat-title">{{ stat.title }}</h3>
                        <p class="stat-description">{{ stat.description }}</p>
                        
                        <!-- Tag additionnel -->
                        <span class="stat-tag" v-if="stat.tag">
                            {{ stat.tag }}
                        </span>
                    </div>
                </div>
            </div>
            
            <!-- CTA supplémentaire -->
            <div class="stats-cta" v-if="showStats">
                <moreButton @click="handleCtaClick" label="Découvrir nos services"/>
            </div>

        </div>
    </section>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, reactive} from 'vue';
import moreButton from '../button/moreButton.vue';
import { useRouter } from 'vue-router';

// Animation des nombres
interface AnimatedStat {
    value: number;
    hasPlus: boolean;
    title: string;
    description: string;
    tag: string;
    animated: boolean;
    displayValue: number;
}

const easeOutCubic = (t: number) => 1 - Math.pow(1 - t, 3);

const router = useRouter();

// Données des statistiques
const stats = reactive<AnimatedStat[]>([
    {
        value: 1000,
        hasPlus: true,
        title: "Entreprises Accompagnées",
        description: "Partenariats solides à travers le monde",
        tag: "En croissance",
        animated: false,
        displayValue: 0
    },
    {
        value: 1700,
        hasPlus: true,
        title: "Documents Rédigés",
        description: "Solutions juridiques sur mesure",
        tag: "Professionnalisme",
        animated: false,
        displayValue: 0
    },
    {
        value: 9,
        hasPlus: false,
        title: "Années d'Expérience",
        description: "Expertise accumulée depuis 2014",
        tag: "Expertise reconnue",
        animated: false,
        displayValue: 0
    }
]);

// Animer un nombre individuellement
const animateNumber = (stat: AnimatedStat, delay: number) => {
    const duration = 2000;
    let startTime = 0;
    // On supprime la déclaration de animationFrame ici

    const animate = (timestamp: number) => {
        if (!startTime) startTime = timestamp;
        const elapsed = timestamp - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        const easedProgress = easeOutCubic(progress);
        stat.displayValue = Math.floor(easedProgress * stat.value);
        
        if (progress < 1) {
            // On appelle la fonction sans stocker le résultat
            requestAnimationFrame(animate);
        } else {
            stat.displayValue = stat.value;
        }
    };

    setTimeout(() => {
        requestAnimationFrame(animate);
    }, delay);
};

// États
const statsSection = ref<HTMLElement | null>(null);
const showStats = ref(false);
const particles = ref<Array<{ style: Record<string, string> }>>([]);
let observerInstance: IntersectionObserver | null = null;

// CTA
const handleCtaClick = () => {
    router.push('/about');
};

// Créer des particules animées
const createParticles = () => {
    const particleCount = 15;
    particles.value = [];
    
    for (let i = 0; i < particleCount; i++) {
        particles.value.push({
            style: {
                left: `${Math.random() * 100}%`,
                top: `${Math.random() * 100}%`,
                width: `${Math.random() * 4 + 2}px`,
                height: `${Math.random() * 4 + 2}px`,
                animationDelay: `${Math.random() * 2}s`,
                opacity: `${Math.random() * 0.3 + 0.1}`
            }
        });
    }
};

onMounted(() => {
    // Observer pour déclencher les animations
    observerInstance = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                showStats.value = true;
                stats.forEach((stat, index) => {
                    setTimeout(() => {
                        stat.animated = true;
                        animateNumber(stat, index * 200);
                    }, index * 100);
                });
                createParticles();
            }
        });
    }, {
        threshold: 0.3,
        rootMargin: '50px'
    });
    
    if (statsSection.value) {
        observerInstance.observe(statsSection.value);
    }
});

onUnmounted(() => {
    if (statsSection.value && observerInstance) {
        observerInstance.unobserve(statsSection.value);
    }
});
</script>

<style scoped>
/* Reset et base */
.stat-section {
    width: 100%;
    min-height: 100vh;
    padding: 4rem 1rem;
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
}

/* Background avec particules */
.stats-background {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 0;
}

.particle {
    position: absolute;
    background: linear-gradient(90deg, #3b82f6, #8b5cf6);
    border-radius: 50%;
    animation: float 6s infinite ease-in-out;
    filter: blur(1px);
}

@keyframes float {
    0%, 100% { transform: translateY(0) rotate(0deg); }
    50% { transform: translateY(-20px) rotate(180deg); }
}

/* Conteneur principal */
.stats-container {
    max-width: 1280px;
    margin: 0 auto;
    position: relative;
    z-index: 1;
}

/* En-tête de section */
.section-header {
    text-align: center;
    margin-bottom: 4rem;
    opacity: 0;
    transform: translateY(30px);
    animation: fadeInUp 0.8s 0.3s forwards;
}

.title-line {
    display: block;
    font-size: 2.5rem;
    font-weight: 800;
    color: #f8fafc;
    line-height: 1.2;
}

.title-line.highlight {
    background: linear-gradient(90deg, #3b82f6, #8b5cf6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.section-subtitle {
    font-size: 1.125rem;
    color: #94a3b8;
    margin-top: 1rem;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

/* Grille des statistiques */
.stats-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 3rem;
    margin-bottom: 4rem;
}

@media (min-width: 768px) {
    .stats-grid {
        grid-template-columns: repeat(3, 1fr);
        gap: 2rem;
    }
    
    .title-line {
        font-size: 3rem;
    }
}

/* Item de statistique */
.stat-item {
    background: rgba(30, 41, 59, 0.7);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 24px;
    padding: 3rem 2rem;
    position: relative;
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    opacity: 0;
    transform: translateY(50px);
    text-align: center;
}

.stat-item.animated {
    animation: slideUp 0.6s forwards;
}

.stat-item:hover {
    transform: translateY(-10px);
    border-color: rgba(59, 130, 246, 0.5);
    box-shadow: 
        0 20px 40px rgba(0, 0, 0, 0.3),
        0 0 0 1px rgba(59, 130, 246, 0.1),
        inset 0 0 50px rgba(59, 130, 246, 0.05);
}

.stat-item:nth-child(1).animated { animation-delay: 0s; }
.stat-item:nth-child(2).animated { animation-delay: 0.2s; }
.stat-item:nth-child(3).animated { animation-delay: 0.4s; }

@keyframes slideUp {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Valeur numérique */
.stat-number {
    font-size: 5rem;
    font-weight: 900;
    background: var(--primary-blue);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1.5rem;
    line-height: 1;
    letter-spacing: -0.02em;
}

.stat-number .plus {
    font-size: 3.5rem;
    margin-left: 4px;
    vertical-align: super;
}

/* Contenu texte */
.stat-content {
    text-align: center;
}

.stat-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 0.75rem;
}

.stat-description {
    font-size: 1rem;
    color: #94a3b8;
    margin-bottom: 1.5rem;
    line-height: 1.6;
}

/* Tag */
.stat-tag {
    display: inline-block;
    padding: 0.5rem 1rem;
    background: rgba(59, 130, 246, 0.1);
    color: #3b82f6;
    font-size: 0.875rem;
    font-weight: 600;
    border-radius: 12px;
    border: 1px solid rgba(59, 130, 246, 0.2);
}

/* CTA */
.stats-cta {
    text-align: center;
    opacity: 0;
    animation: fadeIn 0.8s 1.2s forwards;
}

/* Animations globales */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

/* Responsive adjustments */
@media (max-width: 767px) {
    .stat-section {
        padding: 3rem 1rem;
    }
    
    .title-line {
        font-size: 2rem;
    }
    
    .stat-number {
        font-size: 3.5rem;
    }
    
    .stat-number .plus {
        font-size: 2.5rem;
    }
    
    .stat-title {
        font-size: 1.25rem;
    }
}

/* Dark mode optimizations */
@media (prefers-color-scheme: dark) {
    .stat-item {
        background: rgba(15, 23, 42, 0.8);
    }
}

/* Reduced motion */
@media (prefers-reduced-motion: reduce) {
    .stat-item,
    .cta-button,
    .particle {
        animation: none !important;
        transition: none !important;
    }
}
</style>