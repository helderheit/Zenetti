var API_URL_PREFIX = "api/1.0/";

function apiGetInfo(onSuccess, onError){
  $.ajax
  ({
    type: "GET",
    url: API_URL_PREFIX+"info",
    contentType : 'application/json',
    async: true,
    success: function(data){
      onSuccess(data);
    },
    error: onError,
});
}

function apiLogout(){
  //clears sessionStorage
  sessionStorage.clear();
  $(".menuitem").hide();
}

function apiLogin(username, password, onSuccess, onError){
  // Gets a Token for the api, then hands over onSuccess Callback to getOwnAccountInfo
    $.ajax
    ({
      type: "GET",
      url: API_URL_PREFIX+"token",
      dataType: 'json',
      async: true,

      success: function(data){
        sessionStorage["loggedIn"] = true;
        sessionStorage["token"] = data["token"];
        sessionStorage["username"] = username;
        onSuccess();

      },
      error: onError,
      beforeSend: function (xhr) {
          xhr.setRequestHeader ("Authorization", "Basic " +
                                btoa(username + ":" + password));
      }
  });
}

function apiRenewToken(onSuccess,onError){
  // Gets a new Tokenfor the api
    $.ajax
    ({
      type: "GET",
      url: API_URL_PREFIX+"token",
      dataType: 'json',
      async: true,
      success: function(data){
        sessionStorage["loggedIn"] = true;
        sessionStorage["token"] = data["token"];
        onSuccess();
      },
      error: onError,
      beforeSend: function (xhr) {
          xhr.setRequestHeader ("Authorization", "Basic " +
                                btoa(sessionStorage["token"] + ":" + ""));
      }
  });
}

function apiGetUsers(onSuccess, onError){
  // Gets a list of users from the api and hands it over to onSuccess Callback
    $.ajax
    ({
      type: "GET",
      url: API_URL_PREFIX+"users",
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