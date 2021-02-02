
  function validate(){
    var name = document.getElementById("name").value;
    var phone = document.getElementById("phone").value;
    var email = document.getElementById("email").value;
    var error_message = document.getElementById("error_message");
    

    if(name.length < 5){
      text = "נא להכניס שם מלא";
      error_message.innerHTML = text;
      return false;
     
    }
   
    if(isNaN(phone) || phone.length < 10){
      text = "נא להכניס מספר טלפון תקין";
      error_message.innerHTML = text;
      return false;
      
    }
    if(email.indexOf("@") == -1 || email.length < 6){
      text = "נא להכניס כתובת תקינה";
      error_message.innerHTML = text;
      return false;
      
      
    }
   
    alert("ההודעה נשלחה בהצלחה");
     document.getElementById("btn").value="ההודעה נשלחה";
     return false;
  
  }