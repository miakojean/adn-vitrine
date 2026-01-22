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

      <!-- Section des accordéons -->
      <div class="accordion-container">
        <div 
          v-for="(service, index) in services" 
          :key="index"
          class="accordion"
          :class="[service.theme, { active: activeAccordion === index }]"
        >
          <button 
            class="accordion-header"
            @click="toggleAccordion(index)"
          >
            <div class="accordion-header-content">
              <div class="accordion-icon">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 21h19.5m-18-18v18m10.5-18v18m6-13.5V21M6.75 6.75h.75m-.75 3h.75m-.75 3h.75m3-6h.75m-.75 3h.75m-.75 3h.75M6.75 21v-3.375c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21M3 3h12m-.75 4.5H21m-3.75 3.75h.008v.008h-.008v-.008Zm0 3h.008v.008h-.008v-.008Zm0 3h.008v.008h-.008v-.008Z" />
                </svg>
              </div>
              <h3 class="accordion-title">{{ service.title }}</h3>
            </div>
            <div class="accordion-indicator">
              <span class="accordion-number">0{{ index + 1 }}</span>
              <svg 
                class="accordion-arrow" 
                width="20" 
                height="20" 
                viewBox="0 0 24 24" 
                fill="none" 
                stroke="currentColor" 
                stroke-width="2"
              >
                <path d="M6 9l6 6 6-6" />
              </svg>
            </div>
          </button>
          
          <div class="accordion-content">
            <div class="accordion-body">
              <p class="accordion-description">{{ service.description }}</p>
              
              <div class="accordion-features">
                <h4 class="features-title">Ce que nous proposons :</h4>
                <ul class="features-list">
                  <li v-for="(feature, featureIndex) in service.features" :key="featureIndex">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    {{ feature }}
                  </li>
                </ul>
              </div>
              
              <mainButton label="besoin d'un service" type="button" class="accordion-action-btn"/>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import mainButton from '../button/mainButton.vue';

// Composants SVG définis proprement


const activeAccordion = ref<number | null>(0);

const toggleAccordion = (index: number) => {
  activeAccordion.value = activeAccordion.value === index ? null : index;
};

const services = [
  {
    title: "Création et la protection d'entreprise",
    description: "Des solutions sur mesure pour lancer et sécuriser votre entreprise.",
    theme: "theme-purple",
    features: ["Constitution d'entreprises", "Dissolution d'entreprises", "Diagnostic juridique", "Propriété intellectuelle", "etc."]
  },
  {
    title: "Suivi et accompagnement juridique",
    description: "Au cas où vous disposeriez d'une entreprise, nous vous accompagnons dans la gestion de vos obligations juridiques.",
    theme: "theme-blue",
    features: ["Accompagnement","Rédaction de contrats", "Gestion des litiges", "Conformité réglementaire", "etc."]
  },
  {
    title: "La conformité et ressources humaines",
    description: "Nous vous aidons à respecter les normes légales et à gérer vos ressources humaines.",
    theme: "theme-pink",
    features: [
      "Audit de conformité", 
      "Formation en droit du travail", 
      "Gestion des ressources humaines", 
      "Mise en conformité de site web",
      "Pack spécial RH"
    ]
  }
];
</script>

<style scoped>
.services-section {
  position: relative;
  background-color: #0f172a;
  padding: 6rem 1.5rem;
  overflow: hidden;
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

/* Styles des accordéons */
.accordion-container {
  max-width: 900px;
  margin: 0 auto;
}

.accordion {
  background: rgba(30, 41, 59, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 20px;
  margin-bottom: 1.5rem;
  overflow: hidden;
  transition: all 0.3s ease;
  backdrop-filter: blur(10px);
}

.accordion.active {
  background: rgba(30, 41, 59, 0.6);
}

.accordion-header {
  width: 100%;
  padding: 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: transparent;
  border: none;
  color: #ffffff;
  cursor: pointer;
  text-align: left;
  transition: background-color 0.3s ease;
}

.accordion-header:hover {
  background: rgba(255, 255, 255, 0.02);
}

.accordion-header-content {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.accordion-icon {
  width: 56px;
  height: 56px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.theme-purple .accordion-icon {
  background: rgba(139, 92, 246, 0.1);
  color: #a78bfa;
}

.theme-blue .accordion-icon {
  background: rgba(59, 130, 246, 0.1);
  color: #60a5fa;
}

.theme-pink .accordion-icon {
  background: rgba(236, 72, 153, 0.1);
  color: #f472b6;
}

.accordion-title {
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0;
}

.accordion-indicator {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.accordion-number {
  font-family: monospace;
  font-size: 1.25rem;
  font-weight: 700;
  opacity: 0.3;
  color: #ffffff;
}

.accordion-arrow {
  transition: transform 0.3s ease;
}

.accordion.active .accordion-arrow {
  transform: rotate(180deg);
}

.accordion-content {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.4s ease;
}

.accordion.active .accordion-content {
  max-height: 500px;
}

.accordion-body {
  padding: 0 2rem 2rem 2rem;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
}

.accordion-description {
  color: #94a3b8;
  line-height: 1.6;
  margin-bottom: 2rem;
  font-size: 1.05rem;
}

.accordion-features {
  margin-bottom: 2rem;
}

.features-title {
  color: #ffffff;
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.features-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: grid;
  gap: 0.75rem;
}

.features-list li {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  color: #cbd5e1;
  font-size: 0.95rem;
}

.features-list li svg {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}

.theme-purple .features-list li svg {
  color: #a78bfa;
}

.theme-blue .features-list li svg {
  color: #60a5fa;
}

.theme-pink .features-list li svg {
  color: #f472b6;
}

/* Styles pour le bouton personnalisé */
.accordion-action-btn {
  margin-top: 1rem;
}

/* Responsive */
@media (max-width: 768px) {
  .services-section {
    padding: 4rem 1rem;
  }

  .title {
    font-size: 2.25rem;
  }

  .accordion-header {
    padding: 1.5rem;
  }

  .accordion-header-content {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }

  .accordion-title {
    font-size: 1.25rem;
  }

  .accordion-body {
    padding: 0 1.5rem 1.5rem 1.5rem;
  }

  .accordion-number {
    display: none;
  }
}
</style>