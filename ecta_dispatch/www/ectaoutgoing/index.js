$("#approve").on('click', function(e){
    e.preventDefault();
    var dispatch = $(this).attr("data-target");
    console.log(dispatch);
});