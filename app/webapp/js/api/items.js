function apiAddItem(collectionId, data, onSuccess, onError){
  // Add a collection
    $.ajax
    ({
      type: "POST",
      url: API_URL_PREFIX+"items/"+collectionId,
      contentType : 'application/json',
      async: true,
      data:JSON.stringify(data),
      success: function(){
        onSuccess();
      },
      error: onError,
      beforeSend: function (xhr) {
          xhr.setRequestHeader ("Authorization", "Basic " +
                                btoa(sessionStorage["token"] + ":" + ""));
      }
  });
}

function apiGetItem(itemId, onSuccess, onError){
  // Get a collection from the api and hand it over to onSuccess Callback
    $.ajax
    ({
      type: "GET",
      url: API_URL_PREFIX+"items/"+itemId,
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

function apiRemoveItem(collectionId, itemId, onSuccess, onError){
  // Removes a item
    $.ajax
    ({
      type: "DELETE",
      url: API_URL_PREFIX+"items/"+collectionId+"/"+itemId,
      contentType : 'application/json',
      async: true,
      success: function(){
        onSuccess();
      },
      error: onError,
      beforeSend: function (xhr) {
          xhr.setRequestHeader ("Authorization", "Basic " +
                                btoa(sessionStorage["token"] + ":" + ""));
      }
  });
}