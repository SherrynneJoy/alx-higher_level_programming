$(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.get(url, function (data) {
    const translation = data.hello;
    $('#hello').text(translation);
  }, 'json');
});
