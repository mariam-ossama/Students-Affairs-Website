
function validate_department_assignment()
{
    var department= document.d_form.department;
    if(department.value == "select department")
    {
        alert("department is required");
        return false;
    }
}