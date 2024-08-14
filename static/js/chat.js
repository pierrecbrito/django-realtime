const grupo = $("#titulo-chat").text()
const nome = $('#nome-usuario').text()

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + grupo
    + '/'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    console.log(data)
    $("#caixa-mensagens").append(`<p class="mensagem"><b>${data.remetente} - </b>${data.mensagem} <span id="momento">${data.momento}</span></p> `)
    rolarParaBaixo()
};

chatSocket.onclose = function(e) {
    Toastify({
        text: "Comunicação perdida com o servidor.", 
        duration: 6000,
        style: {
            background: "#8B17FA",
        }
    }).showToast();
    console.error('Chat socket closed unexpectedly');
};

$("#caixa-mensagem").on( "keyup", function(e) {
    if(e.key==="Enter") {
        let mensagem = $("#input-mensagem").val()
        chatSocket.send(JSON.stringify({
            'remetente': nome,
            'mensagem': mensagem
        }));
        $("#input-mensagem").val('')
    }
   
});


const rolarParaBaixo = () => {
    $('#caixa-mensagens').scrollTop($('#caixa-mensagens')[0].scrollHeight);
}

rolarParaBaixo()





