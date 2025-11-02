function scrollFunc(direction, container) {
    console.log(direction, container)
    let elment = document.getElementById(container)
    let screenWidth = window.screen.width/2;
    console.log(screenWidth)
    console.log(elment)
    if (direction === "Right") {
        elment.scrollLeft += screenWidth
    } else {
            elment.scrollLeft -= screenWidth
        
    }

}