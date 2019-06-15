var ws = require('nodejs-websocket');

var server = ws.createServer(function (conn) {
    console.log('New Connection');
    //接收消息触发事件
    conn.on('text', function (str) {
        console.log(str);
        boardcast(str);
    });
    //给客户端发消息
    // setTimeout(function () {
    //     conn.sendText('来自服务端的消息');
    // }, 2000)
    //发生异常触发事件
    conn.on('error', function (err) {
        console.log(err);
    })
    //链接关闭触发事件
    conn.on('close', function () {
        console.log(1);
    })
}).listen(2333);
//广播对象(给每个客户端都发送消息)
function boardcast(str) {
    server.connections.forEach(function (conn) {
        conn.sendText(str);
    });
}