$(".checkbox").on("click", function(){
    if($(this).hasClass("checked")){
        $(this).removeClass("checked");
    }else{
        $(this).addClass("checked");
    }
});