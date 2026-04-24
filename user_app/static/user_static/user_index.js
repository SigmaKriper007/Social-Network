$(document).on("click", ".tab", function(e) {
    e.preventDefault();

    $(".tab").removeClass("active");
    $(this).addClass("active");

    $.get($(this).data("url"), function(data) {
        $(".auth-card").replaceWith(data);
    });
});