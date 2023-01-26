

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

    //   Data Clear
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
    document.getElementById("restart").addEventListener("click", function () {
        Swal.fire({
            icon: "info",
            title: "<strong>Project Restart..</strong>",
            html: `<input type="password" id="confirmpassword" placeholder="Enter Conform Password" class="form-control">`,
            text: "All Data Remove Please Confirmed..",
            showCloseButton: true,
            showCancelButton: true,
            focusConfirm: false,
        }).then((okay) => {
            console.log(okay);
            if (okay["isConfirmed"]) {
                if (password == "") {
                    alert("Enter Password");
                } else {
                    var password = $("#confirmpassword").val();
                    $("#confirmpasswordsend").val(password);
                    $("#conformForm").submit();
                }
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
            text: `Are You Sure Delete Data For Name : ${Name}`,
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
        var Name = $(this).attr("data-delete-Name")
        Swal.fire({
            icon: 'info',
            title: '<strong>Oops...</strong>',
            text: `Are You Sure Delete Data For Name : ${Name}`,
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
            text: `Are You Sure Restore Data For Name Is :${Name}`,
            showCancelButton: true,

        }).then(okay => {
            if (okay['isConfirmed']) {
                window.location.href = `/dashboard/selectedmember/delete/restore/?restore=${restoreId}&deletedId=${deletedId}`;
            } else {
                window.location.href = "";
            }
        });
    });


    // rendom Selected Member Show
    $('#TodayRandomEmployee').click(function () {
        const username = JSON.parse(document.getElementById('username').textContent)
        const randomIndex = Math.floor(Math.random() * username.length);
        const item = username[randomIndex];
        document.getElementById("randomname").innerHTML = item


        // array.push(Data);
        // const selectedMemberObj = JSON.parse(document.getElementById('selectedMemberObj').textContent)
        // var array = []


        // console.log(array)
        // console.log(selectedMemberObj)
        // function random_item(items) {
        //     return items[Math.floor(Math.random() * items.length)];
        // }
        // var items = [254, 45, 212, 365, 2543];
        // console.log(random_item(items));
    })

});





