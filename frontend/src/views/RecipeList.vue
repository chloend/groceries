<template>
    <div>
        <h1 class="text-2xl sm:text-4xl font-bold pl-4 sm:pl-0">Recipes</h1>
        <ul id="recipe-list" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 2xl:grid-cols-4 gap-4">
            <li  v-for="recipe in recipes" :key="recipe.id" class="recipe-item">
                <div class="flex flex-col place-content-around h-60 p-4 rounded-lg bg-gray-800 border border-gray-700 shadow-md shadow-gray-700">
                    <a class="self-center h-2/6" v-bind:href="recipe.slug ">
                        <h2 class="recipe-name text-center mb-2 text-xl font-bold tracking-tight text-white">{{ recipe.name }}</h2>
                    </a>
                    <a v-bind:href="recipe.slug" class="inline-flex items-center w-32 ml-auto px-3 py-2 text-sm text-center text-white font-medium rounded-lg bg-lime-600 hover:bg-lime-700 focus:ring-4 focus:outline-none focus:ring-lime-800">
                    Full recipe
                    <svg class="rtl:rotate-180 w-3.5 h-3.5 ms-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 10">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 5h12m0 0L9 1m4 4L9 9"/>
                    </svg>
                </a>
                </div>
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