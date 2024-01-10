$(function () {
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.get(url, function (data) {
    const charName = data.name;
    $('#character').text(charName);
  });
});
