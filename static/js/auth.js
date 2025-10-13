const registerForm = document.querySelector('#registerForm')

if (registerForm) {

    registerForm.addEventListener('submit', function (e) {
        e.preventDefault()

        const formData = new FormData(registerForm)
        const data = Object.fromEntries(formData)

        console.log(data)
        fetch("/auth/register", {
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
                    location.href = "/dress"
                } else {
                    throw new Error(data.message);

                }
            })
            .catch(error => {
                alert(error)
            })


    })
}

const loginForm = document.querySelector('#loginForm')
if (loginForm) {

    loginForm.addEventListener('submit', function (e) {
        e.preventDefault()

        const formData = new FormData(loginForm)
        const data = Object.fromEntries(formData)

        console.log(data)
        fetch("/auth/login", {
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
                    location.href = "/dress"
                } else {
                    throw new Error(data.message);

                }
            })
            .catch(error => {
                alert(error)
            })


    })
}