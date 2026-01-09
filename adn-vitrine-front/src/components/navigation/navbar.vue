<template>
<nav class="main__nav">
    <div class="nav__logo">
        <h3>Adn consutling</h3>
    </div>
    <navButton/>
</nav>
</template>

<script lang="ts">
import navButton from './navButton.vue';

export default {
    name: 'navbar',
    components:{
        navButton,
    }
};
</script>

<style scoped>
/* Work on mobile first */

.main__nav{
    width: 100%;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 20px;
    box-sizing: border-box;
    position: absolute;
    top: 0;
    left: 0;
    z-index: 10;
}

.nav__logo h3{
    color: white;
    font-size: 24px;
    font-weight: 600;
}
</style>