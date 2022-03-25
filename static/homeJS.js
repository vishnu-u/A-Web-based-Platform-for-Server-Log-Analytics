var loader = function (e) {
  let f = e.target.files;
  let show = "<span> Selected file:</span>" + f[0].name;
  let output = document.getElementById("file");
  output.innerHTML = show;
  output.classList.add("active");
};

//add event listener for input

let fileInput = document.getElementById("file");
fileInput.addEventListener("change", loader);
