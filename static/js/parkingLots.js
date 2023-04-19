var parent = document.querySelector(".parent");
console.log(parent)

var child = parent.children;

teste = Array.from(child)

teste.forEach(element => {
    element.addEventListener("click", () => {
        console.log(element)
        if(element.classList.contains("True") && element.classList.contains("park") ){
            console.log("if 1")
            element.classList.remove("True")
        }
        else{
            console.log("else")
            element.classList.add("True")
        }
    })
});