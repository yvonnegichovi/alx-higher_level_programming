$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function (data) {
      $.each(data.results, function (index, movie) {
        $('<li>').text(movie.title).appendTo('#list_movies');
      });
    },
    error: function () {
      $('#list_movies').append('<li>Error fetching movies</li>');
    }
  });
});
