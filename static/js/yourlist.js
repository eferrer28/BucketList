  $(function() {
$( "#sortable" ).sortable();
$( "#sortable" ).disableSelection();
});
        
 $(document).ready(function(){
	$(".increase" ).mouseover(function() {
	 $("img").css({"display": "inline"});
	});
	$(".increase").mouseout(function() {
	 $("img").css({"display": "none"}) 
	});
 });

