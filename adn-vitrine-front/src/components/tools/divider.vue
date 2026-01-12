<template>
    <div 
        class="divider-gradient"
        :class="{
            'divider--horizontal': direction === 'horizontal',
            'divider--vertical': direction === 'vertical',
            'divider--small': size === 'small',
            'divider--medium': size === 'medium',
            'divider--large': size === 'large',
            'divider--reverse': reverse
        }"
        :style="{
            '--color-start': colorStart,
            '--color-middle': colorMiddle,
            '--color-end': colorEnd,
            '--gradient-angle': gradientAngle,
            'margin': margin
        }"
        :aria-hidden="true"
    ></div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'DividerGradient',
    props: {
        direction: {
            type: String as () => 'horizontal' | 'vertical',
            default: 'horizontal',
            validator: (value: string) => ['horizontal', 'vertical'].includes(value)
        },
        size: {
            type: String as () => 'small' | 'medium' | 'large',
            default: 'medium',
            validator: (value: string) => ['small', 'medium', 'large'].includes(value)
        },
        colorStart: {
            type: String,
            default: '#0066cc' // Bleu
        },
        colorMiddle: {
            type: String,
            default: '#00cc99' // Vert
        },
        colorEnd: {
            type: String,
            default: '#ff3366' // Rose
        },
        gradientAngle: {
            type: String,
            default: '90deg'
        },
        reverse: {
            type: Boolean,
            default: false
        },
        margin: {
            type: String,
            default: '0'
        }
    }
});
</script>

<style scoped>
.divider-gradient {
    --color-start: #0066cc;
    --color-middle: #00cc99;
    --color-end: #ff3366;
    --gradient-angle: 90deg;
    
    background: linear-gradient(
        var(--gradient-angle),
        var(--color-start),
        var(--color-middle),
        var(--color-end)
    );
    border-radius: 100px;
}

/* Directions */
.divider--horizontal {
    width: 100%;
    height: 4px;
}

.divider--vertical {
    width: 4px;
    height: 100px;
    margin: 0 auto;
}

/* Tailles */
.divider--small.divider--horizontal {
    height: 2px;
}

.divider--small.divider--vertical {
    width: 2px;
    height: 60px;
}

.divider--medium.divider--horizontal {
    height: 4px;
}

.divider--medium.divider--vertical {
    width: 4px;
    height: 100px;
}

.divider--large.divider--horizontal {
    height: 6px;
}

.divider--large.divider--vertical {
    width: 6px;
    height: 150px;
}

/* Effet reverse */
.divider--reverse {
    background: linear-gradient(
        var(--gradient-angle),
        var(--color-end),
        var(--color-middle),
        var(--color-start)
    ) !important;
}

/* Animation optionnelle */
.divider-gradient {
    animation: fadeIn 0.5s ease-out;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: scaleX(0.8);
    }
    to {
        opacity: 1;
        transform: scaleX(1);
    }
}

/* Pour l'animation au scroll */
.divider--vertical {
    animation: slideUp 0.8s ease-out;
}

@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(20px);
        height: 0;
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>