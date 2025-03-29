/* Add your Application JavaScript */
document.addEventListener('DOMContentLoaded', function() {
    // Wait for the page to load and for flash messages to be rendered
    setTimeout(function() {
      let alerts = document.querySelectorAll('.alert-container .alert');
      alerts.forEach(alert => {
        alert.style.transition = "opacity 0.5s ease-out";
        alert.style.opacity = 0;
        setTimeout(() => alert.remove(), 500);  // Remove after transition
      });
    }, 5000); // 5 seconds timeout (you can adjust this duration)
  });
