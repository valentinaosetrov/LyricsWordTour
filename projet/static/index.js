$(document).ready(function(){
    // When the image with id "speaknow" is clicked, show an alert
    $("#debut").click(function(){
        var album = "debut";
        alert(album);
        localStorage.setItem("album", album);
        window.location.href = "song_list.html";
    });
    $("#fearless").click(function(){
        var album = "fearless";
        localStorage.setItem("album", album);
        window.location.href = "song_list.html";
    });
    $("#speaknow").click(function(){
        alert("speak now clicked!");
    });
    $("#red").click(function(){
        alert("red clicked!");
    });
    $("#1989").click(function(){
        alert("1989 clicked!");
    });
    $("#reputation").click(function(){
        alert("reputation clicked!");
    });
    $("#lover").click(function(){
        alert("lover clicked!");
    });
    $("#folklore").click(function(){
        alert("flkl clicked!");
    });
    $("#evermore").click(function(){
        alert("ev clicked!");
    });
    $("#midnights").click(function(){
        alert("m clicked!");
    });


});