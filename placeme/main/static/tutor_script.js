import {
    setupThemeToggle,
    setupSidebarToggle,
    setupNavigation,
    activatePage,
    placements,
    renderPlacements,
    showPlacementDetails
} from './common.js';

// --- DOM Element References ---
const placementList = document.getElementById('placementList');
const studentList = document.getElementById('studentList');
const navLogout = document.getElementById('navLogout');

// --- Tutor Data (Placeholder for student list) ---
let students = [
    { id: "s1", name: "Student 1", rollNo: "KGR22CS001" },
    { id: "s2", name: "Student 2", rollNo: "KGR22CS002" },
];

// --- Page Navigation ---
// For logout, simply redirect (since /logout/ works manually)
if (navLogout) {
    navLogout.addEventListener('click', () => {
        window.location.href = "index.html";
    });
}

// --- Tutor Placement Functions ---
function renderPlacementsForTutor() {
    console.log("renderPlacementsForTutor called");
    if (!placementList) {
        console.error("placementList is NULL inside renderPlacementsForTutor");
        return;
    }
    // Render placements using the shared function
    renderPlacements(placements, placementList, false);

    // Attach event listener for click events on placementList
    placementList.addEventListener('click', (event) => {
        const placementItem = event.target.closest('.placement-list-item');
        if (placementItem) {
            const placementId = parseInt(placementItem.dataset.placementId, 10);
            console.log("placementId:", placementId);
            showPlacementDetails(placementId, "tutor");
        }
    });
}

// --- Tutor Student Functions ---
function renderStudents() {
    if (!studentList) {
        console.error("studentList is NULL inside renderStudents");
        return;
    }
    studentList.innerHTML = '';
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
        `;
        studentList.appendChild(listItem);
    });
    studentList.addEventListener('click', (event) => {
        const editButton = event.target.closest('.edit-student-button');
        if (editButton) {
            const studentId = editButton.dataset.studentId;
            openEditStudentModal(studentId);
        }
    });
}

// --- Tutor Profile Rendering ---
// Remove any static assignment; assume the template already renders the correct tutor info.
function renderTutorProfile() {
    // Do nothing here so that the server-rendered profile remains intact.
}

// --- Modal Functions ---
let currentEditingStudentId = null;
function openEditStudentModal(studentId) {
    const student = students.find(s => s.id === studentId);
    if (!student) {
        console.error("Student not found:", studentId);
        return;
    }
    currentEditingStudentId = studentId;
    document.getElementById('studentName').value = student.name;
    document.getElementById('studentRollNo').value = student.rollNo;
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
    currentEditingStudentId = null;
}

function saveStudentChanges() {
    if (!currentEditingStudentId) return;
    const student = students.find(s => s.id === currentEditingStudentId);
    if (!student) {
        console.error("Student not found for editing:", currentEditingStudentId);
        return;
    }
    const newName = document.getElementById('studentName').value;
    const newRollNo = document.getElementById('studentRollNo').value;
    student.name = newName;
    student.rollNo = newRollNo;
    renderStudents();
    closeEditStudentModal();
}

const modalSave = document.querySelector('#editStudentModal .modal-save');
if (modalSave) {
    modalSave.addEventListener('click', saveStudentChanges);
}

const modalCancel = document.querySelector('#editStudentModal .modal-cancel');
if (modalCancel) {
    modalCancel.addEventListener('click', closeEditStudentModal);
}

// --- Setup Filter Buttons ---
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

// --- Setup Details Back Button ---
function setupDetailsBackButton() {
    const detailsBackButton = document.getElementById('detailsBackButton');
    if (detailsBackButton) {
        detailsBackButton.addEventListener('click', () => {
            activatePage('placementsPage');
        });
    }
}

// --- Initialization (Tutor) ---
function initTutor() {
    console.log("initTutor called");
    setupThemeToggle();
    setupSidebarToggle();
    setupNavigation();

    activatePage('placementsPage');
    renderPlacementsForTutor();
    renderStudents();
    renderTutorProfile();
    // Removed any call that sets header info (like setUserInfo) so the template header remains.
}

// Initialize when DOM is fully loaded
document.addEventListener("DOMContentLoaded", initTutor);
