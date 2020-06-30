document.querySelector("#gotoButton").addEventListener("click", function(event){
  window.location = document.querySelector("select[name=goto]").value;
});


function logout() {
  var panel = document.getElementById("AdminPanel");
  var input = document.getElementById("Password");
  panel.style.display = 'none';
  input.style.display = 'block';
}

function areYouSure() {
  var hiddenDiv = document.getElementById("deleteButton");
  console.log(hiddenDiv);
  hiddenDiv.style.display = 'block';
}

function dropdown(elementID) {
  var boxID = document.getElementById(elementID);
  //window.alert("Hello");
  if (boxID.style.display === 'none') {
    boxID.style.display = 'block';
  } else {
    boxID.style.display = "none";
  }
}

document.querySelectorAll(".entry .btn").forEach((item) => {
  item.addEventListener("click", (event) => {
    event.target.parentElement.classList.toggle("collapsed")
  })
});

// let selector = document.querySelectorAll(".entry");
//
// for (let element in selector) {
//   console.log(selector[element]);
//   selector[element].addEventListener("onclick", function(event) {
//     console.log(event);
//   })
// }
