<template>
    <main>
        <navbar/>
        <contactSection/>
        <footerSection/>
    </main>
</template>

<script lang="ts">
import navbar from '../components/navigation/navbar.vue';
import blogSection from '../components/sections/blogSection.vue';
import contactSection from '../components/sections/contactSection.vue';
import footerSection from '../components/sections/footerSection.vue';

export default {
  name: 'HomePage',
  components:{
    navbar,
    blogSection,
    contactSection,
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