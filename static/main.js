function getPrediction(){
	$.ajax({url:'/prediction/'}).then(function(response){
		var no_train = response[0];
		var train = response[1];
		var header, message, percent;
		if(train > no_train){
			header = "Train!"
			percent = Math.round(train * 100);
		} else {
			header = "No train!"
			percent = Math.round(no_train * 100);
		}
		message = "We are " + percent + "% sure."
		$('#header').html(header)
		$('#prediction').html(message)
	}).fail(function(err){
		return err;
	})
}
$(document).ready(function(){
	getPrediction();
	setInterval(getPrediction, 1000 * 60)
})
