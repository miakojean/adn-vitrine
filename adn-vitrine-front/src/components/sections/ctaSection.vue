<template>
    <section class="hero-carousel">
        <!-- Conteneur du carrousel -->
        <div class="carousel-container">
            <!-- Slides avec images de fond -->
            <div 
                v-for="(slide, index) in slides" 
                :key="index"
                :class="['carousel-slide', { active: currentSlide === index }]"
                :style="{ backgroundImage: `url(${slide.image})` }"
            >
                <!-- Overlay sombre pour meilleure lisibilité -->
                <div class="slide-overlay"></div>
                
                <!-- Contenu textuel -->
                <div class="slide-content">
                    <!-- Titre avec effet lettre par lettre -->
                    <h2 ref="titleRefs">
                        <span 
                            v-for="(char, charIndex) in slide.title" 
                            :key="charIndex"
                            class="title-char"
                            :style="{
                                animationDelay: `${charIndex * 0.05}s`,
                                opacity: currentSlide === index ? 1 : 0
                            }"
                        >
                            {{ char === ' ' ? '&nbsp;' : char }}
                        </span>
                    </h2>
                    <p>{{ slide.description }}</p>
                    <moreButton :label="slide.buttonText"/>
                </div>
            </div>
            
            <!-- Indicateurs de slides -->
            <div class="carousel-indicators">
                <button
                    v-for="(slide, index) in slides"
                    :key="index"
                    :class="['indicator', { active: currentSlide === index }]"
                    @click="goToSlide(index)"
                    :aria-label="`Aller au slide ${index + 1}`"
                ></button>
            </div>
            
            <!-- Boutons de navigation 
                <button class="carousel-btn prev" @click="prevSlide" aria-label="Slide précédent">
                    <span>&#10094;</span>
                </button>
                <button class="carousel-btn next" @click="nextSlide" aria-label="Slide suivant">
                    <span>&#10095;</span>
                </button>
            -->
        </div>
    </section>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, onUnmounted, watch, nextTick } from 'vue';
import heroImage_1 from '../../assets/pic/pexels-ekaterina-bolovtsova-6077381.jpg';
import heroImage_2 from '../../assets/pic/pexels-matreding-12953639.jpg';
import heroImage_3 from '../../assets/pic/pexels-roboseal34-35457179.jpg';
import heroImage_4 from '../../assets/pic/pexels-vizualproduction-11205891.jpg'
import moreButton from '../button/moreButton.vue';

interface Slide {
    image: string;
    title: string;
    description: string;
    buttonText?: string;
}

export default defineComponent({
    name: 'HeroCarousel',
    components: {
        moreButton
    },
    setup() {
        const slides = ref<Slide[]>([
            {
                image: heroImage_2,
                title: 'Bienvenue chez ADN Consulting SAS.',
                description: 'un cabinet juridique innovant dédié à accompagner les PME, startups et entrepreneurs indépendants.',
                buttonText: 'Découvrir'
            },
            {
                image: heroImage_1,
                title: 'Nous Aidons les Organisations à se Sécuriser Juridiquement.',
                description: 'Notre expertise couvre le droit des affaires, la propriété intellectuelle et le droit du numérique, afin de répondre efficacement à vos besoins spécifiques.',
                buttonText: 'Explorer'
            },
            {
                image: heroImage_3,
                title: 'Solutions juridiques digitales.',
                description: 'Plongez au cœur de l\'innovation juridique.',
                buttonText: 'En savoir plus'
            },
            {
                image: heroImage_4,
                title: 'Expertise légale',
                description: 'Le Cabinet ADN Consulting SAS intègre des technologies légales innovantes pour optimiser vos processus juridiques et gagner en efficacité.',
                buttonText: 'Visiter'
            }
        ]);

        const currentSlide = ref(0);
        const interval = ref<number | null>(null);
        const autoPlayDelay = 5000; // 5 secondes
        const titleRefs = ref<HTMLElement[]>([]);

        // Fonction pour réinitialiser l'animation des lettres
        const resetTitleAnimation = () => {
            // Réinitialiser l'opacité de toutes les lettres
            const allChars = document.querySelectorAll('.title-char');
            allChars.forEach(char => {
                (char as HTMLElement).style.opacity = '0';
                (char as HTMLElement).style.animation = 'none';
            });
            
            // Forcer un reflow pour redémarrer l'animation
            void nextTick(() => {
                const activeChars = titleRefs.value[currentSlide.value]?.querySelectorAll('.title-char');
                if (activeChars) {
                    activeChars.forEach((char: Element, index: number) => {
                        const htmlChar = char as HTMLElement;
                        htmlChar.style.opacity = '1';
                        htmlChar.style.animation = `typing 0.5s ease forwards`;
                        htmlChar.style.animationDelay = `${index * 0.05}s`;
                    });
                }
            });
        };

        // Fonction pour passer au slide suivant
        const nextSlide = () => {
            currentSlide.value = (currentSlide.value + 1) % slides.value.length;
            resetTitleAnimation();
        };

        // Fonction pour passer au slide précédent
        const prevSlide = () => {
            currentSlide.value = (currentSlide.value - 1 + slides.value.length) % slides.value.length;
            resetTitleAnimation();
        };

        // Fonction pour aller à un slide spécifique
        const goToSlide = (index: number) => {
            currentSlide.value = index;
            resetAutoPlay();
            resetTitleAnimation();
        };

        // Démarrer le défilement automatique
        const startAutoPlay = () => {
            if (interval.value) {
                clearInterval(interval.value);
            }
            interval.value = window.setInterval(() => {
                nextSlide();
            }, autoPlayDelay);
        };

        // Réinitialiser l'autoplay
        const resetAutoPlay = () => {
            if (interval.value) {
                clearInterval(interval.value);
            }
            startAutoPlay();
        };

        // Arrêter l'autoplay au survol
        const pauseAutoPlay = () => {
            if (interval.value) {
                clearInterval(interval.value);
                interval.value = null;
            }
        };

        // Initialiser le carrousel
        onMounted(() => {
            startAutoPlay();
            // Lancer l'animation pour le premier slide
            setTimeout(() => {
                resetTitleAnimation();
            }, 100);
        });

        // Observer les changements de slide
        watch(currentSlide, () => {
            resetTitleAnimation();
        });

        // Nettoyer à la destruction du composant
        onUnmounted(() => {
            if (interval.value) {
                clearInterval(interval.value);
            }
        });

        return {
            slides,
            currentSlide,
            titleRefs,
            nextSlide,
            prevSlide,
            goToSlide,
            pauseAutoPlay,
            resetAutoPlay
        };
    }
});
</script>

<style scoped>
/* Styles mobiles first */
.hero-carousel {
    width: 100%;
    height: 100vh;
    overflow: hidden;
    position: relative;
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
    background-repeat: no-repeat;
    opacity: 0;
    transition: opacity 1s ease-in-out;
    display: flex;
    justify-content: center;
    align-items: center;
}

.carousel-slide.active {
    opacity: 1;
}

.slide-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(
        to bottom,
        rgba(0, 0, 0, 0.3) 0%,
        rgba(0, 0, 0, 0.5) 50%,
        rgba(0, 0, 0, 0.7) 100%
    );
}

.slide-content {
    position: relative;
    z-index: 2;
    text-align: center;
    padding: 1rem;
    max-width: 1000px;
}

.slide-content h2 {
    color: white;
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 1rem;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.502);
    display: inline-block;
    /*overflow: hidden;*/
}

/* Conteneur pour les lettres */
.title-char {
    display: inline-block;
    opacity: 0;
    transform: translateY(20px);
    animation: typing 0.5s ease forwards;
}

/* Animation lettre par lettre */
@keyframes typing {
    0% {
        opacity: 0;
        transform: translateY(20px);
    }
    50% {
        opacity: 1;
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

.slide-content p {
    color: white;
    font-size: 1.125rem;
    font-weight: 600;
    margin-bottom: 2rem;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
    animation: fadeInUp 0.8s ease-out 0.5s both;
}

.carousel-indicators {
    position: absolute;
    bottom: 2rem;
    left: 0;
    right: 0;
    display: flex;
    justify-content: center;
    gap: 0.75rem;
    z-index: 10;
}

.indicator {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    border: 2px solid white;
    background: transparent;
    cursor: pointer;
    padding: 0;
    transition: all 0.3s ease;
}

.indicator.active {
    background: white;
    transform: scale(1.2);
}

.carousel-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(255, 255, 255, 0.2);
    color: white;
    border: none;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    font-size: 1.5rem;
    cursor: pointer;
    z-index: 10;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    backdrop-filter: blur(4px);
}

.carousel-btn:hover {
    background: rgba(255, 255, 255, 0.3);
    transform: translateY(-50%) scale(1.1);
}

.carousel-btn.prev {
    left: 1rem;
}

.carousel-btn.next {
    right: 1rem;
}

/* Animation pour le contenu */
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

/* Responsive design */
@media (min-width: 640px) {
    .slide-content h2 {
        font-size: 2.5rem;
    }
    
    .slide-content p {
        font-size: 1.25rem;
    }
    
    .carousel-btn {
        width: 60px;
        height: 60px;
        font-size: 2rem;
    }
}

@media (min-width: 768px) {
    .slide-content h2 {
        font-size: 3rem;
    }
    
    .carousel-btn.prev {
        left: 2rem;
    }
    
    .carousel-btn.next {
        right: 2rem;
    }
}

@media (min-width: 1024px) {
    .slide-content h2 {
        font-size: 3.5rem;
    }
    
    .carousel-btn {
        width: 70px;
        height: 70px;
    }
}

/* Pour arrêter l'autoplay au survol */
.carousel-container:hover .carousel-btn {
    opacity: 1;
}

/* Pause autoplay on hover */
@media (hover: hover) {
    .carousel-container:hover {
        animation-play-state: paused;
    }
}
</style>