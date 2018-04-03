function edit_parent() {

	$.ajax(
		{
			url: 'http://127.0.0.1:5000/edit_parent/',
			contentType: 'application/json; charset=utf-8',
			data: JSON.stringify({
				'fname_p': $("#fname_p").val(),
				'lname_p': $("#lname_p").val(),
				'bday_p': $("#bday_p").val(),
				'add_p': $("#add_p").val(),
                }),
			type: "PUT",
			dataType: "json",
			error: function (e) {
			},
			success: function (resp) {
                if (resp.status == 'ok') {
                	alert("Successfully updated!")
                    window.location.replace('p_prof.html')

                 }
				else {
					alert("ERROR")
				}

			}
		});
}