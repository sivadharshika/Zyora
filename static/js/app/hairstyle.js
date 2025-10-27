document.addEventListener("DOMContentLoaded", ()=>{

    /* === Load Category === */

    const categoryContainer = document.getElementById("categoryContainer")

    fetch('/category/getAllNames?category=hairStyle')
    .then(res => res.json())
    .then(categoryData =>{
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
        else{
            throw new Error(categoryData.message);   
        }
    })
    .catch(err =>{
        alert(err)
    })



    /* === Load Nail Art === */

    const hairstyleContainer = document.getElementById("hairstyleContainer")

    fetch('/hairStyle/getAll')
    .then(res => res.json())
    .then(hairStyleData =>{
        if (hairStyleData.status == "success") {
            let data = hairStyleData.data

            hairstyleContainer.innerHTML = ""

            data.forEach(hairStyle => {
                let hairStyleCardSnippet = `
                    <div class="card p-0 border-0" style="flex: 1 0 30%;">
                        <div class="card-header p-0 border-0 bg-transparent" 
                            style="height: 350px; 
                            overflow: hidden; 
                            background-image: url(data:image/jpeg;base64,${hairStyle.image});
                            background-position: center;
                            background-size: cover;
                            background-repeat: no-repeat
                        ">
                        </div>
                        <div class="hairstyleCardBody p-2">
                            <h5 class="card-title" style="font: bold;">${hairStyle.title}</h5>
                        </div>
                        <div class="card-footer d-flex justify-content-between"
                            style="background-color: var(--text); color: white !important;">
                            <i class="bi bi-share-fill"></i>
                            <i class="bi bi-bookmarks-fill"></i>
                            <i class="bi bi-download"></i>
                        </div>
                    </div>
                `

                hairstyleContainer.innerHTML += hairStyleCardSnippet
            });
        }
        else{
            throw new Error(hairStyleData.message);   
        }
    })
    .catch(err =>{
        alert(err)
    })
})