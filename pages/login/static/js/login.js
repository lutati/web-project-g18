
  function validate(){
    var email = document.getElementById("email").value;
    var error_message = document.getElementById("error_message");
    

    if(email.indexOf("@") == -1 || email.length < 6){
      text = "נא להכניס כתובת תקינה";
      error_message.innerHTML = text;
      return false;
    }
   
    if(document.getElementById("password").value.length <8){
        text = "הזן סיסמא בעלת 8 תווים לפחות";
        error_message.innerHTML = text;
        return false;
    }
  
  }