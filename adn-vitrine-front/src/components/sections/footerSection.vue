<template>
    <footer class="footer-section">
        <div class="container">
            <div class="footer-main">
                <!-- Logo & Description -->
                <div class="footer-brand">
                    <div class="brand-logo">
                        <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
                            <rect width="32" height="32" rx="6" fill="#3B82F6"/>
                            <path d="M10 16L14 20L22 12" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                        <span class="brand-name">Nexus</span>
                    </div>
                    <p class="brand-description">
                        Créateurs d'expériences digitales exceptionnelles.
                    </p>
                </div>

                <!-- Quick Links -->
                <div class="footer-links">
                    <div class="links-group">
                        <h3 class="links-title">Services</h3>
                        <ul class="links-list">
                            <li><a href="#services" class="footer-link">Développement Web</a></li>
                            <li><a href="#services" class="footer-link">Design UI/UX</a></li>
                            <li><a href="#services" class="footer-link">Applications Mobile</a></li>
                        </ul>
                    </div>
                    
                    <div class="links-group">
                        <h3 class="links-title">Entreprise</h3>
                        <ul class="links-list">
                            <li><a href="/about" class="footer-link">À propos</a></li>
                            <li><a href="/team" class="footer-link">Équipe</a></li>
                            <li><a href="/careers" class="footer-link">Carrières</a></li>
                        </ul>
                    </div>
                    
                    <div class="links-group">
                        <h3 class="links-title">Contact</h3>
                        <ul class="links-list">
                            <li><a href="mailto:contact@nexus.com" class="footer-link">contact@nexus.com</a></li>
                            <li><a href="tel:+33123456789" class="footer-link">+33 1 23 45 67 89</a></li>
                            <li class="footer-link">Paris, France</li>
                        </ul>
                    </div>
                </div>

                <!-- Social Links -->
                <div class="social-section">
                    <h3 class="social-title">Suivez-nous</h3>
                    <div class="social-links">
                        <a href="https://twitter.com" class="social-link" target="_blank" aria-label="Twitter">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                                <path d="M22 4.01C21 4.5 20.02 4.69 19 5C17.879 3.735 16.217 3.665 15 4.5C13.879 5.335 13.5 6.5 14 8C10 7.5 7 5.5 4 2C4 2 1 8 8 11C6 12 4 12 2 11C2 16 6.5 19.5 12 19.5C17.5 19.5 21.5 15.5 21.5 10C21.5 9.5 21.5 9 21.4 8.5C22.338 7.735 23 6.5 23 5C23 4.5 22.5 4 22 4.01Z" fill="currentColor"/>
                            </svg>
                        </a>
                        <a href="https://linkedin.com" class="social-link" target="_blank" aria-label="LinkedIn">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                                <path d="M16 8C17.5913 8 19.1174 8.63214 20.2426 9.75736C21.3679 10.8826 22 12.4087 22 14V21H18V14C18 13.4696 17.7893 12.9609 17.4142 12.5858C17.0391 12.2107 16.5304 12 16 12C15.4696 12 14.9609 12.2107 14.5858 12.5858C14.2107 12.9609 14 13.4696 14 14V21H10V14C10 12.4087 10.6321 10.8826 11.7574 9.75736C12.8826 8.63214 14.4087 8 16 8Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                <path d="M6 9H2V21H6V9Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                <path d="M4 6C5.10457 6 6 5.10457 6 4C6 2.89543 5.10457 2 4 2C2.89543 2 2 2.89543 2 4C2 5.10457 2.89543 6 4 6Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </a>
                        <a href="https://github.com" class="social-link" target="_blank" aria-label="GitHub">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                                <path d="M12 2C6.477 2 2 6.477 2 12C2 16.418 5.578 20 10 21C10.5 21.083 10.75 20.75 10.75 20.438C10.75 20.125 10.729 19.5 10.729 18.875C7.999 19.438 7.25 18.125 7.125 17.562C7 17.312 6.625 16.562 6.125 16.375C5.75 16.188 5.125 15.75 6.125 15.75C7.125 15.75 7.688 16.688 7.875 17.062C8.5 18.375 9.625 18 10.75 17.75C10.875 17.125 11.188 16.688 11.5 16.438C8.875 16.188 6.125 15.312 6.125 11.438C6.125 10.313 6.5 9.375 7.125 8.625C7 8.375 6.625 7.375 7.25 6.125C7.25 6.125 8.125 5.875 10.75 7.375C11.875 7.062 13 7 14.125 7.062C15.25 7 16.375 7.062 17.5 7.375C20.125 5.875 21 6.125 21 6.125C21.625 7.375 21.25 8.375 21.125 8.625C21.75 9.375 22.125 10.313 22.125 11.438C22.125 15.312 19.375 16.188 16.75 16.438C17.125 16.75 17.5 17.312 17.5 18.25C17.5 19.625 17.5 20.75 17.5 20.438C17.5 20.75 17.75 21.083 18.25 21C22.422 20 26 16.418 26 12C26 6.477 21.523 2 16 2H12Z" fill="currentColor"/>
                            </svg>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Divider -->
            <div class="footer-divider"></div>

            <!-- Bottom Section -->
            <div class="footer-bottom">
                <div class="copyright">
                    © {{ new Date().getFullYear() }} Nexus. Tous droits réservés.
                </div>
                <div class="legal-links">
                    <a href="/legal" class="legal-link">Mentions légales</a>
                    <a href="/privacy" class="legal-link">Confidentialité</a>
                    <a href="/terms" class="legal-link">Conditions</a>
                </div>
            </div>
        </div>
    </footer>
</template>

<script setup lang="ts"></script>

<style scoped>
/* === VARIABLES === */
:root {
    --footer-bg: #0f172a;
    --footer-text: #f8fafc;
    --footer-text-muted: #94a3b8;
    --footer-primary: #3b82f6;
    --footer-border: rgba(255, 255, 255, 0.1);
}

/* === BASE STYLES === */
.footer-section {
    background: var(--footer-bg);
    color: var(--footer-text);
    padding: 4rem 1rem 2rem;
    border-top: 1px solid var(--footer-border);
}

.container {
    max-width: 1280px;
    margin: 0 auto;
}

/* === MAIN SECTION === */
.footer-main {
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;
    gap: 3rem;
    margin-bottom: 3rem;
}

/* Brand Section */
.footer-brand {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.brand-logo {
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.brand-name {
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--footer-text);
}

.brand-description {
    color: var(--footer-text-muted);
    line-height: 1.5;
    font-size: 0.9rem;
    margin: 0;
}

/* Links Section */
.footer-links {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
}

.links-group {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.links-title {
    font-size: 0.875rem;
    font-weight: 600;
    color: var(--footer-text);
    margin: 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.links-list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.footer-link {
    color: var(--footer-text-muted);
    text-decoration: none;
    font-size: 0.9rem;
    line-height: 1.4;
}

.footer-link:hover {
    color: var(--footer-primary);
}

/* Social Section */
.social-section {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.social-title {
    font-size: 0.875rem;
    font-weight: 600;
    color: var(--footer-text);
    margin: 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.social-links {
    display: flex;
    gap: 1rem;
}

.social-link {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 36px;
    height: 36px;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 8px;
    color: var(--footer-text-muted);
}

.social-link:hover {
    background: rgba(255, 255, 255, 0.1);
    color: var(--footer-primary);
}

/* Divider */
.footer-divider {
    height: 1px;
    background: var(--footer-border);
    margin: 2rem 0;
}

/* === BOTTOM SECTION === */
.footer-bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 1rem;
}

.copyright {
    color: var(--footer-text-muted);
    font-size: 0.85rem;
}

.legal-links {
    display: flex;
    gap: 1.5rem;
}

.legal-link {
    color: var(--footer-text-muted);
    text-decoration: none;
    font-size: 0.85rem;
}

.legal-link:hover {
    color: var(--footer-primary);
}

/* === RESPONSIVE === */
@media (max-width: 768px) {
    .footer-main {
        grid-template-columns: 1fr;
        gap: 2rem;
    }
    
    .footer-links {
        grid-template-columns: repeat(2, 1fr);
        gap: 1.5rem;
    }
    
    .footer-bottom {
        flex-direction: column;
        text-align: center;
        gap: 1rem;
    }
    
    .legal-links {
        justify-content: center;
    }
}

@media (max-width: 480px) {
    .footer-section {
        padding: 3rem 1rem 1.5rem;
    }
    
    .footer-links {
        grid-template-columns: 1fr;
    }
}
</style>