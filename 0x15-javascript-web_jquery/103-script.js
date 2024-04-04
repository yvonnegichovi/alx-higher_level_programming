$(document).ready(function() {
    function fetchTranslation() {
        const languageCode = $('#language_code').val();
        const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

        $.get(url, function(data) {
            $('#hello').text(data.hello);
        }).fail(function(jqXHR, textStatus, errorThrown) {
            console.error('Error:', errorThrown);
            $('#hello').text('Error: Failed to fetch translation');
        });
    }

    $('#btn_translate').click(fetchTranslation);

    $('#language_code').keypress(function(event) {
        if (event.which === 13) {
            fetchTranslation();
        }
    });
});
