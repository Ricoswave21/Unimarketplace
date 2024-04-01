document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission


    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;


    let errorMessage = validateLogin(email, password);


    if (errorMessage) {
        document.getElementById("error-message").innerText = errorMessage;
    } else {
        document.getElementById("error-message").innerText = "";
        console.log("Login successful");
        // Redirect or perform other actions upon successful login
    }
});

