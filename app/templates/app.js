function edit_parent() {
    $.ajax({
        url: 'http://127.0.0.1:5000/edit_parent',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify({
        }),
        type: "POST",
        dataType: "json",
        success: function (resp) {

        }
    });
}