<template>
    <section class="team-section" ref="teamSection">
        <!-- Background décoratif -->
        <div class="team-background">
            <div class="floating-shape shape-1"></div>
            <div class="floating-shape shape-2"></div>
            <div class="floating-shape shape-3"></div>
            <div class="grid-overlay"></div>
        </div>

        <!-- Conteneur principal -->
        <div class="team-container">
            <!-- En-tête de section -->
            <div class="section-header" :class="{ 'animated': showContent }">
                <span class="section-label">NOTRE ÉQUIPE</span>
                <h2 class="section-title">
                    <span class="title-line">Rencontrez les esprits</span>
                    <span class="title-line highlight">brillants derrière notre succès</span>
                </h2>
                <p class="section-description">
                    Une équipe passionnée et diversifiée, unie par l'innovation et l'excellence.
                    Découvrez les experts qui transforment vos idées en réalité.
                </p>
            </div>

            <!-- Navigation des catégories -->
            <div class="team-categories" :class="{ 'animated': showContent }">
                <button 
                    v-for="category in categories" 
                    :key="category.id"
                    :class="['category-btn', { active: activeCategory === category.id }]"
                    @click="setActiveCategory(category.id)"
                >
                    <span class="category-text">{{ category.name }}</span>
                    <span class="category-count">{{ category.count }}</span>
                </button>
            </div>

            <!-- Grille des membres -->
            <div class="team-grid">
                <transition-group name="stagger-fade">
                    <div 
                        v-for="member in filteredMembers" 
                        :key="member.id"
                        class="team-card"
                        :class="{ 'animated': showContent }"
                        @mouseenter="() => hoverCard(member.id)"
                        @mouseleave="() => resetCard(member.id)"
                        @click="() => openModal(member)"
                    >
                        <!-- Carte principale -->
                        <div class="card-inner">
                            <!-- Photo de profil -->
                            <div class="member-photo">
                                <div class="photo-frame">
                                    <img 
                                        :src="member.photo" 
                                        :alt="member.name"
                                        loading="lazy"
                                        :class="{ 'loaded': imageLoaded[member.id] }"
                                        @load="() => imageLoad(member.id)"
                                    />
                                    <div class="photo-overlay"></div>
                                    <div class="photo-shine"></div>
                                </div>
                                
                                <!-- État en ligne -->
                                <div 
                                    class="online-status" 
                                    :class="{ online: member.online }"
                                ></div>
                            </div>

                            <!-- Informations du membre -->
                            <div class="member-info">
                                <h3 class="member-name">{{ member.name }}</h3>
                                <p class="member-role">{{ member.role }}</p>
                                
                                <!-- Tags de compétences -->
                                <div class="member-tags">
                                    <span 
                                        v-for="tag in member.tags.slice(0, 3)" 
                                        :key="tag"
                                        class="tag"
                                    >
                                        {{ tag }}
                                    </span>
                                    <span 
                                        v-if="member.tags.length > 3" 
                                        class="tag more"
                                    >
                                        +{{ member.tags.length - 3 }}
                                    </span>
                                </div>

                                <!-- Bio courte -->
                                <p class="member-bio">
                                    {{ truncateText(member.bio, 100) }}
                                </p>
                            </div>

                            <!-- Footer de la carte -->
                            <div class="card-footer">
                                <!-- Social links -->
                                <div class="social-links">
                                    <a 
                                        v-for="social in member.social" 
                                        :key="social.platform"
                                        :href="social.url" 
                                        class="social-link"
                                        @click.stop
                                        target="_blank"
                                        rel="noopener noreferrer"
                                        :aria-label="`${member.name} sur ${social.platform}`"
                                    >
                                        <span class="social-icon">{{ social.icon }}</span>
                                    </a>
                                </div>

                                <!-- Bouton d'action -->
                                <button 
                                    class="view-profile-btn"
                                    @click.stop="() => openModal(member)"
                                >
                                    <span>Voir le profil</span>
                                    <svg class="arrow" width="16" height="16" viewBox="0 0 24 24">
                                        <path d="M5 12H19M19 12L12 5M19 12L12 19" 
                                              stroke="currentColor" 
                                              stroke-width="2" 
                                              stroke-linecap="round" 
                                              stroke-linejoin="round"/>
                                    </svg>
                                </button>
                            </div>

                            <!-- Effet de halo -->
                            <div class="card-halo"></div>
                        </div>

                        <!-- Carte arrière (au hover) -->
                        <div class="card-back">
                            <div class="back-content">
                                <h4>Expertise</h4>
                                <ul class="expertise-list">
                                    <li v-for="expertise in member.expertise" :key="expertise">
                                        {{ expertise }}
                                    </li>
                                </ul>
                                <div class="stats">
                                    <div class="stat">
                                        <span class="stat-value">{{ member.projects }}</span>
                                        <span class="stat-label">Projets</span>
                                    </div>
                                    <div class="stat">
                                        <span class="stat-value">{{ member.experience }} ans</span>
                                        <span class="stat-label">Expérience</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </transition-group>
            </div>

            <!-- Bouton CTA -->
            <div class="team-cta" :class="{ 'animated': showContent }">
                <moreButton label="Rejoindre notre équipe" />
            </div>
        </div>

        <!-- Modal de profil -->
        <transition name="modal">
            <div v-if="selectedMember" class="profile-modal" @click.self="closeModal">
                <div class="modal-content">
                    <button class="modal-close" @click="closeModal" aria-label="Fermer">
                        <svg width="24" height="24" viewBox="0 0 24 24">
                            <path d="M18 6L6 18M6 6L18 18" 
                                  stroke="currentColor" 
                                  stroke-width="2" 
                                  stroke-linecap="round"/>
                        </svg>
                    </button>

                    <div class="modal-body">
                        <!-- Photo et infos basiques -->
                        <div class="modal-header">
                            <div class="modal-photo">
                                <img :src="selectedMember.photo" :alt="selectedMember.name" />
                                <div class="modal-status" :class="{ online: selectedMember.online }"></div>
                            </div>
                            <div class="modal-header-info">
                                <h3>{{ selectedMember.name }}</h3>
                                <p class="modal-role">{{ selectedMember.role }}</p>
                                <p class="modal-department">{{ selectedMember.department }}</p>
                            </div>
                        </div>

                        <!-- Informations détaillées -->
                        <div class="modal-details">
                            <div class="detail-section">
                                <h4>Biographie</h4>
                                <p>{{ selectedMember.fullBio }}</p>
                            </div>

                            <div class="detail-section">
                                <h4>Expertises</h4>
                                <div class="expertise-grid">
                                    <div 
                                        v-for="expertise in selectedMember.expertise" 
                                        :key="expertise"
                                        class="expertise-item"
                                    >
                                        <span class="expertise-dot"></span>
                                        <span>{{ expertise }}</span>
                                    </div>
                                </div>
                            </div>

                            <div class="detail-section">
                                <h4>Contact</h4>
                                <div class="contact-info">
                                    <a :href="`mailto:${selectedMember.email}`" class="contact-item">
                                        <span class="contact-icon">✉️</span>
                                        <span>{{ selectedMember.email }}</span>
                                    </a>
                                    <div class="contact-item">
                                        <span class="contact-icon">📱</span>
                                        <span>{{ selectedMember.phone }}</span>
                                    </div>
                                </div>
                            </div>

                            <div class="detail-section">
                                <h4>Statistiques</h4>
                                <div class="stats-grid">
                                    <div class="stat-card">
                                        <span class="stat-number">{{ selectedMember.projects }}</span>
                                        <span class="stat-title">Projets</span>
                                    </div>
                                    <div class="stat-card">
                                        <span class="stat-number">{{ selectedMember.experience }}</span>
                                        <span class="stat-title">Années d'exp</span>
                                    </div>
                                    <div class="stat-card">
                                        <span class="stat-number">{{ selectedMember.clients }}</span>
                                        <span class="stat-title">Clients</span>
                                    </div>
                                    <div class="stat-card">
                                        <span class="stat-number">{{ selectedMember.awards }}</span>
                                        <span class="stat-title">Récompenses</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </transition>
    </section>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted, reactive } from 'vue';
import moreButton from '../button/moreButton.vue';

// Types
interface TeamMember {
    id: number;
    name: string;
    role: string;
    department: string;
    photo: string;
    bio: string;
    fullBio: string;
    tags: string[];
    expertise: string[];
    social: Array<{
        platform: string;
        url: string;
        icon: string;
    }>;
    email: string;
    phone: string;
    projects: number;
    experience: number;
    clients: number;
    awards: number;
    online: boolean;
    category: string[];
}

interface Category {
    id: string;
    name: string;
    icon: string;
    count: number;
}

// Références
const teamSection = ref<HTMLElement | null>(null);
const showContent = ref(false);
const activeCategory = ref('all');
const selectedMember = ref<TeamMember | null>(null);
const imageLoaded = reactive<Record<number, boolean>>({});

// Catégories
const categories: Category[] = [
    { id: 'all', name: 'Toute l\'équipe', icon: '👥', count: 12 },
    { id: 'dev', name: 'Développement', icon: '💻', count: 5 },
    { id: 'design', name: 'Design', icon: '🎨', count: 3 },
    { id: 'marketing', name: 'Marketing', icon: '📈', count: 2 },
    { id: 'management', name: 'Management', icon: '👔', count: 2 }
];

// Données des membres
const teamMembers: TeamMember[] = [
    {
        id: 1,
        name: 'Alexandre Dubois',
        role: 'Lead Développeur Full-Stack',
        department: 'Développement',
        photo: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop',
        bio: 'Expert en architectures cloud et solutions évolutives.',
        fullBio: 'Avec plus de 10 ans d\'expérience dans le développement full-stack, Alexandre excelle dans la création d\'architectures cloud robustes et évolutives. Passionné par les technologies émergentes et les bonnes pratiques de développement.',
        tags: ['React', 'Node.js', 'AWS', 'TypeScript', 'Docker'],
        expertise: ['Architecture Cloud', 'DevOps', 'Microservices', 'CI/CD'],
        social: [
            { platform: 'LinkedIn', url: '#', icon: '💼' },
            { platform: 'GitHub', url: '#', icon: '💻' },
            { platform: 'Twitter', url: '#', icon: '🐦' }
        ],
        email: 'alexandre@entreprise.com',
        phone: '+33 1 23 45 67 89',
        projects: 42,
        experience: 10,
        clients: 28,
        awards: 5,
        online: true,
        category: ['dev', 'management']
    },
    {
        id: 2,
        name: 'Sophie Martin',
        role: 'Directrice Artistique',
        department: 'Design',
        photo: 'https://images.unsplash.com/photo-1494790108755-2616b612b786?w=400&h=400&fit=crop',
        bio: 'Spécialiste en design d\'interface et expérience utilisateur.',
        fullBio: 'Sophie combine une expertise en design d\'interface avec une approche centrée sur l\'utilisateur. Elle dirige une équipe de designers talentueux pour créer des expériences digitales mémorables et fonctionnelles.',
        tags: ['UI/UX', 'Figma', 'Design System', 'Prototypage'],
        expertise: ['Design Thinking', 'Recherche Utilisateur', 'Accessibilité', 'Animation'],
        social: [
            { platform: 'Behance', url: '#', icon: '🎨' },
            { platform: 'Dribbble', url: '#', icon: '🏀' },
            { platform: 'Instagram', url: '#', icon: '📸' }
        ],
        email: 'sophie@entreprise.com',
        phone: '+33 1 23 45 67 90',
        projects: 38,
        experience: 8,
        clients: 45,
        awards: 7,
        online: true,
        category: ['design', 'management']
    },
    {
        id: 3,
        name: 'Thomas Lambert',
        role: 'Développeur Frontend',
        department: 'Développement',
        photo: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w-400&h=400&fit=crop',
        bio: 'Passionné par Vue.js et les animations web modernes.',
        fullBio: 'Thomas est spécialisé dans le développement frontend avec Vue.js. Il adore créer des interfaces interactives et performantes, en mettant l\'accent sur les animations fluides et l\'expérience utilisateur.',
        tags: ['Vue.js', 'JavaScript', 'CSS3', 'Animation'],
        expertise: ['Vue.js', 'Performance Web', 'Animations', 'Responsive Design'],
        social: [
            { platform: 'GitHub', url: '#', icon: '💻' },
            { platform: 'CodePen', url: '#', icon: '✒️' },
            { platform: 'Twitter', url: '#', icon: '🐦' }
        ],
        email: 'thomas@entreprise.com',
        phone: '+33 1 23 45 67 91',
        projects: 27,
        experience: 4,
        clients: 19,
        awards: 2,
        online: false,
        category: ['dev']
    },
    {
        id: 4,
        name: 'Emma Chen',
        role: 'Chef de Projet Digital',
        department: 'Management',
        photo: 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=400&h=400&fit=crop',
        bio: 'Experte en gestion agile et coordination d\'équipes.',
        fullBio: 'Emma excelle dans la gestion de projets digitaux complexes. Elle utilise des méthodologies agiles pour garantir la livraison dans les délais et le respect des budgets, tout en maintenant une communication transparente avec les clients.',
        tags: ['Agile', 'Scrum', 'Jira', 'Gestion'],
        expertise: ['Gestion de Projet', 'Méthodologies Agile', 'Planification', 'Communication'],
        social: [
            { platform: 'LinkedIn', url: '#', icon: '💼' },
            { platform: 'Twitter', url: '#', icon: '🐦' },
            { platform: 'Medium', url: '#', icon: '📝' }
        ],
        email: 'emma@entreprise.com',
        phone: '+33 1 23 45 67 92',
        projects: 56,
        experience: 6,
        clients: 34,
        awards: 3,
        online: true,
        category: ['management']
    },
    {
        id: 5,
        name: 'Karim Alami',
        role: 'Expert DevOps',
        department: 'Développement',
        photo: 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=400&h=400&fit=crop',
        bio: 'Spécialiste en automatisation et infrastructure cloud.',
        fullBio: 'Karim est un expert DevOps passionné par l\'automatisation et l\'optimisation des processus de développement. Il met en place des infrastructures robustes et sécurisées pour assurer la scalabilité des applications.',
        tags: ['Kubernetes', 'Docker', 'AWS', 'CI/CD'],
        expertise: ['Infrastructure Cloud', 'Automatisation', 'Sécurité', 'Monitoring'],
        social: [
            { platform: 'GitHub', url: '#', icon: '💻' },
            { platform: 'LinkedIn', url: '#', icon: '💼' },
            { platform: 'Dev.to', url: '#', icon: '👨‍💻' }
        ],
        email: 'karim@entreprise.com',
        phone: '+33 1 23 45 67 93',
        projects: 31,
        experience: 7,
        clients: 22,
        awards: 4,
        online: true,
        category: ['dev']
    },
    {
        id: 6,
        name: 'Léa Petit',
        role: 'Designer UX/UI',
        department: 'Design',
        photo: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=400&h=400&fit=crop',
        bio: 'Focus sur la recherche utilisateur et les tests d\'utilisabilité.',
        fullBio: 'Léa est spécialisée en recherche utilisateur et design d\'interaction. Elle combine des méthodes qualitatives et quantitatives pour créer des interfaces intuitives et accessibles à tous les utilisateurs.',
        tags: ['User Research', 'Wireframing', 'Testing', 'Accessibility'],
        expertise: ['Recherche Utilisateur', 'Tests Utilisabilité', 'Prototypage', 'Design Accessible'],
        social: [
            { platform: 'Behance', url: '#', icon: '🎨' },
            { platform: 'LinkedIn', url: '#', icon: '💼' },
            { platform: 'Twitter', url: '#', icon: '🐦' }
        ],
        email: 'lea@entreprise.com',
        phone: '+33 1 23 45 67 94',
        projects: 29,
        experience: 5,
        clients: 21,
        awards: 3,
        online: false,
        category: ['design']
    }
];

// Computed
const filteredMembers = computed(() => {
    if (activeCategory.value === 'all') {
        return teamMembers;
    }
    return teamMembers.filter(member => 
        member.category.includes(activeCategory.value)
    );
});

// Méthodes
const setActiveCategory = (categoryId: string) => {
    activeCategory.value = categoryId;
};

const hoverCard = (memberId: number) => {
    const card = document.querySelector(`.team-card[data-member="${memberId}"]`);
    if (card) {
        card.classList.add('hover');
    }
};

const resetCard = (memberId: number) => {
    const card = document.querySelector(`.team-card[data-member="${memberId}"]`);
    if (card) {
        card.classList.remove('hover');
    }
};

const openModal = (member: TeamMember) => {
    selectedMember.value = member;
    document.body.style.overflow = 'hidden';
};

const closeModal = () => {
    selectedMember.value = null;
    document.body.style.overflow = '';
};

const truncateText = (text: string, maxLength: number) => {
    if (text.length <= maxLength) return text;
    return text.substring(0, maxLength) + '...';
};

const imageLoad = (memberId: number) => {
    imageLoaded[memberId] = true;
};

const scrollToContact = () => {
    // Implémentez la navigation vers la section contact
    console.log('Navigation vers contact');
};

// Intersection Observer
const observer = new IntersectionObserver(
    (entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                showContent.value = true;
            }
        });
    },
    {
        threshold: 0.1,
        rootMargin: '50px'
    }
);

// Lifecycle
onMounted(() => {
    if (teamSection.value) {
        observer.observe(teamSection.value);
    }
});

onUnmounted(() => {
    if (teamSection.value) {
        observer.unobserve(teamSection.value);
    }
    closeModal();
});
</script>

<style scoped>
/* Base */
.team-section {
    width: 100%;
    min-height: 100vh;
    padding: 5rem 1rem;
    position: relative;
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    overflow: hidden;
}

/* Background */
.team-background {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 0;
}

.floating-shape {
    position: absolute;
    border-radius: 50%;
    background: linear-gradient(45deg, #3b82f6, #8b5cf6);
    opacity: 0.1;
    filter: blur(40px);
    animation: float 15s infinite ease-in-out;
}

.shape-1 {
    width: 300px;
    height: 300px;
    top: 10%;
    left: 10%;
    animation-delay: 0s;
}

.shape-2 {
    width: 400px;
    height: 400px;
    bottom: 10%;
    right: 10%;
    animation-delay: 5s;
    background: linear-gradient(45deg, #10b981, #3b82f6);
}

.shape-3 {
    width: 200px;
    height: 200px;
    top: 50%;
    right: 20%;
    animation-delay: 10s;
    background: linear-gradient(45deg, #8b5cf6, #ec4899);
}

.grid-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: 
        linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
    background-size: 50px 50px;
}

@keyframes float {
    0%, 100% {
        transform: translate(0, 0) rotate(0deg);
    }
    33% {
        transform: translate(30px, -50px) rotate(120deg);
    }
    66% {
        transform: translate(-20px, 40px) rotate(240deg);
    }
}

/* Conteneur */
.team-container {
    max-width: 1280px;
    margin: 0 auto;
    position: relative;
    z-index: 1;
}

/* En-tête */
.section-header {
    text-align: center;
    margin-bottom: 4rem;
    opacity: 0;
    transform: translateY(30px);
    transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
}

.section-header.animated {
    opacity: 1;
    transform: translateY(0);
}

.section-label {
    display: inline-block;
    padding: 0.5rem 1.5rem;
    background: rgba(59, 130, 246, 0.1);
    color: #3b82f6;
    font-size: 0.875rem;
    font-weight: 600;
    border-radius: 20px;
    margin-bottom: 1.5rem;
    letter-spacing: 1px;
}

.section-title {
    margin-bottom: 1rem;
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

.section-description {
    font-size: 1.125rem;
    color: #94a3b8;
    max-width: 700px;
    margin: 0 auto;
    line-height: 1.6;
}

/* Catégories */
.team-categories {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    justify-content: center;
    margin-bottom: 3rem;
    opacity: 0;
    transform: translateY(20px);
    transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1) 0.2s;
}

.team-categories.animated {
    opacity: 1;
    transform: translateY(0);
}

.category-btn {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.75rem 1.5rem;
    background: rgba(30, 41, 59, 0.5);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    color: #cbd5e1;
    font-size: 0.95rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.category-btn::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
    transition: left 0.6s ease;
}

.category-btn:hover::before {
    left: 100%;
}

.category-btn:hover {
    border-color: rgba(59, 130, 246, 0.3);
    transform: translateY(-2px);
}

.category-btn.active {
    background: linear-gradient(135deg, #3b82f6, #8b5cf6);
    color: white;
    border-color: transparent;
    box-shadow: 0 4px 20px rgba(59, 130, 246, 0.3);
}

.category-icon {
    font-size: 1.25rem;
}

.category-count {
    background: rgba(255, 255, 255, 0.1);
    padding: 0.25rem 0.5rem;
    border-radius: 10px;
    font-size: 0.75rem;
    font-weight: 600;
}

/* Grille */
.team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 2rem;
    margin-bottom: 4rem;
}

/* Cartes */
.team-card {
    position: relative;
    height: 420px;
    perspective: 1000px;
    opacity: 0;
    transform: translateY(50px);
    transition: all 0.6s cubic-bezier(0.4, 0, 0.2, 1);
}

.team-card.animated {
    opacity: 1;
    transform: translateY(0);
}

.team-card:nth-child(1) { transition-delay: 0.3s; }
.team-card:nth-child(2) { transition-delay: 0.4s; }
.team-card:nth-child(3) { transition-delay: 0.5s; }
.team-card:nth-child(4) { transition-delay: 0.6s; }
.team-card:nth-child(5) { transition-delay: 0.7s; }
.team-card:nth-child(6) { transition-delay: 0.8s; }

.card-inner,
.card-back {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    border-radius: 20px;
    overflow: hidden;
    transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);
}

.card-inner {
    background: rgba(30, 41, 59, 0.7);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    display: flex;
    flex-direction: column;
    padding: 2rem;
    z-index: 2;
}

.team-card:hover .card-inner {
    transform: rotateY(180deg);
}

.card-back {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    transform: rotateY(180deg);
    padding: 2rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.team-card:hover .card-back {
    transform: rotateY(0deg);
}

/* Photo */
.member-photo {
    position: relative;
    width: 120px;
    height: 120px;
    margin: 0 auto 1.5rem;
}

.photo-frame {
    position: relative;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    overflow: hidden;
    border: 4px solid rgba(59, 130, 246, 0.2);
}

.photo-frame img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
    opacity: 0;
    transform: scale(0.9);
}

.photo-frame img.loaded {
    opacity: 1;
    transform: scale(1);
}

.photo-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(45deg, transparent, rgba(59, 130, 246, 0.1));
}

.photo-shine {
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: linear-gradient(
        45deg,
        transparent 30%,
        rgba(255, 255, 255, 0.1) 50%,
        transparent 70%
    );
    transform: rotate(30deg);
    animation: shine 3s infinite linear;
}

@keyframes shine {
    0% { transform: translateX(-100%) rotate(30deg); }
    100% { transform: translateX(100%) rotate(30deg); }
}

.online-status {
    position: absolute;
    bottom: 10px;
    right: 10px;
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: #ef4444;
    border: 2px solid #1e293b;
    transition: all 0.3s ease;
}

.online-status.online {
    background: #10b981;
    box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.3);
}

/* Informations */
.member-info {
    text-align: center;
    flex: 1;
}

.member-name {
    font-size: 1.5rem;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 0.5rem;
}

.member-role {
    color: #3b82f6;
    font-size: 0.95rem;
    font-weight: 600;
    margin-bottom: 1rem;
}

.member-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    justify-content: center;
    margin-bottom: 1rem;
}

.tag {
    padding: 0.25rem 0.75rem;
    background: rgba(59, 130, 246, 0.1);
    color: #3b82f6;
    font-size: 0.75rem;
    font-weight: 500;
    border-radius: 12px;
    border: 1px solid rgba(59, 130, 246, 0.2);
}

.tag.more {
    background: rgba(148, 163, 184, 0.1);
    color: #94a3b8;
    border-color: rgba(148, 163, 184, 0.2);
}

.member-bio {
    color: #94a3b8;
    font-size: 0.875rem;
    line-height: 1.5;
    margin-bottom: 1.5rem;
}

/* Footer */
.card-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: auto;
}

.social-links {
    display: flex;
    gap: 0.5rem;
}

.social-link {
    width: 36px;
    height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 10px;
    color: #94a3b8;
    text-decoration: none;
    transition: all 0.3s ease;
}

.social-link:hover {
    background: rgba(59, 130, 246, 0.2);
    color: #3b82f6;
    transform: translateY(-2px);
}

.view-profile-btn {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    background: transparent;
    border: 1px solid rgba(59, 130, 246, 0.3);
    color: #3b82f6;
    font-size: 0.875rem;
    font-weight: 600;
    border-radius: 10px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.view-profile-btn:hover {
    background: rgba(59, 130, 246, 0.1);
    transform: translateX(4px);
}

/* Carte arrière */
.back-content {
    color: #f8fafc;
}

.back-content h4 {
    font-size: 1.25rem;
    margin-bottom: 1rem;
    color: #3b82f6;
}

.expertise-list {
    list-style: none;
    padding: 0;
    margin-bottom: 1.5rem;
}

.expertise-list li {
    padding: 0.5rem 0;
    color: #cbd5e1;
    font-size: 0.875rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.expertise-list li:last-child {
    border-bottom: none;
}

.stats {
    display: flex;
    justify-content: space-around;
    margin-top: auto;
}

.stat {
    text-align: center;
}

.stat-value {
    display: block;
    font-size: 1.5rem;
    font-weight: 700;
    color: #3b82f6;
    margin-bottom: 0.25rem;
}

.stat-label {
    font-size: 0.75rem;
    color: #94a3b8;
}

/* Halo */
.card-halo {
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at center, rgba(59, 130, 246, 0.1) 0%, transparent 70%);
    opacity: 0;
    transition: opacity 0.3s ease;
    pointer-events: none;
    z-index: -1;
}

.team-card:hover .card-halo {
    opacity: 1;
}

/* CTA */
.team-cta {
    text-align: center;
    opacity: 0;
    transform: translateY(30px);
    transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1) 0.6s;
}

.team-cta.animated {
    opacity: 1;
    transform: translateY(0);
}

.join-team-btn {
    display: inline-flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
    padding: 1.5rem 3rem;
    background: linear-gradient(135deg, #3b82f6, #8b5cf6);
    border: none;
    border-radius: 20px;
    color: white;
    cursor: pointer;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.join-team-btn::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    transition: left 0.6s ease;
}

.join-team-btn:hover::before {
    left: 100%;
}

.join-team-btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(59, 130, 246, 0.4);
}

.btn-icon {
    font-size: 2rem;
}

.btn-text {
    font-size: 1.25rem;
    font-weight: 700;
}

.btn-subtext {
    font-size: 0.875rem;
    opacity: 0.9;
}

/* Modal */
.profile-modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(15, 23, 42, 0.9);
    backdrop-filter: blur(10px);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
    padding: 1rem;
}

.modal-content {
    width: 100%;
    max-width: 800px;
    max-height: 90vh;
    background: linear-gradient(135deg, #1e293b, #0f172a);
    border-radius: 24px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    overflow: hidden;
    position: relative;
}

.modal-close {
    position: absolute;
    top: 1.5rem;
    right: 1.5rem;
    width: 40px;
    height: 40px;
    background: rgba(255, 255, 255, 0.1);
    border: none;
    border-radius: 50%;
    color: white;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
    z-index: 10;
}

.modal-close:hover {
    background: rgba(239, 68, 68, 0.2);
    transform: rotate(90deg);
}

.modal-body {
    padding: 3rem;
    overflow-y: auto;
    max-height: calc(90vh - 6rem);
}

.modal-header {
    display: flex;
    align-items: center;
    gap: 2rem;
    margin-bottom: 3rem;
}

.modal-photo {
    position: relative;
    width: 120px;
    height: 120px;
    flex-shrink: 0;
}

.modal-photo img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
    border: 4px solid rgba(59, 130, 246, 0.3);
}

.modal-status {
    position: absolute;
    bottom: 5px;
    right: 5px;
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: #ef4444;
    border: 3px solid #1e293b;
}

.modal-status.online {
    background: #10b981;
}

.modal-header-info h3 {
    font-size: 2rem;
    color: #f8fafc;
    margin-bottom: 0.5rem;
}

.modal-role {
    font-size: 1.25rem;
    color: #3b82f6;
    font-weight: 600;
    margin-bottom: 0.25rem;
}

.modal-department {
    color: #94a3b8;
    font-size: 1rem;
}

.modal-details {
    display: grid;
    gap: 2rem;
}

.detail-section h4 {
    font-size: 1.25rem;
    color: #f8fafc;
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid rgba(59, 130, 246, 0.3);
}

.detail-section p {
    color: #cbd5e1;
    line-height: 1.6;
}

.expertise-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 1rem;
}

.expertise-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    color: #cbd5e1;
}

.expertise-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #3b82f6;
}

.contact-info {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.contact-item {
    display: flex;
    align-items: center;
    gap: 1rem;
    color: #cbd5e1;
    text-decoration: none;
    transition: color 0.3s ease;
}

.contact-item:hover {
    color: #3b82f6;
}

.contact-icon {
    font-size: 1.25rem;
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1rem;
}

.stat-card {
    background: rgba(30, 41, 59, 0.5);
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
    border: 1px solid rgba(255, 255, 255, 0.1);
}

.stat-number {
    display: block;
    font-size: 2rem;
    font-weight: 700;
    color: #3b82f6;
    margin-bottom: 0.5rem;
}

.stat-title {
    color: #94a3b8;
    font-size: 0.875rem;
}

/* Animations */
.modal-enter-active,
.modal-leave-active {
    transition: opacity 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
    opacity: 0;
}

.modal-enter-active .modal-content,
.modal-leave-active .modal-content {
    transition: transform 0.3s ease;
}

.modal-enter-from .modal-content,
.modal-leave-to .modal-content {
    transform: scale(0.9);
}

.stagger-fade-enter-active {
    transition: all 0.6s ease;
}

.stagger-fade-enter-from {
    opacity: 0;
    transform: translateY(30px);
}

/* Responsive */
@media (max-width: 768px) {
    .team-grid {
        grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    }
    
    .title-line {
        font-size: 2rem;
    }
    
    .section-description {
        font-size: 1rem;
    }
    
    .team-categories {
        overflow-x: auto;
        padding-bottom: 1rem;
        justify-content: flex-start;
    }
    
    .modal-body {
        padding: 2rem 1.5rem;
    }
    
    .modal-header {
        flex-direction: column;
        text-align: center;
        gap: 1rem;
    }
}

@media (max-width: 640px) {
    .team-card {
        height: 380px;
    }
    
    .card-inner {
        padding: 1.5rem;
    }
}

/* Scrollbar */
.modal-body::-webkit-scrollbar {
    width: 8px;
}

.modal-body::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 4px;
}

.modal-body::-webkit-scrollbar-thumb {
    background: rgba(59, 130, 246, 0.3);
    border-radius: 4px;
}

.modal-body::-webkit-scrollbar-thumb:hover {
    background: rgba(59, 130, 246, 0.5);
}
</style>