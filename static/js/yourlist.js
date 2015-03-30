  $(function() {
$( "#sortable" ).sortable();
$( "#sortable" ).disableSelection();
});
        
 $(document).ready(function(){
	$(".increase" ).mouseover(function() {
	 $(".image").css({"display": "inline"});
	});
	$(".increase").mouseout(function() {
	 $(".image").css({"display": "none"}) 
	});
 });
