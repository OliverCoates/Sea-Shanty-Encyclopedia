//query select all

window.onkeyup = keyup;  // Listener for when a key is pressed

var passwordTextValue;

function keyup(e) {
  passwordTextValue = e.target.value;
  if (e.keyCode == 13 && passwordTextValue == "Password")  { // Check for when enter pressed
    //window.alert("Hey!");
    e.target.value = ""; // Reset what is in the password field
    var panel = document.getElementById("AdminPanel");
    var input = document.getElementById("Password");
    panel.style.display = 'block';
    input.style.display = 'none';
  }
}

function logout() {
  var panel = document.getElementById("AdminPanel");
  var input = document.getElementById("Password");
  panel.style.display = 'none';
  input.style.display = 'block';
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
