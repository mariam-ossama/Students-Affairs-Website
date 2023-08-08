
function message()
{
    window.alert(" deleted");
}

function deletemessage () 
{
    if (confirm("are you sure you want to delete ?"))
       {
           message();
       }
      
}


window .onload= function disableinput ()
{
   document.getElementById("dis").disabled= true ;
   document.getElementById("phoneNumber").required= true ;
   document.getElementById("dateOfBirth").required= true ;
} 

function validate_name ()
{
    var name = document.a_form.name ;
    if(name.value.length ==0)
    {
        alert("name is required");
        return false;
    }
}
function validate_department()
{
    var level = document.a_form.level ;
    var department = document.a_form.department ;
    if(department.disabled == false)
    {
      if(department.value == "select department")
      {
        alert("department is required");
        return false;
      }
      else if(department.value != "General" && ( level.value == 1 || level.value == 2)) 

       {
        alert("department must be general because level is less than 3");
        return false;
     
       }
       else if (department.value == "General" && ( level.value == 3 || level.value == 4))
       {
        alert("department can't be general because level is greater than 2");
        return false;
       }
    }
}

function ageCalculator()
        {
            var userinput = document.getElementById("DOB").value;
            var dob = new Date(userinput);
    
             //calculate month difference from current date in time
            var month_diff = Date.now() - dob.getTime();
    
            //convert the calculated difference in date format
            var age_dt = new Date(month_diff); 
    
            //extract year from date    
             var year = age_dt.getUTCFullYear();
    
            //now calculate the age of the user
            var age = Math.abs(year - 1970);
             if (age<18)
             {
                //return document.getElementById("result").innerHTML = "ok";
                alert("student can not be younger than 18 years old")  ;
             
             }
    
        }
function validate_form()
{
    var id = document.a_form.id ;
    var level = document.a_form.level ;
    var gpa = document.a_form.gpa ;
    var status= document.a_form.status ;
    var gender = document.a_form.gender ;
    var email = document.a_form.email ;
    var dateOfBirth = document.a_form.dateOfBirth ;
    var phoneNumber = document.a_form.phoneNumber ;

    validate_name ();
    if(id.value.length ==0)
    {
        alert("ID is required");
        return false;
    }

    if(level.value == "select level")
    {
        alert("level is required");
        return false;
    }
    
    validate_department();

    if(gpa.value.length ==0)
    {
        alert("gpa is required");
        return false;
    }

    if (status.value.length ==0)
    {
        alert("status is required");
        return false;
    }

    if (gender.value.length ==0)
    {
        alert("gender is required");
        return false;
    }

    if (email.value.length ==0)
    {
        alert("email is required");
        return false;
    }
     
    if (dateOfBirth.value.length ==0)
    {
        alert("date of birth is required");
        return false;
    }

    ageCalculator();
    

    if (phoneNumber.value.length == 0)
    {
        alert("phone_number is required");
        return false;
    }

}