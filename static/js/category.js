const categoryForm = document.querySelector('#categoryForm')

categoryForm.addEventListener('submit', function (e) {
    e.preventDefault()

    let id = document.getElementById("categoryId")?.value
    const formData = new FormData(categoryForm)
    const data = Object.fromEntries(formData)
    if (id) {
        // console.log(data)
        fetch("/category/update?id=" + id, {
            method: "PUT",
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                console.log(data)

                if (data.status == "success") {
                    alert(data.message)
                    location.reload()
                } else {
                    throw new Error(data.message);

                }
            })
            .catch(error => {
                alert(error)
            })
    }
    else {
        // console.log(data)
        fetch("/category/new", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(data => {
                console.log(data)

                if (data.status == "success") {
                    alert(data.message)
                    location.reload()
                } else {
                    throw new Error(data.message);

                }
            })
            .catch(error => {
                alert(error)
            })
    }

})

$(document).ready(function () {
    let table = $('#categoryTable').DataTable({
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": "/category/getAll",
            "type": "GET",
            "dataSrc": "data"
        },
        "columns": [
            { "data": "title", "defaultContent": "N/A" },
            { "data": "category", "defaultContent": "N/A" },
            { "data": "description", "defaultContent": "N/A" },
            { "data": "addedTime", "defaultContent": "N/A" },
            { "data": "updatedTime", "defaultContent": "N/A" },
            {
                "data": "id",
                "render": function (data, type, row) {
                    return `
                        <div class="d-flex">
                         <a class="dropdown-item edit-btn" href="javascript:void(0);" data-id="${data}" data-bs-toggle="modal" data-bs-target="#addUserModal"><i class="bi bi-pencil-square me-1"></i></a>
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


    $('#categoryTable tbody').on('click', '.delete-btn', function () {
        let id = $(this).data('id');
        if (confirm('Are you sure you want to delete this category?')) {
            $.ajax({
                url: '/category/delete?id=' + id,
                type: 'DELETE',
                success: function (response) {
                    if (response.status == "success") {
                        alert(response.message)
                        table.ajax.reload();
                    }
                    else {
                        throw response.message
                    }
                },
                error: function (error) {
                    alert(error)
                }
            });
        }
    });
});


document.querySelector("tbody").addEventListener("click", (e) => {
    let id = e.target.closest('.edit-btn')?.dataset.id

    if (id) {
        fetch("/category/getSpecific?id=" + id)
            .then(response => response.json())
            .then(nailArtData => {
                console.log(nailArtData)

                if (nailArtData.status == "success") {
                    let data = nailArtData.data
                    console.log(data)

                    // const file = base64ToFile(, "image.png");

                    // document.getElementById("previewImg").src = "data:image/jpeg;base64," + data.image
                    document.getElementById("title").value = data.title
                    document.getElementById("description").value = data.description
                    setTimeout(() => {
                        document.getElementById("category").value = data.category
                    }, 500);
                    document.getElementById("categoryId").value = data.id
                } else {
                    throw new Error(nailArtData.message);

                }
            })
            .catch(error => {
                alert(error)
            })
    }
}) 