$(function () {

  $('#signupform').ajaxForm(function(data){
    event.preventDefault();

    $('#jquery-loadmodal-js-body').html(data);

    if (data.includes("window.location.href = window.location.href;"))
      {
        window.location.href = "/homepage/getting_started/"
      }
  });

});
