// js/script.js

// --- DOM Element References ---
const sidebar = document.getElementById('sidebar');
const sidebarToggle = document.getElementById('sidebarToggle');
const navPlacements = document.getElementById('navPlacements');
const navStudents = document.getElementById('navStudents');
const navLogout = document.getElementById('navLogout');
const viewProfileButton = document.getElementById('viewProfileButton');
const placementsPage = document.getElementById('placementsPage');
const studentsPage = document.getElementById('studentsPage');
const profilePage = document.getElementById('profilePage');
const themeToggle = document.getElementById('themeToggle');
const body = document.body;
const appHeader = document.querySelector('.app-header'); // Get the header


// --- Placements ---
const addPlacementBtn = document.getElementById('addPlacementBtn');
const placementModal = document.getElementById('placementModal');
const closePlacementModal = document.getElementById('closePlacementModal');
const savePlacementBtn = document.getElementById('savePlacement');
const cancelPlacementBtn = document.getElementById('cancelPlacement');
const placementList = document.getElementById('placementList');

// --- Students ---
const studentModal = document.getElementById('studentModal');
const closeStudentModal = document.getElementById('closeStudentModal');
const saveStudentBtn = document.getElementById('saveStudent');
const cancelStudentBtn = document.getElementById('cancelStudent');
const studentList = document.getElementById('studentList');
const sortStudentsBtn = document.getElementById('sortStudents');
const filterStudentsBtn = document.getElementById('filterStudents');
const exportStudentsBtn = document.getElementById('exportStudentsBtn');
const uploadGradeSheetBtn = document.getElementById('uploadGradeSheetBtn');

// --- Data (Placeholder) ---
let placements = [
    { id: 1, title: "Placement Offer 1", description: "Description 1", stipend: '10000', location: 'kochi', skillSet: 'full stack', contact: 'placement1@gmail.com' },
    { id: 2, title: "Placement Offer 2", description: "Description 2", stipend: '15000', location: 'Banglore', skillSet: 'AI', contact: 'placement2@gmail.com' },
];
let students = [
    { id: "s1", name: "Student 1", rollNo: "KGR22CS001" },
];
let currentPlacementId = null;
let currentStudentId = null;


// --- Theme Switching ---
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'light') {
    body.classList.remove('theme-dark');
    body.classList.add('theme-light');
} else {
    body.classList.add('theme-dark');
    body.classList.remove('theme-light');
    localStorage.setItem('theme', 'dark'); // Ensure localStorage is set
}

themeToggle.addEventListener('click', () => {
    body.classList.toggle('theme-dark');
    body.classList.toggle('theme-light');
    localStorage.setItem('theme', body.classList.contains('theme-light') ? 'light' : 'dark');
});

// --- Sidebar Toggle ---
sidebarToggle.addEventListener('click', () => {
    sidebar.classList.toggle('sidebar-collapsed');
    // Add/remove 'sidebar-expanded' for persistent expanded state.
    if (sidebar.classList.contains('sidebar-collapsed')) {
        sidebar.classList.remove('sidebar-expanded');
    } else {
        sidebar.classList.add('sidebar-expanded');
    }
});

// --- Page Navigation ---
function activatePage(pageId) {
    document.querySelectorAll('.page').forEach(page => {
        page.classList.remove('active-page');
    });
    document.getElementById(pageId).classList.add('active-page');

    document.querySelectorAll('.nav-button').forEach(button => {
        button.classList.remove('active');
    });

    const activeButton = document.querySelector(`.nav-button[data-page="${pageId}"]`);
    if (activeButton) {
        activeButton.classList.add('active');
    }

    // Show/hide the header based on the active page
    if (pageId === 'profilePage') {
        appHeader.classList.add('header-hidden'); // Add class to hide header
    } else {
        appHeader.classList.remove('header-hidden'); // Remove class to show header
    }
}

// Event delegation for navigation
document.querySelector('.sidebar-nav').addEventListener('click', (event) => {
    const target = event.target.closest('.nav-button');
    if (target) {
        const pageId = target.dataset.page;
        if (pageId) {
            activatePage(pageId);
            if (pageId === 'placementsPage') {
                renderPlacements();
            } else if (pageId === 'studentsPage'){
                renderStudents();
            }
        }
    }
});

viewProfileButton.addEventListener('click', () => activatePage('profilePage'));
//navLogout.addEventListener('click', () => window.location.href = "/logout/");


// --- Placement and Student Management Functions (No Changes Here) ---
// ... (Your existing placement and student functions: renderPlacements, openPlacementModal, etc.) ...
// --- Placement Management Functions -------

        function renderPlacements() {
            placementList.innerHTML = '';
            placements.forEach(placement => {
                const listItem = document.createElement('li');
                listItem.classList.add('placement-list-item');
                listItem.dataset.itemId = placement.id;
                listItem.innerHTML = `
                     <div class="placement-info">
                          <i class="material-icons placement-icon">business_center</i>
                        <span>${placement.title}</span>
                    </div>
                    <div class="placement-actions">
                        <button class="app-button-icon edit-placement" data-id="${placement.id}">
                            <i class="material-icons">edit</i>
                        </button>
                        <button class="app-button-icon delete-placement" data-id="${placement.id}">
                            <i class="material-icons">delete</i>
                        </button>
                    </div>
                `;
                placementList.appendChild(listItem);
            });
        }
 // Event delegation for placement actions
placementList.addEventListener('click', (event) => {
    const target = event.target;
    if (target.closest('.edit-placement')) {
        const placementId = parseInt(target.closest('.edit-placement').dataset.id);
        editPlacement(placementId);
    } else if (target.closest('.delete-placement')) {
        const placementId = parseInt(target.closest('.delete-placement').dataset.id);
        deletePlacement(placementId);
    }
});
  function openPlacementModal(placement = null){
            // Populate modal fields if editing
             if (placement) {
                 currentPlacementId = placement.id;
                 document.getElementById('placementTitle').value = placement.title;
                 document.getElementById('placementDescription').value = placement.description;
                 document.getElementById('placementStipend').value = placement.stipend;
                 document.getElementById('placementLocation').value = placement.location;
                 document.getElementById('placementSkillSet').value = placement.skillSet;
                 document.getElementById('placementContact').value = placement.contact;
             } else{

                 currentPlacementId = null;
                 document.getElementById('placementTitle').value = '';
                 document.getElementById('placementDescription').value = '';
                 document.getElementById('placementStipend').value = '';
                 document.getElementById('placementLocation').value = '';
                 document.getElementById('placementSkillSet').value = '';
                 document.getElementById('placementContact').value = '';

             }
             placementModal.classList.add('modal-open'); // Use class for visibility
        }

        function editPlacement(id) {
             const placement = placements.find(p => p.id === id);
            if(placement){
                openPlacementModal(placement);
            }
         }
        function deletePlacement(id) {
            const confirmed = confirm('Are you sure you want to delete this placement?');
            if (confirmed) {
                placements = placements.filter(p => p.id !== id);
                 renderPlacements(); // Re-render the list
             }
         }
        function savePlacement() {
             // Get values from form fields
            const title = document.getElementById('placementTitle').value;
            const description = document.getElementById('placementDescription').value;
            const stipend = document.getElementById('placementStipend').value;
            const location = document.getElementById('placementLocation').value;
            const skillSet = document.getElementById('placementSkillSet').value;
            const contact = document.getElementById('placementContact').value;

            // Basic validation
            if (!title || !description) {
                alert('Please fill in all required fields.');
                return;
            }

             // Update or create placement
            if (currentPlacementId) {
                 // Edit existing placement
                const index = placements.findIndex(p => p.id === currentPlacementId);
                placements[index] = { id: currentPlacementId, title, description, stipend, location, skillSet, contact };
            } else {
                // Create new placement
                 const newPlacement = {
                    id: Date.now(), // Unique ID
                    title,
                    description,
                    stipend,
                    location,
                    skillSet,
                    contact
                };
                placements.push(newPlacement);
             }
             renderPlacements(); // Re-render the list
             closePlacementModalFunc(); // Close the modal
        }
        function closePlacementModalFunc() {
              placementModal.classList.remove('modal-open');
         }

         addPlacementBtn.addEventListener('click', () => openPlacementModal());
         closePlacementModal.addEventListener('click', closePlacementModalFunc);
         savePlacementBtn.addEventListener('click', savePlacement);
         cancelPlacementBtn.addEventListener('click', closePlacementModalFunc);

 // ------- Student Management Functions -------

        function renderStudents() {
           studentList.innerHTML = ''; // Clear previous list items

            students.forEach(student => {
                const listItem = document.createElement('li');
                 listItem.classList.add('student-list-item');
                listItem.dataset.itemId = student.id;

                listItem.innerHTML = `
                    <div class="student-info">
                        <i class="material-icons student-icon">person</i>
                        <span class="student-name">${student.name}</span>
                        <span class="student-rollno">(${student.rollNo})</span>
                    </div>
                    <div class="student-actions">
                        <button class="app-button-icon edit-student" data-id="${student.id}">
                            <i class="material-icons">edit</i>
                        </button>
                    </div>
                `;
                studentList.appendChild(listItem);
            });
        }
      // Event delegation for student actions
studentList.addEventListener('click', (event) => {
    const target = event.target;
    if (target.closest('.edit-student')) {
        const studentId = target.closest('.edit-student').dataset.id;
        editStudent(studentId);
    }
});
        function openStudentModal(student = null) {
           if (student) {
                currentStudentId = student.id;
                document.getElementById('studentName').value = student.name;
                document.getElementById('studentRollNo').value = student.rollNo;
            } else {
                currentStudentId = null;
                document.getElementById('studentName').value = '';
                document.getElementById('studentRollNo').value = '';
            }
            studentModal.classList.add('modal-open'); // Use class for visibility
        }

        function editStudent(id) {
            const student = students.find(s => s.id === id);
            if (student) {
                openStudentModal(student);
            }
        }

        function saveStudent() {
            const name = document.getElementById('studentName').value;
            const rollNo = document.getElementById('studentRollNo').value;

            if (!name || !rollNo) {
                alert('Please fill in all fields.');
                return;
            }

             if (currentStudentId) {
                // Edit existing student
                const index = students.findIndex(s => s.id === currentStudentId);
                students[index] = { id: currentStudentId, name, rollNo };
            } else {
                // Create new student
                const newStudent = { id: 's' + Date.now(), name, rollNo }; //  's' prefix
                students.push(newStudent);
            }

             renderStudents();
             closeStudentModalFunc();
        }

         function closeStudentModalFunc() {
            studentModal.classList.remove('modal-open');
         }
        closeStudentModal.addEventListener('click', closeStudentModalFunc);
        saveStudentBtn.addEventListener('click', saveStudent);
        cancelStudentBtn.addEventListener('click', closeStudentModalFunc);

        sortStudentsBtn.addEventListener('click', () => {
            alert('Sort functionality would be implemented here.');
        });

        filterStudentsBtn.addEventListener('click', () => {
            alert('Filter functionality would be implemented here.');
        });

        exportStudentsBtn.addEventListener('click', () => {
            alert('Export functionality would be implemented here.');
        });
        uploadGradeSheetBtn.addEventListener('click',()=>{
             alert('Upload Grade Sheet functionality would be implemented here.');
        });
// --- DOM Element References ---
// ... (existing references) ...
const backButton = document.getElementById('backButton'); // Add back button
let previousPage = 'placementsPage'; // Keep track of the previous page, default to placements

// --- Page Navigation ---
function activatePage(pageId) {
    document.querySelectorAll('.page').forEach(page => {
        page.classList.remove('active-page');
    });
    document.getElementById(pageId).classList.add('active-page');

    document.querySelectorAll('.nav-button').forEach(button => {
        button.classList.remove('active');
    });

    const activeButton = document.querySelector(`.nav-button[data-page="${pageId}"]`);
    if (activeButton) {
        activeButton.classList.add('active');
    }

    if (pageId === 'profilePage') {
        appHeader.classList.add('header-hidden');
    } else {
        appHeader.classList.remove('header-hidden');
        previousPage = pageId; // Store the previous page (except when going to profile)
    }
}

// ... (rest of your navigation, placement, and student functions) ...

// Add event listener for the back button:
backButton.addEventListener('click', () => {
    activatePage(previousPage); // Go back to the stored previous page
});

// ... (rest of your script.js) ...
// --- Initial Setup ---
activatePage('placementsPage');
renderPlacements();