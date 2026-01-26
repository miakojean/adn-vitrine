<template>
  <section class="services-section" id="services">
    <div class="glow-bg glow-left"></div>
    <div class="glow-bg glow-right"></div>

    <div class="container">
      <div class="header-content">
        <span class="badge">NOS SERVICES</span>
        <h2 class="title">
          Garantissons ensemble votre <br />
          <span class="highlight">sécurité</span>
        </h2>
        <p class="subtitle">
          Nous concevons des expériences digitales qui allient esthétique minimaliste
          et performance technique de pointe.
        </p>
      </div>

      <div class="cards-grid">
        <div 
          v-for="(service, index) in services" 
          :key="index"
          class="card"
          :class="service.theme"
        >
          <div class="card-top">
            <div class="icon-box">
              <component :is="service.icon" />
            </div>
            <span class="card-number">0{{ index + 1 }}</span>
          </div>

          <div class="card-body">
            <h3 class="card-title">{{ service.title }}</h3>
            <p class="card-text">{{ service.description }}</p>
            
            <div class="card-divider"></div>
            
            <ul class="features">
              <li v-for="feature in service.features" :key="feature">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="20 6 9 17 4 12"></polyline>
                </svg>
                {{ feature }}
              </li>
            </ul>
          </div>

          <button class="card-btn">
            Explore
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="5" y1="12" x2="19" y2="12"></line>
              <polyline points="12 5 19 12 12 19"></polyline>
            </svg>
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { h } from 'vue';

/**
 * Définition des icônes comme composants fonctionnels.
 * Cette méthode est 100% sécurisée contre les failles XSS car 
 * Vue traite ces éléments comme des nœuds virtuels (VNodes).
 */
const IconCreation = () => h('svg', { 
  xmlns: 'http://www.w3.org/2000/svg', 
  width: '24', 
  height: '24', 
  viewBox: '0 0 24 24', 
  fill: 'none', 
  'stroke-width': '1.5', 
  stroke: 'currentColor',
  class: 'size-6' 
}, [
  h('path', { 
    'stroke-linecap': 'round', 
    'stroke-linejoin': 'round', 
    d: 'M2.25 21h19.5m-18-18v18m10.5-18v18m6-13.5V21M6.75 6.75h.75m-.75 3h.75m-.75 3h.75m3-6h.75m-.75 3h.75m-.75 3h.75M6.75 21v-3.375c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21M3 3h12m-.75 4.5H21m-3.75 3.75h.008v.008h-.008v-.008Zm0 3h.008v.008h-.008v-.008Zm0 3h.008v.008h-.008v-.008Z' 
  })
]);

const IconAccompagnement = () => h('svg', { 
  xmlns: 'http://www.w3.org/2000/svg',
  width: '24', 
  height: '24', 
  viewBox: '0 0 24 24', 
  fill: 'none', 
  strokeWidth: '1.5',
  stroke: 'currentColor',
  class: 'size-6'
}, [
  h('path', { 
    strokeLinecap: 'round',
    strokeLinejoin: 'round',
    d: 'M14.25 6.087c0-.355.186-.676.401-.959.221-.29.349-.634.349-1.003 0-1.036-1.007-1.875-2.25-1.875s-2.25.84-2.25 1.875c0 .369.128.713.349 1.003.215.283.401.604.401.959v0a.64.64 0 0 1-.657.643 48.39 48.39 0 0 1-4.163-.3c.186 1.613.293 3.25.315 4.907a.656.656 0 0 1-.658.663v0c-.355 0-.676-.186-.959-.401a1.647 1.647 0 0 0-1.003-.349c-1.036 0-1.875 1.007-1.875 2.25s.84 2.25 1.875 2.25c.369 0 .713-.128 1.003-.349.283-.215.604-.401.959-.401v0c.31 0 .555.26.532.57a48.039 48.039 0 0 1-.642 5.056c1.518.19 3.058.309 4.616.354a.64.64 0 0 0 .657-.643v0c0-.355-.186-.676-.401-.959a1.647 1.647 0 0 1-.349-1.003c0-1.035 1.008-1.875 2.25-1.875 1.243 0 2.25.84 2.25 1.875 0 .369-.128.713-.349 1.003-.215.283-.4.604-.4.959v0c0 .333.277.599.61.58a48.1 48.1 0 0 0 5.427-.63 48.05 48.05 0 0 0 .582-4.717.532.532 0 0 0-.533-.57v0c-.355 0-.676.186-.959.401-.29.221-.634.349-1.003.349-1.035 0-1.875-1.007-1.875-2.25s.84-2.25 1.875-2.25c.37 0 .713.128 1.003.349.283.215.604.401.96.401v0a.656.656 0 0 0 .658-.663 48.422 48.422 0 0 0-.37-5.36c-1.886.342-3.81.574-5.766.689a.578.578 0 0 1-.61-.58v0Z'
  })
]);

const IconConformite = () => h('svg', { 
  xmlns: 'http://www.w3.org/2000/svg',
  width: '24', 
  height: '24', 
  viewBox: '0 0 24 24', 
  fill: 'none', 
  strokeWidth: '1.5',
  stroke: 'currentColor',
  class: 'size-6'
}, [
  h('path', { 
    strokeLinecap: 'round',
    strokeLinejoin: 'round',
    d: 'M9 12.75 11.25 15 15 9.75m-3-7.036A11.959 11.959 0 0 1 3.598 6 11.99 11.99 0 0 0 3 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285Z'
  })
]);

const services = [
  {
    title: "Création et la protection d'entreprise",
    description: "Des solutions sur mesure pour lancer et sécuriser votre entreprise.",
    theme: "theme-purple",
    icon: IconCreation,
    features: ["Constitution d'entreprises", "Dissolution d'entreprises", "Design System"]
  },
  {
    title: "Suivi et accompagnement juridique",
    description: "Nous vous accompagnons dans la gestion de vos obligations juridiques.",
    theme: "theme-blue",
    icon: IconAccompagnement,
    features: ["Rédaction de contrats", "Gestion des litiges", "Conformité réglementaire"]
  },
  {
    title: "La conformité et ressources humaines",
    description: "Nous vous aidons à respecter les normes légales et à gérer vos ressources humaines.",
    theme: "theme-pink",
    icon: IconConformite,
    features: ["Audit de conformité", "Formation en droit du travail", "Gestion des ressources humaines"]
  }
];
</script>

<style scoped>
/* Les styles restent identiques à la version précédente */
.services-section {
  position: relative;
  background-color: #0f172a;
  padding: 6rem 1.5rem 1rem 1.5rem;
  overflow: hidden;
  color: #f8fafc;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.container {
  width: 100%;
  max-width: 1280px;
  margin: 0 auto;
  position: relative;
  z-index: 2;
}

.glow-bg {
  position: absolute;
  width: 600px;
  height: 600px;
  border-radius: 50%;
  filter: blur(120px);
  opacity: 0.15;
  pointer-events: none;
  z-index: 1;
}

.glow-left { background: #3b82f6; top: -100px; left: -100px; }
.glow-right { background: #8b5cf6; bottom: -100px; right: -100px; }

.header-content {
  text-align: center;
  max-width: 700px;
  margin: 0 auto 5rem auto;
}

.badge {
  display: inline-block;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: #3b82f6;
  background: rgba(59, 130, 246, 0.1);
  padding: 8px 16px;
  border-radius: 50px;
  margin-bottom: 1.5rem;
  border: 1px solid rgba(59, 130, 246, 0.2);
}

.title {
  font-size: 3rem;
  line-height: 1.1;
  font-weight: 800;
  margin-bottom: 1.5rem;
  color: #ffffff;
}

.highlight {
  background: linear-gradient(90deg, #3b82f6, #8b5cf6);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.subtitle {
  font-size: 1.125rem;
  line-height: 1.6;
  color: #94a3b8;
}

.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
  gap: 2rem;
}

.card {
  background: rgba(30, 41, 59, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 24px;
  padding: 2.5rem;
  transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
  display: flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
  backdrop-filter: blur(10px);
}

.card:hover {
  transform: translateY(-8px);
  background: rgba(30, 41, 59, 0.6);
  box-shadow: 0 20px 40px -5px rgba(0, 0, 0, 0.3);
}

.card-top {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 2rem;
}

.icon-box {
  width: 56px;
  height: 56px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.theme-purple .icon-box { background: rgba(139, 92, 246, 0.1); color: #a78bfa; }
.theme-blue .icon-box { background: rgba(59, 130, 246, 0.1); color: #60a5fa; }
.theme-pink .icon-box { background: rgba(236, 72, 153, 0.1); color: #f472b6; }

.card-number {
  font-family: monospace;
  font-size: 1.5rem;
  font-weight: 700;
  opacity: 0.1;
  color: #ffffff;
}

.card-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 1rem;
}

.card-text {
  color: #94a3b8;
  line-height: 1.6;
  font-size: 1rem;
  margin-bottom: 2rem;
  flex-grow: 1;
}

.card-divider {
  height: 1px;
  background: rgba(255, 255, 255, 0.1);
  width: 100%;
  margin-bottom: 2rem;
}

.features {
  list-style: none;
  padding: 0;
  margin: 0 0 2rem 0;
}

.features li {
  display: flex;
  align-items: center;
  gap: 10px;
  color: #cbd5e1;
  margin-bottom: 12px;
  font-size: 0.95rem;
}

.card-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  background: transparent;
  border: none;
  font-weight: 600;
  cursor: pointer;
}

.theme-purple .card-btn, .theme-purple .features li svg { color: #a78bfa; }
.theme-blue .card-btn, .theme-blue .features li svg { color: #60a5fa; }
.theme-pink .card-btn, .theme-pink .features li svg { color: #f472b6; }
</style>