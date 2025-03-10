document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('studentForm');

    form.addEventListener('submit', function(event) {
        let isValid = true;

        // Reset error messages
        document.querySelectorAll('.error-message').forEach(element => {
            element.textContent = '';
        });

        // Validation for Registration Number
        const reg_no = document.getElementById('reg_no').value.trim();
        if (reg_no === '') {
            document.getElementById('reg_no_error').textContent = 'Registration Number is required.';
            isValid = false;
        }

        // Validation for User
        const user = document.getElementById('user').value;
        if (user === '') {
            document.getElementById('user_error').textContent = 'Please select a user.';
            isValid = false;
        }

        // Validation for Department
        const department = document.getElementById('department').value.trim();
        if (department === '') {
            document.getElementById('department_error').textContent = 'Department is required.';
            isValid = false;
        }

         // Validation for Semester
         const semester = document.getElementById('semester').value;
        if (semester === '') {
            document.getElementById('semester_error').textContent = 'Please select a semester.';
            isValid = false;
        }

        // Validation for Division
        const division = document.getElementById('division').value.trim();
        if (division === '') {
            document.getElementById('division_error').textContent = 'Division is required.';
            isValid = false;
        }

        // Validation for Batch
        const batch = document.getElementById('batch').value.trim();
        if (batch === '') {
            document.getElementById('batch_error').textContent = 'Batch is required.';
            isValid = false;
        }

        if (!isValid) {
            event.preventDefault(); // Prevent form submission if there are errors
        }
    });
});