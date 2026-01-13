<template>
    <main>
        <navbar/>
        <newsletterSection/>
        <footerSection/>
    </main>
</template>

<script lang="ts">
import navbar from '../components/navigation/navbar.vue';
import newsletterSection from '../components/sections/newsletterSection.vue';
import footerSection from '../components/sections/footerSection.vue';

export default {
  name: 'HomePage',
  components:{
    navbar,
    newsletterSection,
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