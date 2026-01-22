<template>
    <article class="team__card">
        <div class="team__picture">
            <img src="https://picsum.photos/800/600" alt="image aléatoire">
        </div>
        <div class="team__info">
            <h3>
                {{ name }}
            </h3>
            <p>{{ role }}</p>

            <div class="social__icons">
                <i class="ri-linkedin-fill"></i>
                <i class="ri-twitter-x-line"></i>
                <i class="ri-facebook-fill"></i>
            </div>
        </div>
    </article>
</template>

<script lang="ts">

export default {
    name: 'teamCards',

    props:{
        name:{
            type: String,
            default: 'John Doe',

        },
        role:{
            type: String,
            default: 'Developer',
        },
    },

    setup(){

    }
};
</script>

<style scoped>

/* Work for mobile first */
.team__card {
    width: 100%;
    min-width: 300px;
    background-color: #0F172A;
    border-radius: 0.5rem;
    display: flex;
    flex-direction: column;
    gap: 1rem;
    border: 1px solid #4c6998;
}

.team__picture img {
    width: 100%;
    height: auto;
    border-radius: 0.5rem;
}

.team__info {
    display: flex;
    flex-direction: column;
    align-items: start;
    gap: 0.5rem;
    color: white;
    padding: 1rem;
}

.team__info h3 {
    font-size: 1.5rem;
    font-weight: 600;
    margin: 0;
    color: white;
}

.team__info p {
    margin: 0;
    color: #dce4f3;
    font-weight: 500;
}

.about {
    margin-top: 0.5rem;
}

.about span {
    font-weight: 600;
    margin-bottom: 0.25rem;
    display: block;
    text-align: start;
}

.about p {
    font-size: 0.9rem;
    color: #dce4f3;
    text-align: justify;
    font-weight: 400;
}

.social__icons {
    margin-top: 0.5rem;
    display: flex;
    gap: 1rem;
    color: #dce4f3;
}
</style>