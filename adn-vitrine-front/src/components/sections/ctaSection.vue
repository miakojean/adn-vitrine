<template>
    <section class="hero-carousel">
        <div class="carousel-container">
            <div 
                v-for="(slide, index) in slides" 
                :key="index"
                :class="['carousel-slide', { active: currentSlide === index }]"
                :style="{ backgroundImage: `url(${slide.image})` }"
            >
                <div class="slide-overlay"></div>
                
                <div class="slide-content">
                    <h2>{{ slide.title }}</h2>
                    <p>{{ slide.description }}</p>
                    <moreButton 
                        :label="slide.buttonText" 
                        @click="() => router.push('/services')"
                    />
                </div>
            </div>
            
            <div class="carousel-indicators">
                <button
                    v-for="(_, index) in slides"
                    :key="index"
                    :class="['indicator', { active: currentSlide === index }]"
                    @click="goToSlide(index)"
                    :aria-label="`Aller au slide ${index + 1}`"
                ></button>
            </div>

            </div>
    </section>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';
import heroImage_1 from '../../assets/pic/pexels-ekaterina-bolovtsova-6077381.jpg';
import heroImage_2 from '../../assets/pic/pexels-matreding-12953639.jpg';
import heroImage_3 from '../../assets/pic/pexels-roboseal34-35457179.jpg';
import heroImage_4 from '../../assets/pic/pexels-vizualproduction-11205891.jpg';
import moreButton from '../button/moreButton.vue';

interface Slide {
    image: string;
    title: string;
    description: string;
    buttonText?: string;
}

export default defineComponent({
    name: 'HeroCarousel',
    components: { moreButton },
    setup() {
        const router = useRouter();
        const currentSlide = ref(0);
        const interval = ref<number | null>(null);
        const autoPlayDelay = 5000;

        const slides = ref<Slide[]>([
            {
                image: heroImage_2,
                title: 'Bienvenue chez ADN Consulting.',
                description: 'Nous accompagnons les entreprises dans leur sécurité juridique',
                buttonText: 'Découvrir'
            },
            {
                image: heroImage_1,
                title: 'Sécurisez votre organisation juridiquement.',
                description: 'Expertise en droit des affaires, propriété intellectuelle et droit du numérique pour vos besoins spécifiques.',
                buttonText: 'Explorer'
            },
            {
                image: heroImage_3,
                title: 'Solutions juridiques digitales.',
                description: 'Plongez au cœur de l\'innovation juridique avec nos outils modernes.',
                buttonText: 'En savoir plus'
            },
            {
                image: heroImage_4,
                title: 'Expertise légale augmentée.',
                description: 'Nous intégrons des technologies légales pour optimiser vos processus et gagner en efficacité.',
                buttonText: 'Visiter'
            }
        ]);

        const nextSlide = () => {
            currentSlide.value = (currentSlide.value + 1) % slides.value.length;
        };

        const prevSlide = () => {
            currentSlide.value = (currentSlide.value - 1 + slides.value.length) % slides.value.length;
        };

        const goToSlide = (index: number) => {
            currentSlide.value = index;
            resetAutoPlay();
        };

        const startAutoPlay = () => {
            interval.value = window.setInterval(nextSlide, autoPlayDelay);
        };

        const resetAutoPlay = () => {
            if (interval.value) clearInterval(interval.value);
            startAutoPlay();
        };

        onMounted(() => startAutoPlay());
        onUnmounted(() => {
            if (interval.value) clearInterval(interval.value);
        });

        return {
            router,
            slides,
            currentSlide,
            nextSlide,
            prevSlide,
            goToSlide
        };
    }
});
</script>

<style scoped>
.hero-carousel {
    width: 100%;
    height: 100vh;
    overflow: hidden;
    position: relative;
    background-color: #000;
}

.carousel-container {
    position: relative;
    width: 100%;
    height: 100%;
}

.carousel-slide {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
    opacity: 0;
    transition: opacity 1.2s ease-in-out; /* Transition douce entre les images */
    display: flex;
    justify-content: center;
    align-items: center;
}

.carousel-slide.active {
    opacity: 1;
    z-index: 1;
}

.slide-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(
        to bottom,
        rgba(0, 0, 0, 0.3) 0%,
        rgba(0, 0, 0, 0.5) 60%,
        rgba(0, 0, 0, 0.8) 100%
    );
}

.slide-content {
    position: relative;
    z-index: 2;
    text-align: center;
    padding: 0 1.5rem;
    width: 100%;
    max-width: 900px;
}

.slide-content h2 {
    color: white;
    /* Taille fluide : min 1.8rem (mobile) -> max 3.5rem (desktop) */
    font-size: clamp(1.8rem, 7vw, 3.8rem);
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 1.5rem;
    text-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
    word-break: keep-all; /* Évite les coupures de mots laides */
}

.slide-content p {
    color: rgba(255, 255, 255, 0.9);
    /* Taille fluide : min 1rem -> max 1.3rem */
    font-size: clamp(1rem, 3vw, 1.3rem);
    line-height: 1.5;
    margin-bottom: 2.5rem;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
    text-shadow: 0 2px 5px rgba(0, 0, 0, 0.5);
}

/* Indicateurs */
.carousel-indicators {
    position: absolute;
    bottom: 3rem;
    left: 0;
    right: 0;
    display: flex;
    justify-content: center;
    gap: 1rem;
    z-index: 10;
}

.indicator {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    border: 1.5px solid white;
    background: transparent;
    cursor: pointer;
    transition: all 0.3s ease;
    padding: 0;
}

.indicator.active {
    background: white;
    transform: scale(1.3);
}

/* Boutons de navigation */
.carousel-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(255, 255, 255, 0.1);
    color: white;
    border: none;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    cursor: pointer;
    z-index: 10;
    backdrop-filter: blur(5px);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background 0.3s;
}

.carousel-btn:hover {
    background: rgba(255, 255, 255, 0.3);
}

.carousel-btn.prev { left: 1rem; }
.carousel-btn.next { right: 1rem; }

/* Responsive adjustments pour tablettes et + */
@media (min-width: 768px) {
    .slide-content {
        padding: 0 3rem;
    }
}
</style>