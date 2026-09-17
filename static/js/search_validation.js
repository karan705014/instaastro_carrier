// function validateSearch() {

//     const input = document.getElementById("searchInput");
//     const error = document.getElementById("searchError");

//     const search = input.value.trim();

//     if (search.length < 3) {

//         error.classList.remove("d-none");
//         input.classList.add("is-invalid");

//         return false;
//     }

//     error.classList.add("d-none");
//     input.classList.remove("is-invalid");

//     return true;
// }


// document
//     .getElementById("searchInput")
//     .addEventListener("input", function () {

//         const error = document.getElementById("searchError");

//         if (this.value.trim().length >= 3) {

//             error.classList.add("d-none");
//             this.classList.remove("is-invalid");

//         }

//     });