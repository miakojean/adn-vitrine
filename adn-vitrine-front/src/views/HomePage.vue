<template>
  <main>
    <navbar/>
    <ctaSection/>
    <statSection/>
    <teamSection/>
    <patnerSection/>
    <servicesSection/>
    <footerSection/>
  </main>
</template>

<script lang="ts">
import navbar from '../components/navigation/navbar.vue';
import ctaSection from '../components/sections/ctaSection.vue';
import statSection from '../components/sections/statSection.vue';
import teamSection from '../components/sections/teamSection.vue';
import patnerSection from '../components/sections/patnerSection.vue';
import servicesSection from '../components/sections/serviceSection.vue';
import footerSection from '../components/sections/footerSection.vue';

export default {
  name: 'HomePage',
  components:{
    navbar,
    ctaSection,
    statSection,
    teamSection,
    patnerSection,
    servicesSection,
    footerSection
  }
};
</script>

<style scoped>
main{
  width: 100%;
  overflow-x: hidden;
  background: #0F172A;
}
</style>