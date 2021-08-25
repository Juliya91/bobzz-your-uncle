// Code for sidenav taken from Materialize (https://materializecss.com/navbar.html)

$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    // Code for confirm password taken from Online Web Tutor 
    // (https://onlinewebtutorblog.com/how-to-validate-password-and-confirm-password-using-jquery/) and edited slightly
    $("#confirm_password").on('keyup', function() {
      let password = $("#password").val();
      let confirmPassword = $("#confirm_password").val();
      if (password != confirmPassword)
      $("#CheckPassMatch").html("Password does not match !").css("color", "red");
      else
        $("#CheckPassMatch").html("Password match !").css("color", "green");
    });
  });