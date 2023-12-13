class RecipeFilter {
    constructor(apiEndpoint) {
        this.apiEndpoint = apiEndpoint;
        this.selectedCategories = [];
        this.checkboxes = document.querySelectorAll('#recipe-categories input[type="checkbox"]');
        this.searchInput = document.getElementById('search-dropdown');
        this.initCheckboxes();
        this.initSearchInput();
    }

    initCheckboxes() {
        this.checkboxes.forEach(checkbox => {
            checkbox.checked = false;
            checkbox.addEventListener('change', () => this.handleCheckboxChange(checkbox));
        });
    }

    initSearchInput() {
        this.searchInput.addEventListener('input', () => {
            this.fetchAndDisplayRecipes();
        });
    }

    handleCheckboxChange(checkbox) {
        var category_id = checkbox.value;
        var index = this.selectedCategories.indexOf(category_id);

        if (checkbox.checked) {
            checkbox.setAttribute('checked', 'checked');
            this.selectedCategories.push(category_id);
        } else {
            checkbox.removeAttribute('checked');
            this.selectedCategories.splice(index, 1);
        }
        this.fetchAndDisplayRecipes();
    }

    async fetchAndDisplayRecipes() {
        try {
            let url = `${this.apiEndpoint}?`;
            const searchValue = this.searchInput.value;

            if (this.selectedCategories.length > 0) {
                url += `categories=${this.selectedCategories.join(',')}`;
            }

            if (searchValue !== undefined && searchValue.trim() !== '') {
                url += `${this.selectedCategories.length > 0 ? '&' : ''}search=${searchValue}`;
            }

            const response = await fetch(url);

            if (!response.ok) {
                throw new Error('Réponse réseau incorrecte');
            }

            const data = await response.json();

            this.updateRecipesUI(data);
        } catch (error) {
            console.error('Une erreur s\'est produite :', error.message);
        }
    } 

    updateRecipesUI(recipes) {
        var recipeList = document.getElementById('recipe-list');
        var existingRecipeItems = recipeList.querySelectorAll('.recipe-item');

        existingRecipeItems.forEach(item => item.remove());
    
        var fragment = document.createDocumentFragment();
        recipes.forEach(function (recipe) {
            var recipeElement = document.createElement('li');
            recipeElement.className = 'recipe-item';
            recipeElement.innerHTML = `
            <div class="flex flex-col place-content-around h-60 p-4 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
                <a class="self-center h-2/6" href="${recipe.slug}">
                    <h5 class="recipe-name text-center mb-2 text-xl font-bold tracking-tight text-gray-900 dark:text-white">${recipe.name}</h5>
                </a>
                <ul class="flex flex-wrap justify-center content-between h-1/4">
                    ${recipe.categories.map(category => `<li class="shrink-0 bg-purple-100 text-purple-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-gray-700 dark:text-purple-400 border border-purple-400">${category.name}</li>`).join('')}
                </ul>
                <a href="${recipe.slug}" class="inline-flex items-center w-40 ml-auto px-3 py-2 text-sm font-medium text-center text-white bg-lime-600 rounded-lg hover:bg-lime-700 focus:ring-4 focus:outline-none focus:ring-lime-800 dark:bg-lime-600 dark:hover:bg-lime-700 dark:focus:ring-lime-800">
                    Aller à la recette
                    <svg class="rtl:rotate-180 w-3.5 h-3.5 ms-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 10">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 5h12m0 0L9 1m4 4L9 9"/>
                    </svg>
                </a>
            </div>
        `;

        fragment.appendChild(recipeElement);
        });
        recipeList.appendChild(fragment);
    }
}