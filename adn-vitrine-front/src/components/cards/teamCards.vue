<template>
  <article class="talent-card">
    <div class="card-glow"></div>

    <div class="image-wrapper">
      <img :src="picUrl" :alt="name" class="profile-pic" loading="lazy">
      <div class="image-overlay"></div>
      
      <div class="role-badge">{{ role }}</div>
    </div>

    <div class="content-box">
      <div class="info-header">
        <h3 class="name">{{ name }}</h3>
        <div class="divider"></div>
      </div>

      <!-- 
        <div class="social-wrapper">
          <a href="#" class="social-link" aria-label="LinkedIn">
            <component :is="IconLinkedin" />
          </a>
          <a href="#" class="social-link" aria-label="Twitter">
            <component :is="IconTwitter" />
          </a>
          <a href="#" class="social-link" aria-label="Facebook">
            <component :is="IconFacebook" />
          </a>
        </div>
      -->
      
    </div>
  </article>
</template>

<script setup lang="ts">

// Props avec TypeScript (Syntaxe Script Setup recommandée)
interface Props {
  name?: string;
  role?: string;
  picUrl?: string;
}

withDefaults(defineProps<Props>(), {
  name: 'John Doe',
  role: 'Senior Developer',
  picUrl: 'https://picsum.photos/800/800' // Format carré recommandé pour ce design
});

</script>

<style scoped>
.talent-card {
  position: relative;
  width: 100%;
  max-width: 300px;
  max-height: 500px;
  background: rgba(30, 41, 59, 0.5);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 24px;
  overflow: hidden;
  transition: all 0.5s cubic-bezier(0.23, 1, 0.32, 1);
  backdrop-filter: blur(12px);
}

/* Effet de lueur au survol */
.card-glow {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle at 50% 0%, rgba(59, 130, 246, 0.15), transparent 70%);
  opacity: 0;
  transition: opacity 0.5s ease;
}

.talent-card:hover {
  transform: translateY(-12px);
  border-color: rgba(59, 130, 246, 0.3);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
}

.talent-card:hover .card-glow {
  opacity: 1;
}

/* Container Image */
.image-wrapper {
  position: relative;
  width: 100%;
  aspect-ratio: 1 / 1.1;
  overflow: hidden;
}

.profile-pic {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.7s ease;
}

.talent-card:hover .profile-pic {
  transform: scale(1.08);
}

.image-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to bottom, transparent 60%, #0f172a 100%);
}

.role-badge {
  position: absolute;
  bottom: 20px;
  left: 20px;
  background: rgba(59, 130, 246, 0.2);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(59, 130, 246, 0.3);
  color: #60a5fa;
  padding: 6px 14px;
  border-radius: 50px;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 1px;
  text-transform: uppercase;
}

/* Contenu Texte */
.content-box {
  padding: 1.5rem 2rem 2rem 2rem;
  text-align: center;
}

.name {
  font-size: 1.5rem;
  font-weight: 800;
  color: #ffffff;
  margin: 0;
  letter-spacing: -0.02em;
}

.divider {
  height: 2px;
  width: 40px;
  background: #3b82f6;
  margin: 12px auto;
  border-radius: 2px;
  transition: width 0.3s ease;
}

.talent-card:hover .divider {
  width: 80px;
}

/* Réseaux Sociaux */
.social-wrapper {
  display: flex;
  justify-content: center;
  gap: 1.25rem;
  margin-top: 1.5rem;
}

.social-link {
  color: #94a3b8;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.social-link:hover {
  color: #ffffff;
  transform: translateY(-3px);
}
</style>