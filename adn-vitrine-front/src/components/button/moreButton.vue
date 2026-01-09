<template>
    <button class="cta-button" @click="handleCtaClick">
        <span> {{ label }}</span>
        <svg class="arrow-icon" width="20" height="20" viewBox="0 0 24 24" fill="none">
            <path d="M5 12H19M19 12L12 5M19 12L12 19" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
    </button>
</template>

<script lang="ts">
export default {
    name: 'moreButton',

    props: {
        label:{
            type: String,
            default: 'Découvrir notre portfolio',
        }
    },

    setup() {
        const handleCtaClick = () => {
        window.location.href = '/portfolio';
        };

        return {
            handleCtaClick,
        };
    },
};
</script>

<style scoped>
.cta-button {
    display: inline-flex;
    align-items: center;
    gap: 0.75rem;
    padding: 1rem 2.5rem;
    background: linear-gradient(90deg, #3b82f6, #8b5cf6);
    color: white;
    border: none;
    border-radius: 50px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.cta-button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    transition: left 0.5s ease;
}

.cta-button:hover::before {
    left: 100%;
}

.cta-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(59, 130, 246, 0.4);
}

.cta-button:active {
    transform: translateY(0);
}

.arrow-icon {
    transition: transform 0.3s ease;
}

.cta-button:hover .arrow-icon {
    transform: translateX(4px);
}
</style>