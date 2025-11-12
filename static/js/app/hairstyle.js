document.addEventListener("DOMContentLoaded", () => {

    /* === Load Category === */

    const categoryContainer = document.getElementById("categoryContainer")

    fetch('/category/getAllNames?category=hairStyle')
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



    /* === Load hairstyle === */

    const hairstyleContainer = document.getElementById("hairstyleContainer")

    fetch('/hairStyle/getAll')
        .then(res => res.json())
        .then(hairStyleData => {
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
                        <div class="hairstyleCardBody d-flex justify-content-between align-items-center p-2">
                            <h5 class="card-title" style="font: bold;">${hairStyle.title}</h5>
                        </div>
                        <a href="/select?id=${hairStyle.id}&category=hairStyle">
                                <i 
                                    class="bi ${hairStyle.isSelected == true ? "bi-suit-heart-fill" : "bi-suit-heart"} fs-4 select-btn" 
                                    style="color:${hairStyle.isSelected == true ? "var(--primary)" : "black"}"
                                >
                                </i>
                                </a>
                        <div class="card-footer d-flex justify-content-between"
                            style="background-color: var(--text); color: white !important;">
                            <i class="bi bi-share-fill"></i>
                            <i class="bi bi-download"></i>
                            <i class="bi bi-save"></i>
                        </div>
                    </div>
                `

                    hairstyleContainer.innerHTML += hairStyleCardSnippet
                });
            }
            else {
                throw new Error(hairStyleData.message);
            }
        })
        .catch(err => {
            alert(err)
        })




/* === Load Selected Items === */

const selectedContainer = document.getElementById("selectedContainer")

fetch('/select/getAll')
    .then(res => res.json())
    .then(selectedData => {
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
                        <div class="hairStyleCardBody d-flex justify-content-between align-items-center p-2">
                            <h5 class="card-title" style="font: bold;">${item.title}</h5>
                            
                            <a href="/select?id=${item.id}&category=hairStyle">
                                <i 
                                    class="bi ${item.isSelected == true ? "bi-suit-heart-fill" : "bi-suit-heart"} fs-4 select-btn" 
                                    style="color:${item.isSelected == true ? "var(--primary)" : "black"}"
                                >
                                </i>
                            </a>

                        </div>
                    </div>
                `

                selectedContainer.innerHTML += selectedCardSnippet
            });
        }
        else {
            throw new Error(selectedData.message);
        }
    })
    .catch(err => {
        alert(err)
    })
})