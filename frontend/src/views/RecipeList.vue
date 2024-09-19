<template>
    <div>
        <h1>Recipes</h1>
        <ul id="recipe-list">
            <li  v-for="recipe in recipes" :key="recipe.id" class="recipe-item">
                <h2 class="recipe-name">{{ recipe.name }}</h2>
            </li>
        </ul>
    </div>
</template>

<script>
import axios from '@/axios';

export default {
    data() {
        return {
            recipes: [],
        };
    },
    created() {
        this.fetchRecipes();
    },
    methods: {
        async fetchRecipes() {
            try {
                const response = await axios.get('recipes/');
                this.recipes = response.data;
            } catch (error) {
                console.error('Error fetching recipes : ', error);
            }
        }
    }
}
</script>

<style>
h1,
.recipe-name {
    color: white;
    text-align: center;
}
</style>