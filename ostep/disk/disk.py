from manim import *
import math


class Disk(Scene):
    def construct(self):
        mem = VGroup(Rectangle(width=2.5, height=4, fill_color=BLUE_A, fill_opacity=.8))
        mem.add(Text('内存').scale(.8).next_to(mem, UP))
        disk = VGroup(Circle(1.5, fill_color=BLUE, fill_opacity=.8, stroke_color=WHITE))
        disk.add(Text('磁盘').scale(.8).move_to(disk))
        arrow = Arrow(ORIGIN, RIGHT, buff=0)
        VGroup(mem, arrow, disk).arrange(RIGHT)
        pages = VGroup(*[Rectangle(width=2.5, height=.5, fill_color=BLUE, fill_opacity=.8) for _ in range(8)]
                       ).arrange(DOWN, buff=0).move_to(mem[0])
        self.play(Create(mem))
        self.play(Create(pages))
        self.play(Create(VGroup(arrow, disk)))
        self.wait()
        self.clear()

        platter = Circle(2, fill_color=BLUE_A, fill_opacity=.8, stroke_color=WHITE)
        track1 = Cutout(platter, Circle(1.5), fill_color=BLUE_E, fill_opacity=.8)
        track2 = Cutout(Circle(1.5), Circle(1), fill_color=BLUE_D, fill_opacity=.8)
        track3 = Cutout(Circle(1), Circle(.5), fill_color=BLUE_C, fill_opacity=.8)
        sectors1 = VGroup()
        sectors2 = VGroup()
        sectors3 = VGroup()
        for sector in range(12):
            sectors1.add(Text(str(sector)
                              ).scale(.5).move_to([1.75*math.cos(sector*(-PI/6)), 1.75*math.sin(sector*(-PI/6)), 0]))
        for sector in range(12, 24):
            sectors2.add(Text(str(sector)
                              ).scale(.5).move_to([1.25*math.cos(sector*(-PI/6)), 1.25*math.sin(sector*(-PI/6)), 0]))
        for sector in range(24, 36):
            sectors3.add(Text(str(sector)
                              ).scale(.4).move_to([.75*math.cos(sector*(-PI/6)), .75*math.sin(sector*(-PI/6)), 0]))
        head = Circle(.2, color=YELLOW, fill_opacity=.5, stroke_width=0).move_to(sectors1[6])
        arm = Difference(Rectangle(width=.4, height=2.5), Circle(.2).shift(UP*1.25), color=YELLOW_E, fill_opacity=.8)
        arm.next_to(head, DOWN, buff=-.2)
        head.z_index = 1
        arm.z_index = 1
        spindle = Dot(color=BLUE_B)
        disk = VGroup(track1, track2, track3, sectors1, sectors2, sectors3)
        self.play(Create(platter))
        self.play(Create(VGroup(track1, track2, track3)))
        self.play(Create(VGroup(sectors1, sectors2, sectors3)), run_time=2)
        self.play(Create(head))
        self.play(Create(arm[:2]))
        self.play(Create(spindle))
        self.play(Rotate(disk, 2*PI), run_time=5)
        delay = Text('旋转延迟+寻道延迟+传输延迟').next_to(platter, UP, buff=1)
        delay[:4].set(color=BLUE_C)
        delay[5:9].set(color=BLUE_D)
        delay[10:].set(color=BLUE_E)
        self.play(Circumscribe(sectors1[8], shape=Circle))
        self.play(Rotate(disk, PI/3))
        self.play(Write(delay[:4]))
        self.play(Rotate(VGroup(head, arm), -PI/15, about_point=arm.get_bottom()))
        self.play(Write(delay[5:9]))
        self.play(Write(delay[10:]))
        self.play(Create(VGroup(delay[4], delay[9])))
        self.play(Circumscribe(delay[:9]))
        self.play(FadeOut(delay))
        self.play(Indicate(VGroup(track2, track3, sectors2, sectors3)))
        self.play(Rotate(disk, 2*PI/3))
        self.wait()
        self.play(Rotate(disk, 11*PI/6), run_time=3)
        self.play(Rotate(VGroup(head, arm), -PI/5), Rotate(disk, 2*PI/3))
        self.play(Circumscribe(sectors3[0], shape=Circle))
        self.play(Rotate(sectors3, -PI/3))
        self.wait()
        self.clear()

        tracks = VGroup(NumberLine(x_range=[0, 10, 1], length=5, include_numbers=True, color=BLUE))
        tracks.add(Text('磁道').scale(.6).next_to(tracks, LEFT))
        head = VGroup(Triangle(color=YELLOW, fill_opacity=1).scale(.1).rotate(PI))
        head.add(Text('磁头').scale(.6).next_to(head, UP))
        jobs = VGroup(Dot(LEFT*.5), Dot(RIGHT), Dot(RIGHT*2))
        sstf = Text('最短寻道时间优先').scale(.8).set_color_by_gradient(BLUE_A, BLUE_E).next_to(tracks[0], DOWN, buff=1)
        self.play(Create(VGroup(tracks, head.next_to(tracks[0], UP), jobs)), Write(sstf))
        self.play(head.animate.shift(LEFT*.5), FadeOut(jobs[0]))
        self.play(head.animate.shift(RIGHT*1.5), FadeOut(jobs[1]))
        self.play(head.animate.shift(RIGHT), FadeOut(jobs[2]))
        starved = Dot(LEFT*2)
        self.play(Create(starved))
        for times in range(5):
            self.play(head.animate.shift(RIGHT*.5*pow(-1, times)), run_time=.2)
        arrow_starved = Arrow(ORIGIN, DOWN).next_to(starved, UP)
        self.play(Create(arrow_starved))
        self.play(FadeOut(sstf, arrow_starved))
        scan = Text('SCAN/电梯').scale(.8).next_to(tracks[0], DOWN, buff=1).set_color_by_gradient(BLUE_A, BLUE_E)
        self.play(FadeIn(jobs))
        self.play(head.animate.shift(LEFT*.5), FadeOut(jobs[2]))
        self.play(head.animate.shift(LEFT), FadeOut(jobs[1]))
        self.play(head.animate.shift(LEFT*1.5), FadeOut(jobs[0]))
        self.play(head.animate.shift(LEFT*1.5), FadeOut(starved))
        self.play(head.animate.shift(LEFT*.5))
        self.play(FadeIn(jobs, starved))
        self.play(head.animate.shift(RIGHT*5), FadeOut(jobs, starved))
        self.play(Write(scan))
        self.wait()
        self.clear()


class RAID(Scene):
    def construct(self):
        disk = VGroup(*[VGroup(Rectangle(width=2, height=1, fill_color=BLUE, fill_opacity=.8)) for _ in range(4)]
                      ).arrange(DOWN, buff=0)
        raid0 = VGroup(disk.copy(), disk.copy(), disk.copy(), disk.copy()).arrange(RIGHT)
        for block in range(16):
            raid0[block % 4][int(block/4)].add(Text(str(block)).scale(.8).move_to(raid0[block % 4][int(block/4)]))
        stripe = SurroundingRectangle(VGroup(raid0[0][0], raid0[1][0], raid0[2][0], raid0[3][0]))
        raid0_txt = Text('RAID-0').next_to(raid0, DOWN).set_color_by_gradient(BLUE_A, BLUE_E)
        self.play(Create(raid0))
        self.play(Create(stripe))
        self.play(FadeOut(stripe))
        self.play(Write(raid0_txt))

        raid1_txt = Text('RAID-1').next_to(raid0, DOWN).set_color_by_gradient(BLUE_A, BLUE_E)
        self.play(Transform(raid0_txt, raid1_txt))
        disk_blue_e = VGroup(*[VGroup(Rectangle(width=2, height=1, fill_color=BLUE_E, fill_opacity=.8))
                               for _ in range(4)]).arrange(DOWN, buff=0)
        raid1 = VGroup(disk.copy(), disk_blue_e.copy())
        for block in range(8):
            raid1[block % 2][int(block/2)].add(Text(str(block)).scale(.8).move_to(raid1[block % 2][int(block/2)]))
        raid1 = VGroup(raid1[0], raid1[0].copy(), raid1[1], raid1[1].copy()).arrange(RIGHT)
        self.play(FadeOut(raid0), FadeIn(raid1))
        data = Text('data', color=YELLOW).scale(.8)
        self.play(Transform(raid1[0][0][1], data.move_to(raid1[0][0])),
                  Transform(raid1[1][0][1], data.copy().move_to(raid1[1][0])))
        self.wait()
        self.clear()

        parity = VGroup(*[VGroup(Rectangle(width=2, height=1, fill_color=YELLOW_E, fill_opacity=.8)) for _ in range(4)]
                        ).arrange(DOWN, buff=0)
        for block in range(4):
            parity[block].add(Text('P'+str(block)).scale(.8).move_to(parity[block]))
        raid4 = raid0.copy().add(parity).arrange(RIGHT)
        raid4_c = raid4.copy()
        self.play(Create(raid4))
        self.play(ReplacementTransform(VGroup(raid4[0][0][1], raid4[1][0][1], raid4[2][0][1], raid4[3][0][1]).copy(),
                                       raid4[4][0][1]))
        block_datas = VGroup(Text('00'), Text('10'), Text('00'), Text('10'), Text('00')).scale(.8).set(color=YELLOW)
        for data in range(5):
            block_datas[data].move_to(raid4[data][0][1])
        self.play(ReplacementTransform(VGroup(raid4[0][0][1], raid4[1][0][1], raid4[2][0][1], raid4[3][0][1],
                                              raid4[4][0][1]),
                                       VGroup(block_datas[0], block_datas[1], block_datas[2], block_datas[3],
                                              block_datas[4])))
        parity_calc = Text('new_parity = (old_data^new_data)^old_parity', color=BLUE_D).scale(.8).next_to(raid4, UP)
        write = VGroup(Text('11').scale(.8).move_to(raid4[2][0][1]), Text('11').scale(.8).move_to(raid4[4][0][1])
                       ).set(color=YELLOW)
        self.play(Write(parity_calc))
        self.play(Indicate(raid4[2][0][0], color=BLUE), Indicate(raid4[4][0][0], color=YELLOW_E))
        self.play(FadeOut(parity_calc))
        self.play(Transform(block_datas[2], write[0]), Transform(block_datas[4], write[1]))
        self.play(FadeOut(block_datas[3]))
        self.play(ReplacementTransform(VGroup(block_datas[:3], block_datas[4]).copy(), block_datas[3]))
        raid4_txt = Text('RAID-4').next_to(raid4, DOWN).set_color_by_gradient(BLUE_A, BLUE_E)
        self.play(Write(raid4_txt))
        self.play(ReplacementTransform(VGroup(block_datas[0], block_datas[1], block_datas[2], block_datas[3],
                                              block_datas[4]),
                                       VGroup(raid4_c[0][0][1], raid4_c[1][0][1], raid4_c[2][0][1], raid4_c[3][0][1],
                                              raid4_c[4][0][1])))
        data_indication = VGroup(SurroundingRectangle(raid4[1][0][1]), SurroundingRectangle(raid4[2][2][1]))
        parity_indication = VGroup(SurroundingRectangle(raid4[4][0][1]), SurroundingRectangle(raid4[4][2][1]))
        self.play(Create(data_indication[0]), Create(data_indication[1]))
        self.play(Create(parity_indication[0]), Create(parity_indication[1]))
        self.play(FadeOut(data_indication, parity_indication, raid4_txt))

        buff = 2.25
        self.play(VGroup(raid4[1][1], raid4[2][1], raid4[3][1], raid4[4][1]).animate.shift(LEFT*buff),
                  raid4[0][1].animate.shift(RIGHT*buff*4),
                  VGroup(raid4[2][2], raid4[3][2], raid4[4][2]).animate.shift(LEFT*buff*2),
                  VGroup(raid4[0][2], raid4[1][2]).animate.shift(RIGHT*buff*3),
                  VGroup(raid4[3][3], raid4[4][3]).animate.shift(LEFT*buff*3),
                  VGroup(raid4[0][3], raid4[1][3], raid4[2][3]).animate.shift(RIGHT*buff*2))

        raid5_indication = VGroup(SurroundingRectangle(raid4[1][0][1]), SurroundingRectangle(raid4[2][2][1]),
                                  SurroundingRectangle(raid4[4][0][1]), SurroundingRectangle(raid4[4][2][1]))
        self.play(Create(raid5_indication[0]), Create(raid5_indication[1]),
                  Create(raid5_indication[2]), Create(raid5_indication[3]))
        self.play(FadeOut(raid5_indication))
        self.wait()
        raid5_txt = Text('RAID-5').next_to(raid4, DOWN).set_color_by_gradient(BLUE_A, BLUE_E)
        self.play(Write(raid5_txt))
        self.wait()
        self.clear()

        analysis = Table([['N', 'N/2', 'N-1', 'N-1'], ['0', '1~N/2', '1', '1'], ['', '', '', ''],
                          ['N·S', '(N/2)·S', '(N-1)·S', '(N-1)·S'], ['N·S', '(N/2)·S', '(N-1)·S', '(N-1)·S'],
                          ['N·R', 'N·R', '(N-1)·R', 'N·R'], ['N·R', '(N/2)·R', 'R/2', '(N/4)·R'],
                          ['', '', '', ''], ['D', 'D', 'D', 'D'], ['D', 'D', '2D', '2D']],
                         col_labels=[Text('RAID-0', color=BLUE_A), Text('RAID-1', color=BLUE_B),
                                     Text('RAID-4', color=BLUE_C), Text('RAID-5', color=BLUE_D)],
                         row_labels=[Text('容量', color=RED), Text('可靠性', color=GREEN), Text('吞吐量', color=YELLOW_E),
                                     Text('连续读', color=YELLOW_E), Text('连续写', color=YELLOW_E),
                                     Text('随机读', color=YELLOW_E), Text('随机写', color=YELLOW_E),
                                     Text('延迟', color=YELLOW), Text('读', color=YELLOW), Text('写', color=YELLOW)]
                         ).scale(.5)
        self.play(Create(VGroup(analysis.get_rows()[0], analysis.get_entries((2, 1)),
                                analysis.get_horizontal_lines()[0])))
        self.play(Create(analysis.get_rows()[1][1:]), run_time=3)
        self.play(Create(VGroup(analysis.get_horizontal_lines()[1], analysis.get_entries((3, 1)))))
        self.play(Create(analysis.get_rows()[2][1:], run_time=3))
        self.play(Create(VGroup(analysis.get_horizontal_lines()[2], analysis.get_horizontal_lines()[7],
                         analysis.get_entries((4, 1)), analysis.get_entries((9, 1)))))
        self.play(Create(VGroup(analysis.get_rows()[4][:2], analysis.get_rows()[5][:2])))
        self.play(Create(VGroup(analysis.get_rows()[6][:2], analysis.get_rows()[7][:2])))
        self.play(Create(VGroup(analysis.get_rows()[9][:2], analysis.get_rows()[10][:2])))
        self.play(Create(analysis.get_columns()[2][4:6]))
        filling_table = VGroup(*self.mobjects)
        self.wait()
        self.clear()

        self.play(Create(raid1))
        read = VGroup(raid1[0][0], raid1[1][1], raid1[2][0], raid1[3][1])
        next_read = VGroup(raid1[0][2], raid1[1][3], raid1[2][2], raid1[3][3])
        self.play(read.animate.set(fill_color=YELLOW_E))
        self.play(read[:2].animate.set(fill_color=BLUE), read[2:].animate.set(fill_color=BLUE_E),
                  next_read.animate.set(fill_color=YELLOW_E))
        self.wait()
        self.clear()

        self.play(FadeIn(filling_table))
        self.play(Create(analysis.get_entries((7, 3))))
        self.play(Create(analysis.get_entries((8, 3))))
        self.play(Create(analysis.get_columns()[2][-2:]))
        self.play(Create(VGroup(analysis.get_rows()[4][3:], analysis.get_rows()[5][3:])))
        filling_table = VGroup(*self.mobjects)
        self.wait()
        self.clear()

        self.play(Create(raid4))
        self.play(Create(SurroundingRectangle(VGroup(raid4[0][0], raid4[1][0], raid4[2][0], raid4[3][0], raid4[4][0]))))
        self.wait()
        self.clear()

        self.play(FadeIn(filling_table))
        self.play(Create(analysis.get_rows()[-5][3:]), run_time=2)
        self.play(Create(analysis.get_columns()[-2][-4:], run_time=3))
        self.play(Create(analysis.get_columns()[-1][-4:], run_time=3))
        self.wait()
