<template>
    <section class="services-section" id="services">
        <!-- Background Elements -->
        <div class="background-elements" aria-hidden="true">
            <div class="glow glow-1"></div>
            <div class="glow glow-2"></div>
            <div class="particles"></div>
        </div>

        <div class="container">
            <!-- Section Header -->
            <div class="section-header">
                <div class="header-content">
                    <span class="badge">SERVICES PREMIUM</span>
                    <h1 class="title">
                        Solutions Digitales 
                        <span class="highlight">Sur Mesure</span>
                    </h1>
                    <p class="subtitle">
                        Nous transformons vos idées en expériences digitales exceptionnelles.
                        Découvrez notre expertise à travers une gamme complète de services.
                    </p>
                    
                    <!-- Stats -->
                    <div class="header-stats">
                        <div class="stat" v-for="stat in headerStats" :key="stat.id">
                            <span class="stat-value">{{ stat.value }}</span>
                            <span class="stat-label">{{ stat.label }}</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Services Grid -->
            <div class="services-grid">
                <div 
                    v-for="(service, index) in services" 
                    :key="service.id"
                    class="service-card"
                    :class="{
                        'featured': service.featured,
                        'hovered': hoveredCard === index
                    }"
                    @mouseenter="hoveredCard = index"
                    @mouseleave="hoveredCard = null"
                    @click="openServiceDetails(service)"
                >
                    <!-- Card Glow Effect -->
                    <div class="card-glow" :style="{ background: service.gradient }"></div>
                    
                    <!-- Service Icon & Number -->
                    <div class="service-header">
                        <div class="service-icon">
                            <div class="icon-wrapper" :style="{ color: service.color }">
                                <span class="icon" v-html="service.icon"></span>
                            </div>
                            <span class="service-number">0{{ index + 1 }}</span>
                        </div>
                    </div>

                    <!-- Service Content -->
                    <div class="service-content">
                        <div class="service-title-container">
                            <h3 class="service-title">{{ service.title }}</h3>
                            <span class="service-category">{{ service.category }}</span>
                        </div>
                        
                        <p class="service-description">{{ service.description }}</p>
                        
                        <!-- Service Features -->
                        <ul class="service-features">
                            <li v-for="feature in service.features.slice(0, 3)" :key="feature">
                                <span class="feature-dot"></span>
                                <span>{{ feature }}</span>
                            </li>
                        </ul>

                        <!-- CTA Button -->
                        <div class="service-cta">
                            <button 
                                class="cta-button"
                                @click.stop="openServiceDetails(service)"
                            >
                                <span>Explorer</span>
                                <svg class="arrow-icon" width="16" height="16" viewBox="0 0 24 24" fill="none">
                                    <path d="M5 12H19M19 12L12 5M19 12L12 19" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                            </button>
                            <span class="duration">{{ service.duration }}</span>
                        </div>
                    </div>

                    <!-- Hover Indicator -->
                    <div class="hover-indicator"></div>
                </div>
            </div>

            <!-- View All CTA -->
            <div class="view-all-container">
                <button class="view-all-button" @click="scrollToContact">
                    <span>Voir tous nos services</span>
                    <div class="arrow-circle">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                            <path d="M5 12H19M19 12L12 5M19 12L12 19" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                    </div>
                </button>
            </div>

            <!-- Testimonial -->
            <div class="testimonial-section">
                <div class="testimonial-card">
                    <div class="quote-icon">"</div>
                    <blockquote class="testimonial-text">
                        Leur approche méthodique et leur expertise technique ont transformé notre présence digitale. 
                        Chaque service est exécuté avec une précision remarquable.
                    </blockquote>
                    <div class="testimonial-author">
                        <div class="author-avatar">SM</div>
                        <div class="author-info">
                            <span class="author-name">Sarah Martin</span>
                            <span class="author-role">Directrice Marketing, TechCorp</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Service Details Modal -->
        <div 
            v-if="selectedService" 
            class="service-modal-overlay"
            @click.self="closeModal"
            :class="{ 'active': showModal }"
        >
            <div class="service-modal">
                <button class="modal-close" @click="closeModal">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                        <path d="M18 6L6 18M6 6L18 18" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </button>

                <div class="modal-content">
                    <div class="modal-header">
                        <div class="service-tag" :style="{ background: selectedService.color + '20', color: selectedService.color }">
                            {{ selectedService.category }}
                        </div>
                        <h2 class="modal-title">{{ selectedService.title }}</h2>
                        <p class="modal-subtitle">{{ selectedService.fullDescription }}</p>
                    </div>

                    <div class="modal-body">
                        <!-- Process Steps -->
                        <div class="process-section" v-if="selectedService.process">
                            <h3>Notre Processus</h3>
                            <div class="process-steps">
                                <div 
                                    v-for="(step, index) in selectedService.process" 
                                    :key="index"
                                    class="process-step"
                                >
                                    <div class="step-number">{{ index + 1 }}</div>
                                    <div class="step-content">
                                        <h4>{{ step.title }}</h4>
                                        <p>{{ step.description }}</p>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Key Benefits -->
                        <div class="benefits-section">
                            <h3>Avantages Clés</h3>
                            <div class="benefits-grid">
                                <div 
                                    v-for="benefit in selectedService.benefits" 
                                    :key="benefit"
                                    class="benefit-card"
                                >
                                    <div class="benefit-icon">✓</div>
                                    <span>{{ benefit }}</span>
                                </div>
                            </div>
                        </div>

                        <!-- Technologies -->
                        <div class="tech-section" v-if="selectedService.technologies">
                            <h3>Technologies Utilisées</h3>
                            <div class="tech-tags">
                                <span 
                                    v-for="tech in selectedService.technologies" 
                                    :key="tech"
                                    class="tech-tag"
                                >
                                    {{ tech }}
                                </span>
                            </div>
                        </div>

                        <!-- CTA -->
                        <div class="modal-cta">
                            <button class="primary-cta" @click="contactAboutService">
                                <span>Discuter de ce projet</span>
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                                    <path d="M5 12H19M19 12L12 5M19 12L12 19" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                            </button>
                            <button class="secondary-cta" @click="closeModal">
                                Voir d'autres services
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';

// --- Refs ---
const hoveredCard = ref<number | null>(null);
const selectedService = ref<any>(null);
const showModal = ref(false);

// --- Data ---
const headerStats = [
    { id: 1, value: '98%', label: 'Satisfaction Client' },
    { id: 2, value: '150+', label: 'Projets Livrés' },
    { id: 3, value: '24/7', label: 'Support' },
    { id: 4, value: '3x', label: 'ROI Moyen' }
];

const services = [
    {
        id: 1,
        title: 'Développement Web Avancé',
        description: 'Applications web performantes et évolutives construites avec les technologies modernes.',
        fullDescription: 'Nous créons des applications web sur mesure qui répondent à vos besoins spécifiques tout en offrant une expérience utilisateur exceptionnelle.',
        category: 'Développement',
        icon: '⚡',
        color: '#3b82f6',
        gradient: 'linear-gradient(135deg, #3b82f620, #1e40af20)',
        features: [
            'Applications React/Vue.js',
            'API RESTful & GraphQL',
            'Bases de données NoSQL/SQL',
            'Architecture microservices',
            'Tests automatisés'
        ],
        process: [
            { title: 'Analyse des besoins', description: 'Compréhension approfondie de vos objectifs' },
            { title: 'Conception UX/UI', description: 'Design centré sur l\'utilisateur' },
            { title: 'Développement agile', description: 'Itérations rapides et feedback continu' },
            { title: 'Tests & Optimisation', description: 'Assurance qualité et performance' }
        ],
        benefits: [
            'Temps de chargement optimisé',
            'Expérience utilisateur fluide',
            'Code maintenable et scalable',
            'Sécurité renforcée',
            'SEO intégré'
        ],
        technologies: ['React', 'Vue.js', 'Node.js', 'TypeScript', 'MongoDB'],
        duration: '4-8 semaines',
        featured: true
    },
    {
        id: 2,
        title: 'Design UI/UX Créatif',
        description: 'Interfaces intuitives et expériences utilisateur mémorables qui engagent votre audience.',
        fullDescription: 'Notre équipe de designers crée des interfaces qui allient esthétique et fonctionnalité pour des expériences digitales captivantes.',
        category: 'Design',
        icon: '🎨',
        color: '#8b5cf6',
        gradient: 'linear-gradient(135deg, #8b5cf620, #7c3aed20)',
        features: [
            'Recherche utilisateur',
            'Wireframes interactifs',
            'Design systems',
            'Prototypage avancé',
            'Tests utilisateurs'
        ],
        benefits: [
            'Conversion améliorée',
            'Navigation intuitive',
            'Identité visuelle forte',
            'Accessibilité optimale',
            'Design responsive'
        ],
        technologies: ['Figma', 'Sketch', 'Adobe XD', 'Principle'],
        duration: '2-4 semaines',
        featured: false
    },
    {
        id: 3,
        title: 'Stratégie Marketing Digital',
        description: 'Campagnes ciblées et stratégies data-driven pour maximiser votre visibilité en ligne.',
        fullDescription: 'Nous élaborons des stratégies marketing digitales qui génèrent des leads qualifiés et augmentent votre ROI.',
        category: 'Marketing',
        icon: '📈',
        color: '#10b981',
        gradient: 'linear-gradient(135deg, #10b98120, #05966920)',
        features: [
            'Analyse de marché',
            'Stratégie SEO/SEA',
            'Marketing automation',
            'Analytics avancés',
            'Content marketing'
        ],
        benefits: [
            'Visibilité accrue',
            'Lead generation',
            'ROI mesurable',
            'Marque renforcée',
            'Audience engagée'
        ],
        technologies: ['Google Analytics', 'HubSpot', 'SEMrush', 'Mailchimp'],
        duration: 'En continu',
        featured: true
    }
];

// --- Methods ---
const openServiceDetails = (service: any) => {
    selectedService.value = service;
    showModal.value = true;
    document.body.style.overflow = 'hidden';
};

const closeModal = () => {
    showModal.value = false;
    setTimeout(() => {
        selectedService.value = null;
        document.body.style.overflow = '';
    }, 300);
};

const contactAboutService = () => {
    closeModal();
    const contactSection = document.getElementById('contact');
    if (contactSection) {
        contactSection.scrollIntoView({ behavior: 'smooth' });
    }
};

const scrollToContact = () => {
    const contactSection = document.getElementById('contact');
    if (contactSection) {
        contactSection.scrollIntoView({ behavior: 'smooth' });
    }
};

// --- Lifecycle ---
onMounted(() => {
    // Animation des cartes au scroll
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.classList.add('animate-in');
                }, index * 100);
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.service-card').forEach(card => {
        observer.observe(card);
    });
});
</script>

<style scoped>
/* === VARIABLES === */
:root {
    --primary-blue: #3b82f6;
    --primary-blue-dark: #1e40af;
    --accent-purple: #8b5cf6;
    --accent-purple-dark: #7c3aed;
    --success-green: #10b981;
    --success-green-dark: #059669;
    --bg-dark: #0f172a;
    --bg-darker: #0a0f1e;
    --bg-card: rgba(30, 41, 59, 0.4);
    --text-primary: #f8fafc;
    --text-secondary: #cbd5e1;
    --text-muted: #94a3b8;
    --border-color: rgba(255, 255, 255, 0.1);
    --border-light: rgba(255, 255, 255, 0.05);
    --shadow-lg: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
    --shadow-md: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
    --radius-lg: 24px;
    --radius-md: 16px;
    --radius-sm: 12px;
    --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* === BASE STYLES === */
.services-section {
    position: relative;
    padding: 8rem 1rem;
    background: linear-gradient(135deg, var(--bg-darker) 0%, var(--bg-dark) 100%);
    overflow: hidden;
    color: var(--text-primary);
    min-height: 100vh;
    display: flex;
    align-items: center;
}

.container {
    max-width: 1280px;
    margin: 0 auto;
    width: 100%;
    position: relative;
    z-index: 2;
}

/* === BACKGROUND ELEMENTS === */
.background-elements {
    position: absolute;
    inset: 0;
    pointer-events: none;
    z-index: 1;
}

.glow {
    position: absolute;
    border-radius: 50%;
    filter: blur(80px);
    opacity: 0.15;
    animation: float 20s ease-in-out infinite;
}

.glow-1 {
    width: 400px;
    height: 400px;
    background: var(--primary-blue);
    top: -100px;
    left: 20%;
    animation-delay: 0s;
}

.glow-2 {
    width: 300px;
    height: 300px;
    background: var(--accent-purple);
    bottom: -50px;
    right: 10%;
    animation-delay: 10s;
}

.particles {
    position: absolute;
    inset: 0;
    background-image: 
        radial-gradient(circle at 1px 1px, rgba(255, 255, 255, 0.03) 1px, transparent 0);
    background-size: 40px 40px;
}

@keyframes float {
    0%, 100% { transform: translate(0, 0) scale(1); }
    33% { transform: translate(30px, -20px) scale(1.05); }
    66% { transform: translate(-20px, 15px) scale(0.95); }
}

/* === HEADER SECTION === */
.section-header {
    text-align: center;
    margin-bottom: 6rem;
    animation: fadeInUp 0.8s ease-out;
}

.header-content {
    max-width: 800px;
    margin: 0 auto;
}

.badge {
    display: inline-block;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 2px;
    color: var(--primary-blue);
    margin-bottom: 2rem;
    text-transform: uppercase;
    background: rgba(59, 130, 246, 0.1);
    padding: 8px 20px;
    border-radius: 25px;
    border: 1px solid rgba(59, 130, 246, 0.2);
    backdrop-filter: blur(4px);
}

.title {
    font-size: clamp(2.5rem, 5vw, 4rem);
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 1.5rem;
    background: linear-gradient(135deg, var(--text-primary) 0%, var(--text-secondary) 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}

.highlight {
    background: linear-gradient(135deg, var(--primary-blue), var(--accent-purple));
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    position: relative;
}

.highlight::after {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 0;
    width: 100%;
    height: 3px;
    background: linear-gradient(90deg, var(--primary-blue), var(--accent-purple));
    border-radius: 2px;
}

.subtitle {
    font-size: 1.25rem;
    color: var(--text-secondary);
    line-height: 1.6;
    margin-bottom: 3rem;
    opacity: 0.9;
}

/* === HEADER STATS === */
.header-stats {
    display: flex;
    justify-content: center;
    gap: 3rem;
    flex-wrap: wrap;
    margin-top: 3rem;
}

.stat {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 1.5rem;
    min-width: 120px;
}

.stat-value {
    font-size: 2.5rem;
    font-weight: 800;
    color: var(--text-primary);
    margin-bottom: 0.5rem;
    background: linear-gradient(135deg, var(--primary-blue), var(--accent-purple));
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}

.stat-label {
    font-size: 0.875rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: 500;
}

/* === SERVICES GRID === */
.services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    margin-bottom: 4rem;
}

.service-card {
    position: relative;
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    padding: 2.5rem;
    backdrop-filter: blur(10px);
    transition: var(--transition);
    cursor: pointer;
    opacity: 0;
    transform: translateY(30px);
    overflow: hidden;
}

.service-card.animate-in {
    opacity: 1;
    transform: translateY(0);
    animation: cardAppear 0.6s ease-out forwards;
}

@keyframes cardAppear {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.service-card:hover {
    transform: translateY(-10px);
    border-color: var(--primary-blue);
    box-shadow: var(--shadow-lg);
}

.service-card.featured {
    border-color: var(--primary-blue);
    background: linear-gradient(
        135deg,
        rgba(59, 130, 246, 0.1),
        var(--bg-card)
    );
}

.service-card.hovered .card-glow {
    opacity: 1;
}

/* Card Glow Effect */
.card-glow {
    position: absolute;
    inset: 0;
    opacity: 0;
    transition: opacity 0.4s;
    z-index: 0;
    border-radius: var(--radius-lg);
}

/* Service Header */
.service-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
}

.service-icon {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.icon-wrapper {
    width: 56px;
    height: 56px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(255, 255, 255, 0.05);
    border-radius: var(--radius-md);
    font-size: 1.5rem;
    transition: var(--transition);
}

.service-card:hover .icon-wrapper {
    transform: scale(1.1) rotate(5deg);
    background: rgba(255, 255, 255, 0.1);
}

.service-number {
    font-size: 0.875rem;
    font-weight: 700;
    color: var(--text-muted);
    opacity: 0.7;
}

/* Service Content */
.service-title-container {
    margin-bottom: 1.5rem;
}

.service-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 0.5rem;
    line-height: 1.3;
}

.service-category {
    font-size: 0.875rem;
    color: var(--primary-blue);
    background: rgba(59, 130, 246, 0.1);
    padding: 4px 12px;
    border-radius: 20px;
    display: inline-block;
}

.service-description {
    color: var(--text-secondary);
    line-height: 1.6;
    margin-bottom: 1.5rem;
    font-size: 1rem;
}

/* Service Features */
.service-features {
    list-style: none;
    padding: 0;
    margin: 1.5rem 0;
}

.service-features li {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 0.75rem;
    color: var(--text-secondary);
    font-size: 0.9rem;
}

.feature-dot {
    width: 6px;
    height: 6px;
    background: var(--primary-blue);
    border-radius: 50%;
    flex-shrink: 0;
}

/* Service CTA */
.service-cta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 2rem;
    padding-top: 1.5rem;
    border-top: 1px solid var(--border-light);
}

.cta-button {
    display: flex;
    align-items: center;
    gap: 8px;
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid var(--border-color);
    color: var(--text-primary);
    padding: 10px 20px;
    border-radius: var(--radius-md);
    font-weight: 500;
    cursor: pointer;
    transition: var(--transition);
}

.cta-button:hover {
    background: var(--primary-blue);
    border-color: var(--primary-blue);
    transform: translateX(5px);
}

.arrow-icon {
    transition: transform 0.3s;
}

.cta-button:hover .arrow-icon {
    transform: translateX(3px);
}

.duration {
    font-size: 0.875rem;
    color: var(--text-muted);
}

/* Hover Indicator */
.hover-indicator {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 3px;
    background: linear-gradient(90deg, var(--primary-blue), var(--accent-purple));
    transform: scaleX(0);
    transition: transform 0.3s;
    border-radius: 0 0 var(--radius-lg) var(--radius-lg);
}

.service-card:hover .hover-indicator {
    transform: scaleX(1);
}

/* === VIEW ALL CTA === */
.view-all-container {
    text-align: center;
    margin: 4rem 0;
}

.view-all-button {
    display: inline-flex;
    align-items: center;
    gap: 1rem;
    background: none;
    border: 1px solid var(--border-color);
    color: var(--text-primary);
    padding: 1rem 2rem;
    border-radius: var(--radius-md);
    font-size: 1rem;
    font-weight: 500;
    cursor: pointer;
    transition: var(--transition);
}

.view-all-button:hover {
    background: rgba(255, 255, 255, 0.05);
    border-color: var(--primary-blue);
    transform: translateY(-2px);
    gap: 1.5rem;
}

.arrow-circle {
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--primary-blue);
    border-radius: 50%;
    transition: var(--transition);
}

.view-all-button:hover .arrow-circle {
    transform: rotate(45deg);
    background: var(--accent-purple);
}

/* === TESTIMONIAL SECTION === */
.testimonial-section {
    margin-top: 6rem;
    animation: fadeInUp 0.8s ease-out 0.2s both;
}

.testimonial-card {
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(139, 92, 246, 0.1));
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    padding: 3rem;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.quote-icon {
    font-size: 4rem;
    color: var(--primary-blue);
    opacity: 0.3;
    margin-bottom: 1.5rem;
}

.testimonial-text {
    font-size: 1.25rem;
    font-style: italic;
    color: var(--text-primary);
    line-height: 1.6;
    margin-bottom: 2rem;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

.testimonial-author {
    display: inline-flex;
    align-items: center;
    gap: 1rem;
    padding: 1rem 2rem;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 50px;
    border: 1px solid var(--border-color);
}

.author-avatar {
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--primary-blue);
    color: white;
    border-radius: 50%;
    font-weight: 600;
    font-size: 1rem;
}

.author-info {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.author-name {
    font-weight: 600;
    color: var(--text-primary);
}

.author-role {
    font-size: 0.875rem;
    color: var(--text-muted);
}

/* === MODAL === */
.service-modal-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.8);
    backdrop-filter: blur(10px);
    z-index: 1000;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 1rem;
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.3s, visibility 0.3s;
}

.service-modal-overlay.active {
    opacity: 1;
    visibility: visible;
}

.service-modal {
    background: var(--bg-dark);
    border-radius: var(--radius-lg);
    padding: 3rem;
    max-width: 800px;
    width: 100%;
    max-height: 90vh;
    overflow-y: auto;
    position: relative;
    border: 1px solid var(--border-color);
    box-shadow: var(--shadow-lg);
    transform: translateY(20px) scale(0.95);
    transition: transform 0.3s;
}

.service-modal-overlay.active .service-modal {
    transform: translateY(0) scale(1);
}

.modal-close {
    position: absolute;
    top: 1.5rem;
    right: 1.5rem;
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid var(--border-color);
    border-radius: 50%;
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: var(--transition);
    color: var(--text-primary);
    z-index: 10;
}

.modal-close:hover {
    background: rgba(255, 255, 255, 0.2);
    transform: rotate(90deg);
}

.modal-header {
    margin-bottom: 3rem;
}

.service-tag {
    display: inline-block;
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 0.875rem;
    font-weight: 500;
    margin-bottom: 1rem;
}

.modal-title {
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 1rem;
    line-height: 1.2;
}

.modal-subtitle {
    color: var(--text-secondary);
    line-height: 1.6;
    font-size: 1.125rem;
}

.modal-body {
    margin-bottom: 2rem;
}

/* Process Steps */
.process-section {
    margin-bottom: 3rem;
}

.process-section h3 {
    font-size: 1.5rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 2rem;
}

.process-steps {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.process-step {
    display: flex;
    gap: 1.5rem;
    align-items: flex-start;
    padding: 1.5rem;
    background: rgba(255, 255, 255, 0.05);
    border-radius: var(--radius-md);
    border: 1px solid var(--border-light);
}

.step-number {
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--primary-blue);
    color: white;
    border-radius: 50%;
    font-weight: 600;
    flex-shrink: 0;
}

.step-content h4 {
    font-size: 1.125rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 0.5rem;
}

.step-content p {
    color: var(--text-secondary);
    line-height: 1.6;
}

/* Benefits */
.benefits-section {
    margin-bottom: 3rem;
}

.benefits-section h3 {
    font-size: 1.5rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 1.5rem;
}

.benefits-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
}

.benefit-card {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 1rem;
    background: rgba(255, 255, 255, 0.05);
    border-radius: var(--radius-sm);
    border: 1px solid var(--border-light);
}

.benefit-icon {
    color: var(--success-green);
    font-weight: bold;
    font-size: 1.125rem;
}

/* Technologies */
.tech-section {
    margin-bottom: 3rem;
}

.tech-section h3 {
    font-size: 1.5rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 1.5rem;
}

.tech-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
}

.tech-tag {
    padding: 6px 16px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--border-color);
    border-radius: 20px;
    font-size: 0.875rem;
    color: var(--text-secondary);
}

/* Modal CTA */
.modal-cta {
    display: flex;
    gap: 1rem;
    padding-top: 2rem;
    border-top: 1px solid var(--border-color);
}

.primary-cta {
    flex: 2;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.75rem;
    background: var(--primary-blue);
    color: white;
    border: none;
    padding: 1rem 2rem;
    border-radius: var(--radius-md);
    font-weight: 600;
    cursor: pointer;
    transition: var(--transition);
}

.primary-cta:hover {
    background: var(--primary-blue-dark);
    transform: translateY(-2px);
}

.secondary-cta {
    flex: 1;
    background: rgba(255, 255, 255, 0.1);
    color: var(--text-primary);
    border: 1px solid var(--border-color);
    padding: 1rem 2rem;
    border-radius: var(--radius-md);
    font-weight: 500;
    cursor: pointer;
    transition: var(--transition);
}

.secondary-cta:hover {
    background: rgba(255, 255, 255, 0.15);
}

/* === ANIMATIONS === */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* === RESPONSIVE === */
@media (max-width: 1024px) {
    .services-grid {
        grid-template-columns: repeat(2, 1fr);
    }
    
    .header-stats {
        gap: 2rem;
    }
}

@media (max-width: 768px) {
    .services-section {
        padding: 4rem 1rem;
    }
    
    .services-grid {
        grid-template-columns: 1fr;
        gap: 1.5rem;
    }
    
    .service-card {
        padding: 2rem;
    }
    
    .title {
        font-size: 2rem;
    }
    
    .header-stats {
        gap: 1.5rem;
    }
    
    .stat {
        min-width: 100px;
        padding: 1rem;
    }
    
    .stat-value {
        font-size: 2rem;
    }
    
    .testimonial-card {
        padding: 2rem;
    }
    
    .modal-cta {
        flex-direction: column;
    }
}

@media (max-width: 480px) {
    .service-header {
        flex-direction: column;
        align-items: flex-start;
        gap: 1rem;
    }
    
    .service-cta {
        flex-direction: column;
        gap: 1rem;
        align-items: flex-start;
    }
    
    .header-stats {
        gap: 1rem;
    }
    
    .service-modal {
        padding: 2rem 1.5rem;
    }
}

/* === REDUCED MOTION === */
@media (prefers-reduced-motion: reduce) {
    .service-card,
    .cta-button,
    .view-all-button,
    .modal-close,
    .primary-cta,
    .secondary-cta,
    .glow {
        transition: none;
        animation: none;
    }
    
    .service-card {
        opacity: 1;
        transform: none;
    }
}
</style>