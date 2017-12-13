/*
    Boilerplate Python 3 SocketIO Flask app
*/

var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', function() {
    socket.emit('connected');
});

socket.on('pong', function() {
    console.log("PONG RECEIVED");
    socket.emit('ping', {data: 'Still connected'});
});


socket.on('update', function(data) {
    console.log("RECEIVED UPDATE");
    update(JSON.parse(data));
});


function update(data) {
    $("#version").text(data.version);
    $("#time").text(data.time);
}
