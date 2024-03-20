// window.onscroll = () => {
//     sections.forEach(sec => {
//         let top = window.scrollY;
//         let offset = sec.offsetTop - 150;
//         let height = sec.offsetHeight;

//         if(top >= offset && top < offset + height) {
//             sec.classList.add('show-animate');
//         }
//         else{
//             sec.classList.remove('show-animate');
//         }

//     })
// }

// let sections = document.querySelectorAll('animate');


saveImg.addEventListener("click", () => {
    // Change buttons as needed
    test.style.visibility = 'hidden';
    topic2222.innerHTML = topics[(Math.floor(Math.random() * (topics.length)))];
    // Start the countdown timer
    var tt = setInterval(function(){
        const upload = (file) => {
            fetch('/submit', {
                method: 'POST',
                body: file
            })
            .then(function (response) {
                return response.json();
              })
              .then(function (data) {
                var prediction = data.prediction;
          
                // Update the HTML with the prediction result
                document.getElementById("predictionText").textContent = "Prediction: " + prediction;
          
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
              .catch(function (error) {
                console.log("Error:", error);
              });
        }
        var temp = document.getElementById('yay')
        timer--;
        if (timer === 0) {
            clearInterval(tt);
            timer = 8;
            temp.innerHTML = 8;
            test.style.visibility = 'visible';
            canvas.toBlob(function(blob) {
                var data = new FormData();
                data.append('file', blob);
                upload(data);
            });
        }
        temp.innerHTML = timer;
    }, 1000);
});


const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry)
        if(entry.isIntersecting) {
            entry.target.classList.add('show');
        }
        else{
            entry.target.classList.remove('show');
        }
    });
});

const hiddenElements = document.querySelectorAll('.animate');
hiddenElements.forEach((el) => observer.observe(el));