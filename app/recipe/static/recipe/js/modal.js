// modal.js

let cells = document.querySelectorAll('[data-recipe-modal-target]');
let cell;
let count = 0;

// Show modal
async function showModal() {
    // Use AJAX to dynamically load RecipesList view content
    const response = await fetch('/api/recipes'); // RecipesList view URL
    const data = await response.json();

    // Create a list element to hold recipe names
    const listElement = document.createElement('ul');

    // Iterate over each recipe and create a list item for each one
    data.forEach(recipe => {
        const listItem = document.createElement('li');
        listItem.setAttribute('data-recipe-slug', recipe.slug);
        listItem.setAttribute('tabindex', '0');
        listItem.setAttribute('data-recipe', recipe.name);
        listItem.classList.add('cursor-pointer');

        listItem.textContent = recipe.name; // Add recipe name as text content of the list item
        listElement.appendChild(listItem);
    });

    // Insert the list into the modal
    document.getElementById('recipe-modal-content').innerHTML = '';  // Clear existing content
    document.getElementById('recipe-modal-content').appendChild(listElement);

    // Show modal
    document.getElementById('recipe-modal').classList.add('block');
    document.getElementById('recipe-modal').classList.remove('hidden');
}

// Event manager to open modal with each cell
cells.forEach(c => {
    // Add count value to data-recipe-modal-attribute from the cell
    c.setAttribute('data-recipe-modal-target', c.getAttribute('data-recipe-modal-target') + count);
    c.addEventListener('click', () => {
        // Save current cell and store it in a variable
        cell = c;
        showModal();
    });
    count++;
});

// Add selected recipe into the table cell
async function addRecipe(recipe) {
    // Retrieve Recipe details from the server
    const recipeSlug = recipe.getAttribute('data-recipe-slug');
    const response = await fetch(`/api/recipes/${recipeSlug}`);
    const data = await response.json();

    // cell variable is defined above the function addRecipe
    cell.innerHTML = '';
    cell.textContent = recipe.textContent;

    // Update grocery list
    const groceryList = document.getElementById('grocery-list');

    // Get existing grocery list from localStorage
    let existingGroceryList = localStorage.getItem('grocery-list');
    existingGroceryList = existingGroceryList ? JSON.parse(existingGroceryList) : [];

    // Add new ingredients to the list
    data.ingredients.forEach(ingredient => {
        if (!existingGroceryList.includes(ingredient.food)) {
            const listItem = document.createElement('li');
            listItem.textContent = `${ingredient.food}`;
            groceryList.appendChild(listItem);
        
            // Add the new ingredient to the existing list
            existingGroceryList.push(`${ingredient.food}`);
        }
    });

    // Save the updated list of ingredients to localStorage
    localStorage.setItem('grocery-list', JSON.stringify(existingGroceryList));

    // Use data-model-target attribute from the cell as a unique key
    let storageKey = 'cellContent_' + cell.getAttribute('data-recipe-modal-target');

    // Store content in localStorage
    localStorage.setItem(storageKey, cell.innerHTML);
}

// Close modal
function closeModal() {
    document.getElementById('recipe-modal').classList.add('hidden');
    document.getElementById('recipe-modal').classList.remove('block');
}

// Close modal with icon
document.querySelector('[data-recipe-modal-hide]').addEventListener('click', () => {
    closeModal();
});

document.getElementById('recipe-modal-content').addEventListener('click', (e) => {
    let selectedRecipe = e.target.closest('[data-recipe]');

    if (selectedRecipe) {
        // Select a recipe and add it in the cell
        addRecipe(selectedRecipe);
        closeModal();
    }
});
