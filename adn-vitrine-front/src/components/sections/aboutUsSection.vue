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
      <mainButton 
        label="Nos services" 
        type="button" 
        class="mt-4" 
        @click="() => router.push('/services')"
      />
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
            <button 
                class="nav-btn prev" 
                @click="scrollPrev" 
                aria-label="Précédent" 
                :disabled="currentIndex === 0"
            >
                <svg viewBox="0 0 24 24" width="24" height="24"><path fill="currentColor" d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/></svg>
            </button>

        <div class="carousel__container" ref="carouselRef" @scroll="handleScroll">
          <teamCards 
            v-for="member in teamMembers" 
            :key="member.name" 
            class="carousel__item" 
            :name="member.name" 
            :role="member.role"
            :picUrl="member.pictureUrl"
          />
        </div>

        <button 
          class="nav-btn next" 
          @click="scrollNext" 
          aria-label="Suivant" 
          :disabled="currentIndex >= teamMembers.length - itemsPerView"
        >
          <svg viewBox="0 0 24 24" width="24" height="24"><path fill="currentColor" d="M8.59 16.59L10 18l6-6-6-6-1.41 1.41L13.17 12z"/></svg>
        </button>
        </div>
      
      <div class="carousel__indicators">
        <div class="indicator-track">
          <div 
            class="indicator-bar" 
            :style="{
              width: `${indicatorWidth}%`,
              transform: `translateX(${indicatorPosition}%)`
            }"
          ></div>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent, ref, computed, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';
import mainButton from '../button/mainButton.vue';
import divider from '../tools/divider.vue';
import teamCards from '../cards/teamCards.vue';

// Pictures import
import pic1 from '../../assets/memberPic/PHOTO MME ANGE DESIRE NIOULE.jpg'
import pic2 from '../../assets/memberPic/grâce_nioule.jpeg'
import pic3 from '../../assets/memberPic/monsieur_roch.jpeg'
import pic4 from '../../assets/memberPic/malaro.jpeg'
import pic5 from '../../assets/memberPic/tosseta.jpeg'
import pic6 from '../../assets/memberPic/IMG_9088.jpeg'

interface Member {
  id?: number;
  name: string;
  pictureUrl?: string;
  role: string;
  bio: string;
}

export default defineComponent({
  name: 'AboutUsSection',
  components: { mainButton, divider, teamCards },
  setup() {
    const router = useRouter(); // Correction syntaxique : exécution de la fonction
    const carouselRef = ref<HTMLElement | null>(null);
    const currentIndex = ref(0);
    const itemsPerView = ref(1);
    const scrollDebounce = ref<ReturnType<typeof setTimeout> | null>(null);
    
    const statistics = [
      { number: '1000+', label: 'Entreprises accompagnées' },
      { number: '1700+', label: 'Documents rédigés' },
      { number: '20+', label: 'Pays clients' },
      { number: '03', label: 'Filiales' },
      { number: '8+', label: "Années d'expérience" },
      { number: '1', label: 'Legaltech' }
    ];

    const teamMembers: Member[] = [
      { name: 'Ange Désiré NIOULE', pictureUrl: pic1, role: 'fondatrice & CEO', bio: '...' },
      { name: 'Emlice KPANDJO', pictureUrl: pic1, role: 'Directrice juridique', bio: '...' },
      { name: 'Rushdan BACHABI', pictureUrl: pic3, role: 'Directeur des innovations', bio: '...' },
      { name: 'Tosseta DOH', pictureUrl: pic5, role: 'Legal Marketing Officer', bio: '...' },
      { name: 'Josué KOFFI', pictureUrl: pic6, role: 'Legal Sales officer', bio: '...' },
      { name: 'Nathanael NESSON', pictureUrl: pic1, role: 'Graphiste Designer', bio: '...' },
      { name: 'Malaro DJANE', pictureUrl: pic4, role: 'Assistante Administrative et Executive', bio: '...' },
      { name: 'Grâce NIOULE', pictureUrl: pic2, role: 'Community Manager', bio: '...' },
      { name: 'Jean Yves MIAKO', pictureUrl: pic1, role: 'Développeur full stack', bio: '...' },
      { name:'Assi ELOU Hervé', pictureUrl: pic1, role: 'Legal ops', bio: '...' },
    ];

    // Calculs pour le carrousel
    const visibleDots = computed(() => Math.ceil(teamMembers.length / itemsPerView.value));
    const indicatorWidth = computed(() => 100 / visibleDots.value);
    const indicatorPosition = computed(() => {
      const slideGroup = Math.floor(currentIndex.value / itemsPerView.value);
      return slideGroup * 100;
    });

    const updateCurrentIndex = () => {
      if (!carouselRef.value) return;
      const scrollLeft = carouselRef.value.scrollLeft;
      const cardWidth = carouselRef.value.offsetWidth / itemsPerView.value;
      const newIndex = Math.round(scrollLeft / cardWidth);
      currentIndex.value = Math.max(0, Math.min(newIndex, teamMembers.length - itemsPerView.value));
    };

    const handleScroll = () => {
      if (scrollDebounce.value) clearTimeout(scrollDebounce.value);
      scrollDebounce.value = setTimeout(updateCurrentIndex, 100);
    };

    const scrollNext = () => {
      if (carouselRef.value) {
        carouselRef.value.scrollBy({ left: carouselRef.value.clientWidth, behavior: 'smooth' });
      }
    };

    const scrollPrev = () => {
      if (carouselRef.value) {
        carouselRef.value.scrollBy({ left: -carouselRef.value.clientWidth, behavior: 'smooth' });
      }
    };

    const updateItemsPerView = () => {
      const width = window.innerWidth;
      if (width >= 1024) itemsPerView.value = 3;
      else if (width >= 768) itemsPerView.value = 2;
      else itemsPerView.value = 1;
    };

    onMounted(() => {
      updateItemsPerView();
      window.addEventListener('resize', updateItemsPerView);
    });

    onUnmounted(() => {
      window.removeEventListener('resize', updateItemsPerView);
      if (scrollDebounce.value) clearTimeout(scrollDebounce.value);
    });

    return { 
      router, 
      statistics, 
      carouselRef, 
      currentIndex,
      itemsPerView,
      indicatorWidth,
      indicatorPosition,
      scrollNext, 
      scrollPrev,
      handleScroll,
      teamMembers 
    };
  }
});
</script>

<style scoped>
.about__section {
    width: 100%;
    padding: 8rem 2rem 1rem 2rem;
    background-color: #0f172a;
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
    color: #c3d8f4;
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
    width: 100vw;
    max-width: 1200px;
    padding: 0 20px;
}

.carousel__container {
    display: flex;
    gap: 24px;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    scrollbar-width: none;
    padding: 20px 0;
    -webkit-overflow-scrolling: touch;
    scroll-behavior: smooth;
}

.carousel__container::-webkit-scrollbar {
    display: none;
}

.carousel__item {
    flex: 0 0 calc(85% - 12px);
    scroll-snap-align: center;
    transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    opacity: 1;
}

/* Navigation Arrows */
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

.nav-btn:hover:not(:disabled) { 
    background: #2563eb; 
    transform: translateY(-50%) scale(1.1); 
}

.nav-btn:disabled {
    background: #64748b;
    cursor: not-allowed;
    opacity: 0.5;
}

.nav-btn.prev { left: -25px; }
.nav-btn.next { right: -25px; }

/* Indicateurs dynamiques */
.carousel__indicators {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 12px;
    margin-top: 20px;
    width: 100%;
    max-width: 300px;
}

.indicator-track {
    width: 100%;
    height: 4px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 2px;
    position: relative;
    overflow: hidden;
}

.indicator-bar {
    position: absolute;
    height: 100%;
    background: #3b82f6;
    border-radius: 2px;
    transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.indicator-dots {
    display: flex;
    gap: 8px;
    justify-content: center;
}

.indicator-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.2);
    border: none;
    cursor: pointer;
    padding: 0;
    transition: all 0.3s ease;
    position: relative;
}

.indicator-dot:hover {
    background: rgba(59, 130, 246, 0.5);
    transform: scale(1.2);
}

.indicator-dot.active {
    background: #3b82f6;
    transform: scale(1.2);
}

.indicator-dot.active::after {
    content: '';
    position: absolute;
    top: -3px;
    left: -3px;
    right: -3px;
    bottom: -3px;
    border: 1px solid #3b82f6;
    border-radius: 50%;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 0.7; }
    50% { opacity: 0.3; }
}

/* Accessibilité */
.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;
}

/* Responsive Desktop */
@media (min-width: 768px) {
    .carousel__item {
        flex: 0 0 calc(50% - 12px);
    }
    
    .nav-btn {
        display: flex;
    }
}

@media (min-width: 1024px) {
    .carousel__item {
        flex: 0 0 calc(33.333% - 16px);
    }
    
    .carousel__wrapper {
        overflow: visible;
    }
}

/* Animation pour le défilement fluide */
@media (prefers-reduced-motion: reduce) {
    .carousel__container,
    .carousel__item,
    .indicator-bar,
    .indicator-dot {
        transition: none;
    }
}
</style>