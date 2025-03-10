// common.js

// --- Data ---
export const placements = [
    { id: 1, title: "Software Engineer Intern", description: "Join our team...", company: "Acme Corp", stipend: '10000', location: 'kochi', skillSet: 'full stack', contact: 'placement1@gmail.com' },
    { id: 2, title: "Data Analyst", description: "Analyze data...", company: "Beta Solutions",  stipend: '15000', location: 'Banglore', skillSet: 'AI', contact: 'placement2@gmail.com' },
    {id: 3,title: "Frontend Developer",description: "Develop and maintain user interfaces...",company: "Gamma Tech",},
    {id: 4,title: "Backend Developer",description: "Build and maintain server-side logic...",company: "Delta Systems",},
    {id: 5,title: "Full Stack Developer",description: "Work on both frontend and backend...",company: "Epsilon Innovations",},
    {id: 6,title: "UI/UX Designer",description: "Design intuitive and engaging user interfaces...",company: "Zeta Designs",},
];

export const notifications = [ // Example - you might not need this for the tutor
    { id: 1, title: "New Placement Added!" },
    { id: 2, title: "Deadline Approaching" },
    { id: 3, title: "Application Status Update" }
];

export let studentData = {
    likedPlacements: [],
    appliedPlacements: [],
    name: 'Student Name',
    email: 'student@example.com',
    cgpa: '8.5',
    backlogs: '0'
};


// --- Theme Toggle ---
export function setupThemeToggle() {
    const themeToggle = document.getElementById('themeToggle');
    if (themeToggle) {
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme === 'light') {
            document.body.classList.remove('theme-dark');
            document.body.classList.add('theme-light');
        } else {
            document.body.classList.add('theme-dark');  // Default to dark if no saved theme
            document.body.classList.remove('theme-light');
            localStorage.setItem('theme', 'dark'); // Set default in localStorage
        }

        themeToggle.addEventListener('click', () => {
            document.body.classList.toggle('theme-dark');
            document.body.classList.toggle('theme-light');
            localStorage.setItem('theme', document.body.classList.contains('theme-light') ? 'light' : 'dark');
        });
    }
}

// --- Sidebar Toggle ---
export function setupSidebarToggle() {
    const sidebarToggle = document.getElementById('sidebarToggle');
    const sidebar = document.getElementById('sidebar');
    if (sidebarToggle && sidebar) {
        sidebarToggle.addEventListener('click', () => {
            sidebar.classList.toggle('sidebar-collapsed');
            // Add/remove 'sidebar-expanded' for persistent expanded state.
            sidebar.classList.toggle('sidebar-expanded', !sidebar.classList.contains('sidebar-collapsed'));
        });
    }
}

// --- Navigation ---
export function setupNavigation() {
    document.querySelector('.sidebar-nav')?.addEventListener('click', (event) => { // Use optional chaining
        const target = event.target.closest('.nav-button');
        if (target) {
            const pageId = target.dataset.page;
            if (pageId) {
                activatePage(pageId);
            }
        }
    });

     const backButton = document.getElementById('backButton'); //For profile page.
        if(backButton){
            backButton.addEventListener('click', () => {
            activatePage('placementsPage'); // Go back to the placements page
        });
    }
     // View Profile button event listener
    const viewProfileButton = document.getElementById('viewProfileButton');
    if (viewProfileButton) {
        viewProfileButton.addEventListener('click', () => {
            activatePage('profilePage');
        });
    }
}

export function activatePage(pageId) {
    document.querySelectorAll('.page').forEach(page => {
        page.classList.remove('active-page');
    });
    const page = document.getElementById(pageId);
    if (page) {
        page.classList.add('active-page');
    }

    document.querySelectorAll('.nav-button').forEach(button => {
        button.classList.remove('active');
    });
    const activeButton = document.querySelector(`.nav-button[data-page="${pageId}"]`);
    if (activeButton) {
        activeButton.classList.add('active');
    }

    const appHeader = document.querySelector('.app-header'); // Get header for hiding
     if (pageId === 'profilePage') {
        if(appHeader) appHeader.classList.add('header-hidden');
    } else {
        if(appHeader) appHeader.classList.remove('header-hidden');
    }
}

// --- Placement Rendering (Shared) ---
export function renderPlacements(placements, placementList, showActions = false) {
  if(!placementList) return;
    placementList.innerHTML = '';
    placements.forEach(placement => {
        const listItem = document.createElement('li');
        listItem.classList.add('placement-list-item');
        listItem.dataset.placementId = placement.id; // Store ID for later use

        let actionsHTML = '';
        if (showActions) {
            //  actions for tutor
        }
        else{
              const isLiked = studentData.likedPlacements.includes(placement.id);
              actionsHTML = ` <div class="placement-actions">
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
}

// --- Set User Info in Header (Shared) ---
export function setUserInfo(name, role, avatarText) {
    const userName = document.getElementById('userName');
    const userRole = document.getElementById('userRole');
    const userAvatar = document.getElementById('userAvatar');

    if (userName) userName.textContent = name;
    if (userRole) userRole.textContent = role;
    if (userAvatar) userAvatar.textContent = avatarText;
}
// --- Show Placement Details (Shared, from previous responses) ---

export function showPlacementDetails(placementId, userRole = "student") { // Add userRole parameter
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

    // --- Conditional Button (Register for Student, Edit/Delete for Tutor) ---
    let actionButton = null;
    if (userRole === "student") {
        actionButton = document.createElement('button');
        actionButton.textContent = studentData.appliedPlacements.includes(placementId) ? 'Registered' : 'Register';
        actionButton.classList.add('app-button');
        actionButton.disabled = studentData.appliedPlacements.includes(placementId);
        actionButton.dataset.placementId = placementId;

        actionButton.addEventListener('click', () => {
            handleRegistration(placementId);
        });
    } else if (userRole === "tutor") {
      //placeholder for tutor
    }

    // --- Clear and Append Button ---
    const existingButton = detailsPage.querySelector('.app-button'); // Or a more general selector
    if (existingButton) {
        detailsPage.removeChild(existingButton);
    }
      if (actionButton) { // Append only if a button was created
        detailsPage.appendChild(actionButton);
    }


    activatePage('detailsPage');
}
// --- Handle Registration (Moved from student_script.js) ---
function handleRegistration(placementId) {
	console.log("handleRegistration called with placementId:", placementId);
    if (!studentData.appliedPlacements.includes(placementId)) {
        studentData.appliedPlacements.push(placementId);
        // Update button state immediately:
        const registerButton = document.querySelector(`#detailsPage [data-placement-id="${placementId}"]`);
        if (registerButton) {
            registerButton.textContent = 'Registered';
            registerButton.disabled = true;
        }
			renderPlacements(placements, placementList); // Re-render placements after registration
    }

}
