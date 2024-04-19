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
          // invert the image
          invertImage(url);
          // send it to a new window
          console.log("AAAAAAAAAAAAAAAAAAAAAAAA");
          window.location.href = 'postupload.html?imageUrl=' + encodeURIComponent(url);
        })
    } else {
      displayPopup('Please Upload Image File.');
    }
}

function invertImage(file) {
    console.log('aaaaa');
}



