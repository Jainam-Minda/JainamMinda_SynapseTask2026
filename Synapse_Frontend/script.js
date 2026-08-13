const contactForm = document.getElementById("contactForm");
const formMessage = document.getElementById("formMessage");

contactForm.addEventListener("submit", function (event) {

    event.preventDefault();

    const contactData = {
        name: document.getElementById("name").value.trim(),
        phone: document.getElementById("phone").value.trim(),
        email: document.getElementById("email").value.trim(),
        address: document.getElementById("address").value.trim(),
        message: document.getElementById("message").value.trim()
    };

    console.log("Contact Form Data:");
    console.log(contactData);

    formMessage.textContent =
        "Thanks! Your message has been recorded.";

    contactForm.reset();

});