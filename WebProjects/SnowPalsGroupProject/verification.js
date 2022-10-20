

function Clr() {
    "use strict";
    
    document.getElementById("username").value = "";
    document.getElementById("password").value = "";
    document.getElementById("email").value = "";
    document.getElementById("number").value = "";

    return;
}


function Reg(user, pass, num, email) {
   
    "use strict";
    
    var regex_pass1 = /(?=.*[-+_!@#$%^&*., ?])/; //needs to equal false
    var regex_user1 = /(?=.*[-+_!@#$%^&*., ?])(\d)/; //needs to equal false
    var regex_pass2 = /(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/; // needs to equal true
    var regex_user2 = /(?=.*[a-zA-Z0-9])/; //needs to equal true
    var regex_num = /(?=.*[0-9])/; //needs to equal true
    var regex_email = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/; //needs to equal true
    
    if (regex_pass1.test(pass) === true && (user.length >= 6) && regex_user1.test(user) === false && isNaN(user.charAt(0)) === true && (pass.length >= 8) && (num.length == 10) && (regex_num.test(num) == true) && (regex_email.test(email)) == true) {
        
        if (regex_pass2.test(pass) === true && regex_user2.test(user) === true) {
            
            var checkboxes_a = document.getElementsByName("activities[]");
            var checkboxes_l = document.getElementsByName("locations[]");
            var radio_btns = document.getElementsByName("skill");
            var boxes_a = 0;
            var boxes_l = 0;
            var boxes_r = 0;

        for(var i = 0; i < checkboxes_a.length; i++){
                if(checkboxes_a[i].checked == true){
                boxes_a++;
                 }
         }
        for(var j = 0; j < checkboxes_l.length; j++){
                if(checkboxes_l[j].checked == true){
                boxes_l++;
                }
        }
        for(var k = 0; k < radio_btns.length; k++){
                if(radio_btns[k].checked == true){
                boxes_r++;
                }
        }
        if (boxes_a > 0 && boxes_l > 0 && boxes_r > 0){

        
        return;

    }
        else {


        alert("Please make at least one selection from each category");

        Clr();


    }

       
        } else {
            
           
            alert("Form is not completed correctly");
            
            Clr();
        }
        
    } else {
        
        
        alert("Form is not completed correctly");
        
        Clr();
    }
    
}

