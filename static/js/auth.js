const registerForm = document.querySelector('#registerForm')
registerForm.addEventListener('submit', function (e) {
    e.preventDefault()

    const formData = new FormData(registerForm)
    const data = Object.fromEntries(formData)

    console.log(data)
    fetch("/register", {
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
        .catch(error =>{
            alert(error)
        })


})