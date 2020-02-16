
	


	$(document).ready(function(){ $('#submit').click (function()
		// body...
	 {
		var pass1= document.getElementById('id_password1').value;
		var pass2=document.getElementById('id_password2').value;
		if (pass1!=pass2) {
			alert("password not match");
			return false;
		}

		else if(pass1.length<8 || pass2.length<8)

		{
            alert("password is short plese chose at least 8 charceter ");
			return false;

		}

		
	});
 
    });
