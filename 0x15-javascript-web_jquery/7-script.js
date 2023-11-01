const getUrl = "https://swapi-api.alx-tools.com/api/people/5/?format=json";

$.get(getUrl, function(data){
    $("#character").text(data.name);
});