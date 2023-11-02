const getUrl = "https://www.fourtonfish.com/hellosalut/hello/";

$("#btn_translate").click(function(){
    const value = $("#language_code").val();
    $.get(getUrl + value, function(data) {
        $("#hello").text(data.hello);
    });
});
