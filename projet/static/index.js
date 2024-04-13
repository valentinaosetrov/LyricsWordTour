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
        var album = "speaknow";
        localStorage.setItem("album", album);
        window.location.href = "song_list.html";
    });
    $("#red").click(function(){
        var album = "red";
        localStorage.setItem("album", album);
        window.location.href = "song_list.html";
        alert("red clicked!");
    });
    $("#1989").click(function(){
        var album = "1989";
        localStorage.setItem("album", album);
        window.location.href = "song_list.html";
        alert("1989 clicked!");
    });
    $("#reputation").click(function(){
        var album = "reputation";
        localStorage.setItem("album", album);
        window.location.href = "song_list.html";
        alert("reputation clicked!");
    });
    $("#lover").click(function(){
        var album = "lover";
        localStorage.setItem("album", album);
        window.location.href = "song_list.html";
        alert("lover clicked!");
    });
    $("#folklore").click(function(){
        var album = "folklore";
        localStorage.setItem("album", album);
        window.location.href = "song_list.html";
        alert("flkl clicked!");
    });
    $("#evermore").click(function(){
        var album = "evermore";
        localStorage.setItem("album", album);
        window.location.href = "song_list.html";
        alert("ev clicked!");
    });
    $("#midnights").click(function(){
        var album = "midnights";
        localStorage.setItem("album", album);
        window.location.href = "song_list.html";
        alert("m clicked!");
    });


});