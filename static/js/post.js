$(document).ready(function () {
  $(".text").click(function () {
    $(".overlay").fadeIn(500);
  });
  $(".overlay").not(".text").click(function() {
    $(".overlay").fadeOut(500);
  });
  $("[type = submit]").click(function () {
    var post = $("textarea").val();
    $("<p class='post'>" + post + "</p>").appendTo("section");
  });
});