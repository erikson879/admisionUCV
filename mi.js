


function yourfunction(){ 
	var start = new Date;
	console.log(start);
	$('#timer').text((new Date - start) * 600000+":"+(new Date - start) / 1000 + " Seconds"); }


