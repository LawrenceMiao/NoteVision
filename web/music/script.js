fileInput = document.querySelector(".file-input"),
progressArea = document.querySelector(".progress-area"),
uploadedArea = document.querySelector(".uploaded-area");
const fileUploadBtn = document.querySelector(".file-upload-btn");

fileUploadBtn.addEventListener("click", () => {
  fileInput.click();
});

fileInput.onchange = (event) => {
    event.preventDefault();  // Prevent the default form submission
  
    let fileInput = event.target;
    let file = fileInput.files?.[0];
    if (file) {
      uploadFile(file);
    }
};
  

// Popup shows when an error message is hit
function displayPopup(message) {
  const popupOverlay = document.getElementById('popupOverlay');
  const popupMessage = document.getElementById('popupMessage');
  popupMessage.innerText = message;

  popupOverlay.style.display = 'flex';

  const closePopup = document.getElementById('closePopup');
  closePopup.addEventListener('click', () => {
    popupOverlay.style.display = 'none';
  });
}

// Check and make sure the only files being submitted are image files.
function uploadFile(file) {
    // Check if the selected file is an image
    if (file.type.startsWith('image/')) {
      // Create a FormData object to send the file as a binary payload
      let formData = new FormData();
      formData.append('file', file);
  
      // Make an AJAX request to the server
      fetch('http://127.0.0.1:5000/upload', {
        method: 'POST',
        body: formData,
      })
        .then(function (response) {
          return response.blob();
        })
        .then(function (blob) {
          var url = URL.createObjectURL(blob);
          // Handle the response text if needed
          console.log(url);
          // Continue with the rest of your logic
          const postUploadElement = document.querySelector('.post-upload');
          postUploadElement.style.display = 'block';

          
                // Update the HTML with the prediction result
                document.getElementById("predictionText").textContent = "Prediction: ";
          
                // Display the prediction popup
                var modal = document.getElementById("predictionPopup");
                var span = document.getElementsByClassName("close")[0];
                var predictionText = document.getElementById("predictionText");
          
                predictionText.textContent = prediction;
                modal.style.display = "block";
          
                // Close the prediction popup when the user clicks the close button
                span.onclick = function () {
                  modal.style.display = "none";
                };
          
                // Close the prediction popup when the user clicks outside the modal content
                window.onclick = function (event) {
                  if (event.target == modal) {
                    modal.style.display = "none";
                  }
                };
        })
    } else {
      displayPopup('Please Upload Image File.');
    }
}




