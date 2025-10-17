const dressForm = document.querySelector('#dressForm')

nailArtForm.addEventListener('submit', function (e) {
    e.preventDefault()

    const formData = new FormData(dressForm)

    fetch("/dress/new", {
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