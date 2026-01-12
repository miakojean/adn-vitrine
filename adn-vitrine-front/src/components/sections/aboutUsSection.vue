<template>
    <section class="about__section">
        <div class="main__description">
            <h2>Qui sommes-nous?</h2>
            <divider 
                direction="horizontal" 
                size="small" 
                :color-start="'#3b82f6'" 
                :color-middle="'#1e293b'" 
                :color-end="'#1e293b'" 
                gradient-angle="90deg" 
                :margin="'1.5rem 0'"
            />
            <p>
                Depuis sa création, le Cabinet ADN Consulting SAS
                s'est donné pour mission de faire en sorte que dans 
                toutes les actions et engagements, les entrepreneurs, 
                les PMEs et startups voient leurs intérêts grandement 
                protégés et grandissent sainement. Cela, à travers 
                une équipe compétente et smart et des offres répondant 
                aux besoins et réalités desdits entrepreneurs, PMEs et startups. 
                D'où son positionnement stratégique sur l'échiquier national et international.
            </p>
            <mainButton label="Nos services"/>
        </div>

        <!-- About the firm statistics -->
        <div class="about__statistic flex flex-col justify-center items-center mt-10 gap-4">
            <h3 class=" text-3xl font-bold ">Adn consulting c'est</h3>
            
            <div class="">
                <img src="../../assets/pic/pexels-roboseal34-35457179.jpg">
            </div>

            <div class="grid grid-cols-3 gap-2 mt-6">
                <div class="statistic__item flex flex-col justify-center gap-2">
                    <h3 class="text-3xl font-bold">1000+</h3>
                    <p>Entreprises accompagnées</p>
                </div>
                <divider 
                    direction="vertical" 
                    size="small" 
                    :color-start="'#f3f3f3'" 
                    :color-middle="'#f3f3f3'" 
                    :color-end="'#f3f3f3'" 
                    gradient-angle="180deg" 
                    :margin="'0 1rem'"
                />
                <div class="statistic__item flex flex-col justify-center gap-2">
                    <h3 class="text-3xl font-bold">1700+</h3>
                    <p>Documents redigés</p>
                </div>
                <divider 
                    direction="vertical" 
                    size="small" 
                    :color-start="'#f3f3f3'" 
                    :color-middle="'#f3f3f3'" 
                    :color-end="'#f3f3f3'" 
                    gradient-angle="180deg" 
                    :margin="'0 1rem'"
                />
                <div class="statistic__item flex flex-col justify-center gap-2">
                    <h3 class="text-3xl font-bold">20+</h3>
                    <p>Pays clients</p>
                </div>
                <divider 
                    direction="vertical" 
                    size="small" 
                    :color-start="'#f3f3f3'" 
                    :color-middle="'#f3f3f3'" 
                    :color-end="'#f3f3f3'" 
                    gradient-angle="180deg" 
                    :margin="'0 1rem'"
                />
                <div class="statistic__item flex flex-col justify-center gap-2">
                    <h3 class="text-3xl font-bold">03</h3>
                    <p>Filiales</p>
                </div>
                <divider 
                    direction="vertical" 
                    size="small" 
                    :color-start="'#f3f3f3'" 
                    :color-middle="'#f3f3f3'" 
                    :color-end="'#f3f3f3'" 
                    gradient-angle="180deg" 
                    :margin="'0 1rem'"
                />
                <div class="statistic__item flex flex-col justify-center gap-2">
                    <h3 class="text-3xl font-bold">8+</h3>
                    <p>Années d'expérience</p>
                </div>
                <divider 
                    direction="vertical" 
                    size="small" 
                    :color-start="'#f3f3f3'" 
                    :color-middle="'#f3f3f3'" 
                    :color-end="'#f3f3f3'" 
                    gradient-angle="180deg" 
                    :margin="'0 1rem'"
                />
                <div class="statistic__item flex flex-col justify-center gap-2">
                    <h3 class="text-3xl font-bold">1</h3>
                    <p>Legaltech</p>
                </div>
            </div>
        </div>

        <!-- About the team -->
        <div class="about__team">
            <h3 class=" text-3xl font-bold mt-10 ">Notre équipe</h3>
            <p class="mt-4">
                Notre équipe est composée de professionnels passionnés et dévoués, 
                spécialisés dans divers domaines du droit et de la technologie. 
                Ensemble, nous travaillons en synergie pour offrir des solutions 
                innovantes et adaptées aux besoins spécifiques de nos clients.
            </p>
            <div class="team__members grid grid-cols-3 gap-4 mt-6">
                <div class="member__card flex flex-col justify-center items-center gap-2">
                    <h4 class="text-xl font-semibold">Jean Dupont</h4>
                    <p class="text-sm text-gray-400">Avocat spécialisé en droit des affaires</p>
                </div>
                <div class="member__card flex flex-col justify-center items-center gap-2">
                    <h4 class="text-xl font-semibold">Marie Curie</h4>
                    <p class="text-sm text-gray-400">Consultante en conformité réglementaire</p>
                </div>
                <div class="member__card flex flex-col justify-center items-center gap-2">
                    <h4 class="text-xl font-semibold">Ali Hassan</h4>
                    <p class="text-sm text-gray-400">Expert en legaltech et innovation juridique</p>
                </div>
            </div>
        </div>

    </section>
</template>

<script lang="ts">
import mainButton from '../button/mainButton.vue';
import divider from '../tools/divider.vue';

export default {
    name: 'aboutUsSection',

    components:{
        mainButton,
        divider
    }
};
</script>

<style scoped>

/* For mobile first */

.about__section {
    width: 100%;
    padding: 5rem 1rem;
    color: rgb(219, 211, 211);
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    flex-direction: column;
    gap: 2rem;
}

.main__description{
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 1rem;
}

.main__description h2 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    font-weight: 600;
    color: white;
}

.main__description p {
    font-size: 1rem;
    margin-bottom: 1rem;
    color: white;
    text-align: justify;
    line-height: 2;
}
</style>