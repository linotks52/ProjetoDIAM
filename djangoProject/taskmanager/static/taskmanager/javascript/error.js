  var errorMessage = "{{ error_message }}";
  if (errorMessage) {
    var errorDiv = document.getElementById("error-message");
    errorDiv.innerHTML = errorMessage;
    alert(errorMessage);
  }