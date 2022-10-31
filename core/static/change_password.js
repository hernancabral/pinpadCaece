$(function() {
	$( "#PINform" ).draggable();
});

$( "#PINcode" ).html(
	"<form action='' method='' name='PINform' id='PINform' autocomplete='off' draggable='true'>" +
		"<input id='PINbox' type='password' value='' name='PINbox' disabled />" +
		"<br/>" +
		"<input type='button' class='PINbutton' name='1' value='1' id='1' onClick=addNumber(this); />" +
		"<input type='button' class='PINbutton' name='2' value='2' id='2' onClick=addNumber(this); />" +
		"<input type='button' class='PINbutton' name='3' value='3' id='3' onClick=addNumber(this); />" +
		"<input type='button' class='PINbutton' name='A' value='A' id='A' onClick=addNumber(this); />" +
		"<br>" +
		"<input type='button' class='PINbutton' name='4' value='4' id='4' onClick=addNumber(this); />" +
		"<input type='button' class='PINbutton' name='5' value='5' id='5' onClick=addNumber(this); />" +
		"<input type='button' class='PINbutton' name='6' value='6' id='6' onClick=addNumber(this); />" +
		"<input type='button' class='PINbutton' name='B' value='B' id='B' onClick=addNumber(this); />" +
		"<br>" +
		"<input type='button' class='PINbutton' name='7' value='7' id='7' onClick=addNumber(this); />" +
		"<input type='button' class='PINbutton' name='8' value='8' id='8' onClick=addNumber(this); />" +
		"<input type='button' class='PINbutton' name='9' value='9' id='9' onClick=addNumber(this); />" +
		"<input type='button' class='PINbutton' name='C' value='C' id='C' onClick=addNumber(this); />" +
		"<br>" +
		"<br>" +
		"<input type='button' class='PINbutton' name='*' value='*' id='*' onClick=addNumber(this); />" +
		"<input type='button' class='PINbutton' name='0' value='0' id='0' onClick=addNumber(this); />" +
		"<input type='button' class='PINbutton' name='#' value='#' id='#' onClick=addNumber(this); />" +
		"<input type='button' class='PINbutton' name='D' value='D' id='D' onClick=addNumber(this); />" +
		"<br>" +
		"<input type='button' class='PINbutton clear' name='-' value='clear' id='-' onClick=clearForm(this); />" +
		"<input type='button' class='PINbutton enter' name='+' value='enter' id='+' onClick=submitForm(PINbox); />" +
	"</form>"
);

function addNumber(e){
	var v = $( "#PINbox" ).val();
	$( "#PINbox" ).val( v + e.value );
}
function clearForm(e){
	$( "#PINbox" ).val( "" );
}
function submitForm(e) {
	if (e.value == "") {
		alert("Enter a PIN");
	} else {
		apiCall( e.value, function( r ) {
            Swal.fire({
              title: 'Pin Cambiado',
              text: 'Por favor ingresarlo en la pantalla principal',
              icon: 'success',
              html: '<a href="/">Ir al inicio</a> '
            })
		});

		document.getElementById('PINbox').value = "";
	};
};

function apiCall( value, callback ) {
	$.ajax({
		type: "POST",
		contentType: "application/json",
		url: "/api/change-password/" + value,
		success: function ( r ) {
			callback( r );
		},
		error: function ( response ) {
			console.log( response )
		},
	});
}
