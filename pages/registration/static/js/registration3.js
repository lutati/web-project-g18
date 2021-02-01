

  function validate(){
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var error_message = document.getElementById("error_message");
    

    if(name.length < 2){
      text = "אתה לא מעודכן נא להכניס שם מלא";
      error_message.innerHTML = text;
      return false;
     
    }
   
    if(email.indexOf("@") == -1 || email.length < 6){
      text = "נא להכניס כתובת תקינה";
      error_message.innerHTML = text;
      return false;
       
    }
    if (document.getElementById('password').value !=
    document.getElementById('confirm_password').value) {
        text = "הסיסמאות אינן זהות. נא אשר סיסמא";
        error_message.innerHTML = text;
        return false;
    }

    if(document.getElementById('confirm_password').value.length <8 ||document.getElementById('password').value.length <8){
        text = "הזן סיסמא בעלת 8 תווים לפחות";
        error_message.innerHTML = text;
        return false;
    }


    alert("הרישום בוצע בהצלחה");
     document.getElementById("btn").value="הרישום בוצע";
  }