// common.js

// Load content from localStorage during page loading
document.addEventListener('DOMContentLoaded', () => {
    cells.forEach(c => {
        // Use unique key for localStorage
        let storageKey = 'cellContent_' + c.getAttribute('data-recipe-modal-target');
        let cellContent = c;

        if(cellContent) {
            let storedContent = localStorage.getItem(storageKey);

            if (storedContent) {
                cellContent.innerHTML = storedContent;
            }
        }
    });

     // Load grocery list from localStorage
     const groceryList = document.getElementById('grocery-list');
     let existingGroceryList = localStorage.getItem('grocery-list');
 
     if (existingGroceryList) {
         existingGroceryList = JSON.parse(existingGroceryList);

         existingGroceryList.forEach(ingredient => {
             const listItem = document.createElement('li');
             listItem.textContent = ingredient;
             groceryList.appendChild(listItem);
         });
     }
});

// Function to clear the grocery list in localStorage
function clearGroceryList() {
    localStorage.removeItem('grocery-list');
    // Clear the displayed grocery list on the page
    document.getElementById('grocery-list').innerHTML = '';
}

// Event to clear grocery list
document.getElementById('clear-grocery-list-button').addEventListener('click', clearGroceryList);
