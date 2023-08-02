$(document).ready(function () {
  var socket = io("192.168.2.106:5000");
  socket.on("connect", function () {
    console.log("conectou");
  });

  socket.on("message", function (data) {
    console.log("enviou mensagem");
    $("#chat-container").append($("<p>").text(data));
    // Scroll to the bottom of the chat container
    $("#chat-container").scrollTop($("#chat-container")[0].scrollHeight);
  });

  $("#botao").on("click", function () {
    console.log("clicou botao");
    sendMessage(socket);
  });

  $("#mensagem").on("keypress", function () {
    if (event.key === "Enter") {
      console.log("deu enter");
      sendMessage(socket);
    }
  });
});

function sendMessage(socket) {
  if ($("#usuario").val().length !== 0 && $("#mensagem").val().length !== 0) {
    socket.send($("#usuario").val() + ": " + $("#mensagem").val());

    // Clear mensagem input field
    $("#mensagem").val("");

    // Set default placeholder
    $("#usuario").attr("placeholder", "Usuário");
    $("#mensagem").attr("placeholder", "Mensagem");

    // Set default input-container input border
    $("#input-container input").css("border", "none");
  } else {
    // Change placeholder when the text of input is empty
    $("#usuario").attr("placeholder", "Precisa ter um usuário");
    $("#mensagem").attr("placeholder", "Precisa ter uma mensagem");

    // Set a red border for input-container input
    $("#input-container input").css("border", "solid 1px red");
    $(".placeholder").css("color", "red");
  }
}
