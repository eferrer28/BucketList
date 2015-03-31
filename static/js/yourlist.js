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


  $(document).ready(function() {
    $("#sortable").sortable({
      update: function(event, ui) {
        var serial = $('#sortable').sortable('serialize');
    $.ajax({
      url: "{% url 'index' %}",
      type: "post",
      data: { 'content': serial, 'csrfmiddlewaretoken' : '{{ csrf_token }}' } 
    });
      },
    }).disableSelection();
  });
