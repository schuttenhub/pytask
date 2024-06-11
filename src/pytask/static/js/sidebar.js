document.addEventListener('DOMContentLoaded', function() {
    // Get all sidebar items
    var sidebarItems = document.querySelectorAll('.nav-item a');
  
    // Function to handle click on sidebar items
    sidebarItems.forEach(function(item) {
      item.addEventListener('click', function(e) {
        e.preventDefault(); // Prevent default link behavior
  
        // Remove active class and aria-current from all items
        sidebarItems.forEach(function(el) {
          el.classList.remove('active');
          el.removeAttribute('aria-current');
          el.classList.add('link-body-emphasis')
        });
  
        // Add active class and aria-current to the clicked item
        this.classList.add('active');
        this.setAttribute('aria-current', 'page');
        this.classList.remove('link-body-emphasis');

        window.location.href = this.getAttribute('href');
      });
    });
  });
  