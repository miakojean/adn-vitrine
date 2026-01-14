<template>
  <div class="blog-tabs">
    <div 
      class="tabs-container" 
      :class="[variant, { 'centered': centered, 'full-width': fullWidth }]"
    >
      <div class="tabs-nav" ref="tabsNav">
        <button
          v-for="(tab, index) in tabs"
          :key="tab.id || index"
          class="tab-button"
          :class="{ 'active': activeTab === tab.id }"
          @click="selectTab(tab.id)"
          role="tab"
          :aria-selected="activeTab === tab.id"
          :aria-controls="`tabpanel-${tab.id}`"
          :id="`tab-${tab.id}`"
          type="button"
        >
          <span v-if="tab.icon" class="tab-icon">{{ tab.icon }}</span>
          {{ tab.label }}
          <span class="tab-count" v-if="tab.count !== undefined">
            {{ tab.count }}
          </span>
        </button>
        
        <div v-if="variant !== 'pills'" class="tab-indicator" :style="indicatorStyle"></div>
      </div>
    </div>
    
    <div class="tabs-content">
      <div
        v-for="(tab, index) in tabs"
        :key="`content-${tab.id || index}`"
        :id="`tabpanel-${tab.id}`"
        class="tab-panel"
        :class="{ 'active': activeTab === tab.id }"
        role="tabpanel"
        :aria-labelledby="`tab-${tab.id}`"
        :hidden="activeTab !== tab.id"
      >
        <slot :name="`tab-${tab.id}`" :tab="tab">
          <div v-if="tab.content" class="default-content">
            {{ tab.content }}
          </div>
        </slot>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType, ref, onMounted, onUpdated, onUnmounted } from 'vue';

export interface Tab {
  id: string | number;
  label: string;
  count?: number;
  icon?: string;
  content?: string;
}

export default defineComponent({
  name: 'BlogTabs',
  props: {
    tabs: {
      type: Array as PropType<Tab[]>,
      required: true,
      validator: (tabs: Tab[]) => tabs.length > 0
    },
    initialTab: {
      type: [String, Number],
      default: null
    },
    variant: {
      type: String as PropType<'default' | 'minimal' | 'pills'>,
      default: 'default'
    },
    centered: {
      type: Boolean,
      default: false
    },
    fullWidth: {
      type: Boolean,
      default: false
    }
  },
  emits: ['tab-change'],
  setup(props, { emit }) {
    const activeTab = ref<string | number>('');
    const tabsNav = ref<HTMLElement | null>(null);
    const indicatorStyle = ref({
      width: '0px',
      transform: 'translateX(0px)',
      opacity: 0
    });

    const updateIndicator = () => {
      if (!tabsNav.value || props.variant === 'pills') return;
      
      const activeButton = tabsNav.value.querySelector('.tab-button.active') as HTMLElement;
      if (!activeButton) return;
      
      const navRect = tabsNav.value.getBoundingClientRect();
      const buttonRect = activeButton.getBoundingClientRect();
      
      indicatorStyle.value = {
        width: `${buttonRect.width}px`,
        transform: `translateX(${buttonRect.left - navRect.left}px)`,
        opacity: 1
      };
    };

    const selectTab = (tabId: string | number) => {
      if (activeTab.value === tabId) return;
      activeTab.value = tabId;
      emit('tab-change', tabId);
      // On attend le prochain tick pour que la classe .active soit appliquée au DOM
      requestAnimationFrame(updateIndicator);
    };

    onMounted(() => {
      activeTab.value = props.initialTab || props.tabs[0].id;
      window.addEventListener('resize', updateIndicator);
      setTimeout(updateIndicator, 50);
    });

    onUpdated(() => {
      updateIndicator();
    });

    onUnmounted(() => {
      window.removeEventListener('resize', updateIndicator);
    });

    return { activeTab, tabsNav, indicatorStyle, selectTab };
  }
});
</script>

<style scoped>
.blog-tabs {
  width: 100%;
  display: flex;
  flex-direction: column; /* Changé de center pour éviter les bugs de layout */
}

.tabs-container {
  position: relative;
  border-bottom: 1px solid #eaeaea;
  margin-bottom: 2rem;
  overflow-x: auto;
  scrollbar-width: none;
}

.tabs-container::-webkit-scrollbar { display: none; }

.tabs-nav {
  display: flex;
  position: relative;
  gap: 0.5rem;
  min-width: min-content;
}

/* Application des props de layout */
.tabs-container.centered .tabs-nav { justify-content: center; }
.tabs-container.full-width .tabs-nav { display: grid; grid-template-columns: repeat(auto-fit, minmax(50px, 1fr)); }

.tab-button {
  background: none;
  border: none;
  padding: 0.75rem 1.25rem;
  font-size: 0.95rem;
  font-weight: 500;
  color: #64748b; /* Fallback si la variable n'existe pas */
  cursor: pointer;
  transition: all 0.3s ease;
  white-space: nowrap;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  outline: none;
}

.tab-button:hover { color: #0066cc; }

.tab-button.active {
  color: #0066cc;
  font-weight: 600;
}

.tab-count {
  background: #f1f5f9;
  color: #64748b;
  font-size: 0.75rem;
  padding: 2px 8px;
  border-radius: 10px;
}

.tab-button.active .tab-count {
  background: #0066cc;
  color: white;
}

.tab-indicator {
  position: absolute;
  bottom: 0;
  height: 3px;
  background: #0066cc;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Variantes */
.pills { border-bottom: none; }
.pills .tab-button { border-radius: 99px; }
.pills .tab-button.active {
  background: #0066cc;
  color: white;
}

.tab-panel {
  display: none;
  animation: fadeIn 0.4s ease;
}
.tab-panel.active { display: block; }

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>