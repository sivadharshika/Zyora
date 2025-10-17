const nailArtForm = document.querySelector('#nailArtForm')

nailArtForm.addEventListener('submit', function (e) {
    e.preventDefault()

    const formData = new FormData(nailArtForm)

    // console.log(data)
    fetch("/nailArt/new", {
        method: "POST",
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            console.log(data)

            if (data.status == "success") {
                alert(data.message)
                // location.reload()
            } else {
                throw new Error(data.message);

            }
        })
        .catch(error => {
            alert(error)
        })
})



$(document).ready(function () {
    let table = $('#nailArtTable').DataTable({
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": "/nailArt/getAll",
            "type": "GET",
            "dataSrc": "data"
        },
        "columns": [
            { 
                "data": "image", 
                "render": function(data, type, row) {
                    return `<img src="data:image/jpeg;base64, ${data}" style="width: 150px">`;
                },
                "orderable": false
            },
            { "data": "title", "defaultContent": "N/A" },
            { "data": "description", "defaultContent": "N/A" },
            { "data": "category", "defaultContent": "N/A" },
            { "data": "addedTime", "defaultContent": "N/A" },
            { "data": "updatedTime", "defaultContent": "N/A" },
            { 
                "data": "id",
                "render": function(data, type, row) {
                    return `
                        <div class="d-flex">
                         <a class="dropdown-item edit-btn" href="javascript:void(0);" data-id="${data}"><i class="bi bi-pencil-square me-1"></i></a>
                              <a class="dropdown-item delete-btn" href="javascript:void(0);" data-id="${data}"><i class="bi bi-trash3 me-1"></i></a>
                        </div>
                    `;
                },
                "orderable": false
            }
        ],
        "order": [[0, "asc"]],
        "paging": true,
        "searching": true,
        "autoWidth": false,
    });
  

    // $('#roleTable tbody').on('click', '.delete-btn', function() {
    //     let id = $(this).data('id');
    //     showConfirmation('Are you sure you want to delete this role?', function () {
    //         $.ajax({
    //             url: '/role/delete?id=' + id,
    //             type: 'DELETE',
    //             success: function (response) {
    //                 if (response.status == "success") {
    //                     showAlert('success', response.message)
    //                     table.ajax.reload();
    //                 }   
    //                 else{
    //                     throw response.message
    //                 }
    //             },
    //             error: function (error) {
    //                 showAlert('danger', error)
    //             }
    //         });
    //     })
    // });

    // $('input[name="tableHeaders"]').on('click', function() {
    //     let checked = $(this).prop('checked');
    //     $('#roleTable tbody input[type="checkbox"]').prop('checked', checked);
    // });
});


const nailArtModal = document.getElementById("addUserModal")

nailArtModal.addEventListener("shown.bs.modal", ()=>{
    fetch("/category/getAllNames")
        .then(response => response.json())
        .then(data => {
            console.log(data)

            if (data.status == "success") {

                let categoryData = data.data



                const categorySelect = document.getElementById("category")
                categorySelect.innerHTML = ""
                categoryData.forEach(category => {
                    let option = `<option value="${category.id}">${category.title}</option>`
                    
                    categorySelect.innerHTML += option
                });
            } else {
                throw new Error(data.message);

            }
        })
        .catch(error => {
            alert(error)
        })
})