$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    $.get(url, function (data) {
      $('#hello').text(data.hello);
    }).fail(function (jqXHR, textStatus, errorThrown) {
      console.error('Error:', errorThrown);
      $('#hello').text('Error: Failed to fetch translation');
    });
  });
});
