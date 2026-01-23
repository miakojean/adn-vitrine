<template>
<nav class="main__nav" :class="{ 'nav--scrolled': isScrolled, 'nav--menu-open': isMenuOpen }">
    <div class="nav__logo">
        <h3>ADN Consulting</h3>
    </div>
    
    <!-- Menu desktop -->
    <div class="nav__menu">
        <ul class="nav__links">
            <li><router-link to="/" class="nav__link" exact-active-class="active">Accueil</router-link></li>
            <li><router-link to="/about" class="nav__link" active-class="active">À propos</router-link></li>
            <li><router-link to="/services" class="nav__link" active-class="active">Services</router-link></li>
            <li><router-link to="/blog" class="nav__link" active-class="active">Blog</router-link></li>
            <li><router-link to="/newsletter" class="nav__link" active-class="active">Newsletter</router-link></li>
        </ul>
    </div>

    <div class="cta__button">
        <mainButton label="Besoin d'un contrat"/>
    </div>
    
    <!-- Menu mobile -->
    <button class="nav__hamburger" @click="toggleMenu" aria-label="Menu">
        <span></span>
        <span></span>
        <span></span>
    </button>
    
    <!-- Menu mobile (version router) -->
    <div class="nav__menu mobile" :class="{ 'active': isMenuOpen }">
        <ul class="nav__links">
            <li><router-link to="/" class="nav__link" exact-active-class="active" @click="closeMenu">Accueil</router-link></li>
            <li><router-link to="/about" class="nav__link" active-class="active" @click="closeMenu">À propos</router-link></li>
            <li><router-link to="/services" class="nav__link" active-class="active" @click="closeMenu">Services</router-link></li>
            <li><router-link to="/blog" class="nav__link" active-class="active" @click="closeMenu">Blog</router-link></li>
            <li><router-link to="/newsletter" class="nav__link" active-class="active" @click="closeMenu">Newsletter</router-link></li>
        </ul>
        <div class="nav__cta">
            <mainButton @click="navigateToExternal('contratchap.com')"/>
        </div>
    </div>
    
    <!-- Overlay mobile -->
    <div class="nav__overlay" :class="{ 'active': isMenuOpen }" @click="closeMenu"></div>
</nav>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, onUnmounted } from 'vue';
import mainButton from '../button/mainButton.vue';
import { useRouter } from 'vue-router';

export default defineComponent({
    name: 'navbar',
    components: {
        mainButton
    },
    setup() {
        const router = useRouter();
        const isScrolled = ref(false);
        const isMenuOpen = ref(false);
        
        const handleScroll = () => {
            isScrolled.value = window.scrollY > 50;
        };
        
        const toggleMenu = () => {
            isMenuOpen.value = !isMenuOpen.value;
            if (isMenuOpen.value) {
                document.body.style.overflow = 'hidden';
            } else {
                document.body.style.overflow = '';
            }
        };
        
        const closeMenu = () => {
            isMenuOpen.value = false;
            document.body.style.overflow = '';
        };
        
        // Navigation programmatique
        const navigateTo = (route: string) => {
            router.push(route);
            closeMenu();
        };

        const navigateToExternal = (url: string) => {
            window.location.href = url;
            closeMenu();
        };
        
        // Fermer le menu avec la touche Escape
        const handleEscape = (e: KeyboardEvent) => {
            if (e.key === 'Escape' && isMenuOpen.value) {
                closeMenu();
            }
        };
        
        onMounted(() => {
            window.addEventListener('scroll', handleScroll);
            window.addEventListener('keydown', handleEscape);
        });
        
        onUnmounted(() => {
            window.removeEventListener('scroll', handleScroll);
            window.removeEventListener('keydown', handleEscape);
            document.body.style.overflow = '';
        });
        
        return {
            router,
            isScrolled,
            isMenuOpen,
            toggleMenu,
            closeMenu,
            navigateTo,
            navigateToExternal
        };
    }
});
</script>

<style scoped>
/* Base mobile first */
.main__nav {
    width: 100%;
    height: 70px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 20px;
    box-sizing: border-box;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1000;
    background: transparent;
    transition: all 0.3s ease;
}

.main__nav.nav--scrolled {
    backdrop-filter: blur(10px);
    box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
    height: 65px;
}

.nav__logo h3 {
    color: white;
    font-size: 22px;
    font-weight: 700;
    letter-spacing: 0.5px;
    transition: color 0.3s ease;
}
 
.nav--scrolled .nav__logo h3 {
    color: #eee;
}

/* Menu desktop - caché sur mobile */
.nav__menu {
    display: none;
}

.nav__hamburger {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 30px;
    height: 21px;
    background: transparent;
    border: none;
    cursor: pointer;
    padding: 0;
    z-index: 1001;
}

.nav__hamburger span {
    width: 100%;
    height: 3px;
    background: white;
    transition: all 0.3s ease;
    border-radius: 3px;
}

.nav--scrolled .nav__hamburger span {
    background: #1a1a1a;
}

.nav--menu-open .nav__hamburger span:nth-child(1) {
    transform: rotate(45deg) translate(6px, 6px);
}

.nav--menu-open .nav__hamburger span:nth-child(2) {
    opacity: 0;
}

.nav--menu-open .nav__hamburger span:nth-child(3) {
    transform: rotate(-45deg) translate(7px, -7px);
}

/* Menu mobile */
.nav__overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    background: rgba(0, 0, 0, 0.5);
    opacity: 0;
    visibility: hidden;
    transition: all 0.3s ease;
    z-index: 999;
}

.nav__overlay.active {
    opacity: 1;
    visibility: visible;
}

.nav__menu.mobile {
    position: fixed;
    top: 0;
    right: -100%;
    width: 80%;
    max-width: 350px;
    height: 100vh;
    background: #0F172A;
    padding: 80px 30px 40px;
    box-sizing: border-box;
    transition: right 0.4s ease;
    z-index: 1000;
    display: flex;
    flex-direction: column;
    overflow-y: auto;
}

.nav__menu.mobile.active {
    right: 0;
}

.nav__menu.mobile .nav__links {
    flex-direction: column;
    gap: 0;
    margin-bottom: 40px;
    list-style: none;
    padding: 0;
}

.nav__menu.mobile .nav__link {
    color: #eee;
    font-size: 18px;
    padding: 15px 0;
    border-bottom: 1px solid #eee;
    display: block;
    text-align: left;
    text-decoration: none;
    transition: color 0.3s ease;
}

.nav__menu.mobile .nav__link:hover {
    color: #0066cc;
}

.nav__menu.mobile .nav__link.active {
    color: #0066cc;
    border-bottom-color: #0066cc;
    font-weight: 600;
}

.nav__menu.mobile .nav__cta {
    margin-top: auto;
    width: 100%;
}

.cta__button {
    display: none;
}

/* Styles pour les liens router */
.nav__link {
    color: white;
    text-decoration: none;
    transition: color 0.3s ease;
    position: relative;
    padding: 5px 0;
}

.nav__link.router-link-exact-active,
.nav__link.router-link-active {
    color: #0066cc;
}

.nav__link.router-link-exact-active::after,
.nav__link.router-link-active::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 2px;
    background: #0066cc;
    border-radius: 2px;
}

/* Responsive pour tablette et desktop */
@media (min-width: 768px) {
    .main__nav {
        padding: 0 30px;
        height: 80px;
    }
    
    .nav--scrolled {
        height: 75px;
    }
    
    .nav__logo h3 {
        font-size: 24px;
    }
    
    /* Cacher le hamburger et menu mobile */
    .nav__hamburger,
    .nav__menu.mobile,
    .nav__overlay {
        display: none;
    }
    
    /* Afficher le menu desktop */
    .nav__menu:not(.mobile) {
        display: flex;
        align-items: center;
        gap: 40px;
    }
    
    .nav__links {
        display: flex;
        gap: 30px;
        list-style: none;
        margin: 0;
        padding: 0;
    }
    
    .nav__link {
        color: white;
        font-size: 16px;
        font-weight: 500;
    }
    
    .nav--scrolled .nav__link {
        color: white;
    }
    
    .nav__link:hover {
        color: #0066cc;
    }
    
    .nav__link.active {
        color: #0066cc;
    }
    
    .nav__link.active::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 2px;
        background: #0066cc;
        border-radius: 2px;
    }
    
    .cta__button {
        display: block;
    }
}

@media (min-width: 1024px) {
    .main__nav {
        padding: 0 50px;
    }
    
    .nav__menu:not(.mobile) {
        gap: 50px;
    }
    
    .nav__links {
        gap: 40px;
    }
    
    .nav__link {
        font-size: 17px;
    }
}

/* Animation pour le lien actif */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(-10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.nav__menu.mobile .nav__link {
    animation: fadeIn 0.3s ease forwards;
    opacity: 0;
}

.nav__menu.mobile .nav__link:nth-child(1) { animation-delay: 0.1s; }
.nav__menu.mobile .nav__link:nth-child(2) { animation-delay: 0.2s; }
.nav__menu.mobile .nav__link:nth-child(3) { animation-delay: 0.3s; }
.nav__menu.mobile .nav__link:nth-child(4) { animation-delay: 0.4s; }
.nav__menu.mobile .nav__link:nth-child(5) { animation-delay: 0.5s; }

/* Smooth scroll behavior */
html {
    scroll-behavior: smooth;
}
</style>