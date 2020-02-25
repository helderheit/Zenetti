function apiAddCollection(data, onSuccess, onError){
  // Add a collection
    $.ajax
    ({
      type: "POST",
      url: API_URL_PREFIX+"collections",
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

function apiGetCollections(onSuccess, onError){
  // Get a list of collections from the api and hand it over to onSuccess Callback
    $.ajax
    ({
      type: "GET",
      url: API_URL_PREFIX+"collections",
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
function apiGetCollection(collectionId, onSuccess, onError){
  // Get a collection from the api and hand it over to onSuccess Callback
    $.ajax
    ({
      type: "GET",
      url: API_URL_PREFIX+"collections/"+collectionId,
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

function apiRemoveCollection(collectionId, onSuccess, onError){
  // Removes a collection
    $.ajax
    ({
      type: "DELETE",
      url: API_URL_PREFIX+"collections/"+collectionId,
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

function apiUpdateCollection(collectionId, data, onSuccess, onError){
  // Update a collection
    $.ajax
    ({
      type: "PUT",
      url: API_URL_PREFIX+"collections/"+collectionId,
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