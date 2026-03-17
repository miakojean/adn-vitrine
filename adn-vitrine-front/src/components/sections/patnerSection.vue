<template>
    <section class="partners-section" ref="partnersSection">
        <div class="partners-background">
            <div class="floating-shape shape-1"></div>
            <div class="floating-shape shape-2"></div>
            <div class="dot-pattern"></div>
        </div>

        <div class="container">
            <div class="section-header" :class="{ 'animated': showContent }">
                <span class="section-label">Nos partenaires</span>
                <h2 class="section-title">
                    Ils nous font <span class="highlight">Confiance</span>
                </h2>
                <p class="section-description">
                    Nous collaborons avec les leaders du marché pour offrir des solutions 
                    innovantes et performantes à nos clients.
                </p>
            </div>

            <div class="carousel-wrapper" :class="{ 'animated': showContent }">
                <div class="carousel-container" @mouseenter="pauseCarousel" @mouseleave="resumeCarousel">
                    <div class="carousel-track" ref="carouselTrack">
                        <div 
                            v-for="(partner, index) in [...partnersData, ...partnersData]" 
                            :key="index"
                            class="carousel-item"
                        >
                            <div class="logo-wrapper">
                                <img 
                                    :src="partner.logo" 
                                    :alt="partner.name"
                                    class="partner-logo"
                                />
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="cta-container" :class="{ 'animated': showContent }">
                <moreButton label="Rejoindre l'aventure" @click="() => router.push('/contact')"/>
            </div>
        </div>
    </section>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, nextTick } from 'vue';
import moreButton from '../button/moreButton.vue';
import { useRouter } from 'vue-router';

// Imports (Inchangés)
import partnerPic1 from '../../assets/partners/logo.png'
import partnerPic2 from '../../assets/partners/PROPARCO_Logo_RVB-1.png';
import partnerPic3 from '../../assets/partners/giz-logo-01.jpg';
import partnerPic4 from '../../assets/partners/OIP (4).webp'
import partnerPic5 from '../../assets/partners/OIP (1).webp';
import partnerPic6 from '../../assets/partners/OIP (2).webp';
import partnerPic7 from '../../assets/partners/millennium-challenge-corporation-logo-png_seeklogo-245301.png';
import partnerPic8 from '../../assets/partners/clients-logo-05.png';


interface Partner { id: number; name: string; logo: string; category: string; }

const router = useRouter();
const partnersData: Partner[] = [
    { id: 1, name: 'millenium', category: 'AI', logo: partnerPic7 },
    { id: 2, name: 'Contratchap', category: 'General', logo: partnerPic1 },
    { id: 3, name: 'giz', category: 'Search', logo: partnerPic3 },
    { id: 4, name: 'oip', category: 'Networking', logo: partnerPic4 },
    { id: 5, name: 'Intel', category: 'Hardware', logo: partnerPic5 },
    { id: 6, name: 'Meta', category: 'Social', logo: partnerPic6 },
    { id: 8, name: 'Discord', category: 'Community', logo: partnerPic8 },
    { id: 9, name: 'proparco', category: 'Finance', logo: partnerPic2 },
    
];

const partnersSection = ref<HTMLElement | null>(null);
const showContent = ref(false);

const pauseCarousel = () => {
    document.documentElement.style.setProperty('--play-state', 'paused');
};

const resumeCarousel = () => {
    document.documentElement.style.setProperty('--play-state', 'running');
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => { if (entry.isIntersecting) showContent.value = true; });
}, { threshold: 0.1 });

onMounted(() => {
    if (partnersSection.value) observer.observe(partnersSection.value);
    nextTick(() => {
        document.documentElement.style.setProperty('--carousel-speed', '40s');
        document.documentElement.style.setProperty('--play-state', 'running');
    });
});

onUnmounted(() => {
    if (partnersSection.value) observer.unobserve(partnersSection.value);
});
</script>

<style scoped>
:root {
    --carousel-speed: 40s;
    --play-state: running;
}

.partners-section {
    position: relative;
    padding: 8rem 0;
    background-color: #ffffff;
    overflow: hidden;
    color: #1e293b;
}

/* --- BACKGROUND DESIGN --- */
.partners-background {
    position: absolute;
    inset: 0;
    pointer-events: none;
}

.dot-pattern {
    position: absolute;
    inset: 0;
    background-image: radial-gradient(#e2e8f0 1px, transparent 1px);
    background-size: 32px 32px;
    opacity: 0.5;
}

.floating-shape {
    position: absolute;
    filter: blur(80px);
    opacity: 0.4;
    z-index: 0;
}

.shape-1 { width: 400px; height: 400px; background: #dbeafe; top: -10%; left: -5%; }
.shape-2 { width: 300px; height: 300px; background: #ede9fe; bottom: 0%; right: 0%; }

/* --- HEADER --- */
.container {
    max-width: 1200px;
    margin: 0 auto;
    position: relative;
    z-index: 1;
    padding: 0 1.5rem;
}

.section-header {
    text-align: center;
    margin-bottom: 5rem;
    opacity: 0;
    transform: translateY(30px);
    transition: all 1s ease;
}

.section-header.animated { opacity: 1; transform: translateY(0); }

.section-label {
    display: inline-block;
    padding: 0.5rem 1rem;
    background: #f1f5f9;
    border-radius: 100px;
    color: #6366f1;
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 1.5rem;
}

.section-title {
    font-size: clamp(2.5rem, 5vw, 3.5rem);
    font-weight: 850;
    color: #0f172a;
    letter-spacing: -0.02em;
    margin-bottom: 1.5rem;
}

.highlight {
    background: linear-gradient(135deg, #3b82f6 0%, #304be1 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}

.section-description {
    color: #64748b;
    max-width: 650px;
    margin: 0 auto;
    font-size: 1.2rem;
    line-height: 1.7;
}

/* --- CARROUSEL --- */
.carousel-wrapper {
    position: relative;
    margin: 4rem 0;
}

/* Masques dégradés pour un effet de fondu sur les bords */
.carousel-wrapper::before,
.carousel-wrapper::after {
    content: "";
    position: absolute;
    top: 0;
    bottom: 0;
    width: 150px;
    z-index: 2;
    pointer-events: none;
}

/*.carousel-wrapper::before {
    left: 0;
    background: linear-gradient(to right, #ffffff, transparent);
}

.carousel-wrapper::after {
    right: 0;
    background: linear-gradient(to left, #ffffff, transparent);
}*/

.carousel-track {
    display: flex;
    width: max-content;
    gap: 4rem;
    animation: scroll var(--carousel-speed) linear infinite;
    animation-play-state: var(--play-state);
}

@keyframes scroll {
    0% { transform: translateX(0); }
    100% { transform: translateX(calc(-50% - 2rem)); }
}

.logo-wrapper {
    height: 80px;
    width: 180px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.4s ease;
}

.partner-logo {
    max-height: 100%;
    max-width: 100%;
    object-fit: contain;
    filter: grayscale(1) opacity(0.5);
    transition: all 0.4s ease;
}

.logo-wrapper:hover .partner-logo {
    filter: grayscale(0) opacity(1);
    transform: scale(1.1);
}

/* --- CTA --- */
.cta-container {
    text-align: center;
    margin-top: 5rem;
    opacity: 0;
}
.cta-container.animated { opacity: 1; }

@media (max-width: 768px) {
    .section-header { margin-bottom: 3rem; }
    .logo-wrapper { width: 140px; height: 60px; }
    .carousel-wrapper::before, .carousel-wrapper::after { width: 50px; }
}
</style>