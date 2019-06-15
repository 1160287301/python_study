# -*- coding:utf-8 -*-
'''
select()方法接收并监控3个通信列表， 第一个是所有的输入的data,就是指外部发过来的数据，第2个是监控和接收所有要发出去的data(outgoing data),第3个监控错误信息

在网上一直在找这个select.select的参数解释, 但实在是没有, 哎...自己硬着头皮分析了一下。
readable, writable, exceptional = select.select(inputs, outputs, inputs)

第一个参数就是服务器端的socket, 第二个是我们在运行过程中存储的客户端的socket, 第三个存储错误信息。
重点是在返回值, 第一个返回的是可读的list, 第二个存储的是可写的list, 第三个存储的是错误信息的
list
'''
import select
import socket
import queue
from time import sleep
# 创建一个tcp/ip
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
# 将套接字绑定到端口
server_address = ('localhost', 8090)
print('starting up on %s port %s' % server_address)
server.bind(server_address)
# 侦听传入连接
server.listen(5)
# 我们期望从中读取的套接字
inputs = [server]
# 处理要发送的消息
outputs = []
# 输出的消息队列
message_queues = {}

while inputs:
    # 等待至少一个套接字准备好进行处理
    print('等待下一个事件')
    # 开始select 监听, 对input_list 中的服务器端server 进行监听
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    # 处理输出
    # 循环判断是否有客户端连接进来, 当有客户端连接进来时select 将触发
    for s in readable:
        # 判断当前触发的是不是服务端对象, 当触发的对象是服务端对象时,说明有新客户端连接进来了
        # 表示有新用户来连接
        if s is server:
            # A "readable" socket is ready to accept a connection
            connection, client_address = s.accept()
            print('connection from', client_address)
            # this is connection not server
            connection.setblocking(0)
            # 将客户端对象也加入到监听的列表中, 当客户端发送消息时 select 将触发
            inputs.append(connection)

            # Give the connection a queue for data we want to send
            # 为连接的客户端单独创建一个消息队列，用来保存客户端发送的消息
            message_queues[connection] = Queue.Queue()
        else:
            # 有老用户发消息, 处理接受
            # 由于客户端连接进来时服务端接收客户端连接请求，将客户端加入到了监听列表中(input_list), 客户端发送消息将触发
            # 所以判断是否是客户端对象触发
            data = s.recv(1024)
            # 客户端未断开
            if data != '':
                # A readable client socket has data
                print('received "%s" from %s' % (data, s.getpeername()))
                # 将收到的消息放入到相对应的socket客户端的消息队列中
                message_queues[s].put(data)
                # Add output channel for response
                # 将需要进行回复操作socket放到output 列表中, 让select监听
                if s not in outputs:
                    outputs.append(s)
            else:
                # 客户端断开了连接, 将客户端的监听从input列表中移除
                # Interpret empty result as closed connection
                print('closing', client_address)
                # Stop listening for input on the connection
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()

                # Remove message queue
                # 移除对应socket客户端对象的消息队列
                del message_queues[s]

        # Handle outputs
        # 如果现在没有客户端请求, 也没有客户端发送消息时, 开始对发送消息列表进行处理, 是否需要发送消息
        # 存储哪个客户端发送过消息
    for s in writable:
        try:
            # 如果消息队列中有消息,从消息队列中获取要发送的消息
            message_queue = message_queues.get(s)
            send_data = ''
            if message_queue is not None:
                send_data = message_queue.get_nowait()
            else:
                # 客户端连接断开了
                print
                "has closed "
        except Queue.Empty:
            # 客户端连接断开了
            print
            "%s" % (s.getpeername())
            outputs.remove(s)
        else:
            # print "sending %s to %s " % (send_data, s.getpeername)
            # print "send something"
            if message_queue is not None:
                s.send(send_data)
            else:
                print
                "has closed "
            # del message_queues[s]
            # writable.remove(s)
            # print "Client %s disconnected" % (client_address)

        # # Handle "exceptional conditions"
        # 处理异常的情况
    for s in exceptional:
        print('exception condition on', s.getpeername())
        # Stop listening for input on the connection
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        # Remove message queue
        del message_queues[s]

    sleep(1)