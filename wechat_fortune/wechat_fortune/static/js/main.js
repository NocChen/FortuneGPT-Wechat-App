"""
/**
 * This file contains the JavaScript code for interacting with the WeChat Fortune API.
 * It uses the Fetch API to make HTTP requests and the DOM API to manipulate the HTML document.
 */

// Get the form, date input, prediction result, and share button elements from the document
const form = document.getElementById('predictionForm');
const dateInput = document.getElementById('date');
const predictionResult = document.getElementById('predictionResult');
const shareButton = document.getElementById('shareButton');

// Disable the share button initially
shareButton.disabled = true;

// Add an event listener to the form's submit event
form.addEventListener('submit', async (event) => {
    // Prevent the form from being submitted normally
    event.preventDefault();

    // Get the date from the date input
    const date = dateInput.value;

    // Make a POST request to the /predictions endpoint of the WeChat Fortune API
    const response = await fetch('/predictions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ date })
    });

    // If the response is successful, get the prediction from the response and display it
    if (response.ok) {
        const { prediction } = await response.json();
        predictionResult.textContent = `Your prediction for ${date} is: ${prediction}`;

        // Enable the share button
        shareButton.disabled = false;
    } else {
        // If the response is not successful, display an error message
        predictionResult.textContent = 'An error occurred while getting your prediction. Please try again.';
    }
});

// Add an event listener to the share button's click event
shareButton.addEventListener('click', async () => {
    // Get the prediction from the prediction result
    const prediction = predictionResult.textContent;

    // Make a POST request to the /share endpoint of the WeChat Fortune API
    const response = await fetch('/share', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prediction })
    });

    // If the response is successful, display a success message
    if (response.ok) {
        alert('Your prediction has been shared successfully!');
    } else {
        // If the response is not successful, display an error message
        alert('An error occurred while sharing your prediction. Please try again.');
    }
});
"""
