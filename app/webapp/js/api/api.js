

var API_URL_PREFIX = "api/1.0/";

var tokenIntervall = setInterval(renewToken, 60*1000*8);
function renewToken() {
  //renew the api-token every 8 Minutes
  if (sessionStorage.getItem("loggedIn") !== null) {
    apiRenewToken(function(){
      console.log("renewed token");
    },function(){
      apiLogout();
      window.location="login.html";

    });
  }
}

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
  window.location = "/login.html"
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
        getOwnAccountInfo(onSuccess());

      },
      error: onError,
      beforeSend: function (xhr) {
          xhr.setRequestHeader ("Authorization", "Basic " +
                                btoa(username + ":" + password));
      }
  });
}
function getOwnAccountInfo(onSuccess){
  //Get information about logged in user and store it in sessionStorage
  $.ajax
  ({
    type: "GET",
    url: API_URL_PREFIX+"users/"+sessionStorage["username"],
    dataType: 'json',
    async: true,

    success: function(data){
      sessionStorage["name"] = data["name"];
      sessionStorage["admin"] = data["admin"];
      sessionStorage["master"] = data["master"];
      sessionStorage["change_password"] = data["change_password"];
      onSuccess();

    },
    beforeSend: function (xhr) {
        xhr.setRequestHeader ("Authorization", "Basic " +
                              btoa(sessionStorage["token"] + ":" + ""));
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

function apiGetUser(username, onSuccess, onError){
  // Gets a users from the api and hands it over to onSuccess Callback
    $.ajax
    ({
      type: "GET",
      url: API_URL_PREFIX+"users/"+username,
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


function apiAddUser(data, onSuccess, onError){
  // Adds a user
    $.ajax
    ({
      type: "POST",
      url: API_URL_PREFIX+"users",
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

function apiUpdateUser(data, onSuccess, onError){
  // Updates a user
    $.ajax
    ({
      type: "PUT",
      url: API_URL_PREFIX+"users",
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
function apiRemoveUser(username, onSuccess, onError){
  // Removes a user
    $.ajax
    ({
      type: "DELETE",
      url: API_URL_PREFIX+"users/"+username,
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

