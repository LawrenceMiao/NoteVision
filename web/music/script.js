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
        return response.text();
      })
      .then(function (file_path) {
        // make the image B & W
        // blackAndWhite(file_path);
        // send it to a new window
        window.location.href = 'postupload.html?imageUrl=' + encodeURIComponent(file_path);
      })
  } else {
    displayPopup('Please Upload Image File.');
  }
}

// function blackAndWhite(file_path) {
//   const officialPath = "/uploads/" + file_path;

//   // Create an image element
//   var img = new Image();
//   img.crossOrigin = "Anonymous"; // Enable CORS to prevent security issues

//   // When the image is loaded, apply the grayscale filter
//   img.onload = function() {
//     // Create a canvas element
//     var canvas = document.createElement('canvas');
//     var ctx = canvas.getContext('2d');

//     // Set the canvas dimensions to match the image
//     canvas.width = img.width;
//     canvas.height = img.height;

//     // Draw the image onto the canvas
//     ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

//     // Get the image data
//     var imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
//     var data = imageData.data;

//     // Loop through each pixel
//     for (var i = 0; i < data.length; i += 4) {
//         // Convert the pixel to grayscale
//         var avg = (data[i] + data[i + 1] + data[i + 2]) / 3;
//         data[i] = avg; // Red
//         data[i + 1] = avg; // Green
//         data[i + 2] = avg; // Blue
//     }

//     // Put the modified image data back onto the canvas
//     ctx.putImageData(imageData, 0, 0);

//     // Replace the original image with the modified image
//     img.src = canvas.toDataURL();
//   };

//   // Set the source of the image to the file path
//   img.src = officialPath;
// }




