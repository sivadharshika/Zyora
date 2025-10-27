document.addEventListener("DOMContentLoaded", ()=>{

    /* === Load Category === */

    const categoryContainer = document.getElementById("categoryContainer")

    fetch('/category/getAllNames?category=nailArt')
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

    const nailArtContainer = document.getElementById("nailArtContainer")

    fetch('/nailArt/getAll')
    .then(res => res.json())
    .then(nailArtData =>{
        if (nailArtData.status == "success") {
            let data = nailArtData.data

            nailArtContainer.innerHTML = ""

            data.forEach(nailArt => {
                let nailArtCardSnippet = `
                    <div class="card p-0 border-0" style="flex: 1 0 30%;">
                        <div class="card-header p-0 border-0 bg-transparent" 
                            style="height: 350px; 
                            overflow: hidden; 
                            background-image: url(data:image/jpeg;base64,${nailArt.image});
                            background-position: center;
                            background-size: cover;
                            background-repeat: no-repeat
                        ">
                        </div>
                        <div class="nailCardBody p-2">
                            <h5 class="card-title" style="font: bold;">${nailArt.title}</h5>
                        </div>
                        <div class="card-footer d-flex justify-content-between"
                            style="background-color: var(--text); color: white !important;">
                            <i class="bi bi-share-fill"></i>
                            <i class="bi bi-bookmarks-fill"></i>
                            <i class="bi bi-download"></i>
                        </div>
                    </div>
                `

                nailArtContainer.innerHTML += nailArtCardSnippet
            });
        }
        else{
            throw new Error(nailArtData.message);   
        }
    })
    .catch(err =>{
        alert(err)
    })
})