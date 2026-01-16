<template>
    <section class="about__section" id="about">
        <div class="main__description">
            <h2 class="section__title">Qui sommes-nous?</h2>
            <divider 
                direction="horizontal" 
                size="small" 
                :color-start="'#3b82f6'" 
                :color-middle="'#1e293b'" 
                :color-end="'#1e293b'" 
                gradient-angle="90deg" 
                :margin="'1.5rem 0'"
            />
            <p>
                Depuis sa création, le Cabinet ADN Consulting SAS
                s'est donné pour mission de faire en sorte que dans 
                toutes les actions et engagements, les entrepreneurs, 
                les PMEs et startups voient leurs intérêts grandement 
                protégés et grandissent sainement.
            </p>
            <mainButton label="Nos services" type="button" class="mt-4"/>
        </div>

        <div class="about__statistic flex flex-col justify-center items-center mt-16 gap-8 w-full">
            <h3 class="text-3xl font-bold text-white">ADN Consulting c'est</h3>
            
            <div class="stats__image-container">
                <img src="../../assets/pic/pexels-roboseal34-35457179.jpg" alt="ADN Consulting Office" class="stats__img">
                <div class="stats__overlay"></div>
            </div>

            <div class="stats__grid">
                <div v-for="(stat, index) in statistics" :key="index" class="stat__card">
                    <h3 class="stat__number">{{ stat.number }}</h3>
                    <p class="stat__label">{{ stat.label }}</p>
                </div>
            </div>
        </div>

        <div class="about__team w-full flex flex-col justify-center items-center gap-8 mt-20">
            <div class="team__header text-center">
                <h3 class="text-4xl font-bold text-white">Notre équipe</h3>
                <p class="mt-4 text-gray-400 max-w-2xl">
                    Des professionnels passionnés et dévoués, spécialisés dans divers domaines du droit et de la technologie.
                </p>
            </div>

            <div class="carousel__wrapper">
                <button class="nav-btn prev" @click="scrollPrev" aria-label="Précédent">
                    <svg viewBox="0 0 24 24" width="24" height="24"><path fill="currentColor" d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/></svg>
                </button>

                <div class="carousel__container" ref="carouselRef">
                    <teamCards v-for="n in 6" :key="n" class="carousel__item" />
                </div>

                <button class="nav-btn next" @click="scrollNext" aria-label="Suivant">
                    <svg viewBox="0 0 24 24" width="24" height="24"><path fill="currentColor" d="M8.59 16.59L10 18l6-6-6-6-1.41 1.41L13.17 12z"/></svg>
                </button>
            </div>
            
            <div class="carousel__indicators">
                <div class="indicator-bar"></div>
            </div>
        </div>
    </section>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import mainButton from '../button/mainButton.vue';
import divider from '../tools/divider.vue';
import teamCards from '../cards/teamCards.vue';

export default defineComponent({
    name: 'AboutUsSection',
    components: { mainButton, divider, teamCards },
    setup() {
        const carouselRef = ref<HTMLElement | null>(null);
        const statistics = [
            { number: '1000+', label: 'Entreprises accompagnées' },
            { number: '1700+', label: 'Documents rédigés' },
            { number: '20+', label: 'Pays clients' },
            { number: '03', label: 'Filiales' },
            { number: '8+', label: "Années d'expérience" },
            { number: '1', label: 'Legaltech' }
        ];

        const scrollNext = () => {
            if (carouselRef.value) {
                carouselRef.value.scrollBy({ left: 350, behavior: 'smooth' });
            }
        };

        const scrollPrev = () => {
            if (carouselRef.value) {
                carouselRef.value.scrollBy({ left: -350, behavior: 'smooth' });
            }
        };

        return { statistics, carouselRef, scrollNext, scrollPrev };
    }
});
</script>

<style scoped>
.about__section {
    width: 100%;
    padding: 8rem 2rem 1rem 2rem;
    background-color: #0f172a; /* Fond sombre profond pour le contraste */
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 2rem;
}

/* --- Description --- */
.main__description {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    width: 100%;
    max-width: 800px;
    text-align: center;
}

.section__title {
    font-size: clamp(2rem, 5vw, 3rem);
    font-weight: 800;
    color: white;
    letter-spacing: -1px;
}

.main__description p {
    font-size: 1.1rem;
    color: #94a3b8;
    line-height: 1.8;
    text-align: center;
}

/* --- Statistiques Style Premium --- */
.stats__image-container {
    position: relative;
    width: 100%;
    max-width: 900px;
    border-radius: 24px;
    overflow: hidden;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
}

.stats__img {
    width: 100%;
    height: 400px;
    object-fit: cover;
    transition: transform 0.5s ease;
}

.stats__image-container:hover .stats__img {
    transform: scale(1.05);
}

.stats__grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 2rem;
    width: 100%;
    max-width: 1100px;
    margin-top: 3rem;
}

.stat__card {
    padding: 1.5rem;
    border-radius: 16px;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.05);
    transition: all 0.3s ease;
}

.stat__card:hover {
    background: rgba(59, 130, 246, 0.1);
    border-color: #3b82f6;
    transform: translateY(-5px);
}

.stat__number {
    font-size: 2.5rem;
    font-weight: 800;
    color: #3b82f6;
    margin-bottom: 0.5rem;
}

.stat__label {
    font-size: 0.9rem;
    color: #cbd5e1;
    font-weight: 500;
}

/* --- Carrousel Logic --- */
.carousel__wrapper {
    position: relative;
    width: 100vw; /* Bord à bord sur mobile */
    max-width: 1200px;
    padding: 0 20px;
}

.carousel__container {
    display: flex;
    gap: 24px;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    scrollbar-width: none; /* Firefox */
    padding: 20px 0;
    -webkit-overflow-scrolling: touch;
}

.carousel__container::-webkit-scrollbar {
    display: none; /* Chrome/Safari */
}

.carousel__item {
    flex: 0 0 85%; /* Mobile peek-a-boo */
    scroll-snap-align: center;
    transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Navigation Arrows (Cachées sur mobile) */
.nav-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: #3b82f6;
    color: white;
    border: none;
    cursor: pointer;
    display: none;
    align-items: center;
    justify-content: center;
    z-index: 10;
    box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    transition: all 0.3s ease;
}

.nav-btn:hover { background: #2563eb; transform: translateY(-50%) scale(1.1); }
.nav-btn.prev { left: -25px; }
.nav-btn.next { right: -25px; }

/* Responsive Desktop */
@media (min-width: 1024px) {
    .carousel__item {
        flex: 0 0 calc(33.333% - 16px);
        scroll-snap-align: start;
    }
    .nav-btn {
        display: flex;
    }
    .carousel__wrapper {
        overflow: visible;
    }
}

/* Indicateur de scroll minimaliste pour mobile */
.carousel__indicators {
    width: 100px;
    height: 4px;
    background: rgba(255,255,255,0.1);
    border-radius: 2px;
    position: relative;
    margin-top: 10px;
}

.indicator-bar {
    width: 40%;
    height: 100%;
    background: #3b82f6;
    border-radius: 2px;
}
</style>