<template>
    <main>
        <navbar/>
        <aboutUsSection/>
        <footerSection/>
    </main>
</template>

<script lang="ts">
import navbar from '../components/navigation/navbar.vue';
import aboutUsSection from '../components/sections/aboutUsSection.vue';
import footerSection from '../components/sections/footerSection.vue';

export default {
    name: 'AboutUsPage',

    components:{
        navbar,
        aboutUsSection,
        footerSection
    }
}
</script>

<style scoped>
main{
width: 100%;
height: 100%;
background: #0F172A;
display: flex;
flex-direction: column;
gap: 1rem;
}
</style>