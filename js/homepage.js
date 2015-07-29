// assigning a global variable so the width is adjustable across more function calls
var width = 0;
// the function receives an argument (num) from the function call, that helps me to know the id of the checkbox
function incrementProgressBar(num) {
    // get the DOM element containing the progress bar
    var x = document.getElementById("progress-bar");
    // make a list of the DOM elements containing the checkboxes
    var y = document.getElementsByClassName("checkbox");
    // defining a percentage-increase for each checkbox
    var perc_list = [5, 10, 20, 15, 20, 15, 15];
    // looping over the amount of checkboxes (represented through their future %values)
    for (i in perc_list) {
        // if the argument is the same as the index
        if (num == i) {
            // addresses the i-th element in the array and looks for the property "checked"
            if (y[i].checked) {
                // if true, the global width gets incremented with the responding %value
                width += perc_list[i];
                // and finally the width value of the progress bar gets increased
                x.style.width = width + "%";
                // if the bar is full, call the little extra function :)
                if (x.style.width === "100%") {
                    congrats();
                }
            // if there is no "checked" property in the tag (=unchecked)
            } else {
                // reduces the width value for the given amount. this only fires at an
                // onclick() event, therefore only when actually unchecking a previously
                // checked checkbox (prevents it from going into minus values)
                width -= perc_list[i];
                x.style.width = width + "%";
                // if the bar is not full, put back to normal
                normalize();
            }
        }
    }

}

function congrats() {
    var y = document.getElementById("surprise");
    y.classList.add("surprise");
    y.innerHTML = "It was a sweet learning journey!";
}

function normalize() {
    var y = document.getElementById("surprise");
    y.classList.remove("surprise");
    y.innerHTML = "";
}