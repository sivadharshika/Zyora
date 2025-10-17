const categoryForm = document.querySelector('#categoryForm')

categoryForm.addEventListener('submit', function (e) {
    e.preventDefault()

    const formData = new FormData(categoryForm)
    const data = Object.fromEntries(formData)

    // console.log(data)
    fetch("/category/new", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
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