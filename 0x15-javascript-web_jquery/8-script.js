$(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, function (data) {
    for (let i = 0; i < data.length; i++) {
      const title = data[i].title;
      $('#list_movies').append('<li>' + title + '</li>');
    }
  });
});
