function apiGetPlainAnnotations(itemId, onSuccess, onError){
  // Get a collection from the api and hand it over to onSuccess Callback
    $.ajax
    ({
      type: "GET",
      url: API_URL_PREFIX+itemId +"/annotations_plain.json",
      contentType : 'application/json',
      async: true,
      success: function(data){
        onSuccess(data);
      },
      error: onError,
      beforeSend: function (xhr) {
          xhr.setRequestHeader ("Authorization", "Basic " +
                                btoa(sessionStorage["token"] + ":" + ""));
      }
  });
}
