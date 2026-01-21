<template>
  <div class="success-icon">
    <svg 
      xmlns="http://www.w3.org/2000/svg" 
      viewBox="0 0 52 52" 
      :style="{ width: size + 'px', height: size + 'px' }"
    >
      <circle 
        class="checkmark-circle" 
        cx="26" cy="26" r="21" 
        fill="none" 
      />
      <path 
        class="checkmark-check" 
        fill="none" 
        d="M14.1 27.2l7.1 7.2 16.7-16.8" 
      />
    </svg>
  </div>
</template>

<script setup>
defineProps({
  size: {
    type: [String, Number],
    default: 100
  }
})
</script>

<style scoped>
.success-icon {
  display: flex;
  justify-content: center;
  align-items: center;
}

.checkmark-circle {
  stroke-dasharray: 166;
  stroke-dashoffset: 166;
  stroke-width: 2;
  stroke-miterlimit: 10;
  stroke: #7bfd72;
  fill: none;
  animation: stroke 0.6s cubic-bezier(0.65, 0, 0.45, 1) forwards;
}

.checkmark-check {
  transform-origin: 50% 50%;
  stroke-dasharray: 42;
  stroke-dashoffset: 42;
  stroke-width: 3;
  stroke: #7bfd72;
  animation: stroke 0.6s cubic-bezier(0.65, 0, 0.45, 1) 0.8s forwards;
}

@keyframes stroke {
  100% {
    stroke-dashoffset: 0;
  }
}
</style>