function markTodoCompleted(todoId) {
    // Construct the URL with the todo ID
    const url = `/todo/complete/${todoId}`;

    // Send a POST request to the server
    fetch(url, {
        method: 'POST', // Specify the method
        // Optional: Include headers, like for CSRF tokens if needed
        headers: {
            'Content-Type': 'application/json',
            // 'X-CSRFToken': csrfToken, // Uncomment and provide your CSRF token if needed
        },
        // No need to send body data since todoId is in the URL
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok.');
        }
        fetch('/')
        return response.json(); // Parse the JSON response body
    })
    .then(data => {
        console.log(data.message); // Log the success message
    })
    .catch(error => {
        console.error('Error:', error);
        // Optional: Inform the user that an error occurred
    });
}

function uncompleteAll() {
    const url = `/uncomplete_all`;
    fetch(url, {
        method: 'POST',
        headers: {'Content-Type': 'application/json',}
    })
}
