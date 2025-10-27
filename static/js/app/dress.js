document.addEventListener("DOMContentLoaded", () => {

    /* === Load Category === */

    const categoryContainer = document.getElementById("categoryContainer")

    fetch('/category/getAllNames?category=dress')
        .then(res => res.json())
        .then(categoryData => {
            if (categoryData.status == "success") {
                let data = categoryData.data

                categoryContainer.innerHTML = ""

                data.forEach(category => {
                    let categorySnippet = `
                    <div class="col-md-2">
                        <button class="btn" data-id="${category.id}" >${category.title}</button>
                    </div>
                `

                    categoryContainer.innerHTML += categorySnippet
                });
            }
            else {
                throw new Error(categoryData.message);
            }
        })
        .catch(err => {
            alert(err)
        })



    /* === Load Dress === */

    const dressContainer = document.getElementById("dressContainer")

    fetch('/dress/getAll')
    .then(res => res.json())
    .then(dressData => {
        if (dressData.status == "success") {
                let data = dressData.data

                dressContainer.innerHTML = ""

            data.forEach(dress => {
                let dressCardSnippet = `
                    <div class="card p-0 border-0" style="flex: 1 0 30%;">
                        <div class="card-header p-0 border-0 bg-transparent" 
                            style="height: 350px; 
                            overflow: hidden; 
                            background-image: url(data:image/jpeg;base64,${dress.image});
                            background-position: center;
                            background-size: cover;
                            background-repeat: no-repeat
                        ">
                        </div>
                        <div class="nailCardBody p-2">
                            <h5 class="card-title" style="font: bold;">${dress.title}</h5>
                        </div>
                        <div class="card-footer d-flex justify-content-between"
                            style="background-color: var(--text); color: white !important;">
                            <i class="bi bi-share-fill"></i>
                            <i class="bi bi-download"></i>
                            <i class="bi bi-save"></i>
                        </div>
                    </div>
                `

                dressContainer.innerHTML += dressCardSnippet
            });
        }
        else {
            throw new Error(dressData.message);
            }
    })
    .catch(err => {
        alert(err)
    })
})