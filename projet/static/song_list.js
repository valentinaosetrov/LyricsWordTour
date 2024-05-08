$(document).ready(function(){
    // retrouver l'album choisi
    var album = localStorage.getItem("album");
    $('#' + album).show();

});