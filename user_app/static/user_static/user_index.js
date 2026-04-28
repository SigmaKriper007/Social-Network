// переключение между регистрацией / логином / назад
$(document).on("click", ".tab, .back-btn", function(e) {
    e.preventDefault();

    $.get($(this).data("url"), function(data) {
        $(".auth-card").replaceWith(data);
    });
});


// регистрация + логин
$(document).on("submit", ".auth-form", function(e) {
    e.preventDefault();

    let form = $(this);

    $.ajax({
        url: form.attr("action"),
        type: "POST",
        data: form.serialize(),

        success: function(response) {

            // регистрация успешна → confirm email
            if (response.message === "User Created") {
                $.get("/user/form/confirm-email/", function(data) {
                    $(".auth-card").replaceWith(data);
                });
            }

            // логин успешен → на главную
            if (response.message === "Login Success") {
                window.location.href = response.redirect_url;
            }

            // ошибки
            if (response.error) {
                console.log(response.error);
                alert("Ошибка формы");
            }
        }
    });
});


// confirm email → авторизация
$(document).on("submit", ".confirm-form", function(e) {
    e.preventDefault();

    $.get("/user/form/login/", function(data) {
        $(".auth-card").replaceWith(data);
    });
});