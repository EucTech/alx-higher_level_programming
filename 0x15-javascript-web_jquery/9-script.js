const getUrl = "https://hellosalut.stefanbohacek.dev/?lang=fr";

$.get(getUrl, function(data){
    $("#hello").html("<p>" + data.hello + "</p>");
});