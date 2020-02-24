$(".checkbox").on("click", function(){
    if($(this).hasClass("checked")){
        $(this).removeClass("checked");
    }else{
        $(this).addClass("checked");
    }
});

function loadTemplate(url, onSuccess){
      $.ajax({
            url: url,
            cache: false,
            success: function(data){
                onSuccess(data)
            }
    });
}

function replaceParameter(text, parameter, value){
  var re = new RegExp(parameter, 'g');
  return(text.replace(re, value));
}
