const grupo = $("#titulo-chat").text()

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + grupo
    + '/'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    $("#caixa-mensagens").append(`<p>${data.mensagem}</p>`)
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

$("#caixa-mensagem").on( "keyup", function(e) {
    if(e.key==="Enter") {
        let mensagem = $("#input-mensagem").val()
        chatSocket.send(JSON.stringify({
            'mensagem': mensagem
        }));
        $("#input-mensagem").val('')
    }
   
});


