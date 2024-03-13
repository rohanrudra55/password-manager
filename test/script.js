const form = document.getElementById("user-form");
const nameInput = document.getElementById("name");
const emailInput = document.getElementById("email");
const userDataDiv = document.getElementById("user-data");

form.addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent default form submission

  const name = nameInput.value;
  const email = emailInput.value;

  // Simulate storing data (not actual storage)
  const user = {
    name: name,
    email: email
  };

  // Display the user data in the div
  userDataDiv.textContent = JSON.stringify(user, null, 2); // Pretty-printed JSON format

  // **Note:** This is for demonstration purposes only.
  // In a real application, you would need to consider secure storage mechanisms,
  // such as browser storage APIs or server-side storage.
});
