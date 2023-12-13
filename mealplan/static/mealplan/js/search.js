var searchInput = document.getElementById('search-dropdown');

searchInput.addEventListener('input', () => {
    var searchValue = searchInput.value;
    getRecipeList(searchValue);
});

async function getRecipeList(searchValue) {
    try {
        const response = await fetch(`/api/recipes?search=${searchValue}`);
        
        if (!response.ok) {
            throw new Error('Réponse réseau incorrecte');
        }

        const data = await response.json();

        clearRecipeList(); // clear recipe list before updating display

        if (data.length === 0) {
            displayNoResultsMessage(); // A message is showed if no recipe
        } else {
            updateRecipesUI(data);
        }
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

function displayNoResultsMessage() {
    var noResultsMessage = document.createElement('p');
    noResultsMessage.textContent = 'Aucun résultat trouvé.';
    document.getElementById('recipe-list').appendChild(noResultsMessage);
}

function clearRecipeList() {
    var recipeList = document.getElementById('recipe-list');
    while (recipeList.firstChild) {
        recipeList.removeChild(recipeList.firstChild);
    }
}