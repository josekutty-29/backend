// js/student_script.js

import {
    setupThemeToggle,
    setupSidebarToggle,
    setupNavigation,
    activatePage,
    placements,
    notifications,
    showPlacementDetails,
    studentData // Import studentData
} from './common.js';

// --- DOM Element References ---
const placementList = document.getElementById('placementList');
const notificationList = document.getElementById('notificationList');
const detailsPage = document.getElementById('detailsPage'); // Ensure this exists
const detailsPageTitle = document.getElementById('detailsPageTitle');
const detailsDescription = document.getElementById('detailsDescription');
const detailsBackButton = document.getElementById('detailsBackButton');
const profileName = document.getElementById('profileName');
const profileEmail = document.getElementById('profileEmail');
const profileCGPA = document.getElementById('profileCGPA');
const profileBacklogs = document.getElementById('profileBacklogs');




// --- Filtering ---
let currentFilter = 'available'; // 'available', 'liked', 'applied'

function getFilteredPlacements() {
    switch (currentFilter) {
        case 'available':
            return placements;
        case 'liked':
            return placements.filter(p => studentData.likedPlacements.includes(p.id));
        case 'applied':
            return placements.filter(p => studentData.appliedPlacements.includes(p.id));
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
        const isLiked = studentData.likedPlacements.includes(placement.id);

        listItem.innerHTML = `
            <div class="placement-info">
                <i class="material-icons placement-icon">business_center</i>
                <span class="placement-title">${placement.title}</span>
            </div>
            <div class="placement-actions">
                <button class="like-button" data-placement-id="${placement.id}">
                    <i class="material-icons">${isLiked ? 'favorite' : 'favorite_border'}</i>
                </button>
            </div>
        `;
        placementList.appendChild(listItem);
    });

    // --- Event Delegation (Correct and Efficient) ---
    placementList.addEventListener('click', (event) => {
        const likeButton = event.target.closest('.like-button');
        const placementItem = event.target.closest('.placement-list-item');

        if (likeButton) {
            // Handle Like Button Click
            const placementId = parseInt(likeButton.dataset.placementId, 10);
            toggleLike(placementId);
        } else if (placementItem) {
            // Handle Placement Item Click (excluding like button clicks)
            const placementId = parseInt(placementItem.dataset.placementId, 10);
            showPlacementDetails(placementId);
        }
    });
}

// --- Like Functionality ---
function toggleLike(placementId) {
    const index = studentData.likedPlacements.indexOf(placementId);
    if (index > -1) {
        studentData.likedPlacements.splice(index, 1); // Remove if already liked
    } else {
        studentData.likedPlacements.push(placementId); // Add if not liked
    }
    renderPlacements(); // Re-render to update like button icons
}



// --- Notification Rendering ---
function renderNotifications() {
    if (!notificationList) {
        console.error("notificationList element not found!");
        return;
    }
    notificationList.innerHTML = ''; // Clear previous notifications
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

// --- Profile Rendering ---
function renderStudentProfile() {


    if (profileName) profileName.textContent = studentData.name;
    if (profileEmail) profileEmail.textContent = studentData.email;
    if (profileCGPA) profileCGPA.textContent = studentData.cgpa;
    if (profileBacklogs) profileBacklogs.textContent = studentData.backlogs;
}

// --- Setup Functions ---
function setupFilterButtons() {
    const filterButtons = document.querySelectorAll('.filter-button');
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            currentFilter = button.dataset.filter;  // 'available', 'liked', 'applied'
            renderPlacements(); // Re-render with the new filter

            // Update active button style (optional, for visual feedback)
            filterButtons.forEach(b => b.classList.remove('active'));
            button.classList.add('active');
        });
    });
}

function setupDetailsBackButton() {
    if (detailsBackButton) {
        detailsBackButton.addEventListener('click', () => {
             activatePage('placementsPage'); // Go back to placements
        });
    }
}

// --- Initialization ---
function initStudent() {
    setupThemeToggle();      // From common.js
    setupSidebarToggle();    // From common.js
    setupNavigation();      // From common.js
    setupFilterButtons();  // NEW: Set up filter button listeners
    setupDetailsBackButton();

    activatePage('placementsPage');
    renderPlacements();
    renderNotifications();
    renderStudentProfile();

    // Set user info in the header
    const userName = document.getElementById('userName');
    const userRole = document.getElementById('userRole');
    const userAvatar = document.getElementById('userAvatar');

    if(userName) userName.textContent = studentData.name;
    if(userRole) userRole.textContent = 'Student';
    if(userAvatar) userAvatar.textContent = studentData.name.charAt(0).toUpperCase(); // First letter, uppercase
}

initStudent(); // Call the init function