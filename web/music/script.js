const form = document.querySelector("form"),
fileInput = document.querySelector(".file-input"),
progressArea = document.querySelector(".progress-area"),
uploadedArea = document.querySelector(".uploaded-area");

form.addEventListener("click", () =>{
  fileInput.click();
});

fileInput.onchange = ({target})=>{
  let file = target.files[0];
  if(file){
    let fileName = file.name;
    if(fileName.length >= 12){
      let splitName = fileName.split('.');
      fileName = splitName[0].substring(0, 13) + "... ." + splitName[1];
    }
    uploadFile(fileName);
  }
}

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

function uploadFile(name) {
  let fileInput = document.querySelector('.file-input'); // Assuming file input has a class 'file-input'

  // Get the selected file
  let file = fileInput.files[0];

  // Check if a file is selected
  if (file) {
    // Check if the selected file is an image
    if (file.type.startsWith('image/')) {
      let xhr = new XMLHttpRequest();
      xhr.open("POST", "http://127.0.0.1:5000/upload");

      xhr.upload.addEventListener("progress", ({ loaded, total }) => {
        let fileLoaded = Math.floor((loaded / total) * 100);
        let fileTotal = Math.floor(total / 1000);
        let fileSize;
        (fileTotal < 1024) ? fileSize = fileTotal + " KB" : fileSize = (loaded / (1024 * 1024)).toFixed(2) + " MB";
        let progressHTML = `<li class="row">
                              <i class="fas fa-file-alt"></i>
                              <div class="content">
                                <div class="details">
                                  <span class="name">${name} • Uploading</span>
                                  <span class="percent">${fileLoaded}%</span>
                                </div>
                                <div class="progress-bar">
                                  <div class="progress" style="width: ${fileLoaded}%"></div>
                                </div>
                              </div>
                            </li>`;
        const progressArea = document.getElementById('progressArea'); // Assuming there's an element with id 'progressArea'
        const uploadedArea = document.getElementById('uploadedArea'); // Assuming there's an element with id 'uploadedArea'

        uploadedArea.classList.add("onprogress");
        progressArea.innerHTML = progressHTML;

        if (loaded == total) {
          // Do not clear the progress area; simply update the progress elements
          const uploadedHTML = `<li class="row">
                                <div class="content upload">
                                  <i class="fas fa-file-alt"></i>
                                  <div class="details">
                                    <span class="name">${name} • Uploaded</span>
                                    <span class="size">${fileSize}</span>
                                  </div>
                                </div>
                                <i class="fas fa-check"></i>
                              </li>`;
          progressArea.insertAdjacentHTML("beforeend", uploadedHTML);
        }
      });
      
      xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
          if (xhr.status == 200) {
            // File uploaded successfully, handle the response
            let uploadedFilename = xhr.responseText;
            console.log("Uploaded");
        
            // Use getElementsByClassName since the element has a class, not an ID
            let postUploadElement = document.getElementsByClassName("post-upload")[0];
        
            // Set the display property to "block"
            postUploadElement.style.display = "block";
        
            console.log("success");
        }
        
        }
      };

      let data = new FormData();
      data.append('file', file); // Append the file to the FormData

      xhr.send(data);
    } else {
      // Show an error message for non-image files
      displayPopup("Please select an image file.");
    }
  }
}





