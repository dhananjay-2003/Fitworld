
    document.addEventListener('DOMContentLoaded', function () {
        const form = document.getElementById('appointmentformbook');

        form.addEventListener('submit', function (event) {
            if (!validateForm()) {
                event.preventDefault(); // Prevent form submission if validation fails
            }
        });

        function validateForm() {
            let isValid = true;

            // Reset previous error styles
            resetErrors();

            // Validate each form field
            const fname = document.getElementById('fname');
            const lname = document.getElementById('lname');
            const mobile = document.getElementById('mobile');
            const email = document.getElementById('email');
            const date = document.getElementById('date');
            const time = document.getElementById('time');
            const courseSelect = document.getElementById('course');
            const message = document.getElementById('message');

            isValid = validateField(fname, 'First Name is required.') && isValid;
            isValid = validateField(lname, 'Last Name is required.') && isValid;
            isValid = validateField(mobile, 'Phone Number is required.') && isValid;
            isValid = validatePhone(mobile.value) && isValid;
            isValid = validateField(email, 'Email is required.') && isValid;
            isValid = validateEmail(email.value) && isValid;
            isValid = validateField(date, 'Date is required.') && isValid;
            isValid = validateField(time, 'Time is required.') && isValid;
            isValid = validateField(courseSelect, 'Please select a Purpose.') && isValid;
            isValid = validateField(message, 'Message is required.') && isValid;

            return isValid;
        }

        function validateField(field, errorMessage) {
            if (!field.value.trim()) {
                displayErrorAlert(errorMessage);
                return false;
            }
            return true;
        }

        function validateEmail(email) {
            // Basic email format validation
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                displayErrorAlert('Invalid email format.');
                return false;
            }
            return true;
        }

        function validatePhone(phone) {
            // Basic phone number format validation
            const phoneRegex = /^\d{10}$/;
            if (!phoneRegex.test(phone)) {
                displayErrorAlert('Invalid phone number format.');
                return false;
            }
            return true;
        }

        function displayErrorAlert(errorMessage) {
            alert(errorMessage);
        }

        function resetErrors() {
            // Reset any previous error messages
        }
    });

