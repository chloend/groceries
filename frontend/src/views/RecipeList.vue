<template>
    <div>
        <h1 class="text-white text-2xl sm:text-4xl font-bold pl-4 sm:pl-0">Recipes</h1>
        <ul id="recipe-list" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 2xl:grid-cols-4 gap-4">
            <li  v-for="recipe in recipes" :key="recipe.id" class="recipe-item">
                <RecipeCard :title="recipe.name" :link="recipe.slug">
                    <DefaultButton :link="recipe.slug">Full recipe</DefaultButton>
                </RecipeCard>
            </li>
        </ul>
    </div>
</template>

<script>
import axios from '@/axios';
import RecipeCard from '@/components/RecipeCard.vue';
import DefaultButton from '@/components/DefaultButton.vue';

export default {
    name: 'RecipeList',
    components: {
        RecipeCard,
        DefaultButton,
    },
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