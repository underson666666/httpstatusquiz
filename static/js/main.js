"use strict"
var HSQ = HSQ || {}

HSQ.choiseContainer = document.getElementById("choise-container")
HSQ.dispAns = () => {
    let choises = $(".choise")
    for (let choise of choises) {
        let code = choise.children
        code[0].classList.remove("hide")
        choise.classList.remove("alert-dark")
        if (code[0].innerText == HSQ.answer) {
            choise.classList.add("alert", "alert-success")
        } else {
            choise.classList.add("alert", "alert-danger")
        }
    }
}
HSQ.choiseContainer.addEventListener("click", HSQ.dispAns)

