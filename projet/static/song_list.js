$(document).ready(function(){
    // Retrieve the variable from local storage
    var album = localStorage.getItem("album");
    $('#' + album).show();

    $("#submit").click(function( event ){
        alert("submit click");
        var song = $("#title").val();
        event.preventDefault(); // Prevent the default form submission behavior
        alert("here's the text: " + song); // Alert with the value of the input field
    });
});