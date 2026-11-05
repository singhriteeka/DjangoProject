/* =========================================
   1. MOBILE NAVIGATION
========================================= */

const menuToggle = document.querySelector(".menu-toggle");
const navLinks = document.querySelector(".nav-links");

if (menuToggle && navLinks) {
    menuToggle.addEventListener("click", () => {
        const isOpen = navLinks.classList.toggle("show");

        menuToggle.setAttribute("aria-expanded", isOpen);
    });
}


/* =========================================
   2. PASSWORD VISIBILITY
========================================= */

document.querySelectorAll(".password-toggle").forEach(button => {

    button.addEventListener("click", () => {

        const input = button.parentElement.querySelector("input");

        const isPassword = input.type === "password";

        input.type = isPassword ? "text" : "password";

        button.setAttribute(
            "aria-label",
            isPassword ? "Hide password" : "Show password"
        );

    });

});


/* =========================================
   3. LOGIN AND SIGNUP FORM VALIDATION
========================================= */

document.querySelectorAll(".auth-form").forEach(form => {

    form.addEventListener("submit", event => {

        event.preventDefault();

        const message = form.querySelector(".form-message");

        message.textContent = "";
        message.className = "form-message";

        if (!form.reportValidity()) {
            return;
        }

        const formType = form.dataset.form;

        if (formType === "login") {

            message.textContent =
                "Form validated. Connect your Django backend to log in.";

            message.classList.add("success");

        }

        if (formType === "signup") {

            const password = form.elements.password.value;
            const confirmPassword = form.elements.confirmPassword.value;

            if (password !== confirmPassword) {

                message.textContent = "Passwords do not match.";

                message.classList.add("error");

                return;
            }

            message.textContent =
                "Form validated. Connect your Django backend to create an account.";

            message.classList.add("success");

        }

    });

});