const ornaments = document.querySelector('#ornamentsForm')

ornaments.addEventListener('submit', function (e) {
    e.preventDefault()

    const formData = new FormData(ornaments)

    fetch("/ornament/new", {
        method: "POST",
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            console.log(data)

            if (data.status == "success") {
                alert(data.message)
            } else {
                throw new Error(data.message);

            }
        })
        .catch(error => {
            alert(error)
        })


})