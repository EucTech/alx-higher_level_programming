$(document).ready(function() {
    // Function to handle translation
    function translateHello() {
        const value = $("#language_code").val();
        const getUrl = "https://www.fourtonfish.com/hellosalut/hello/?lang=" + value;
        $.get(getUrl, function(data) {
            $("#hello").text(data.hello);
        });
    }

    $("#btn_translate").click(translateHello);

    $("#language_code").keypress(function(event) {
        if (event.keyCode === 13) {
            translateHello();
        }
    });
});