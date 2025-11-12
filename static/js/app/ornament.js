document.addEventListener("DOMContentLoaded", ()=>{

    /* === Load Category === */

    const categoryContainer = document.getElementById("categoryContainer")

    fetch('/category/getAllNames?category=ornaments')
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



    /* === Load Ornament === */

    const ornamentContainer = document.getElementById("ornamentContainer")

    fetch('/ornament/getAll')
    .then(res => res.json())
    .then(ornamentData =>{
        if (ornamentData.status == "success") {
            let data = ornamentData.data

            ornamentContainer.innerHTML = ""

            data.forEach(ornament => {
                let ornamentCardSnippet = `
                    <div class="card p-0 border-0" style="flex: 1 0 30%;">
                        <div class="card-header p-0 border-0 bg-transparent" 
                            style="height: 350px; 
                            overflow: hidden; 
                            background-image: url(data:image/jpeg;base64,${ornament.image});
                            background-position: center;
                            background-size: cover;
                            background-repeat: no-repeat
                        ">
                        </div>
                        <div class="OrnamentCardBody d-flex justify-content-between align-items-center p-2">
                            <h5 class="card-title" style="font: bold;">${ornament.title}</h5>
                            
                            <a href="/select?id=${ornament.id}&category=ornament">
                                <i 
                                    class="bi ${ornament.isSelected == true? "bi-suit-heart-fill" : "bi-suit-heart" } fs-4 select-btn" 
                                    style="color:${ornament.isSelected == true? "var(--primary)" : "black" }"
                                >
                                </i>
                            </a>

                        </div>
                        
                        <div class="card-footer d-flex justify-content-between"
                            style="background-color: var(--text); color: white !important;">
                            <i class="bi bi-share-fill"></i>
                            <i class="bi bi-bookmarks-fill"></i>
                            <i class="bi bi-download"></i>
                        </div>
                    </div>
                `

                ornamentContainer.innerHTML += ornamentCardSnippet
            });
        }
        else{
            throw new Error(ornamentData.message);   
        }
    })
    .catch(err =>{
        alert(err)
    })

    /* === Load Selected Items === */

    const selectedContainer = document.getElementById("selectedContainer")

    fetch('/select/getAll')
    .then(res => res.json())
    .then(selectedData =>{
        if (selectedData.status == "success") {
            let data = selectedData.data

            selectedContainer.innerHTML = ""

            data.forEach(item => {
                let selectedCardSnippet = `
                    <div class="card p-0 border-0" style="flex: 1 0 30%;">
                        <div class="card-header p-0 border-0 bg-transparent" 
                            style="height: 350px; 
                            overflow: hidden; 
                            background-image: url(data:image/jpeg;base64,${item.image});
                            background-position: center;
                            background-size: cover;
                            background-repeat: no-repeat
                        ">
                        </div>
                        <div class="nailCardBody d-flex justify-content-between align-items-center p-2">
                            <h5 class="card-title" style="font: bold;">${item.title}</h5>
                            
                            <a href="/select?id=${item.id}&category=nailArt">
                                <i 
                                    class="bi ${item.isSelected == true? "bi-suit-heart-fill" : "bi-suit-heart" } fs-4 select-btn" 
                                    style="color:${item.isSelected == true? "var(--primary)" : "black" }"
                                >
                                </i>
                            </a>

                        </div>
                    </div>
                `

                selectedContainer.innerHTML += selectedCardSnippet
            });
        }
        else{
            throw new Error(selectedData.message);   
        }
    })
    .catch(err =>{
        alert(err)
    })
})    



