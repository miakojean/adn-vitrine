<template>
    <footer class="footer-section">
        <div class="container">
            <div class="footer-main">
                <!-- Logo & Description -->
                <div class="footer-brand">
                    <div class="brand-logo">
                        <img src="/LOGO ROND.png" alt="logo d'adn" class="footer__logo">
                        <span class="brand-name">ADN Consuting sas</span>
                    </div>
                    <p class="brand-description">
                        Sécurisez juridiquement votre business.
                    </p>
                </div>

                <!-- Quick Links -->
                <div class="footer-links">
                    <div class="links-group">
                        <h3 class="links-title">Services</h3>
                        <ul class="links-list">
                            <li><a href="#services" class="footer-link">Création et protection d'entreprises</a></li>
                            <li><a href="#services" class="footer-link">Suivi et accompagnement juridique</a></li>
                            <li><a href="#services" class="footer-link">Conformité et ressources humaines</a></li>
                        </ul>
                    </div>
                    
                    <div class="links-group">
                        <h3 class="links-title">Entreprise</h3>
                        <ul class="links-list">
                            <li><a href="/about" class="footer-link">À propos</a></li>
                            <li><a href="/about" class="footer-link">Équipe</a></li>
                        </ul>
                    </div>
                    
                    <div class="links-group" id="#contact">
                        <h3 class="links-title">Contact</h3>
                        <ul class="links-list">
                            <li><a href="mailto:consultingadnsas@gmail.com" class="footer-link">consultingadnsas@gmail.com</a></li>
                            <li><a href="tel:+2250123456789" class="footer-link">+225 01 23 45 67 89</a></li>
                            <li class="footer-link">Abidjan, Côte d'Ivoire</li>
                        </ul>
                    </div>
                </div>

                <!-- Social Links -->
                <div class="social-section">
                    <h3 class="social-title">Suivez-nous</h3>
                    <div class="social-links">
                        <a href="https://www.facebook.com/cabinetADNconsulting/?locale=fr_FR" class="social-link" target="_blank" aria-label="Facebook">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M18 2H15C13.6739 2 12.4021 2.52678 11.4645 3.46447C10.5268 4.40215 10 5.67392 10 7V10H7V14H10V22H14V14H17L18 10H14V7C14 6.73478 14.1054 6.48043 14.2929 6.29289C14.4804 6.10536 14.7348 6 15 6H18V2Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </a>
                        <a href="https://www.linkedin.com/company/adnconsulting/posts/?feedView=all" class="social-link" target="_blank" aria-label="LinkedIn">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                                <path d="M16 8C17.5913 8 19.1174 8.63214 20.2426 9.75736C21.3679 10.8826 22 12.4087 22 14V21H18V14C18 13.4696 17.7893 12.9609 17.4142 12.5858C17.0391 12.2107 16.5304 12 16 12C15.4696 12 14.9609 12.2107 14.5858 12.5858C14.2107 12.9609 14 13.4696 14 14V21H10V14C10 12.4087 10.6321 10.8826 11.7574 9.75736C12.8826 8.63214 14.4087 8 16 8Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                <path d="M6 9H2V21H6V9Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                <path d="M4 6C5.10457 6 6 5.10457 6 4C6 2.89543 5.10457 2 4 2C2.89543 2 2 2.89543 2 4C2 5.10457 2.89543 6 4 6Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </a>
                    </div>
                    <div class="web__site">
                        <a href="https://www.contratchap.com" class="footer-link" target="_blank" rel="noopener noreferrer">www.contratchap.com</a>
                    </div>
                </div>
            </div>

            <!-- Divider -->
            <div class="footer-divider"></div>

            <!-- Bottom Section -->
            <div class="footer-bottom">
                <div class="copyright">
                    © {{ new Date().getFullYear() }} Adn consulting sas. Tous droits réservés.
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

.footer__logo{
    width: 48px;
    height: 48px;
    object-fit: contain;
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
    color: #7cfe7c;
}

.social-link:hover {
    background: rgba(255, 255, 255, 0.1);
    color: #1bcb1b;
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