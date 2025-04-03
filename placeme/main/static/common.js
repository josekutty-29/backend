// common.js

// --- Data ---
export const placements = [
    { id: 1, title: "Software Engineer Intern", description: "Join our team...", company: "Acme Corp", stipend: '10000', location: 'kochi', skillSet: 'full stack', contact: 'placement1@gmail.com' },
    { id: 2, title: "Data Analyst", description: "Analyze data...", company: "Beta Solutions", stipend: '15000', location: 'Banglore', skillSet: 'AI', contact: 'placement2@gmail.com' },
    { id: 3, title: "Frontend Developer", description: "Develop and maintain user interfaces...", company: "Gamma Tech" },
    { id: 4, title: "Backend Developer", description: "Build and maintain server-side logic...", company: "Delta Systems" },
    { id: 5, title: "Full Stack Developer", description: "Work on both frontend and backend...", company: "Epsilon Innovations" },
    { id: 6, title: "UI/UX Designer", description: "Design intuitive and engaging user interfaces...", company: "Zeta Designs" },
];

export const notifications = [
    { id: 1, title: "New Placement Added!" },
    { id: 2, title: "Deadline Approaching" },
    { id: 3, title: "Application Status Update" }
];

// --- Sidebar Toggle ---
export function setupSidebarToggle() {
    const sidebarToggle = document.getElementById('sidebarToggle');
    const sidebar = document.getElementById('sidebar');
    if (sidebarToggle && sidebar) {
        sidebarToggle.addEventListener('click', () => {
            sidebar.classList.toggle('sidebar-collapsed');
            sidebar.classList.toggle('sidebar-expanded', !sidebar.classList.contains('sidebar-collapsed'));
        });
    }
}

// --- Navigation ---
export function setupNavigation() {
    document.querySelector('.sidebar-nav')?.addEventListener('click', (event) => {
        const target = event.target.closest('.nav-button');
        if (target) {
            const pageId = target.dataset.page;
            if (pageId) {
                activatePage(pageId);
            }
        }
    });

    const backButton = document.getElementById('backButton'); 
    if (backButton) {
        backButton.addEventListener('click', () => {
            activatePage('placementsPage');
        });
    }

    const viewProfileButton = document.getElementById('viewProfileButton');
    if (viewProfileButton) {
        viewProfileButton.addEventListener('click', () => {
            activatePage('profilePage');
        });
    }
}

export function activatePage(pageId) {
    if (!pageId) return; // Prevent errors if pageId is undefined or null

    // Deactivate all pages
    document.querySelectorAll('.page').forEach(page => {
        page.classList.remove('active-page');
    });

    // Activate the target page if it exists
    const page = document.getElementById(pageId);
    if (page) {
        page.classList.add('active-page');
    }

    // Deactivate all navigation buttons
    document.querySelectorAll('.nav-button').forEach(button => {
        button.classList.remove('active');
    });

    // Activate the corresponding navigation button
    const activeButton = document.querySelector(`.nav-button[data-page="${pageId}"]`);
    if (activeButton) {
        activeButton.classList.add('active');
    }

    // Toggle header visibility based on the active page
    const appHeader = document.querySelector('.app-header');
    if (appHeader) {
        if (pageId === 'profilePage') {
            appHeader.classList.add('header-hidden');
        } else {
            appHeader.classList.remove('header-hidden');
        }
    }
}

// --- Placement Rendering (Shared) ---
export function renderPlacements(placements, placementList, showActions = false) {
    if (!placementList) return;
    placementList.innerHTML = '';
    placements.forEach(placement => {
        const listItem = document.createElement('li');
        listItem.classList.add('placement-list-item');
        listItem.dataset.placementId = placement.id;
        let actionsHTML = '';
        if (showActions) {
            // For tutor actions if needed
        } else {
            const isLiked = false; // You can update this if you have dynamic liked data
            actionsHTML = `<div class="placement-actions">
                <button class="like-button" data-placement-id="${placement.id}">
                    <i class="material-icons">${isLiked ? 'favorite' : 'favorite_border'}</i>
                </button>
            </div>`;
        }
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
    // Implement toggle functionality as needed
    renderPlacements(placements, document.getElementById('placementList'));
}

// --- Notification Rendering ---
export function renderNotifications() {
    const notificationList = document.getElementById('notificationList');
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

// --- Show Placement Details (Shared) ---
export function showPlacementDetails(placementId, userRole = "student") {
    const placement = placements.find(p => p.id === placementId);
    if (!placement) {
        console.error("Placement not found:", placementId);
        return;
    }
    const detailsPage = document.getElementById('detailsPage');
    if (!detailsPage) {
        console.error("detailsPage element not found!");
        return;
    }
    const detailsPageTitle = document.getElementById('detailsPageTitle');
    const detailsDescription = document.getElementById('detailsDescription');
    if (detailsPageTitle) detailsPageTitle.textContent = placement.title;
    if (detailsDescription) detailsDescription.textContent = placement.description;
    
    // Conditional button creation (if student)
    let actionButton = null;
    if (userRole === "student") {
        actionButton = document.createElement('button');
        actionButton.textContent = 'Register';
        actionButton.classList.add('app-button');
        actionButton.dataset.placementId = placementId;
        actionButton.addEventListener('click', () => {
            handleRegistration(placementId);
        });
    }
    const existingButton = detailsPage.querySelector('.app-button');
    if (existingButton) {
        detailsPage.removeChild(existingButton);
    }
    if (actionButton) {
        detailsPage.appendChild(actionButton);
    }
    activatePage('detailsPage');
}

function handleRegistration(placementId) {
    // Your registration logic here
    console.log("handleRegistration called with placementId:", placementId);
}

// --- Initialization ---
// Ensure we do not override header info so that the server-rendered user name remains intact.
function initStudent() {
    setupThemeToggle();
    setupSidebarToggle();
    setupNavigation();
    setupFilterButtons();
    setupDetailsBackButton();
    activatePage('placementsPage');
    renderPlacements(placements, document.getElementById('placementList'));
    renderNotifications();
    // DO NOT override header information here; let the Django template display the correct user data.
}

function setupFilterButtons() {
    const filterButtons = document.querySelectorAll('.filter-button');
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            currentFilter = button.dataset.filter;
            renderPlacements(placements, document.getElementById('placementList'));
            filterButtons.forEach(b => b.classList.remove('active'));
            button.classList.add('active');
        });
    });
}

function setupDetailsBackButton() {
    const detailsBackButton = document.getElementById('detailsBackButton');
    if (detailsBackButton) {
        detailsBackButton.addEventListener('click', () => {
            activatePage('placementsPage');
        });
    }
}

initStudent();
function setTheme(themeName) {
    localStorage.setItem('theme', themeName);
    document.documentElement.className = themeName;
}

function toggleTheme() {
    if (localStorage.getItem('theme') === 'theme-dark') {
        setTheme('theme-light');
    } else {
        setTheme('theme-dark');
    }
}

(function () {
    if (localStorage.getItem('theme') === 'theme-dark') {
        setTheme('theme-dark');
    } else {
        setTheme('theme-light');  // Default to light theme
    }
})();