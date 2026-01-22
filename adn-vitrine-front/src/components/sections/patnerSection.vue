<template>
    <section class="partners-section" ref="partnersSection">
        <div class="partners-background">
            <div class="floating-shape shape-1"></div>
            <div class="floating-shape shape-2"></div>
            <div class="grid-overlay"></div>
        </div>

        <div class="container">
            <div class="section-header" :class="{ 'animated': showContent }">
                <span class="section-label">Partenariats stratégiques</span>
                <h2 class="section-title">
                    Nos différents <span class="highlight">Partenaires</span>
                </h2>
                <p class="section-description">
                    Nos objectifs sont ambitieux et ne peuvent être atteints qu'en partenariat.
                    Nous collaborons avec les leaders technologiques pour bâtir le futur.
                </p>
            </div>

            <div class="hex-wrapper" :class="{ 'animated': showContent }">
                
                <div class="hex-column side-column">
                    <div 
                        v-for="(partner, index) in leftPartners" 
                        :key="partner.id"
                        class="hex-item small"
                        :style="{ transitionDelay: `${index * 100}ms` }"
                        @mouseenter="activePartner = partner"
                        @mouseleave="activePartner = null"
                    >
                        <div class="hex-content">
                            <img :src="partner.logo" :alt="partner.name" class="partner-logo" />
                        </div>
                        <div class="hex-border"></div>
                    </div>
                </div>

                <div class="hex-column center-column">
                    <div class="hex-item big main-brand">
                        <div class="hex-content">
                            <div class="brand-logo-placeholder">
                                <img src="../../assets/partners/LOGO ROND.png" class="adn__logo" alt="">
                            </div>
                        </div>
                        <div class="hex-pulse"></div>
                        <div class="hex-border"></div>
                    </div>
                </div>

                <div class="hex-column side-column">
                    <div 
                        v-for="(partner, index) in rightPartners" 
                        :key="partner.id"
                        class="hex-item small"
                        :style="{ transitionDelay: `${(index + leftPartners.length) * 100}ms` }"
                        @mouseenter="activePartner = partner"
                        @mouseleave="activePartner = null"
                    >
                        <div class="hex-content">
                            <img :src="partner.logo" :alt="partner.name" class="partner-logo" />
                        </div>
                        <div class="hex-border"></div>
                    </div>
                </div>

            </div>

            <transition name="fade">
                <div v-if="activePartner" class="partner-detail">
                    <span class="detail-name">{{ activePartner.name }}</span>
                    <span class="detail-cat">{{ activePartner.category }}</span>
                </div>
            </transition>

            <div class="cta-container" :class="{ 'animated': showContent }">
                <moreButton label="Devenir partenaire" @click="()=> router.push('/partner')"/>
            </div>
        </div>
    </section>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue';
import moreButton from '../button/moreButton.vue';

import partnerPic1 from '../../assets/partners/6324bc47b4b22-millenium-fdfp-cote-ivoire.png';
import partnerPic2 from '../../assets/partners/MILLENIUM-CHALLENGE-ACCOUNT.png';
import partnerPic3 from '../../assets/partners/giz-logo-01.jpg';
import partnerPic4 from '../../assets/partners/OIP (1).webp';
import partnerPic5 from '../../assets/partners/OIP (1).webp';
import partnerPic6 from '../../assets/partners/OIP (2).webp';
import partnerPic7 from '../../assets/partners/millennium-challenge-corporation-logo-png_seeklogo-245301.png';
import partnerPic8 from '../../assets/partners/clients-logo-05.png';
import { useRouter } from 'vue-router';

// --- Types ---
interface Partner {
    id: number;
    name: string;
    logo: string;
    category: string;
}

const router = useRouter();

// --- Data ---
// J'utilise des SVGs placeholder. Remplace par les URLs de tes images.
const partnersData: Partner[] = [
    { id: 1, name: 'OpenAI', category: 'AI Intelligence', logo: partnerPic1 },
    { id: 2, name: 'AWS', category: 'Cloud Infrastructure', logo: partnerPic2 },
    { id: 3, name: 'Google', category: 'Search & Data', logo: partnerPic3 },
    { id: 4, name: 'Microsoft', category: 'Enterprise Solutions', logo: partnerPic4 },
    { id: 5, name: 'Intel', category: 'Hardware', logo: partnerPic5 },
    { id: 6, name: 'Meta', category: 'Social Connection', logo: partnerPic6 },
    { id: 7, name: 'Asus', category: 'Hardware Partner', logo: partnerPic7 },
    { id: 8, name: 'Discord', category: 'Community', logo: partnerPic8 },
];

// Répartition automatique gauche/droite pour équilibrer le design
const leftPartners = computed(() => partnersData.slice(0, Math.ceil(partnersData.length / 2)));
const rightPartners = computed(() => partnersData.slice(Math.ceil(partnersData.length / 2)));

// --- Logic d'animation ---
const partnersSection = ref<HTMLElement | null>(null);
const showContent = ref(false);
const activePartner = ref<Partner | null>(null);

const observer = new IntersectionObserver(
    (entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                showContent.value = true;
            }
        });
    },
    { threshold: 0.15 }
);

onMounted(() => {
    if (partnersSection.value) observer.observe(partnersSection.value);
});

onUnmounted(() => {
    if (partnersSection.value) observer.unobserve(partnersSection.value);
});
</script>

<style scoped>
/* --- BASE LAYOUT (Similaire TeamSection) --- */
.partners-section {
    position: relative;
    padding: 6rem 1rem;
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    overflow: hidden;
    color: #f8fafc;
    min-height: 80vh;
    display: flex;
    align-items: center;
}

.container {
    max-width: 1280px;
    margin: 0 auto;
    position: relative;
    z-index: 2;
    width: 100%;
}

/* --- BACKGROUND FX --- */
.partners-background {
    position: absolute;
    inset: 0;
    pointer-events: none;
}

.grid-overlay {
    position: absolute;
    inset: 0;
    background-image: 
        linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    mask-image: radial-gradient(circle at center, black 40%, transparent 80%);
}

.floating-shape {
    position: absolute;
    border-radius: 50%;
    filter: blur(60px);
    opacity: 0.15;
    animation: float 10s infinite ease-in-out;
}
.shape-1 { width: 300px; height: 300px; background: #3b82f6; top: -50px; left: 10%; }
.shape-2 { width: 400px; height: 400px; background: #8b5cf6; bottom: -50px; right: 10%; animation-delay: -5s; }

@keyframes float {
    0%, 100% { transform: translate(0, 0); }
    50% { transform: translate(20px, -20px); }
}

/* --- HEADER --- */
.section-header {
    text-align: center;
    margin-bottom: 4rem;
    opacity: 0;
    transform: translateY(20px);
    transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
}
.section-header.animated { opacity: 1; transform: translateY(0); }

.section-label {
    color: #8b5cf6;
    font-size: 0.875rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    display: block;
    margin-bottom: 1rem;
}

.section-title {
    font-size: clamp(2rem, 5vw, 3rem);
    font-weight: 800;
    margin-bottom: 1.5rem;
    line-height: 1.1;
}

.highlight {
    background: linear-gradient(90deg, #3b82f6, #8b5cf6);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}

.section-description {
    color: #94a3b8;
    max-width: 600px;
    margin: 0 auto;
    font-size: 1.1rem;
    line-height: 1.6;
}

/* --- HEXAGON GRID LAYOUT --- */
.hex-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 2rem;
    margin: 3rem 0;
    flex-wrap: wrap;
    opacity: 0;
    transform: scale(0.95);
    transition: all 1s ease 0.2s;
}

.hex-wrapper.animated { opacity: 1; transform: scale(1); }

.hex-column {
    display: flex;
    flex-direction: column;
    gap: 1.5rem; /* Espace vertical entre hexagones */
    align-items: center;
}

/* Décalage pour l'effet "Nid d'abeille" */
.side-column { margin-top: 3rem; }
.side-column:last-child { margin-top: 3rem; }

@media (min-width: 1024px) {
    .side-column { margin-top: 0; }
    /* On décale un hexagone sur deux si on veut, ou on garde colonnes droites */
    .side-column .hex-item:nth-child(even) { margin-left: 3rem; }
    .side-column .hex-item:nth-child(odd) { margin-right: 3rem; }
}

/* --- HEXAGON ITEM --- */
.hex-item {
    position: relative;
    /* Forme Hexagone (Flat Top) */
    clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
    background: rgba(30, 41, 59, 0.4); /* Glass Dark */
    backdrop-filter: blur(10px);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    cursor: pointer;
}

/* Tailles */
.small { width: 140px; height: 120px; }
.big { width: 220px; height: 190px; z-index: 10; background: linear-gradient(135deg, #1e293b, #0f172a); }

/* Contenu interne */
.hex-content {
    width: 70%;
    height: 70%;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 2;
}

.partner-logo {
    max-width: 100%;
    max-height: 100%;
    transition: 0.4s;
    opacity: 1;
}

/* Bordure simulée (car clip-path coupe border) */
.hex-border {
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.02));
    z-index: 1;
    transition: 0.3s;
}

/* --- INTERACTIONS --- */
.hex-item:hover {
    transform: scale(1.1) translateY(-5px);
    background: rgba(59, 130, 246, 0.1);
}

.hex-item:hover .partner-logo {
    filter: grayscale(0%);
    opacity: 1;
}

.hex-item:hover .hex-border {
    background: linear-gradient(135deg, #3b82f6, #8b5cf6);
    opacity: 0.5;
}

/* --- MAIN BRAND SPECIAL STYLES --- */
.main-brand {
    box-shadow: 0 0 50px rgba(0,0,0,0.5);
}

.brand-logo-placeholder {
    width: 120px;
    height: 120px;
    color: #f8fafc;
    filter: drop-shadow(0 0 10px rgba(59, 130, 246, 0.5));
}

.hex-pulse {
    position: absolute;
    inset: -20%;
    background: radial-gradient(circle, rgba(59, 130, 246, 0.4) 0%, transparent 70%);
    z-index: 0;
    opacity: 0;
    animation: pulse 3s infinite;
}
.main-brand .hex-pulse { opacity: 0.4; }

@keyframes pulse {
    0% { transform: scale(0.8); opacity: 0.2; }
    50% { transform: scale(1.1); opacity: 0.4; }
    100% { transform: scale(0.8); opacity: 0.2; }
}

/* --- INFO BULLE --- */
.partner-detail {
    position: absolute;
    bottom: 20%;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(15, 23, 42, 0.8);
    border: 1px solid rgba(59, 130, 246, 0.3);
    padding: 0.5rem 1.5rem;
    border-radius: 20px;
    backdrop-filter: blur(5px);
    text-align: center;
    pointer-events: none;
    z-index: 20;
}
.detail-name { display: block; font-weight: 700; color: white; }
.detail-cat { font-size: 0.75rem; color: #94a3b8; }

.fade-enter-active, .fade-leave-active { transition: opacity 0.3s; }
.fade-enter-from, .fade-leave-to { opacity: 0; }

/* --- CTA --- */
.cta-container {
    text-align: center;
    margin-top: 4rem;
    opacity: 0;
    transform: translateY(20px);
    transition: all 0.8s ease 0.4s;
}
.cta-container.animated { opacity: 1; transform: translateY(0); }

.partner-btn {
    background: transparent;
    color: #f8fafc;
    border: 1px solid rgba(139, 92, 246, 0.5);
    padding: 0.75rem 2rem;
    border-radius: 50px;
    font-weight: 600;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    transition: all 0.3s;
}

.partner-btn:hover {
    background: rgba(139, 92, 246, 0.1);
    border-color: #8b5cf6;
    transform: translateY(-2px);
    box-shadow: 0 4px 20px rgba(139, 92, 246, 0.2);
}

/* --- RESPONSIVE --- */
@media (max-width: 1024px) {
    .hex-wrapper {
        flex-direction: column;
        gap: 1rem;
    }
    .hex-column {
        flex-direction: row;
        justify-content: center;
        flex-wrap: wrap;
    }
    .center-column { order: -1; margin-bottom: 2rem; }
    .side-column { margin: 0; gap: 1rem; }
    .side-column .hex-item:nth-child(even) { margin-left: 0; }
    .side-column .hex-item:nth-child(odd) { margin-right: 0; }
}

@media (max-width: 640px) {
    .small { width: 100px; height: 86px; }
    .big { width: 160px; height: 138px; }
    .section-title { font-size: 2rem; }
}
</style>