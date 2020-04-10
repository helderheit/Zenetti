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

function apiUpdateItem(itemId, data, onSuccess, onError){
  // Update a collection
    $.ajax
    ({
      type: "PUT",
      url: API_URL_PREFIX+"items/"+itemId,
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

function apiUploadImage(file, onSuccess, onError){
    $.ajax({
            url: API_URL_PREFIX+"file-upload",
            type: "post",
            data: file,
            contentType: false,
            processData: false,
            success: function(response){
                onSuccess(response);
            },
            error: function () {
                onError();
            }
        });
}


function apiGetAnnotations(collectionId, itemId, onSuccess, onError){
  // Get a collection from the api and hand it over to onSuccess Callback
    $.ajax
    ({
      type: "GET",
      url: API_URL_PREFIX+collectionId+"/"+itemId +"/annotations.json",
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

function apiUpdateAnnotations(imageId, annotations, onSuccess, onError){
        $.ajax({
            url: API_URL_PREFIX + "images/" + imageId + "/annotations",
            type: "POST",
            contentType: 'application/json',
            async: true,
            data: JSON.stringify({"annotations":annotations}),
            success: function () {
                onSuccess();
            },
            error: onError,
            beforeSend: function (xhr) {
                xhr.setRequestHeader("Authorization", "Basic " +
                    btoa(sessionStorage["token"] + ":" + ""));
            }
        });
}
function apiGetItemsForUser(onSuccess, onError){
  // Get all items for a user from the api and hand it over to onSuccess Callback
    userId = sessionStorage["username"]
    $.ajax
    ({
      type: "GET",
      url: API_URL_PREFIX+"users/"+userId+"/items",
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