from manim import *
import math
config.max_files_cached = 500


class Layer(Scene):
    def construct(self):
        web_page = SVGMobject('web_page.svg').set(color=BLUE).scale(.8)
        client = SVGMobject('client.svg')
        http_msg = VGroup(Text('HTTP请求报文', color=BLACK).scale(.4).set_z_index(2))
        http_msg.add(SurroundingRectangle(http_msg, color=YELLOW_E, fill_opacity=1).set_z_index(1))
        router = ImageMobject('router.png').scale(.4)
        routers = Group(Arrow(ORIGIN, RIGHT*3, color=YELLOW_E), router.copy(), Text('...'), router.copy(),
                        Arrow(ORIGIN, RIGHT, buff=0, color=YELLOW_E)
                        ).arrange(RIGHT)
        server = SVGMobject('server.svg')
        Group(client, routers, server).arrange(RIGHT)
        http_msg.next_to(routers[0], UP)
        web_page.generate_target()
        web_page.target.scale(.8).stretch(.8, 1).move_to(client).shift(UP*.2)
        cross = Cross().scale(.5).move_to(http_msg).set_z_index(3)
        multi_proc = VGroup(*[Rectangle(width=1, height=.5, fill_opacity=1).set(color=YELLOW_E) for _ in range(3)]
                            ).arrange(RIGHT).next_to(server, UP).shift(LEFT*.3)
        for index in range(3):
            multi_proc.add(Text('进程'+str(index), font='MonoSpace', color=BLACK).scale(.5).move_to(multi_proc[index]))
        question = Text('?').next_to(multi_proc, UP)
        self.play(Create(web_page))
        self.play(Create(VGroup(client, http_msg, server)), FadeIn(routers), MoveToTarget(web_page))
        self.play(Create(cross))
        self.play(FadeOut(cross), http_msg.animate.next_to(server, DOWN))
        self.play(ReplacementTransform(server.copy(), multi_proc), Create(question))
        self.play(FadeOut(client, web_page, routers, server, multi_proc, question), http_msg.animate.move_to(ORIGIN))
        port_num = VGroup(Rectangle(width=3, height=1.2, fill_opacity=.8).set(color=BLUE).set_z_index(-1)
                          ).next_to(http_msg, UP, buff=-.6)
        port_num.add(Text('端口号', color=BLACK).scale(.5).next_to(port_num, UP, buff=-.4))
        ip_addr = VGroup(Rectangle(width=3.2, height=1.8, fill_opacity=.8).set(color=GREEN).set_z_index(-2)
                         ).next_to(http_msg, UP, buff=-.7)
        ip_addr.add(Text('IP地址', color=BLACK).scale(.5).next_to(ip_addr, UP, buff=-.4))
        web = VGroup(SVGMobject('web.svg').scale(.7), Text('80', font='MonoSpace', color=BLUE)).arrange(DOWN)
        mail = VGroup(SVGMobject('mail.svg').scale(.6), Text('25', font='MonoSpace', color=BLUE)).arrange(DOWN)
        VGroup(web, mail).arrange(RIGHT, buff=1).next_to(ip_addr, DOWN)
        well_known_txt = Text('熟知端口号').set_color_by_gradient(BLUE_A, BLUE_E).next_to(VGroup(web, mail), DOWN)
        bit16 = VGroup(*[Square(.5, color=BLUE, fill_opacity=.8) for _ in range(16)]
                       ).arrange(RIGHT, buff=0).next_to(ip_addr, DOWN, buff=1)
        bit16.add(Brace(bit16, DOWN))
        bit16.add(Text('16位').scale(.5).next_to(bit16, DOWN))
        port_range = VGroup(Line(ORIGIN, RIGHT*8).set(color=[BLUE_E, BLUE_A])).move_to(bit16)
        tip = Line(ORIGIN, UP*.5, color=BLUE_A)
        port_range.add(tip.copy().move_to(port_range[0].get_start()),
                       tip.copy().move_to(port_range[0].get_start()+RIGHT),
                       tip.copy().set(color=BLUE_E).move_to(port_range[0].get_end()))
        port_range.add(Text('0', font='MonoSpace', color=BLUE_A).scale(.5).next_to(port_range[1], DOWN),
                       Text('1023', font='MonoSpace', color=BLUE_A).scale(.5).next_to(port_range[2], DOWN),
                       Text('65535', font='MonoSpace', color=BLUE_E).scale(.5).next_to(port_range[3], DOWN))
        well_known = VGroup(Brace(Line(port_range[0].get_start(), port_range[0].get_start()+RIGHT), UP))
        well_known.add(Text('熟知端口号').scale(.5).next_to(well_known, UP)).set(color=BLUE_A)
        socket_addr = Text('(IP地址, 端口号)', t2c={'IP地址': GREEN, '端口号': BLUE}
                           ).scale(.6).next_to(ip_addr, DOWN, buff=1)
        socket = VGroup(Rectangle(width=1.5, height=.8, fill_opacity=1).set(color=BLUE_E).set_z_index(1),
                        Text('套接字').scale(.5).set_z_index(1)).next_to(socket_addr, DOWN)
        self.play(Create(VGroup(port_num[0], ip_addr[0])))
        self.play(Write(ip_addr[1]))
        self.play(Write(port_num[1]))
        self.play(Create(VGroup(web, mail)))
        self.play(Write(well_known_txt))
        self.play(FadeOut(web, mail, well_known_txt))
        self.play(ReplacementTransform(port_num[1].copy(), bit16))
        self.play(ReplacementTransform(bit16, port_range))
        self.play(Create(well_known))
        self.play(FadeOut(well_known, port_range))
        self.play(ReplacementTransform(VGroup(ip_addr[1], port_num[1]).copy(), socket_addr), Create(socket))
        self.play(FadeOut(socket_addr, http_msg, ip_addr, port_num), socket.animate.move_to(ORIGIN))
        app = VGroup(Rectangle(width=3, height=1, fill_opacity=.8).set(color=YELLOW_E))
        app.add(Text('应用程序', color=BLACK).scale(.5).next_to(app, UP, buff=-.4))
        down_layer = VGroup(Rectangle(width=3, height=1, fill_opacity=.8).set(color=BLUE))
        down_layer.add(Text('网络底层', color=BLACK).scale(.5).next_to(down_layer, DOWN, buff=-.4))
        VGroup(app, down_layer).arrange(DOWN, buff=0).move_to(socket)
        application = VGroup(Rectangle(width=3, height=.5, fill_opacity=1).set(color=YELLOW_E),
                             Text('应用层', color=BLACK).scale(.5))
        transport = VGroup(Rectangle(width=3, height=.5, fill_opacity=1).set(color=BLUE),
                           Text('传输层', color=BLACK).scale(.5))
        network = VGroup(Rectangle(width=3, height=.5, fill_opacity=1).set(color=GREEN),
                         Text('网络层', color=BLACK).scale(.5))
        link = VGroup(Rectangle(width=3, height=.5, fill_opacity=1).set(color=ORANGE),
                      Text('链路层', color=BLACK).scale(.5))
        physics = VGroup(Rectangle(width=3, height=.5, fill_opacity=1).set(color=RED),
                         Text('物理层', color=BLACK).scale(.5))
        line = Line(ORIGIN, DOWN)
        layers = VGroup(application, line.copy(), transport, line.copy(), network, line.copy(), link, line.copy(),
                        physics).arrange(DOWN, buff=0)
        p2p = VGroup(Line(ORIGIN, LEFT*2).next_to(transport, LEFT, buff=0),
                     Line(ORIGIN, RIGHT*2).next_to(transport, RIGHT, buff=0)).set(color=BLUE)
        web_page = SVGMobject('web_page.svg').set(color=BLUE).scale(.7)
        p2p.add(web_page.copy().next_to(p2p[0], LEFT), web_page.copy().next_to(p2p[1], RIGHT))
        segment = VGroup(Rectangle(width=1.2, height=.5, fill_opacity=1).set(color=YELLOW_E),
                         Text('应用报文', color=BLACK).scale(.4))
        segment.add(Square(.5, color=BLUE, fill_opacity=1).next_to(segment, LEFT, buff=0)).next_to(p2p[0], UP)
        segment.add(Text('报文段', color=BLUE).scale(.5).next_to(segment, UP))
        h2h = VGroup(Line(ORIGIN, LEFT*2).next_to(network, LEFT, buff=0),
                     Line(ORIGIN, RIGHT*2).next_to(network, RIGHT, buff=0))
        h2h.add(client.copy().scale(.7).next_to(h2h[0], LEFT), client.copy().scale(.7).next_to(h2h[1], RIGHT)).set(color=GREEN)
        datagram = VGroup(Rectangle(width=1.2, height=.5, fill_opacity=1).set(color=BLUE),
                          Text('报文段', color=BLACK).scale(.5))
        datagram.add(Square(.5, color=GREEN, fill_opacity=1).next_to(datagram, LEFT, buff=0)).next_to(h2h[0], UP)
        datagram.add(Text('数据报', color=GREEN).scale(.5).next_to(datagram, UP))
        r2r = Group(Line(ORIGIN, LEFT*2, color=ORANGE).next_to(link, LEFT, buff=0),
                    Line(ORIGIN, RIGHT*2, color=ORANGE).next_to(link, RIGHT, buff=0))
        router = ImageMobject('orange_router.png').scale(.4)
        r2r.add(router.copy().next_to(r2r[0], LEFT), router.copy().next_to(r2r[1], RIGHT))
        frm = VGroup(Rectangle(width=1.2, height=.5, fill_opacity=1).set(color=GREEN),
                     Text('数据报', color=BLACK).scale(.5))
        frm.add(Square(.5, color=ORANGE, fill_opacity=1).next_to(frm, LEFT, buff=0)).next_to(r2r[0], UP)
        frm.add(Text('帧', color=ORANGE).scale(.5).next_to(frm, UP))
        bit_flow = VGroup(Line(ORIGIN, LEFT*2).next_to(physics, LEFT, buff=0),
                          Line(ORIGIN, RIGHT*2).next_to(physics, RIGHT, buff=0))
        bits = Text('010100100', font='MonoSpace').scale(.6)
        bit_flow.add(bits.copy().next_to(bit_flow[0], UP).shift(LEFT*.2),
                     bits.copy().next_to(bit_flow[1], UP).shift(RIGHT*.2)).set(color=RED)
        arrow = Arrow(ORIGIN, DOWN, buff=0)
        layer_arrow = VGroup(arrow.copy().move_to(layers[1]), arrow.copy().move_to(layers[3]),
                             arrow.copy().move_to(layers[5]), arrow.copy().move_to(layers[7]))
        self.play(Create(VGroup(app, down_layer)))
        self.play(FadeOut(socket, app), ReplacementTransform(down_layer, layers[2:]))
        self.play(Indicate(transport))
        self.play(Create(p2p))
        self.play(Create(segment[:-1]))
        self.play(Write(segment[-1]))
        self.play(Indicate(network))
        self.play(Create(h2h))
        self.play(FadeOut(segment[-1]), ReplacementTransform(segment[:-1], datagram[:-1]))
        self.play(Write(datagram[-1]))
        self.play(Indicate(link))
        self.play(FadeIn(r2r))
        self.play(FadeOut(datagram[-1]), ReplacementTransform(datagram[:-1], frm[:-1]))
        self.play(Write(frm[-1]))
        self.play(Indicate(physics))
        self.play(Create(bit_flow[:2]), ReplacementTransform(frm[:-1], bit_flow[2:]), FadeOut(frm[-1]))
        self.play(Create(layers[:2]))
        self.play(Create(layer_arrow), run_time=4)
        self.wait()
        self.clear()


class Programme(Scene):
    def construct(self):
        udp_client = Code('udp_client.py', style=Code.styles_list[8]).to_edge(UP, buff=.2)
        protocol = Text('IPv4, UDP', t2c={'IPv4': GREEN, 'UDP': BLUE}).next_to(udp_client[2][:3], RIGHT, buff=1)
        transport = VGroup(Text('传输层').scale(.6), Rectangle(width=10, height=1)
                           ).arrange(DOWN).set(color=BLUE).next_to(udp_client, DOWN)
        network = VGroup(Text('网络层').scale(.6), Rectangle(width=10, height=1)
                         ).arrange(DOWN).set(color=GREEN).next_to(transport, DOWN)
        host = SVGMobject('client.svg').scale(.7)
        sender = VGroup(host.copy(), Text('发送方').scale(.6)).arrange(DOWN).next_to(VGroup(transport, network), LEFT)
        receiver = VGroup(host.copy(), Text('接收方').scale(.6)).arrange(DOWN).next_to(VGroup(transport, network), RIGHT)
        sender_proc = VGroup(*[Rectangle(width=1, height=.5, fill_opacity=1).set(color=YELLOW_E) for _ in range(3)]
                             ).arrange(RIGHT).next_to(sender, UP).shift(RIGHT)
        client_proc_label = ['进程A', '进程B', '进程C']
        for index in range(3):
            sender_proc.add(Text(client_proc_label[index], font='MonoSpace', color=BLACK
                                 ).scale(.5).move_to(sender_proc[index]))
        rcver_proc = sender_proc[:3].copy().next_to(receiver, UP).shift(LEFT)
        for index in range(3):
            rcver_proc.add(Text('进程'+str(index), font='MonoSpace', color=BLACK).scale(.5).move_to(rcver_proc[index]))
        segment = VGroup(Rectangle(width=1, height=.5, fill_opacity=1).set(color=YELLOW_E),
                         Square(.5, color=BLUE, fill_opacity=1)).arrange(LEFT, buff=0)
        segments = VGroup(*[segment.copy() for _ in range(3)]).arrange(RIGHT).move_to(transport[1]).shift(LEFT*2)
        for index in range(3):
            segments[index].add(Text(str(index), font='MonoSpace', color=BLACK).scale(.5).move_to(segments[index][1]))
        multiplex = Text('多路复用').set_color_by_gradient(BLUE_A, BLUE_E).move_to(transport[1]).shift(LEFT*2)
        demultiplex = Text('多路分解').set_color_by_gradient(BLUE_A, BLUE_E).move_to(transport[1]).shift(RIGHT*2)
        udp_header = VGroup(*[VGroup(Rectangle(width=2, height=.5, fill_opacity=1)) for _ in range(4)]
                            ).set_color_by_gradient(BLUE_A, BLUE_E)
        udp_header_field = ['源端口号', '目标端口号', '长度', '校验和']
        for index in range(4):
            udp_header[index].add(Text(udp_header_field[index], color=BLACK).scale(.5))
        Group(Group(udp_header[0], udp_header[1]).arrange(RIGHT, buff=0),
              Group(udp_header[2], udp_header[3]).arrange(RIGHT, buff=0)
              ).arrange(DOWN, buff=0).next_to(udp_client, DOWN, buff=2)
        field_len = VGroup(Brace(udp_header[0], UP))
        field_len.add(Text('16位', font='MonoSpace').scale(.5).next_to(field_len, UP))
        self.play(Create(udp_client))
        self.play(Indicate(udp_client[2][1:3]))
        self.play(Indicate(udp_client[2][3]))
        self.play(ReplacementTransform(udp_client[2][3][-20:-1].copy(), protocol))
        self.play(FadeIn(sender, receiver, transport, network, sender_proc, rcver_proc))
        self.play(ReplacementTransform(sender_proc.copy(), VGroup(segments[0][0], segments[1][0], segments[2][0])))
        self.play(Create(segments[0][1:]), Create(segments[1][1:]), Create(segments[2][1:]))
        self.play(segments.animate.move_to(network[1]).shift(LEFT*2))
        self.play(Write(multiplex))
        self.play(FadeOut(multiplex))
        self.play(segments.animate.shift(RIGHT*4))
        self.play(segments.animate.move_to(transport[1]).shift(RIGHT*2))
        self.play(ReplacementTransform(segments, rcver_proc))
        self.play(Write(demultiplex))
        self.play(FadeOut(sender, receiver, sender_proc, rcver_proc, transport, network, demultiplex))
        self.play(Create(udp_header))
        self.play(Create(field_len))
        self.play(FadeOut(field_len, udp_header, protocol), udp_client.animate.move_to(ORIGIN))
        self.play(Indicate(udp_client[2][5]))
        self.play(Indicate(udp_client[2][6]))
        self.play(Indicate(udp_client[2][6][-5:-1], scale_factor=1.5))
        self.play(Indicate(udp_client[2][8]))
        udp_server = Code('udp_server.py', style=Code.styles_list[8])
        Group(udp_client.copy(), udp_server).arrange(DOWN, buff=.5)
        self.play(udp_client.animate.next_to(udp_server, UP, buff=.5), Create(udp_server))
        self.play(Indicate(udp_server[2][2]))
        self.play(Indicate(udp_server[2][3]))
        self.play(Indicate(udp_server[2][6]))
        self.play(Indicate(udp_server[2][8]))
        self.wait()
        self.clear()

        tcp = Text('TCP', color=BLUE).to_edge(UP).set_z_index(1)
        tcp_client = Code('tcp_client.py', style=Code.styles_list[8])
        self.play(Write(tcp))
        self.play(Create(tcp_client))
        self.play(Indicate(tcp_client[2][3]))
        self.play(Indicate(tcp_client[2][4]))
        self.play(Indicate(tcp_client[2][6]))
        self.play(Indicate(tcp_client[2][7]))
        tcp_server = Code('tcp_server.py', style=Code.styles_list[8]).to_edge(UP, buff=.2)
        listen_socket = VGroup(Rectangle(width=1.5, height=.8, fill_color=WHITE, fill_opacity=1),
                               Text('套接字', color=BLUE_E).scale(.5))
        connect_socket = VGroup(Rectangle(width=1.5, height=.8, fill_opacity=1).set(color=BLUE_E),
                                Text('套接字').scale(.5))
        client_socket = VGroup(Rectangle(width=1.5, height=.8, fill_opacity=1).set(color=BLUE),
                               Text('套接字', color=BLACK).scale(.5))
        Group(client_socket, Group(listen_socket, connect_socket).arrange(DOWN)
              ).arrange(RIGHT, buff=4).next_to(tcp_server, DOWN)
        client_socket.align_to(connect_socket, DOWN)
        listen_socket.add(SVGMobject('listen.svg').flip().scale(.3).next_to(listen_socket, LEFT))
        client = Text('客户', color=BLUE).scale(.6).next_to(client_socket, DOWN, buff=.5)
        server = Text('服务器', color=BLUE_E).scale(.6).next_to(connect_socket, DOWN, buff=.5)
        boundary = DashedLine(ORIGIN, DOWN*5).shift(DOWN)
        connect = DoubleArrow(client_socket.get_right(), connect_socket.get_left())
        self.play(FadeOut(tcp_client))
        self.play(Create(tcp_server), tcp.animate.align_to(tcp_server, RIGHT).shift(LEFT*.2))
        self.play(Indicate(tcp_server[2][2]), Create(listen_socket[:-1]), FadeIn(server))
        self.play(Indicate(tcp_server[2][4]), Create(listen_socket[-1]))
        self.play(Indicate(tcp_server[2][7]), Create(connect_socket))
        self.play(FadeIn(client, boundary, client_socket), Create(connect))
        self.play(Indicate(tcp_server[2][11]), FadeOut(connect_socket, connect, client_socket))
        self.play(FadeIn(connect_socket, connect, client_socket))
        self.wait()
        self.clear()


def bit8(name, colour):
    return VGroup(Rectangle(width=4, height=.5, color=colour, fill_opacity=1), Text(name, color=BLACK).scale(.5))


tcp_header = VGroup(*[bit8('源端口号', BLUE_B), bit8('目标端口号', BLUE_D)]).arrange(RIGHT, buff=0)
tcp_header.add(*Group(VGroup(Rectangle(width=8, height=.5, fill_opacity=1).set(color=GREEN_B),
                             Text('序号', color=BLACK).scale(.5)),
                      VGroup(Rectangle(width=8, height=.5, fill_opacity=1).set(color=GREEN_D),
                             Text('确认号', color=BLACK).scale(.5))
                      ).arrange(DOWN, buff=0).next_to(tcp_header, DOWN, buff=0))
flag = VGroup(*[VGroup(Rectangle(width=.25, height=.5, fill_opacity=1)) for _ in range(8)]
              ).arrange(RIGHT, buff=0).set_color_by_gradient(RED_E, RED_A)
flag_label = ['CWR', 'ECE', 'URG', 'ACK', 'PSH', 'RST', 'SYN', 'FIN']
for index in range(8):
    flag[index].add(Text(flag_label[index], color=BLACK).scale(.35).rotate(PI/2).move_to(flag[index]))
tcp_header.add(*Group(VGroup(Rectangle(width=1, height=.5, fill_opacity=1).set(color=ORANGE),
                             Text('首部长度', color=BLACK).scale(.4)),
                      VGroup(Rectangle(width=1, height=.5, stroke_width=0), Text('未使用').scale(.4)),
                      flag, bit8('接收窗口', YELLOW_B)).arrange(RIGHT, buff=0).next_to(tcp_header, DOWN, buff=0))
tcp_header.add(*Group(bit8('校验和', YELLOW_D), bit8('紧急数据指针', RED_A)
                      ).arrange(RIGHT, buff=0).next_to(tcp_header, DOWN, buff=0))
tcp_header.add(VGroup(Rectangle(width=8, height=1, fill_opacity=1).set(color=WHITE), Text('选项', color=BLACK).scale(.5)
                      ).next_to(tcp_header, DOWN, buff=0))
tcp_header.move_to(ORIGIN)

segment = VGroup(VGroup(Rectangle(width=.8, height=.5, fill_opacity=1).set(color=BLUE_E), Text('首部').scale(.5)))
segment.add(*[Square(.5, color=BLUE, fill_opacity=.8) for _ in range(5)]).arrange(RIGHT, buff=0)
for byte in range(5):
    segment.add(Text(str(byte), font='MonoSpace', color=GREEN_B
                     ).scale(.5).next_to(segment[byte + 1], UP, buff=.1))


class SeqAck(Scene):
    def construct(self):
        self.play(Create(tcp_header))
        self.play(Indicate(tcp_header[2]))
        self.play(tcp_header.animate.to_edge(UP, buff=.2))
        segment.next_to(tcp_header, DOWN)
        send_arrow = VGroup(Arrow(ORIGIN, RIGHT*4, color=GREEN_B),
                            Text('seq = 0', color=GREEN_B, font='MonoSpace').scale(.5)
                            ).arrange(DOWN, buff=0).next_to(segment, DOWN, buff=.2)
        ack = VGroup(segment[:4].copy(), Arrow(ORIGIN, LEFT*4, color=GREEN_D),
                     Text('ack = 5', color=GREEN_D, font='MonoSpace').scale(.5)
                     ).arrange(DOWN, buff=0).next_to(send_arrow, DOWN, buff=.5)
        sender = SVGMobject('client.svg').scale(.8).next_to(Group(send_arrow, ack), LEFT)
        receiver = SVGMobject('client.svg').scale(.8).next_to(Group(send_arrow, ack), RIGHT)
        piggyback = Text('捎带确认').set_color_by_gradient(GREEN_A, GREEN_E).next_to(receiver, RIGHT)
        cumulative_txt = Text('累计确认').set_color_by_gradient(GREEN_A, GREEN_E).next_to(receiver, RIGHT)
        self.play(Create(segment))
        self.play(Circumscribe(segment[6], shape=Circle))
        self.play(Indicate(tcp_header[3]))
        self.play(FadeIn(sender, receiver), Create(send_arrow))
        self.play(Create(ack[1]))
        self.play(Write(ack[2]))
        self.play(Indicate(flag[3]))
        self.play(Create(ack[0]))
        self.play(Write(piggyback))
        self.play(FadeOut(segment, ack, send_arrow), ReplacementTransform(piggyback, cumulative_txt))
        self.play(VGroup(sender, receiver, cumulative_txt).animate.shift(UP*1.2))
        segment.next_to(sender, DOWN)
        segment2 = segment[:4].copy()
        for bit in range(3):
            segment2.add(Text(str(bit+5), font='MonoSpace', color=GREEN_B
                              ).scale(.5).next_to(segment2[bit+1], UP, buff=.1))
        segment2.next_to(sender, DOWN)
        cumulative = VGroup(Arrow(receiver.get_left(), sender.get_right(), color=GREEN_D))
        cumulative.add(Text('ack = 8', font='MonoSpace', color=GREEN_D).scale(.5).next_to(cumulative, UP, buff=0))
        timer = VGroup(Circle(.3), Dot(ORIGIN).scale(.5), Line(ORIGIN, UP*.2), Line(UP*.3, UP*.4)
                       ).set(color=WHITE).next_to(sender, LEFT)
        send_buffer = VGroup(SurroundingRectangle(segment))
        send_buffer.add(Text('发送缓存').scale(.5).next_to(send_buffer, LEFT)).set(color=BLUE_B)
        segment_c = segment.copy()
        ack = VGroup(Arrow(receiver.get_left(), sender.get_right()))
        ack.add(Text('seq = 5', font='MonoSpace').scale(.5).next_to(ack, UP, buff=0)).set(color=GREEN_D)
        lost_ack = VGroup(Arrow(receiver.get_left(), receiver.get_left()+LEFT*2))
        lost_ack.add(Text('seq = 5', font='MonoSpace').scale(.5).next_to(lost_ack, UP, buff=0)).set(color=GREEN_D)
        ack2 = VGroup(Arrow(receiver.get_left(), sender.get_right()))
        ack2.add(Text('seq = 8', font='MonoSpace').scale(.5).next_to(ack2, UP, buff=0)).set(color=GREEN_D)
        self.play(FadeIn(segment))
        self.play(segment.animate.next_to(receiver, DOWN))
        self.play(FadeIn(segment2))
        self.play(segment2.animate.next_to(segment, DOWN))
        self.play(Create(cumulative))
        self.remove(segment, segment2)
        self.play(ReplacementTransform(VGroup(segment.copy(), segment2.copy()), receiver))
        self.play(FadeOut(cumulative, cumulative_txt))
        self.play(FadeIn(segment.next_to(sender, DOWN)))
        self.play(segment.animate.shift(RIGHT*3))
        self.play(FadeOut(segment))
        self.play(Create(timer))
        self.play(Rotate(timer[2], -PI, about_point=timer[1].get_center()))
        self.play(FadeIn(segment.next_to(sender, DOWN)))
        self.play(segment.animate.next_to(receiver, DOWN), Rotate(timer[2], PI, about_point=timer[1].get_center()))
        self.play(FadeIn(segment_c), Create(send_buffer))
        self.play(Create(ack))
        self.play(FadeOut(segment_c))
        self.play(FadeOut(timer, send_buffer, ack))
        self.play(Create(lost_ack))
        self.play(FadeOut(lost_ack))
        self.play(FadeIn(segment_c))
        self.play(segment_c.animate.next_to(segment, DOWN))
        self.play(FadeOut(segment_c))
        self.play(Create(ack))
        self.play(FadeOut(ack, segment))
        self.play(FadeIn(segment2.next_to(sender, DOWN)))
        self.play(segment2.animate.next_to(receiver, DOWN))
        receiver_buffer = VGroup(SurroundingRectangle(segment2))
        receiver_buffer.add(Text('接收缓存').scale(.5).next_to(receiver_buffer, RIGHT)).set(color=BLUE_D)
        self.play(Create(receiver_buffer))
        self.play(FadeIn(segment.next_to(sender, DOWN)))
        self.play(segment.animate.next_to(receiver_buffer[0], DOWN))
        self.play(Create(ack2))
        self.remove(segment, segment2)
        self.play(ReplacementTransform(VGroup(segment.copy(), segment2.copy()), receiver))
        self.play(FadeOut(ack2, receiver_buffer), FadeIn(timer))
        long = Sector(outer_radius=.2, inner_radius=0, angle=5*PI/4, color=RED, arc_center=timer[1].get_center()
                      ).rotate(-3*PI/4, about_point=timer[1].get_center()).set_opacity(.8)
        short = Sector(outer_radius=.2, inner_radius=0, angle=PI/4, color=RED, arc_center=timer[1].get_center()
                       ).rotate(PI/4, about_point=timer[1].get_center()).set_opacity(.8)
        timeout = Sector(outer_radius=.2, inner_radius=0, angle=PI, color=RED, arc_center=timer[1].get_center()
                         ).rotate(-PI/2, about_point=timer[1].get_center()).set_opacity(.8)
        double = Sector(outer_radius=.2, inner_radius=0, angle=PI, color=RED, arc_center=timer[1].get_center()
                        ).rotate(-3*PI/2, about_point=timer[1].get_center()).set_opacity(.8)
        estimate_rtt = Text('EstimatedRTT=(1–α)*EstimatedRTT+α*SampleRTT', font='MonoSpace', color=RED_A
                            ).scale(.7).next_to(Group(sender, receiver), DOWN)
        alpha = Text('EstimatedRTT=0.875*EstimatedRTT+0.125*SampleRTT', font='MonoSpace', color=RED_A
                     ).scale(.7).move_to(estimate_rtt)
        dev_rtt = Text('DevRTT=(1–β)*DevRTT+β*|SampleRTT–EstimatedRTT|', font='MonoSpace', color=RED_B
                       ).scale(.7).next_to(estimate_rtt, DOWN)
        beta = Text('DevRTT=0.75*DevRTT+0.25*|SampleRTT–EstimatedRTT|', font='MonoSpace', color=RED_B
                    ).scale(.7).move_to(dev_rtt)
        timeout_calc = Text('TimeoutInterval=EstimatedRTT+4 *DevRTT', font='MonoSpace', color=RED_C
                            ).scale(.7).next_to(dev_rtt, DOWN)
        fast_retrans = Text('快速重传'
                            ).set_color_by_gradient(GREEN_A, GREEN_E).next_to(Group(sender, receiver), DOWN, buff=1)
        segment3 = segment[:4].copy()
        for byte in range(3):
            segment3.add(Text(str(byte+8), font='MonoSpace', color=GREEN_B).scale(.5).next_to(segment3[byte+1], UP, buff=.1))
        segment3.next_to(sender, DOWN)
        duplicate_ack = Text('冗余ACK').scale(.6).next_to(ack, DOWN, buff=0).set_color_by_gradient(GREEN_A, GREEN_E)
        self.play(Rotate(timer[2], -5*PI/4, about_point=timer[1].get_center()), Create(long))
        self.play(Rotate(timer[2], 5*PI/4, about_point=timer[1].get_center()), FadeOut(long))
        self.play(Rotate(timer[2], -PI/4, about_point=timer[1].get_center()), Create(short))
        self.play(AnimationGroup(FadeIn(segment.next_to(sender, DOWN)),
                                 segment.animate.next_to(receiver, DOWN), run_time=2),
                  AnimationGroup(FadeIn(segment_c.next_to(sender, DOWN)),
                                 segment_c.animate.next_to(receiver, DOWN, buff=1.2), run_time=2, lag_ratio=.5))
        self.play(FadeOut(segment, segment_c, short), Rotate(timer[2], PI/4, about_point=timer[1].get_center()))
        self.play(FadeIn(segment.next_to(sender, DOWN)))
        self.play(segment.animate.next_to(receiver, DOWN))
        self.play(Create(ack))
        self.play(FadeOut(segment, ack))
        self.play(Write(estimate_rtt))
        self.play(TransformMatchingShapes(estimate_rtt, alpha))
        self.play(Write(dev_rtt))
        self.play(TransformMatchingShapes(dev_rtt, beta))
        self.play(Write(timeout_calc))
        self.play(Rotate(timer[2], -PI, about_point=timer[1].get_center()), Create(timeout))
        self.play(Create(double))
        self.play(FadeOut(timer, timeout, double, alpha, beta, timeout_calc))
        self.play(Write(fast_retrans))
        self.play(FadeIn(segment3))
        self.play(segment3.animate.next_to(receiver, DOWN))
        self.play(Create(ack))
        self.play(Write(duplicate_ack))
        self.play(FadeOut(duplicate_ack), Create(ack))
        self.play(Create(ack))
        self.play(FadeIn(segment2.next_to(sender, DOWN)))
        self.play(segment2.animate.next_to(segment3, DOWN))
        self.play(FadeOut(sender, receiver, ack, segment2, segment3, fast_retrans))
        self.wait()


class Congestion(Scene):
    def construct(self):
        congestion_ctrl = Text('拥塞控制').set_color_by_gradient(RED_A, RED_E).next_to(tcp_header, DOWN, buff=1)
        self.add(tcp_header.to_edge(UP, buff=.2))
        # self.play(tcp_header.animate.move_to(ORIGIN))
        # self.play(Indicate(tcp_header[4]))
        # self.play(Indicate(tcp_header[-1]))
        # self.play(Indicate(tcp_header[5]))
        # self.play(Indicate(tcp_header[6]))
        # self.play(Indicate(tcp_header[6][:2]))
        # self.play(Write(congestion_ctrl))
        # self.play(tcp_header.animate.to_edge(UP, buff=.2), FadeOut(congestion_ctrl))
        # sender = SVGMobject('client.svg').scale(.8)
        # receiver = SVGMobject('client.svg').scale(.8)
        # Group(sender, receiver).arrange(RIGHT, buff=6).next_to(tcp_header, DOWN)
        # router = ImageMobject('router.png').scale(.4).next_to(tcp_header, DOWN).set_y(sender.get_y())
        # buffer = VGroup(*[Polygon(ORIGIN, DOWN*.5, [-.4, -.4, 0], [-.4, .1, 0], fill_opacity=.8) for _ in range(5)]
        #                 ).arrange(RIGHT, buff=-.1).set_color_by_gradient(BLUE_A, BLUE_E).next_to(router, DOWN)
        # ax = VGroup(Axes(x_range=[0, 5, 1], y_range=[0, 5, 1], x_length=2.5, y_length=2.5,
        #                  axis_config={'include_numbers': False}).next_to(tcp_header, DOWN))
        # ax.add(Text('链路利用率').scale(.5).next_to(ax[0][0]),
        #        Text('延迟').scale(.5).next_to(ax[0][1].get_end(), LEFT).shift(DOWN*.2))
        # graph = ax[0].plot(lambda x: 2.5*(1/(5-x)-1/5), x_range=[0, 4.5]).set(color=RED)
        # sent = VGroup(*[Square(.5, color=BLUE, fill_opacity=.8) for _ in range(8)]
        #               ).arrange(RIGHT, buff=0).next_to(sender, DOWN, buff=1.2)
        # sent[:3].set(color=GREEN)
        # acked = VGroup(Brace(sent[:3], DOWN, buff=0))
        # acked.add(Text('已确认').scale(.5).next_to(acked, DOWN, buff=0)).set(color=GREEN)
        # unacked = VGroup(Brace(sent[3:5], UP, buff=0))
        # unacked.add(Text('已发送未确认').scale(.5).next_to(unacked, UP, buff=0)).set(color=BLUE)
        # congestion_wnd = VGroup(SurroundingRectangle(sent[3:7], color=RED))
        # congestion_wnd.add(Text('拥塞窗口').set_color_by_gradient(RED_A, RED_E).scale(.6).next_to(congestion_wnd, DOWN))
        # overflow = Cross().scale(.6).move_to(sent[-3:])
        # ecn = VGroup(Arrow(router.get_right(), receiver.get_left()))
        # ecn.add(Text('ECN').scale(.5).next_to(ecn, UP)).set(color=RED)
        # ece = VGroup(Arrow(receiver.get_left(), router.get_right()))
        # ece.add(Text('ECE = 1', font='MonoSpace').scale(.5).next_to(ece, UP))
        # ece.add(ece.copy().next_to(router, LEFT).shift(UP*.25)).set(color=RED)
        # half = SurroundingRectangle(sent[3:5], color=RED)
        # cwr = VGroup(Arrow(sender.get_right(), router.get_left()))
        # cwr.add(Text('CWR = 1', font='MonoSpace').scale(.5).next_to(cwr, UP))
        # cwr.add(cwr.copy().next_to(router, RIGHT).shift(UP*.25)).set(color=RED)
        # self.play(FadeIn(router), Create(buffer))
        # self.play(FadeIn(sender, segment.next_to(sender, DOWN)))
        # self.play(segment.animate.next_to(buffer, DOWN))
        # self.play(FadeOut(segment))
        # self.play(FadeOut(sender, router, buffer))
        # self.play(Create(VGroup(ax, graph)))
        # self.play(FadeOut(ax, graph))
        # self.play(FadeIn(sender, router, receiver))
        # self.play(Create(congestion_wnd))
        # self.play(FadeIn(sent[:5], acked, unacked))
        # self.play(FadeOut(acked, unacked))
        # self.play(Create(sent[-3:]))
        # self.play(Create(overflow))
        # self.play(FadeOut(sent[-3:], overflow))
        # self.play(Create(ecn))
        # self.play(FadeOut(ecn))
        # self.play(Create(ece))
        # self.play(ReplacementTransform(congestion_wnd[0], half), congestion_wnd[1].animate.next_to(half, DOWN))
        # self.play(FadeOut(ece))
        # self.play(Create(cwr))
        # self.play(FadeOut(router, cwr, congestion_wnd[1], half, sent[:5]),
        #           sender.animate.shift(RIGHT), receiver.animate.shift(LEFT))
        # mss8 = VGroup(*[Square(.5, color=YELLOW_E, fill_opacity=.8) for _ in range(8)]
        #               ).arrange(RIGHT, buff=0).next_to(sender, DOWN, buff=1)
        # cwnd8 = SurroundingRectangle(mss8, color=RED)
        # cwnd4 = SurroundingRectangle(mss8[:4], color=RED)
        # cwnd2 = SurroundingRectangle(mss8[:2], color=RED)
        # cwnd1 = SurroundingRectangle(mss8[0], color=RED)
        # cwnd_list = [cwnd1, cwnd2, cwnd4, cwnd8]
        # mss = Text('1MSS', color=RED).scale(.4).move_to(mss8[0])
        # ack = VGroup(Arrow(receiver.get_left(), sender.get_right()))
        # ack.add(Text('ACK').scale(.5).next_to(ack, UP, buff=0)).set(color=GREEN)
        # ack2 = VGroup(ack.copy(), ack.copy()).arrange(DOWN, buff=0).set_y(sender.get_y())
        # ack4 = VGroup(ack2.copy(), ack2.copy()).arrange(DOWN, buff=0).set_y(sender.get_y()).scale(.8)
        # ack_list = [ack, ack2, ack4]
        # self.play(Create(cwnd1), Write(mss))
        # self.play(FadeOut(mss))
        # for rtt in range(3):
        #     self.play(FadeIn(mss8[:int(math.pow(2, rtt))]))
        #     self.play(mss8[:int(math.pow(2, rtt))].animate.next_to(receiver, DOWN))
        #     self.remove()
        #     self.play(FadeOut(mss8[:int(math.pow(2, rtt))]),
        #               ReplacementTransform(mss8[:int(math.pow(2, rtt))].copy(), receiver), Create(ack_list[rtt]))
        #     mss8[:int(math.pow(2, rtt))].next_to(mss8[int(math.pow(2, rtt))], LEFT, buff=0)
        #     self.play(ReplacementTransform(cwnd_list[rtt], cwnd_list[rtt+1]))
        #     self.play(FadeOut(ack_list[rtt]))
        # self.play(FadeIn(mss8))
        # self.play(FadeOut(sender, receiver, cwnd8, mss8))
        plane = Axes(x_range=(0, 15), y_range=[0, 16, 2], x_length=7.5, y_length=4,
                     axis_config={'include_numbers': True}).scale(.9).next_to(tcp_header, DOWN, buff=.1)
        label = VGroup(Text('RTT').scale(.5).next_to(plane[0]).shift(UP*.15),
                       Text('拥塞窗口(MSS)').scale(.5).next_to(plane[1].get_end()).shift(DOWN*.2))
        slow_start1 = plane.plot_line_graph(x_values=range(1, 5), y_values=[1, 2, 4, 8], line_color=GREEN_D,
                                            vertex_dot_style=dict(color=GREEN_B))
        avoidance1 = plane.plot_line_graph(x_values=range(4, 9), y_values=range(8, 13), line_color=YELLOW_E,
                                           vertex_dot_style=dict(color=YELLOW)).set_z_index(1)
        timeout = plane.plot_line_graph(x_values=[8, 9], y_values=[12, 1], line_color=RED,
                                        vertex_dot_style=dict(stroke_width=0, fill_opacity=0))
        dup_ack = plane.plot_line_graph(x_values=[8, 9], y_values=[12, 9], line_color=RED,
                                        vertex_dot_style=dict(stroke_width=0, fill_opacity=0))
        slow_start2 = plane.plot_line_graph(x_values=range(9, 13), y_values=[1, 2, 4, 6], line_color=GREEN_D,
                                            vertex_dot_style=dict(color=GREEN_B))
        avoidance2 = plane.plot_line_graph(x_values=range(12, 16), y_values=range(6, 10), line_color=YELLOW_E,
                                           vertex_dot_style=dict(color=YELLOW))
        fast_recovery = plane.plot_line_graph(x_values=range(9, 16), y_values=range(9, 16), line_color=BLUE_D,
                                              vertex_dot_style=dict(color=BLUE_B))
        slow_start_txt = Text('慢开始').scale(.6).set_color_by_gradient(GREEN_A, GREEN_E
                                                                     ).next_to(slow_start1, UP).shift(LEFT*.3)
        boundary1 = plane.get_vertical_line(plane.coords_to_point(4, 14),
                                            line_config={'dashed_ratio': .7}, color=GREEN_B)
        ssthresh1 = VGroup(plane.get_horizontal_line(plane.coords_to_point(14, 8),
                                                     line_config={'dashed_ratio': .7}, color=YELLOW_E))
        ssthresh1.add(Text('ssthresh', color=YELLOW_E).scale(.5).next_to(ssthresh1, RIGHT))
        avoidance_txt = Text('拥塞避免').scale(.6).set_color_by_gradient(YELLOW_A, YELLOW_E
                                                                     ).next_to(avoidance1, UP, buff=.1)
        boundary2 = plane.get_vertical_line(plane.coords_to_point(8, 14),
                                            line_config={'dashed_ratio': .7}, color=YELLOW_E)
        tahoe = Text('TCP Tahoe').scale(.5).next_to(avoidance2, RIGHT).shift(UP*.3)
        fast_recovery_txt = Text('快速恢复').scale(.6).set_color_by_gradient(BLUE_B, BLUE_D
                                                                         ).next_to(fast_recovery, UP).shift(DOWN*.5)
        reno = Text('TCP Reno').scale(.5).next_to(fast_recovery, RIGHT).shift(UP*.5)
        self.play(FadeIn(plane, label), Create(slow_start1), Write(slow_start_txt), Create(boundary1))
        self.play(Create(ssthresh1))
        self.play(Create(avoidance1), Write(avoidance_txt), Create(boundary2))
        self.play(Create(timeout), ssthresh1.animate.shift(DOWN*.45))
        self.play(Create(VGroup(slow_start2, avoidance2)))
        self.play(Write(tahoe))
        self.play(Create(VGroup(dup_ack, fast_recovery)), Write(fast_recovery_txt))
        self.play(Write(reno))
        self.wait()
        self.clear()


class Test(Scene):
    def construct(self):
        tcp_header.to_edge(UP, buff=.2)
        plane = Axes(x_range=(0, 15), y_range=[0, 16, 2], x_length=7.5, y_length=4,
                     axis_config={'include_numbers': True}).scale(.9).next_to(tcp_header, DOWN, buff=.1)
        slow_start1 = plane.plot_line_graph(x_values=range(1, 5), y_values=[1, 2, 4, 8], line_color=GREEN_D,
                                            vertex_dot_style=dict(color=GREEN_B))
        avoidance1 = plane.plot_line_graph(x_values=range(4, 9), y_values=range(8, 13), line_color=YELLOW_E,
                                           vertex_dot_style=dict(color=YELLOW))
        timeout1 = plane.plot_line_graph(x_values=[8, 9], y_values=[12, 1], line_color=RED,
                                         vertex_dot_style=dict(stroke_width=0, fill_opacity=0))
        timeout2 = plane.plot_line_graph(x_values=[8, 9], y_values=[12, 9], line_color=RED,
                                         vertex_dot_style=dict(stroke_width=0, fill_opacity=0))
        slow_start2 = plane.plot_line_graph(x_values=range(9, 13), y_values=[1, 2, 4, 6], line_color=GREEN_D,
                                            vertex_dot_style=dict(color=GREEN_B))
        avoidance2 = plane.plot_line_graph(x_values=range(12, 16), y_values=range(6, 10), line_color=YELLOW_E,
                                           vertex_dot_style=dict(color=YELLOW))
        fast_recovery = plane.plot_line_graph(x_values=range(9, 16), y_values=range(9, 16), line_color=PURPLE_D,
                                              vertex_dot_style=dict(color=PURPLE_B))
        self.add(plane, slow_start1, avoidance1, timeout1, timeout2, slow_start2, avoidance2, fast_recovery)


class SynFin(Scene):
    def construct(self):
        self.add(tcp_header.to_edge(UP, buff=.2))
        self.play(tcp_header.animate.center())
        self.play(Indicate(flag[2]))
        self.play(Indicate(flag[4]))
        self.play(Indicate(tcp_header[9]))
        self.play(Indicate(flag[5]))
        self.play(Indicate(flag[-2:]))
        self.wait()
        self.clear()

        client = VGroup(Arrow(ORIGIN, DOWN*5.5, buff=0), Text('时间').scale(.5)).arrange(DOWN)
        server = VGroup(Arrow(ORIGIN, DOWN*5.5, buff=0), Text('时间').scale(.5)).arrange(DOWN)
        VGroup(client, server).arrange(RIGHT, buff=4).shift(DOWN*.5)
        client.add(Text('客户').scale(.5).next_to(client, UP),
                   SVGMobject('client.svg').scale(.8).next_to(client[0], LEFT, buff=1))
        server.add(Text('服务器').scale(.5).next_to(server, UP),
                   SVGMobject('server.svg').scale(.8).next_to(server[0], RIGHT, buff=1))

        def state(name, wid, clr, pos, side, size):
            rc = VGroup(Rectangle(width=wid, height=.5, fill_opacity=.8).set(color=clr),
                        Text(name, color=BLACK).scale(size))
            if side == 'c':
                rc.rotate(PI/2).next_to(client[0].get_center()+UP*pos, LEFT, buff=0)
            if side == 's':
                rc.rotate(-PI/2).next_to(server[0].get_center()+UP*pos, RIGHT, buff=0)
            return rc
        connect = Code(code='clientSocket.connect((serverName,serverPort))', language='py', style=Code.styles_list[8]
                       )[2].next_to(client[-1])
        slope1 = math.atan(3/8)
        slope2 = math.atan(1/8)
        syn = VGroup(Arrow(client[0].get_center()+UP*2.25, server[0].get_center()+UP*.75, buff=0))
        syn.add(Text('SYN = 1', font='MonoSpace').scale(.5).rotate(-slope1).next_to(syn, UP, buff=-.8),
                Text('seq = 123', font='MonoSpace').scale(.5).rotate(-slope1).next_to(syn, DOWN, buff=-.8)
                ).set(color=RED)
        synack = VGroup(Arrow(server[0].get_center()+UP*.75, client[0].get_center()+DOWN*.75, buff=0))
        synack.add(Text('SYN = 1', font='MonoSpace').scale(.5).rotate(slope1).next_to(synack, UP, buff=-.8),
                   Text('seq = 321, ack = 124', font='MonoSpace'
                        ).scale(.45).rotate(slope1).next_to(synack, DOWN, buff=-1.2).shift(RIGHT*.3)).set(color=GREEN)
        ack = VGroup(Arrow(client[0].get_center()+DOWN*.75, server[0].get_center()+DOWN*2.25, buff=0))
        ack.add(Text('SYN = 0', font='MonoSpace').scale(.5).rotate(-slope1).next_to(ack, UP, buff=-.8),
                Text('seq = 124, ack = 322', font='MonoSpace').scale(.5).rotate(-slope1).next_to(ack, DOWN, buff=-1.2)
                ).set(color=BLUE)
        syn_sent = state('SYN_SENT', 3, RED, .75, 'c', .5)
        listen = state('LISTEN', 2, WHITE, 1.75, 's', .5)
        syn_rcvd = state('SYN_RCVD', 3, GREEN, -.75, 's', .5)
        handshake_txt = Text('三次握手').set_color_by_gradient(BLUE_A, BLUE_E).next_to(ack, DOWN)
        delayed_syn = VGroup(Line(client[0].get_center()+UP*2.25, UP*(server[0].get_y()+1.5)),
                             Line(UP*(server[0].get_y()+1.5), DOWN*(-server[0].get_y()+.75)),
                             Arrow(DOWN*(-server[0].get_y()+.75), server[0].get_center()+DOWN*1.5, buff=0)
                             ).set(color=RED_B)
        delayed_syn.add(Text('滞留', color=RED_A).scale(.5).next_to(delayed_syn[1]))
        flood = VGroup()
        for syn_seg in range(5):
            flood.add(syn[0].copy().shift(DOWN*syn_seg*.4), synack[0].copy().shift(DOWN*syn_seg*.4))
        flood_txt = Text('SYN泛洪攻击').set_color_by_gradient(RED_A, RED_E).next_to(ack, DOWN)
        hash_func = VGroup(Rectangle(width=1.5, height=.5, fill_opacity=1).set(color=GREEN),
                           Text('哈希函数', color=BLACK).scale(.5))
        hash_input = VGroup(Text('源IP地址', color=YELLOW_E), Text('目标IP地址', color=YELLOW_E),
                            Text('源端口号', color=BLUE), Text('目标端口号', color=BLUE), Text('神秘参数', color=PURPLE)
                            ).scale(.5).arrange(DOWN).next_to(hash_func, UP)
        hash_output = Text('SYNACK报文段序号', color=GREEN).scale(.5).next_to(hash_func, DOWN)
        syn_cookie = Text('SYN Cookie').set_color_by_gradient(GREEN_A, GREEN_E).next_to(hash_output, UP)
        established_c = state('ESTABLISHED', 1, BLUE, .75, 'c', .2)
        established_s = state('ESTABLISHED', 1, BLUE, .25, 's', .2)
        fin_c = VGroup(Arrow(client[0].get_center()+UP*.25, server[0].get_center()+DOWN*.25, buff=0).set_z_index(1))
        fin_c.add(Text('FIN').scale(.5).rotate(-slope2).next_to(fin_c, UP, buff=-.2)).set(color=RED)
        ack_s = VGroup(Arrow(server[0].get_center()+DOWN*.25, client[0].get_center()+DOWN*.75, buff=0))
        ack_s.add(Text('ACK').scale(.5).rotate(slope2).next_to(ack_s, UP, buff=-.2)).set(color=GREEN)
        fin_s = VGroup(Arrow(server[0].get_center() + DOWN*1.25, client[0].get_center() + DOWN*1.75, buff=0
                             ).set_z_index(1))
        fin_s.add(Text('FIN').scale(.5).rotate(slope2).next_to(fin_s, UP, buff=-.2)).set(color=RED)
        ack_c = VGroup(Arrow(client[0].get_center() + DOWN*1.75, server[0].get_center() + DOWN*2.25, buff=0))
        ack_c.add(Text('ACK').scale(.5).rotate(-slope2).next_to(ack_c, UP, buff=-.2)).set(color=GREEN)
        handshake = VGroup(Arrow(client[0].get_center()+UP*2.25, server[0].get_center()+UP*1.75, buff=0, color=RED),
                           Arrow(server[0].get_center()+UP*1.75, client[0].get_center()+UP*1.25, buff=0, color=GREEN),
                           Arrow(client[0].get_center()+UP*1.25, server[0].get_center()+UP*.75, buff=0, color=BLUE))
        fin_wait1 = state('FIN_WAIT_1', 1, RED_B, -.25, 'c', .2)
        close_wait = state('CLOSE_WAIT', 1, RED, -.75, 's', .2)
        fin_wait2 = state('FIN_WAIT_2', 1, RED, -1.25, 'c', .2)
        last_ack = state('LAST_ACK', 1, GREEN, -1.75, 's', .3)
        time_wait = state('TIME_WAIT', 1, WHITE, -2.25, 'c', .2)
        self.play(FadeIn(client[-1]), Write(connect))
        self.play(FadeIn(client[:-1], server), FadeOut(connect), Create(syn[:-1]))
        self.play(Create(syn_sent))
        self.play(Create(synack[:-1]))
        self.play(FadeIn(listen))
        self.play(ReplacementTransform(listen.copy(), syn_rcvd))
        self.play(Create(ack[:-1]))
        self.play(Indicate(ack[1]))
        self.play(Write(handshake_txt))
        self.play(Write(syn[-1]), Write(synack[-1]), Write(ack[-1]))
        self.play(FadeOut(ack))
        self.play(Create(ack))
        self.play(FadeOut(syn_sent, listen, syn_rcvd, syn, synack, ack, handshake_txt))
        self.play(Create(VGroup(delayed_syn[:2], delayed_syn[3])))
        self.play(Create(syn[0].shift(DOWN*3)), Create(delayed_syn[2]))
        self.play(FadeOut(syn[0], delayed_syn))
        syn[0].shift(UP*3)
        self.play(Create(VGroup(syn, synack)))
        self.play(FadeOut(syn, synack))
        self.play(Create(flood))
        self.play(Write(flood_txt))
        self.play(FadeOut(flood, flood_txt))
        self.play(FadeIn(hash_input, hash_func))
        self.remove(hash_input)
        self.play(ReplacementTransform(hash_input.copy(), hash_func))
        self.remove(hash_func)
        self.play(ReplacementTransform(hash_func.copy(), hash_output))
        self.play(Write(syn_cookie))
        self.play(FadeOut(syn_cookie, hash_output))
        self.play(Create(VGroup(syn, synack, ack)))
        check = VGroup(hash_input, Arrow(ORIGIN, DOWN*.5, buff=0), hash_func, Arrow(ORIGIN, DOWN*.5, buff=0),
                       Text('SYN Cookie', color=GREEN).scale(.5)).arrange(DOWN)
        Group(server[-1].copy(), check).arrange(DOWN).next_to(server[0], RIGHT, buff=1)
        self.play(Create(check), server[-1].animate.next_to(check, UP))
        self.play(FadeOut(check), server[-1].animate.next_to(server[0], RIGHT, buff=1),
                  ReplacementTransform(VGroup(syn, synack, ack), handshake))
        communicate = Tex(r'\vdots').next_to(ack, DOWN, buff=-.3)
        listen = state('LISTEN', 1, WHITE, 2.25, 's', .3)
        syn_sent = state('SYN_SENT', 1, RED, 1.75, 'c', .3)
        syn_rcvd = state('SYN_RCVD', 1, GREEN, 1.25, 's', .3)
        server_state = VGroup(listen, syn_rcvd, established_s, close_wait, last_ack)
        client_state = VGroup(syn_sent, established_c, fin_wait1, fin_wait2, time_wait)
        closed_s = server_state.copy().set(color=GREY)
        closed_s.add(Text('CLOSED', color=GREY).scale(.5).rotate(-PI/2).next_to(closed_s, RIGHT))
        closed_c = client_state.copy().set(color=GREY)
        closed_c.add(Text('CLOSED', color=GREY).scale(.5).rotate(PI/2).next_to(closed_c, LEFT))
        timer = VGroup(Circle(.3), Dot(ORIGIN).scale(.5), Line(ORIGIN, UP * .2), Line(UP * .3, UP * .4)
                       ).set(color=WHITE).next_to(time_wait, LEFT)
        lost_last_ack = VGroup(Arrow(client[0].get_center()+DOWN*1.75, UP*(client[0].get_y()-2), buff=0))
        lost_last_ack.add(Text('ACK').scale(.5).rotate(-slope2).next_to(lost_last_ack, DOWN, buff=-.2)).set(color=GREEN)
        self.play(FadeIn(listen, syn_sent, syn_rcvd, established_c, established_s, communicate))
        self.play(Create(fin_c))
        self.play(Create(fin_wait1))
        self.play(Create(ack_s))
        self.play(Create(close_wait), Create(fin_wait2))
        self.play(Create(fin_s))
        self.play(Create(last_ack))
        self.play(Create(ack_c))
        self.play(Create(time_wait))
        self.play(FadeIn(closed_s))
        self.play(Create(timer))
        self.play(Rotate(timer[2], -PI, about_point=timer[1].get_center()))
        self.play(FadeIn(closed_c))
        self.play(FadeOut(closed_c, closed_s))
        self.remove(ack_c)
        self.play(ReplacementTransform(ack_c.copy(), lost_last_ack))
        self.play(FadeOut(lost_last_ack))
        self.play(Create(fin_s))
        self.play(Create(ack_c))
        self.play(Rotate(timer[2], PI, about_point=timer[1].get_center()))
        self.wait()
        self.clear()

        self.play(FadeIn(tcp_header.center()))
        self.play(Indicate(tcp_header[-4]))
        self.play(tcp_header.animate.to_edge(UP))
        sender = SVGMobject('client.svg').scale(.8)
        receiver = SVGMobject('client.svg').scale(.8)
        Group(sender, receiver).arrange(RIGHT, buff=4).next_to(tcp_header, DOWN)
        rwnd_seg = VGroup(Arrow(receiver.get_left(), sender.get_right()))
        rwnd_seg.add(Text('接收窗口').scale(.6).next_to(rwnd_seg, UP, buff=0)).set(color=YELLOW_E)
        received = VGroup(*[Square(.5, color=YELLOW_E, fill_opacity=.8) for _ in range(6)]
                          ).arrange(RIGHT, buff=0).next_to(receiver, DOWN, buff=1)
        rcv_buffer = VGroup(SurroundingRectangle(received[:6], buff=.3))
        rcv_buffer.add(Text('接收缓存').scale(.5).next_to(rcv_buffer, UP)).set(color=BLUE_D)
        rwnd = VGroup(SurroundingRectangle(received[3:6], color=YELLOW_B))
        sent = VGroup(*[Square(.5, color=BLUE, fill_opacity=.8) for _ in range(7)]
                      ).arrange(RIGHT, buff=0).next_to(sender, DOWN, buff=1)
        sent[:3].set(color=GREEN)
        rwnd.generate_target()
        rwnd.target.move_to(sent[3:6]).add(Text('接收窗口', color=YELLOW_B).scale(.5).next_to(rwnd.target, UP))
        overflow = Cross().scale(.4).move_to(sent[5:])
        flow_ctrl = Text('流量控制'
                         ).set_color_by_gradient(YELLOW_A, YELLOW_E).next_to(Group(sender, receiver), DOWN, buff=-.5)
        udp_app = VGroup(Text('UDP'), SVGMobject('dns.svg').scale(.5), SVGMobject('phone.svg').scale(.5)
                         ).arrange(RIGHT, buff=1).set(color=BLUE_B)
        tcp_app = VGroup(Text('TCP'), SVGMobject('web_page.svg').scale(.5), SVGMobject('mail.svg').scale(.4)
                         ).arrange(RIGHT, buff=1).set(color=BLUE_D)
        Group(udp_app, tcp_app).arrange(DOWN, buff=1).next_to(tcp_header, DOWN)
        self.play(FadeIn(sender, receiver), Create(rwnd_seg))
        self.play(FadeIn(rcv_buffer, received[:3]))
        self.play(Create(rwnd))
        self.play(FadeIn(sent[:5]), MoveToTarget(rwnd))
        self.play(Create(sent[5:]))
        self.play(Create(overflow))
        self.play(FadeOut(overflow, sent[5:]))
        self.play(Write(flow_ctrl))
        self.play(FadeOut(sender, receiver, rwnd_seg, rwnd, sent[:5], received[:3], rcv_buffer, flow_ctrl))
        self.play(Indicate(tcp_header[-3]))
        self.play(Create(udp_app))
        self.play(Create(tcp_app))
        self.wait()
        self.clear()

# class Quest(Scene):
#     def construct(self):
