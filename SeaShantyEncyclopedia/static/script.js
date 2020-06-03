//query select all

window.onkeyup = keyup;  // Listener for when a key is pressed

var passwordTextValue;

document.addEventListener('DOMContentLoaded', function() {  // This function runs when the page is loaded.
    if({{session.admin}} == "yes") {
      var panel = document.getElementById("AdminPanel");
      var input = document.getElementById("Password");
      panel.style.display = 'block';
      input.style.display = 'none';
    }
}, false);

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
