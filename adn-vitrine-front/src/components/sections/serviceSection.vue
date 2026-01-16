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

      <!-- On va améliorer cette section -->

      <div class="cards-grid">
        <div 
          v-for="(service, index) in services" 
          :key="index"
          class="card"
          :class="service.theme"
        >
          <div class="card-top">
            <div class="icon-box">
              <span v-html="service.icon"></span>
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
import mainButton from '../button/mainButton.vue';

const services = [
  {
    title: "Création et la protection d'entreprise",
    description: "Des solutions sur mesure pour lancer et sécuriser votre entreprise.",
    theme: "theme-purple",
    icon: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19l7-7 3 3-7 7-3-3z"></path><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"></path><path d="M2 2l7.586 7.586"></path><circle cx="11" cy="11" r="2"></circle></svg>`,
    features: ["Constitution d'entreprises", "Dissolution d'entreprises", "Design System"]
  },
  {
    title: "Suivi et accompagnement juridique",
    description: "Au cas où vous disposeriez d'une entreprise, nous vous accompagnons dans la gestion de vos obligations juridiques.",
    theme: "theme-blue",
    icon: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>`,
    features: ["Rédaction de contrats", "Gestion des litiges", "Conformité réglementaire"]
  },
  {
    title: "La conformité et ressources humaines",
    description: "Nous vous aidons à respecter les normes légales et à gérer vos ressources humaines.",
    theme: "theme-pink",
    icon: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path></svg>`,
    features: ["Audit de conformité", "Formation en droit du travail", "Gestion des ressources humaines"]
  }
];
</script>

<style scoped>
/* NOTE: Aucune variable CSS (var(--)) n'est utilisée ici.
  Toutes les couleurs sont en Hex ou RGBA.
*/

.services-section {
  position: relative;
  background-color: #0f172a; /* Dark slate background */
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

/* --- Background Glows --- */
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

.glow-left {
  background: #3b82f6;
  top: -100px;
  left: -100px;
}

.glow-right {
  background: #8b5cf6;
  bottom: -100px;
  right: -100px;
}

/* --- Header --- */
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
  color: #94a3b8; /* Slate 400 */
}

/* --- Grid --- */
.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
  gap: 2rem;
}

/* --- Card Base Styles --- */
.card {
  background: rgba(30, 41, 59, 0.4); /* Glass effect */
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

/* Theme specifics styling manually applied */
.card.theme-purple:hover { border-color: rgba(139, 92, 246, 0.5); }
.card.theme-blue:hover { border-color: rgba(59, 130, 246, 0.5); }
.card.theme-pink:hover { border-color: rgba(236, 72, 153, 0.5); }

/* --- Card Header --- */
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
  transition: transform 0.3s ease;
}

.card:hover .icon-box {
  transform: scale(1.1) rotate(3deg);
}

/* Icon Colors Hardcoded */
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

/* --- Card Body --- */
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

/* --- Features List --- */
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

.theme-purple .features li svg { color: #a78bfa; }
.theme-blue .features li svg { color: #60a5fa; }
.theme-pink .features li svg { color: #f472b6; }

/* --- Button --- */
.card-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  background: transparent;
  border: none;
  color: #ffffff;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  padding: 0;
  margin-top: auto;
  transition: gap 0.3s ease;
}

.card-btn:hover {
  gap: 12px;
}

.theme-purple .card-btn { color: #a78bfa; }
.theme-blue .card-btn { color: #60a5fa; }
.theme-pink .card-btn { color: #f472b6; }

/* --- Responsive --- */
@media (max-width: 768px) {
  .services-section {
    padding: 4rem 1rem;
  }

  .title {
    font-size: 2.25rem;
  }
  
  .cards-grid {
    grid-template-columns: 1fr;
  }
}
</style>