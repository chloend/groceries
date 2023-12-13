document.addEventListener('DOMContentLoaded', function() {
    // Selected categories go in this list
    var selectedCategories = [];
    
    // Select all checkboxes input type in recipesCategories
    var checkboxes = document.querySelectorAll('#recipe-categories input[type="checkbox"]');

    // Uncheck boxes when loading page
    checkboxes.forEach(function(checkbox) {
        checkbox.checked = false;
    });

    // Event manager for each checkbox
    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            // Handle checkbox 'checked' attribute
            handleCheckboxChange(checkbox, selectedCategories);
            // Update recipes list depending on selected gategories
            fetchAndDisplayRecipes(selectedCategories);
        });
    });

    // Fetch and display recipe depending ons elected categories
    async function fetchAndDisplayRecipes(selectedCategories) {
        try {
            // Get recipe data from the api
            const response = await fetch(`/api/recipes/?categories=${selectedCategories.join(',')}`);

            if (!response.ok) {
                throw new Error('Réponse réseau incorrecte');
            }

            const data = await response.json();

            updateRecipesUI(data); // Update recipes list with the new data
        } catch (error) {
            console.error('Une erreur s\'est produite:', error.message);
        }
    }

    function updateRecipesUI(recipes) {
        var recipeList = document.getElementById('recipe-list'); // Get recipe list
        recipeList.innerHTML = ''; // Clear list before adding new recipes
    
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
            
            recipeList.appendChild(recipeElement); // Add <li> element to recipe list
        });
    }

    // Fonction pour gérer le changement d'état d'une case à cocher
    function handleCheckboxChange(checkbox, selectedCategories) {
        // Obtient l'ID et l'index de la catégorie associée à la case à cocher
        var category_id = checkbox.value;
        var index = selectedCategories.indexOf(category_id);

        // Si la case à cocher est cochée, ajoute la catégorie aux catégories sélectionnées
        if (checkbox.checked) {
            checkbox.setAttribute('checked', 'checked');
            selectedCategories.push(category_id);
        } else {  // Si la case à cocher est décochée, retire la catégorie des catégories sélectionnées
            checkbox.removeAttribute('checked');
            selectedCategories.splice(index, 1);
        }
    }
});