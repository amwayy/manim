from manim import *


class RFC(Scene):
    def construct(self):
        def show_text(text, text_mob):
            sent_start = 0
            sent_end = text.find('.')
            sent_end -= text[:sent_end].count(' ')+text[:sent_end].count('\n')
            while text.find('.') != -1:
                self.play(Write(text_mob[sent_start:sent_end+1]), run_time=.05*(sent_end-sent_start))
                sent_start = sent_end+1
                text = text[text.find('.')+1:]
                sent_end += text.find('.')+1
                sent_end -= text[:text.find('.')].count(' ')+text[:text.find('.')].count('\n')
                while text[text.find('.')+1] and text[text.find('.')+1] != ' ' and text[text.find('.')+1] != '\n':
                    text = text[text.find('.')+1:]
                    sent_end += text.find('.')+1
                    sent_end -= text[:text.find('.')].count(' ')+text[:text.find('.')].count('\n')

        # rfc = VGroup(Text('RFC'), Text('Request for Comments').scale(.7)
        #              ).arrange(DOWN).to_edge(UP).set_color_by_gradient(BLUE_A, BLUE_D)
        # ietf = ImageMobject('pics/ietf.png').scale(.4)
        # rfc_eg = VGroup(Text('TCP: RFC 793', font='MonoSpace'),
        #                 Text('IP: RFC 791', font='MonoSpace')).scale(.8).arrange(RIGHT, buff=1)
        # arrow = Arrow(ORIGIN, RIGHT*.8, buff=0)
        # process = VGroup(SVGMobject('pics/draft.svg'), arrow.copy(), SVGMobject('pics/discussion.svg'), arrow.copy(),
        #                  SVGMobject('pics/draft.svg'), arrow.copy(), SVGMobject('pics/publish.svg')
        #                  ).scale(.5).arrange(RIGHT).shift(LEFT*2)
        # category = VGroup(Text('标准', color=GREEN), Text('信息', color=YELLOW_E),
        #                   Text('实验', color=RED)).scale(.8).arrange(DOWN)
        # category.add(Brace(category, LEFT)).next_to(process, RIGHT, buff=1)
        # april_fools = Text('April Fools\' Day RFC').set_color_by_gradient(GREEN_A, GREEN_E)
        # self.play(Write(rfc[0]))
        # self.play(Write(rfc[1]))
        # self.play(FadeIn(ietf))
        # self.play(FadeOut(ietf))
        # self.play(Write(rfc_eg))
        # self.play(FadeOut(rfc_eg))
        # self.play(Create(process))
        # self.play(Write(category))
        # self.play(FadeOut(process, category))
        # self.play(Write(april_fools))
        # self.wait()
        # self.clear()
        #
        # sob_title = Text('RFC 1438: IETF沉闷宣言', color=GREEN, font='MonoSpace').scale(.8).to_edge(UP, buff=.2)
        # sob_pic = ImageMobject('pics/sob.png').next_to(sob_title, DOWN)
        # sob = 'The current IETF process has two types of RFCs: standards track\n' \
        #       'documents and other RFCs (informational, experimental, FYIs).\n' \
        #       'The intent of the standards track documents is clear, and culminates\n' \
        #       'in an official Internet Standard.  Informational RFCs can be\n' \
        #       'published on a less formal basis, subject to the reasonable\n' \
        #       'constraints of the RFC Editor.  Informational RFCs are not subject to\n' \
        #       'peer review and carry no significance whatsoever within the IETF\n' \
        #       'process.\n\n' \
        #       'The IETF currently has no mechanism or means of publishing documents\n' \
        #       'that express its deep concern about something important, but\n' \
        #       'otherwise contain absolutely no useful information whatsoever.  This\n' \
        #       'document creates a new subseries of RFCs, entitled, IETF Statements\n' \
        #       'Of Boredom (SOBs).  The SOB process is similar to that of the normal\n' \
        #       'standards track.  The SOB is submitted to the IAB, the IRSG, the\n' \
        #       'IESG, the SOB Editor (Morpheus), and the Academie Francais for\n' \
        #       'review, analysis, reproduction in triplicate, translation into ASN.1,\n' \
        #       'and distribution to Internet insomniacs.  However, once everyone has\n' \
        #       'approved the document by falling asleep over it, the process ends and\n' \
        #       'the document is discarded.  The resulting vacuum is viewed as having\n' \
        #       'the technical approval of the IETF, but it is not, and cannot become,\n' \
        #       'an official Internet Standard. '
        # sob_mob = Text(sob, font='MonoSpace').scale(.5).next_to(sob_title, DOWN)
        # security = Text('Security issues are not discussed in this memo, but then again, no\n'
        #                 'other issues of any importance are discussed in this memo either.', font='MonoSpace').scale(.5)
        # self.play(Write(sob_title[:7]), FadeIn(sob_pic))
        # self.play(Write(sob_title[7:]))
        # self.play(FadeOut(sob_pic))
        # show_text(sob, sob_mob)
        # self.play(FadeOut(sob_mob))
        # self.play(Write(security))
        # self.wait()
        # self.clear()
        #
        # rfc1149 = Text('RFC 1149', font='MonoSpace', color=GREEN).scale(.8).to_edge(UP, buff=.2)
        # rfc1149_pic = ImageMobject('pics/avian_carrier.png').scale(.9).next_to(rfc1149, DOWN)
        # pigeon = ImageMobject('pics/pigeon.jpg').scale(.7)
        # Group(rfc1149_pic, pigeon).arrange(RIGHT, buff=1).next_to(rfc1149, DOWN)
        # overview = 'Overview and Rational\n\n' \
        #            'Avian carriers can provide high delay, low throughput, and low\n' \
        #            'altitude service.  The connection topology is limited to a single\n' \
        #            'point-to-point path for each carrier, used with standard carriers,\n' \
        #            'but many carriers can be used without significant interference with\n' \
        #            'each other, outside of early spring.  This is because of the 3D ether\n' \
        #            'space available to the carriers, in contrast to the 1D ether used by\n' \
        #            'IEEE802.3.  The carriers have an intrinsic collision avoidance\n' \
        #            'system, which increases availability.  Unlike some network\n' \
        #            'technologies, such as packet radio, communication is not limited to\n' \
        #            'line-of-sight distance.  Connection oriented service is available in\n' \
        #            'some cities, usually based upon a central hub topology. '
        # overview_mob = Text(overview, font='MonoSpace', t2c={'Overview and Rational': BLUE}
        #                     ).scale(.5).next_to(rfc1149, DOWN)
        # multi_pigeon = VGroup(SVGMobject('pics/pigeon.svg'), SVGMobject('pics/pigeon.svg'),
        #                       SVGMobject('pics/pigeon.svg')
        #                       ).scale(.25).arrange(DOWN).next_to(overview_mob, DOWN).shift(LEFT*2)
        # space_3d = SVGMobject('pics/3d.svg').set(color=BLUE).scale(.8).next_to(multi_pigeon, RIGHT, buff=1)
        # two_pigeon = VGroup(SVGMobject('pics/pigeon.svg'), SVGMobject('pics/pigeon.svg').flip()
        #                     ).scale(.35).arrange(RIGHT, buff=2).next_to(overview_mob, DOWN, buff=1)
        # hub = SVGMobject('pics/hub.svg').set(color=BLUE).scale(.8).next_to(overview_mob, DOWN)
        # self.play(Write(rfc1149))
        # self.play(FadeIn(pigeon, rfc1149_pic))
        # self.play(FadeOut(pigeon, rfc1149_pic))
        # show_text(overview, overview_mob)
        # self.play(Create(multi_pigeon))
        # self.play(multi_pigeon.animate.shift(RIGHT*4))
        # self.play(Create(space_3d))
        # self.play(FadeOut(space_3d, multi_pigeon))
        # self.play(Create(two_pigeon))
        # self.play(two_pigeon[0].animate.shift(RIGHT*.8), two_pigeon[1].animate.shift(LEFT*.8))
        # self.play(two_pigeon[0].animate.shift(UR*.5), two_pigeon[1].animate.shift(DL*.5))
        # self.play(two_pigeon[0].animate.shift(RIGHT), two_pigeon[1].animate.shift(LEFT))
        # self.play(FadeOut(two_pigeon))
        # self.play(Create(hub))
        # self.wait()
        # self.clear()
        #
        # self.add(rfc1149)
        # frame_format = 'Frame Format\n\n' \
        #                'The IP datagram is printed, on a small scroll of paper, in\n' \
        #                'hexadecimal, with each octet separated by whitestuff and blackstuff.\n' \
        #                'The scroll of paper is wrapped around one leg of the avian carrier.\n' \
        #                'A band of duct tape is used to secure the datagram\'s edges.  The\n' \
        #                'bandwidth is limited to the leg length.  The MTU is variable, and\n' \
        #                'paradoxically, generally increases with increased carrier age.  A\n' \
        #                'typical MTU is 256 milligrams.  Some datagram padding may be needed.\n\n' \
        #                'Upon receipt, the duct tape is removed and the paper copy of the\n' \
        #                'datagram is optically scanned into a electronically transmittable\n' \
        #                'form. '
        # ff_mob = Text(frame_format, font='MonoSpace', t2c={'Frame Format': BLUE}).scale(.5).next_to(rfc1149, DOWN)
        # scroll = ImageMobject('pics/scroll.jpg').next_to(ff_mob, DOWN)
        # data = Text('01 23 45 67 89\nAB CD EF 01 23', font='MonoSpace').scale(.8).next_to(ff_mob, DOWN)
        # attach = ImageMobject('pics/packet_one_attached.jpg').scale(.7).next_to(ff_mob, DOWN)
        # axes = VGroup(Axes(x_range=[0, 5, 1], y_range=[0, 5, 1], x_length=2.5, y_length=2.5)).next_to(ff_mob, DOWN)
        # axes.add(Text('年龄').scale(.5).next_to(axes[0][0], RIGHT),
        #          Text('MTU').scale(.5).next_to(axes[0][1].get_end()+DOWN*.2, LEFT))
        # mtu = axes[0].plot(lambda x: x, x_range=[0, 4.5]).set(color=BLUE)
        # scan = ImageMobject('pics/packet_scanning.jpg').scale(.7).next_to(ff_mob, DOWN)
        # show_text(frame_format, ff_mob)
        # self.play(FadeIn(scroll))
        # self.play(FadeOut(scroll))
        # self.play(Write(data))
        # self.play(FadeOut(data))
        # self.play(FadeIn(attach))
        # self.play(FadeOut(attach))
        # self.play(Create(VGroup(axes, mtu)))
        # self.play(FadeOut(axes, mtu))
        # self.play(FadeIn(scan))
        # self.wait()
        # self.clear()
        #
        # self.add(rfc1149)
        # discussion = 'Discussion\n\n' \
        #              'Multiple types of service can be provided with a prioritized pecking\n' \
        #              'order.  An additional property is built-in worm detection and\n' \
        #              'eradication.  Because IP only guarantees best effort delivery, loss\n' \
        #              'of a carrier can be tolerated.  With time, the carriers are self-\n' \
        #              'regenerating.  While broadcasting is not specified, storms can cause\n' \
        #              'data loss.  There is persistent delivery retry, until the carrier\n' \
        #              'drops.  Audit trails are automatically generated, and can often be\n' \
        #              'found on logs and cable trays. '
        # discuss_mob = Text(discussion, font='MonoSpace', t2c={'Discussion': BLUE}).scale(.5).next_to(rfc1149, DOWN)
        # pigeon = SVGMobject('pics/pigeon.svg').scale(.8)
        # worm = SVGMobject('pics/worm.svg').set(color=RED_A).scale(.3)
        # VGroup(pigeon, worm).arrange(RIGHT, buff=1).next_to(discuss_mob, DOWN)
        # storm = ImageMobject('pics/storm.png').set(color=YELLOW_E).scale(.5).next_to(discuss_mob, DOWN)
        # trail = ImageMobject('pics/audit_trail.jpg').scale(.7).next_to(discuss_mob, DOWN)
        # show_text(discussion, discuss_mob)
        # self.play(Create(pigeon), Create(worm))
        # self.play(AnimationGroup(pigeon.animate.move_to(worm), FadeOut(worm), lag_ratio=.5))
        # self.play(FadeOut(pigeon))
        # self.play(Create(pigeon.scale(.8).next_to(storm, DOWN)), FadeIn(storm))
        # self.play(Wiggle(pigeon))
        # self.play(pigeon.animate.rotate(-PI/2))
        # self.play(pigeon.animate.shift(DOWN*5))
        # self.play(FadeOut(storm))
        # self.play(FadeIn(trail))
        # self.wait()
        # self.clear()
        #
        # self.add(rfc1149)
        # security = 'Security Considerations\n\n' \
        #            'Security is not generally a problem in normal operation, but special\n' \
        #            'measures must be taken (such as data encryption) when avian carriers\n' \
        #            'are used in a tactical environment. '
        # security_mob = Text(security, font='MonoSpace', t2c={'Security Considerations': BLUE}).scale(.5)
        # show_text(security, security_mob)
        # self.wait()
        # self.clear()
        #
        # self.add(rfc1149)
        # qos_update = ImageMobject('pics/qos_update.png')
        # ipv6_update = ImageMobject('pics/ipv6_update.png')
        # update = Group(qos_update, ipv6_update).scale(.9).arrange(RIGHT, buff=1).next_to(rfc1149, DOWN)
        # self.play(FadeIn(update))
        # self.wait()
        # self.clear()
        #
        # implementation = Group(ImageMobject('pics/pigeon_and_packet.jpg').scale(.6),
        #                        ImageMobject('pics/packet_one_attached.jpg').scale(.7),
        #                        ImageMobject('pics/send_pigeon.jpg').scale(.6)).arrange(RIGHT)
        # back = VGroup(*[SVGMobject('pics/pigeon.svg').scale(.25) for _ in range(4)]).arrange(DOWN)
        # lost = VGroup(*[SVGMobject('pics/pigeon.svg').scale(.25) for _ in range(5)]).arrange(DOWN)
        # carrier = VGroup(back, lost).arrange(RIGHT)
        # Group(implementation, carrier).arrange(DOWN)
        # carrier.shift(LEFT*2.5)
        # dest = carrier.copy().shift(RIGHT*5)
        # dist = VGroup(Brace(Line(carrier.get_bottom(), dest.get_bottom()), DOWN, buff=-.2))
        # dist.add(Text('5km', font='MonoSpace').scale(.5).next_to(dist, DOWN, buff=0)).set(color=BLUE)
        # self.add(rfc1149)
        # self.play(FadeIn(implementation))
        # self.play(Create(carrier))
        # self.play(Create(dist), carrier.animate.shift(RIGHT*5))
        # self.play(back.animate.flip(), FadeOut(lost, dist))
        # self.play(back.animate.shift(LEFT*5))
        # self.wait()
        # self.clear()
        #
        # rfc1925 = Text('RFC 1925: The Twelve Networking Truths', font='MonoSpace', color=GREEN
        #                ).scale(.8).to_edge(UP, buff=.2)
        # rfc1925_pic = ImageMobject('pics/truth.png').scale(.9).next_to(rfc1925, DOWN)
        # truth1_2 = open('txt/truth1_2.txt').read()
        # truth1_2_mob = Text(truth1_2, font='MonoSpace', t2c={'(1)': BLUE, '(2)': BLUE, '(2a)': BLUE}).scale(.5)
        # truth3_4 = open('txt/truth3_4.txt').read()
        # truth3_4_mob = Text(truth3_4, font='MonoSpace', t2c={'(3)': BLUE, '(4)': BLUE}).scale(.5)
        # VGroup(truth1_2_mob, truth3_4_mob).arrange(DOWN).next_to(rfc1925, DOWN)
        # truth1_2_mob.align_to(truth3_4_mob, LEFT)
        # pregnant = ImageMobject('pics/pregnant.png').scale(.6).next_to(truth1_2_mob, DOWN)
        # pig = ImageMobject('pics/flying_pig.png').next_to(truth3_4_mob, UP, buff=1)
        # self.play(Write(rfc1925), FadeIn(rfc1925_pic))
        # self.play(FadeOut(rfc1925_pic))
        # show_text(truth1_2, truth1_2_mob)
        # self.play(FadeIn(pregnant))
        # self.play(FadeOut(pregnant))
        # self.play(FadeOut(truth1_2_mob))
        # show_text(truth3_4, truth3_4_mob)
        # self.play(FadeIn(pig))
        # self.play(pig.animate.shift(DOWN*8))
        # self.wait()
        # self.clear()
        #
        # truth5_8 = open('txt/truth5_8.txt').read()
        # truth5_8_mob = Text(truth5_8, font='MonoSpace',
        #                     t2c={'(5)': BLUE, '(6)': BLUE, '(6a)': BLUE, '(7)': BLUE, '(7a)': BLUE, '(8)': BLUE}
        #                     ).scale(.5)
        # self.add(rfc1925)
        # show_text(truth5_8, truth5_8_mob)
        # self.play(FadeOut(truth5_8_mob))
        # truth9_12 = open('txt/truth9_12.txt').read()
        # truth9_12_mob = Text(truth9_12, font='MonoSpace',
        #                      t2c={'(9)': BLUE, '(9a)': BLUE, '(10)': BLUE, '(11)': BLUE, '(11a)': BLUE, '(12)': BLUE}
        #                      ).scale(.5)
        # self.add(rfc1925)
        # show_text(truth9_12, truth9_12_mob)
        # self.play(FadeOut(truth9_12_mob))
        # addr = ImageMobject('pics/addr.png')
        # self.play(FadeIn(addr))
        # self.wait()
        # self.clear()
        #
        # rfc3092 = Text('RFC 3092', font='MonoSpace', color=GREEN).to_edge(UP)
        # rfc3092_pic = ImageMobject('pics/foo.png').scale(.9).next_to(rfc3092, DOWN)
        # foobar = Text('foo, bar, foobar?')
        # fubar = Text('FUBAR')
        # furchtbar = Text('furchtbar')
        # ufo = Group(Text('foo fighters'))
        # ufo.add(ImageMobject('pics/ufo.png').next_to(ufo, DOWN))
        # daffy = Group(ImageMobject('pics/daffy_doc.jpg'), ImageMobject('pics/silent_foo.jpg')).arrange(RIGHT, buff=1)
        # fu = SVGMobject('pics/fu.svg').set(color=RED).scale(1.5)
        # foo_dog = Group(ImageMobject('pics/狮子狗.jpg'), ImageMobject('pics/石狮子.png').scale(.6)).arrange(RIGHT)
        # self.play(Write(rfc3092), FadeIn(rfc3092_pic))
        # self.play(FadeOut(rfc3092_pic))
        # self.play(Write(foobar))
        # self.play(FadeOut(foobar[:8]), ReplacementTransform(foobar[8:], fubar))
        # self.play(ReplacementTransform(fubar, furchtbar))
        # self.play(FadeOut(furchtbar))
        # self.play(Write(ufo[0]))
        # self.play(FadeIn(ufo[1]))
        # self.play(FadeOut(ufo))
        # self.play(FadeIn(daffy))
        # self.play(FadeOut(daffy))
        # self.play(Create(fu))
        # self.play(FadeOut(fu))
        # self.play(FadeIn(foo_dog[0]))
        # self.play(FadeIn(foo_dog[1]))
        # self.wait()
        # self.clear()

        rfc257 = Text('RFC 527', font='MonoSpace', color=GREEN).to_edge(UP, buff=.2)
        rfc257_pic = ImageMobject('pics/arpawocky.png')
        jabberwocky = Group(Text(open('txt/jabberwocky.txt').read(), font='MonoSpace').scale(.5).next_to(rfc257, DOWN))
        jabberwocky.add(ImageMobject('pics/Jabberwocky.jpg').scale(.6).next_to(jabberwocky, LEFT))
        arpawocky = Text(open('txt/arpawocky.txt').read(), font='MonoSpace').scale(.5).next_to(rfc257, DOWN)
        arpawocky[:9].next_to(rfc257, DOWN)
        self.play(Write(rfc257), FadeIn(rfc257_pic))
        self.play(FadeOut(rfc257_pic))
        self.play(FadeIn(jabberwocky))
        self.play(FadeOut(jabberwocky[1]), TransformMatchingShapes(jabberwocky[0], arpawocky))
        self.wait()
        self.clear()

        # rfc2324 = Text('RFC 2324: HTCPCP/1.0', font='MonoSpace', color=GREEN).to_edge(UP, buff=.2)
        # rfc2324_pic = Group(ImageMobject('pics/htcpcp.png').scale(.9), ImageMobject('pics/htcpcp.jpg')
        #                     ).arrange(RIGHT, buff=1).next_to(rfc2324, DOWN)
        # self.play(Write(rfc2324), FadeIn(rfc2324_pic))
        # self.wait()
        # self.clear()
        #
        # rfc2795 = Text('RFC 2795: 无限猴子协议组', font='MonoSpce', color=GREEN).to_edge(UP, buff=.2)
        # rfc2795_pic = Group(ImageMobject('pics/monkey_rfc.png').scale(.9), ImageMobject('pics/Monkey-typing.jpg')
        #                     ).arrange(RIGHT, buff=1).next_to(rfc2795, DOWN)
        # self.play(Write(rfc2795), FadeIn(rfc2795_pic))
        # self.wait()
        # self.clear()
        #
        # rfc1606 = Text('RFC 1606: IPv9使用史', font='MonoSpace', color=GREEN).to_edge(UP, buff=.2)
        # rfc1606_pic = ImageMobject('pics/ipv9.png').scale(.9).next_to(rfc1606, DOWN)
        # self.play(Write(rfc1606), FadeIn(rfc1606_pic))
        # self.wait()
        # self.clear()
