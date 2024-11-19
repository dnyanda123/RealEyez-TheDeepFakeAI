// Select the theme toggle checkbox
const themeToggle = document.getElementById('theme-toggle');

// Check for saved user preference
const currentTheme = localStorage.getItem('theme');
if (currentTheme === 'dark') {
    document.body.classList.add('dark-mode');
}

// Add an event listener to toggle between zzlight and dark mode
themeToggle.addEventListener('change', () => {
    document.body.classList.toggle('dark-mode');
    
    // Save the user's preference to localStorage
    if (document.body.classList.contains('dark-mode')) {
        localStorage.setItem('theme', 'dark');
    } else {
        localStorage.setItem('theme', 'light');
    }
});
document.getElementById('image-input').addEventListener('click', function() {
    // Redirect to the login page when the file input is clicked
    window.location.href = 'login.html'; // Change 'login.html' to the actual path of your login page
});

// Optional: Handle the form submission if you still want to do something after login
document.getElementById('image-upload-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission if needed
    // Additional logic can go here if required after login
});
