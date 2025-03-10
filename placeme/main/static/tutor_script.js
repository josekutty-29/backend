// js/tutor_script.js
import {
    setupThemeToggle,
    setupSidebarToggle,
    setupNavigation,
    activatePage,
    placements,
    renderPlacements,
    setUserInfo,
    showPlacementDetails
} from './common.js';

// --- DOM Element References ---
const placementList = document.getElementById('placementList');
const studentList = document.getElementById('studentList');
// ... other DOM element references ...
const navLogout = document.getElementById('navLogout');
console.log("placementList (outside functions):", placementList); // Check *before* functions

// --- Tutor Data (Placeholder) ---
let students = [
    { id: "s1", name: "Student 1", rollNo: "KGR22CS001" },
     { id: "s2", name: "Student 2", rollNo: "KGR22CS002" },
];

// --- Page Navigation ---
navLogout.addEventListener('click', () => window.location.href = "index.html");

// --- Tutor Placement Functions ---
function renderPlacementsForTutor() {
    console.log("renderPlacementsForTutor called");
    console.log("placements (inside renderPlacementsForTutor):", placements); // Log imported placements

    if (!placementList) {
        console.error("placementList is NULL inside renderPlacementsForTutor");
        return; // Exit if placementList is null
    }

    renderPlacements(placements, placementList, false); // Use imported placements

    placementList.addEventListener('click', (event) => {
        // ... (event delegation logic, no changes needed here) ...
         console.log("placementList click event:", event); // Log the entire event
        const placementItem = event.target.closest('.placement-list-item');
        console.log("placementItem:", placementItem);  // Log the found item

        if (placementItem) {
            const placementId = parseInt(placementItem.dataset.placementId, 10);
            console.log("placementId:", placementId, typeof placementId); // Log ID and type
            showPlacementDetails(placementId, "tutor");
        }
    });
}

// --- Tutor student functions (Read only for now)
function renderStudents() {
    if (!studentList) {
        console.error("studentList is NULL inside renderStudents");
        return;
    }
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
                <button class="edit-student-button" data-student-id="${student.id}">Edit</button>
            </div>

        `; //No edit button
        studentList.appendChild(listItem);
    });
     // Event Delegation for Edit Buttons (within renderStudents)
    studentList.addEventListener('click', (event) => {
        const editButton = event.target.closest('.edit-student-button');
        if (editButton) {
            const studentId = editButton.dataset.studentId;
            openEditStudentModal(studentId);
        }
    });
}

// --- Tutor-Specific Profile ---
// ... (renderTutorProfile - no changes needed) ...
function renderTutorProfile() {
    const profileName = document.getElementById('profileName');
    const profileEmail = document.getElementById('profileEmail');
    const profileSemester = document.getElementById('profileSemester');
    const profileDivision = document.getElementById('profileDivision');
    const profileNumStudents = document.getElementById('profileNumStudents');
    const tutorDetails = document.getElementById('tutorDetails');
    if(profileName) profileName.textContent = 'Tutor Name';  // Replace with actual data
    if(profileEmail) profileEmail.textContent = 'tutor@example.com'; // Replace
    if(profileSemester) profileSemester.textContent = 'Fall 2024'; // Replace
    if(profileDivision) profileDivision.textContent = 'A';      // Replace
    if(profileNumStudents) profileNumStudents.textContent = '50';       // Replace
    if(tutorDetails) tutorDetails.style.display = 'block'; // Show tutor details
}
// --- Initialization (Tutor) ---
function initTutor() {
    console.log("initTutor called");
    setupThemeToggle();
    setupSidebarToggle();
    setupNavigation();

    activatePage('placementsPage');
    renderPlacementsForTutor(); // This should render the placements
    renderStudents();
    renderTutorProfile();
    setUserInfo('Tutor Name', 'Tutor', 'T');
}

initTutor();

// --- Modal Functions (Add these) ---

let currentEditingStudentId = null; // Keep track of which student is being edited

function openEditStudentModal(studentId) {
    const student = students.find(s => s.id === studentId);
    if (!student) {
        console.error("Student not found:", studentId);
        return;
    }

    currentEditingStudentId = studentId;

    // Populate the modal with student data
    document.getElementById('studentName').value = student.name;
    document.getElementById('studentRollNo').value = student.rollNo;

    // Show the modal
    const modal = document.getElementById('editStudentModal');
    if (modal) {
        modal.classList.add('modal-open');
    } else {
        console.error("editStudentModal not found!");
    }
}

function closeEditStudentModal() {
    const modal = document.getElementById('editStudentModal');
    if (modal) {
        modal.classList.remove('modal-open');
    }
    currentEditingStudentId = null; // Reset the ID
}


function saveStudentChanges() {
    if (!currentEditingStudentId) return;

    const student = students.find(s => s.id === currentEditingStudentId);
    if (!student) {
        console.error("Student not found for editing:", currentEditingStudentId);
        return;
    }

    // Get values from form
    const newName = document.getElementById('studentName').value;
    const newRollNo = document.getElementById('studentRollNo').value;

    // Update student data
    student.name = newName;
    student.rollNo = newRollNo;

    // Re-render the student list
    renderStudents();

    // Close the modal
    closeEditStudentModal();
}
// Event listener for the modal's Save button
const modalSave = document.querySelector('#editStudentModal .modal-save'); //added event listener here as tutor and student have diff pages.
    if (modalSave) {
        modalSave.addEventListener('click', saveStudentChanges);
    }
 const modalCancel = document.querySelector('#editStudentModal .modal-cancel');
if (modalCancel) {
    modalCancel.addEventListener('click', closeEditStudentModal);
}