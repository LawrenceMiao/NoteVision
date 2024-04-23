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
  popupMessage.style.display = 'flex';
  popupOverlay.style.display = 'flex';

  const closePopup = document.getElementById('closePopup');
  closePopup.addEventListener('click', () => {
    popupOverlay.style.display = 'none';
  });
}


function wait(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function myAsyncFunction() {
  console.log('Start');
  await wait(30000); // Wait for 3 seconds
  console.log('End');
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
        invertImage(file_path);
        // send it to a new window
        window.location.href = 'postupload.html?imageUrl=' + encodeURIComponent(file_path);
      })
  } else {
    displayPopup('Please Upload Image File.');
  }
}

function invertImage(file) {
  myAsyncFunction();
  console.log('aaaaa');
}



