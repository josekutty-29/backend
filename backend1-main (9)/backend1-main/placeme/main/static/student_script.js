import {
    setupThemeToggle,
    setupSidebarToggle,
    setupNavigation,
    activatePage,
    placements,
    notifications,
    showPlacementDetails,
    
} from './common.js';

// --- DOM Element References ---
const placementList = document.getElementById('placementList');
const notificationList = document.getElementById('notificationList');
const detailsPage = document.getElementById('detailsPage');
const detailsPageTitle = document.getElementById('detailsPageTitle');
const detailsDescription = document.getElementById('detailsDescription');
const detailsBackButton = document.getElementById('detailsBackButton');

// --- Filtering ---
let currentFilter = 'available';

function getFilteredPlacements() {
    switch (currentFilter) {
        case 'available':
            return placements;
        case 'liked':
            return placements; // Extend if needed
        case 'applied':
            return placements; // Extend if needed
        default:
            return placements;
    }
}

// --- Placement Rendering ---
function renderPlacements() {
    if (!placementList) {
        console.error("placementList element not found!");
        return;
    }
    const filteredPlacements = getFilteredPlacements();
    placementList.innerHTML = '';
    filteredPlacements.forEach(placement => {
        const listItem = document.createElement('li');
        listItem.classList.add('placement-list-item');
        listItem.dataset.placementId = placement.id;
        let actionsHTML = `<div class="placement-actions">
                <button class="like-button" data-placement-id="${placement.id}">
                    <i class="material-icons">favorite_border</i>
                </button>
            </div>`;
        listItem.innerHTML = `
            <div class="placement-info">
                <i class="material-icons placement-icon">business_center</i>
                <span class="placement-title">${placement.title}</span>
            </div>
            ${actionsHTML}
        `;
        placementList.appendChild(listItem);
    });
    placementList.addEventListener('click', (event) => {
        const likeButton = event.target.closest('.like-button');
        const placementItem = event.target.closest('.placement-list-item');
        if (likeButton) {
            const placementId = parseInt(likeButton.dataset.placementId, 10);
            toggleLike(placementId);
        } else if (placementItem) {
            const placementId = parseInt(placementItem.dataset.placementId, 10);
            showPlacementDetails(placementId);
        }
    });
}

function toggleLike(placementId) {
    console.log("Toggling like for placement:", placementId);
    // Add your like toggle logic here if needed.
    renderPlacements();
}

// --- Notification Rendering ---
function renderNotifications() {
    if (!notificationList) {
        console.error("notificationList element not found!");
        return;
    }
    notificationList.innerHTML = '';
    notifications.forEach(notification => {
        const listItem = document.createElement('li');
        listItem.classList.add('notification-list-item');
        listItem.innerHTML = `
            <div class="notification-info">
                <i class="material-icons notification-icon">info</i>
                <span class="notification-title">${notification.title}</span>
            </div>
        `;
        notificationList.appendChild(listItem);
    });
}

// --- Initialization ---
// IMPORTANT: Do not change header content here—let the Django template render it.
function initStudent() {
    console.log("student script js called")
    setupThemeToggle();
    setupSidebarToggle();
    setupNavigation();
    setupFilterButtons();
    setupDetailsBackButton();

    activatePage('placementsPage');
    renderPlacements();
    renderNotifications();
    // No code here alters the header elements (userName, userRole, etc.)
}

function setupFilterButtons() {
    const filterButtons = document.querySelectorAll('.filter-button');
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            currentFilter = button.dataset.filter;
            renderPlacements();
            filterButtons.forEach(b => b.classList.remove('active'));
            button.classList.add('active');
        });
    });
}
document.getElementById('navLogout').addEventListener('click', function() {
    fetch('/logout/', {
        method: 'GET',  // Use GET since it works manually
        credentials: 'same-origin'
    })
    .then(response => {
        if (response.redirected) {
            sessionStorage.clear();  // Clears frontend session storage
            window.location.href = response.url; // Redirect to login page
        } else {
            console.error('Logout failed: No redirection');
        }
    })
    .catch(error => console.error('Logout error:', error));
});


function setupDetailsBackButton() {
    if (detailsBackButton) {
        detailsBackButton.addEventListener('click', () => {
           activatePage('placementsPage');
        });
    }
}

initStudent();
