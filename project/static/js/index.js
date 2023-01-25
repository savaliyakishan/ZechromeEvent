


(function () {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {
                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                }

                form.classList.add('was-validated')
            }, false)
        })
})()

$(document).ready(function () {

    // datatable Js
    $(document).ready(function () {
        $('#example,#example-Bed,#example-Staff-Pation').DataTable();
    });

    // deletemember Data Clear
    document.getElementById('deleteData').addEventListener('click', function () {
        Swal.fire({
            icon: 'info',
            title: '<strong>Oops...</strong>',
            text: 'All Deleted Employees Data Remove Please Confirmed..',
            showCancelButton: true,

        }).then(okay => {
            if (okay['isConfirmed']) {
                window.location.href = "/dashboard/deletedmember/clearAll/delete/";
            } else {
                window.location.href = "";
            }
        });
    });

    // Project Restart 
    document.getElementById('restart').addEventListener('click', function () {
        Swal.fire({
            icon: 'info',
            title: '<strong>Oops...</strong>',
            text: 'All Data Remove Please Confirmed..',
            showCancelButton: true,

        }).then(okay => {
            if (okay['isConfirmed']) {
                window.location.href = "/dashboard/selectedmember/clearall/";
            } else {
                window.location.href = "";
            }
        });
    });

    // History All clear 
    document.getElementById('Historyclear').addEventListener('click', function () {
        Swal.fire({
            icon: 'info',
            title: '<strong>Oops...</strong>',
            text: 'Please Confirm To History Clear....',
            showCancelButton: true,
        }).then(okay => {
            if (okay['isConfirmed']) {
                window.location.href = "/dashboard/history/clearall/";
            } else {
                window.location.href = "";
            }
        });
    });

    // viewmember Js

    $('.update').click(function () {
        $('#validationCustomUsername').val($(this).attr("data-name"))
        $('#validationCustomEmail').val($(this).attr("data-email"))
        $('#validationCustomid').val($(this).attr("data-id"))
    });


    $('.employeedeleteData').click(function () {
        var id = $(this).attr("data-delete-id")
        var Name = $(this).attr("data-name")
        Swal.fire({
            icon: 'info',
            title: '<strong style="background-color:None;">Oops...</strong>',
            text: `Can You Sure Delete Data For Name : ${Name}`,
            showCancelButton: true,

        }).then(okay => {
            if (okay['isConfirmed']) {
                window.location.href = `/dashboard/delete/${id}`;
            } else {
                window.location.href = "";
            }
        });
    });


    // selectedmember Js

    $('.btntopicadd').click(function () {
        $('#validationCustomid').val($(this).attr("data-id"))
        $('#validationCustomTopicName').val($(this).attr("data-topic"))
        if ($(this).attr("data-topic")) {
            $('#Addtopicmodelhead').html("Update Topic")
            $('#submitbtn').html("Update Topic")
        } else {
            $('#Addtopicmodelhead').html("Add Topic")
            $('#submitbtn').html("Add Topic")
        }
    });

    $('.selectedmemberdelete').click(function () {
        var id = $(this).attr("data-delete-id")
        Swal.fire({
            icon: 'info',
            title: '<strong>Oops...</strong>',
            text: `Can You Sure Delete Data For Id No:${id}`,
            showCancelButton: true,

        }).then(okay => {
            if (okay['isConfirmed']) {
                window.location.href = `/dashboard/selectedmember/delete/${id}`;
            } else {
                window.location.href = "";
            }
        });
    });

    // deletemember JS

    $('.deletedmemberdelete').click(function () {
        var restoreId = $(this).attr("data-restore")
        var deletedId = $(this).attr("data-deletemember")
        var Name = $(this).attr("data-Name")
        Swal.fire({
            icon: 'info',
            title: '<strong>Oops...</strong>',
            text: `Can You Sure Restore Data For Name Is :${Name}`,
            showCancelButton: true,

        }).then(okay => {
            if (okay['isConfirmed']) {
                window.location.href = `/dashboard/selectedmember/delete/restore/?restore=${restoreId}&deletedId=${deletedId}`;
            } else {
                window.location.href = "";
            }
        });
    });

});

