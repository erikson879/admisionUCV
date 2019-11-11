


//function yourfunction(){ 
//	var start = new Date;
//	console.log(start);
//	$('#timer').text((new Date - start) * 600000+":"+(new Date - start) / 1000 + " Seconds"); }
//
function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}

function sleepFor( sleepDuration ){
    var now = new Date().getTime();
    while(new Date().getTime() < now + sleepDuration){ /* do nothing */ } 
}
