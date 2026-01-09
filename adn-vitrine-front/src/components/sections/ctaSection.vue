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
                    <h2>{{ slide.title }}</h2>
                    <p>{{ slide.description }}</p>
                    <button class="cta-button" v-if="slide.buttonText">
                        {{ slide.buttonText }}
                    </button>
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
            
            <!-- Boutons de navigation -->
            <button class="carousel-btn prev" @click="prevSlide" aria-label="Slide précédent">
                <span>&#10094;</span>
            </button>
            <button class="carousel-btn next" @click="nextSlide" aria-label="Slide suivant">
                <span>&#10095;</span>
            </button>
        </div>
    </section>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, onUnmounted } from 'vue';

interface Slide {
    image: string;
    title: string;
    description: string;
    buttonText?: string;
}

export default defineComponent({
    name: 'HeroCarousel',
    setup() {
        const slides = ref<Slide[]>([
            {
                image: '\src\assets\pic\pexels-ekaterina-bolovtsova-6077381.jpg',
                title: 'Bienvenu au pays mon fils le bostwanga t\'attendait',
                description: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Deserunt animi assumenda aut.',
                buttonText: 'Découvrir'
            },
            {
                image: 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80',
                title: 'Une aventure inoubliable',
                description: 'Explorez des paysages à couper le souffle et vivez des expériences uniques.',
                buttonText: 'Explorer'
            },
            {
                image: 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80',
                title: 'Traditions et cultures',
                description: 'Plongez au cœur des traditions ancestrales et des cultures authentiques.',
                buttonText: 'En savoir plus'
            },
            {
                image: 'https://images.unsplash.com/photo-1501785888041-af3ef285b470?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80',
                title: 'Nature préservée',
                description: 'Découvrez une nature intacte et des écosystèmes préservés.',
                buttonText: 'Visiter'
            }
        ]);

        const currentSlide = ref(0);
        const interval = ref<number | null>(null);
        const autoPlayDelay = 5000; // 5 secondes

        // Fonction pour passer au slide suivant
        const nextSlide = () => {
            currentSlide.value = (currentSlide.value + 1) % slides.value.length;
        };

        // Fonction pour passer au slide précédent
        const prevSlide = () => {
            currentSlide.value = (currentSlide.value - 1 + slides.value.length) % slides.value.length;
        };

        // Fonction pour aller à un slide spécifique
        const goToSlide = (index: number) => {
            currentSlide.value = index;
            resetAutoPlay();
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
    max-width: 800px;
    animation: fadeInUp 0.8s ease-out;
}

.slide-content h2 {
    color: white;
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 1rem;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.slide-content p {
    color: white;
    font-size: 1.125rem;
    margin-bottom: 2rem;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
}

.cta-button {
    background: #FF6B35;
    color: white;
    border: none;
    padding: 0.75rem 2rem;
    font-size: 1rem;
    font-weight: 600;
    border-radius: 50px;
    cursor: pointer;
    transition: all 0.3s ease;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.cta-button:hover {
    background: #FF8B35;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(255, 107, 53, 0.4);
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
    
    .cta-button {
        padding: 1rem 2.5rem;
        font-size: 1.125rem;
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