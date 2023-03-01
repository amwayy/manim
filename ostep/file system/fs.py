from manim import *

coord_reference = NumberPlane()


class API(Scene):
    def construct(self):
        c = ImageMobject('c.png')
        txt = ImageMobject('txt.png')
        jpg = ImageMobject('jpg.png')
        mp3 = ImageMobject('mp3.png')
        file = ImageMobject('blank_file.png').scale(.6)
        file_name = Text('file').scale(.6).next_to(file, DOWN, buff=.1)
        file_data = Text('data', color=BLUE).scale(.8).move_to(file)
        directory = ImageMobject('directory.png')
        new_name = Text('new').scale(.6).next_to(file, DOWN, buff=.1)
        self.play(FadeIn(Group(c, txt, jpg, mp3).scale(.6).arrange(RIGHT)))
        self.play(FadeOut(c, txt, jpg, mp3))
        self.play(FadeIn(file))
        self.play(Write(file_name))
        self.play(Write(file_data))
        self.play(FadeIn(directory.copy().scale(1.4).shift(UP*.2)))
        self.play(FadeIn(directory.copy().scale(1.8).shift(UP*.3)))
        self.play(Transform(file_name, new_name))
        self.play(FadeOut(file, file_name, file_data))
        self.clear()

        blank_file = ImageMobject('blank_file.png').scale(.6)
        bits01 = Text('01011\n10010\n01011\n00100', color=BLUE).scale(.5).move_to(blank_file).shift(DOWN*.2)
        inode_num = Text('inode号').scale(.6).next_to(blank_file, DOWN)
        directory = ImageMobject('directory.png').scale(.6).next_to(blank_file, UP, buff=.7)
        mapping = Text('命名→inode号', color=BLUE).scale(.45).move_to(directory).shift(DOWN*.2)
        metadata = Text('元数据').scale(.8).set_color_by_gradient(BLUE_A, BLUE_E).next_to(blank_file, DOWN, buff=2)
        inode = VGroup(SurroundingRectangle(metadata, color=WHITE))
        inode.add(Text('inode').scale(.6).set_color_by_gradient(BLUE_A, BLUE_E).next_to(inode, UP))
        self.play(FadeIn(blank_file))
        self.play(Write(bits01))
        self.play(Write(inode_num))
        self.play(FadeIn(directory), Create(VGroup(Arrow(UP, UP*2, buff=0, color=BLUE), mapping)))
        self.play(Write(metadata))
        self.play(Create(inode))
        self.play(Create(CurvedArrow(inode_num.get_left(), inode[0].get_left(), color=BLUE)))
        self.clear()

        create = Code(code='open("foo", O_CREAT);', style=Code.styles_list[8], language='c', insert_line_no=False)
        fildes = Text('文件描述符').set_color_by_gradient(BLUE_A, BLUE_E).scale(.8)
        cmd = Code('cmd.c', style=Code.styles_list[8], insert_line_no=False)
        VGroup(create, fildes, cmd).arrange(DOWN)
        pointer = Triangle(color=ORANGE, fill_opacity=1).scale(.1).rotate(-PI/2)
        self.play(Write(create))
        self.play(Write(fildes))
        self.play(FadeOut(fildes))
        self.play(Create(VGroup(cmd[:2], cmd[2][:9])))
        self.play(Create(pointer.next_to(cmd[2][2], LEFT)))
        self.play(Circumscribe(cmd[2][2][-1], shape=Circle))
        self.play(pointer.animate.next_to(cmd[2][3], LEFT), Circumscribe(cmd[2][3][5], shape=Circle))
        self.play(Circumscribe(cmd[2][3][-9:-5]))
        self.play(pointer.animate.next_to(cmd[2][4], LEFT))
        self.play(Circumscribe(cmd[2][4][6], shape=Circle))
        self.play(pointer.animate.next_to(cmd[2][6], LEFT))
        self.play(pointer.animate.next_to(cmd[2][7], LEFT))
        self.play(pointer.animate.next_to(cmd[2][9], LEFT), Write(cmd[2][9]))
        self.play(pointer.animate.next_to(cmd[2][10], LEFT), Write(cmd[2][10]))
        self.clear()

        ln = Code(code='ln file file2', language='c', insert_line_no=False, style=Code.styles_list[8])
        file = Group(ImageMobject('blank_file.png').scale(.6))
        file.add(Text('data', color=BLUE).scale(.8).move_to(file), Text('file').scale(.6).next_to(file, DOWN))
        file2 = Group(file[0].copy())
        file2.add(file[1].copy().move_to(file2), Text('file2').scale(.6).next_to(file2, DOWN))
        inode = VGroup(Rectangle(width=1.5, height=1, fill_color=BLUE, fill_opacity=.8))
        inode.add(Text('inode').scale(.7).move_to(inode))
        Group(ln, inode, Group(file, file2).arrange(RIGHT)).arrange(DOWN, buff=1)
        link = Arrow(file.get_top(), inode.get_bottom(), buff=0, color=BLUE)
        link2 = Arrow(file2.get_top(), inode.get_bottom(), buff=0, color=BLUE)
        update = Text('new', color=BLUE).scale(.8).move_to(file[1])
        update2 = update.copy().move_to(file2[1])
        hard_link = Text('硬链接').set_color_by_gradient(BLUE_A, BLUE_E).shift(LEFT*4)
        rc = Text('引用计数=1').scale(.8).set_color_by_gradient(BLUE_A, BLUE_E).next_to(inode, RIGHT, buff=1)
        rc_update = Text('引用计数=0').scale(.8).set_color_by_gradient(BLUE_A, BLUE_E).next_to(inode, RIGHT, buff=1)
        self.play(Write(ln))
        self.play(Succession(FadeIn(file[0]), FadeIn(file2[0])))
        self.play(Create(VGroup(file[1], file2[1])))
        self.play(Create(VGroup(link, link2, inode)))
        self.play(Create(VGroup(file[2], file2[2])))
        self.play(Transform(file[1], update), Transform(file2[1], update2))
        self.play(FadeOut(link, file))
        self.play(Write(hard_link))
        self.play(FadeOut(hard_link))
        self.play(Write(rc))
        self.play(FadeOut(link2, file2), Transform(rc, rc_update))
        self.play(FadeOut(inode))
        self.clear()

        ln_s = Code(code='ln -s file file2', language='c', insert_line_no=False, style=Code.styles_list[8])
        soft_link = Text('软链接').set_color_by_gradient(BLUE_A, BLUE_E).shift(UP*3.5)
        file[1].become(Text('data', color=BLUE).scale(.8).move_to(file[1]))
        file2[1].become(Text('路径', color=BLUE).scale(.8).move_to(file2[1]))
        Group(ln_s, Group(file, file2).arrange(RIGHT)).arrange(DOWN, buff=1)
        redirect = CurvedArrow(file2.get_top(), file.get_top(), color=BLUE)
        self.play(Write(soft_link))
        self.play(Write(ln_s))
        self.play(FadeIn(Group(file, file2)))
        self.play(Create(redirect))
        self.play(FadeOut(file))
        self.play(Create(Cross().move_to(file2)))
        self.clear()

        dir_api = Code('dir.c', style=Code.styles_list[8], insert_line_no=False)
        self.play(Create(dir_api[:2]), Write(dir_api[2][0]))
        self.play(Create(dir_api[2][1:3]))
        self.play(Write(dir_api[2][3]))
        self.clear()
        self.wait()


class FS(Scene):
    def construct(self):
        disk1 = VGroup(*[Square(.4, fill_opacity=.8) for _ in range(32)]).arrange(RIGHT, buff=0)
        disk2 = disk1.copy()
        index = VGroup()
        VGroup(disk1, disk2).arrange(DOWN, buff=1)
        for group in range(8):
            if group < 4:
                index.add(Text(str(group*8)).scale(.5).next_to(disk1[group*8], DOWN))
            else:
                index.add(Text(str(group*8)).scale(.5).next_to(disk2[(group-4)*8], DOWN))
        disk = VGroup(disk1, disk2, index)
        inodes = disk1[3:8]
        datas = VGroup(disk1[8:], disk2)
        d_label = VGroup()
        for block in range(56):
            if block < 24:
                d_label.add(Text('D').scale(.5).move_to(disk1[block+8]))
            else:
                d_label.add(Text('D').scale(.5).move_to(disk2[block-24]))
        i_label = VGroup()
        for block in range(5):
            i_label.add(Text('I').scale(.5).move_to(disk1[block+3]))
        b_label = VGroup(Text('i').scale(.5).move_to(disk1[1]), Text('d').scale(.5).move_to(disk1[2]))
        s_label = Text('S').scale(.5).move_to(disk1[0])
        self.play(Create(disk))
        self.play(Create(d_label), FadeToColor(datas, BLUE))
        self.play(Create(i_label), FadeToColor(inodes, GREEN))
        self.play(Create(b_label), FadeToColor(disk1[1:3], YELLOW_E))
        self.play(Create(s_label), FadeToColor(disk1[0], RED))
        inode = VGroup(Rectangle(width=1, height=.5, fill_color=GREEN, fill_opacity=.8)).next_to(inodes[0], UP)
        inode.add(Text('inode').scale(.5).move_to(inode))
        self.play(Transform(inodes[0].copy(), inode))
        direct = VGroup()
        for data in range(3):
            direct.add(CurvedArrow(inode.get_right(), datas[0][data+1].get_top(), angle=-PI/2))
        indirect = VGroup()
        for data in range(16):
            indirect.add(CurvedArrow(datas[0][0].get_top(), datas[0][data+1].get_top(), angle=-PI/2))
        self.play(Create(direct))
        self.play(FadeOut(direct))
        self.play(Create(VGroup(CurvedArrow(inode.get_right(), datas[0][0].get_top(), angle=-PI/2), indirect)))
        self.wait()
        self.clear()

        rw = Table([['', ''], ['', ''], ['', '']],
                   col_labels=[Text('inode', color=GREEN), Text('数据', color=BLUE)],
                   row_labels=[Text('根文件夹', color=YELLOW), Text('foo', color=YELLOW), Text('bar', color=YELLOW)])
        inode = Square(.5, color=GREEN, fill_opacity=.8)
        data = Square(.5, color=BLUE, fill_opacity=.8)
        root_inode = inode.copy().move_to(rw.get_cell((2, 2)))
        root_data = data.copy().move_to(rw.get_cell((2, 3)))
        foo_inode = inode.copy().move_to(rw.get_cell((3, 2)))
        foo_data = data.copy().move_to(rw.get_cell((3, 3)))
        bar_inode = inode.copy().move_to(rw.get_cell((4, 2)))
        bar_data = VGroup(*[data.copy() for _ in range(3)]).arrange(RIGHT).move_to(rw.get_cell((4, 3)))
        self.play(Create(rw[0]))
        self.play(Create(root_inode))
        self.play(Create(root_data))
        self.play(Create(foo_inode))
        self.play(Create(foo_data))
        self.play(Create(bar_inode))
        for index in range(3):
            self.play(Create(bar_data[index]))
            self.play(Indicate(bar_inode, color=GREEN))
        self.clear()

        inode_bitmap = VGroup(Rectangle(width=2, height=1, fill_color=YELLOW_E, fill_opacity=.8))
        inode_bitmap.add(Text('inode位图').scale(.6).move_to(inode_bitmap))
        data_bitmap = VGroup(inode_bitmap[0].copy())
        data_bitmap.add(Text('数据位图').scale(.6).move_to(data_bitmap))
        VGroup(inode_bitmap, data_bitmap).arrange(RIGHT).next_to(rw, DOWN).shift(RIGHT*2)
        self.play(Create(rw[0]))
        self.play(Create(inode_bitmap))
        self.play(Create(inode.copy().move_to(rw.get_cell((4, 2)))))
        self.play(Create(VGroup(root_inode, root_data, foo_inode, foo_data)))
        self.play(Indicate(foo_inode, color=GREEN))
        self.play(Create(data_bitmap))
        self.play(Create(data.copy().move_to(rw.get_cell((4, 3)))))
        self.play(Indicate(bar_inode, color=GREEN))
        self.clear()

        vsfs = VGroup(Square(.5, color=RED, fill_opacity=.8),
                      *[Rectangle(width=1.5, height=.5, fill_opacity=.8).set(color=YELLOW_E) for _ in range(2)],
                      Rectangle(width=3, height=.5, fill_opacity=.8).set(color=GREEN),
                      Rectangle(width=7, height=.5, fill_opacity=.8).set(color=BLUE)).arrange(RIGHT, buff=0)
        vsfs.add(Text('S').scale(.5).move_to(vsfs[0]), Text('i').scale(.5).move_to(vsfs[1]),
                 Text('d').scale(.5).move_to(vsfs[2]), Text('I').scale(.5).move_to(vsfs[3]),
                 Text('D').scale(.5).move_to(vsfs[4]))
        i2d = CurvedDoubleArrow(vsfs[3].get_top(), vsfs[4].get_top(), angle=-PI/2)
        group = VGroup(Square(.5, color=RED, fill_opacity=.8),
                       *[Square(.5, color=YELLOW_E, fill_opacity=.8) for _ in range(2)],
                       Rectangle(width=1, height=.5, fill_opacity=.8).set(color=GREEN),
                       Rectangle(width=2, height=.5, fill_opacity=.8).set(color=BLUE)).arrange(RIGHT, buff=0)
        group.add(Text('S').scale(.5).move_to(group[0]), Text('i').scale(.5).move_to(group[1]),
                  Text('d').scale(.5).move_to(group[2]), Text('I').scale(.5).move_to(group[3]),
                  Text('D').scale(.5).move_to(group[4]))
        groups = VGroup(*[group.copy() for _ in range(3)]).arrange(RIGHT, buff=0)
        self.play(Create(vsfs))
        self.play(Create(i2d))
        self.play(FadeOut(i2d))
        self.play(ReplacementTransform(vsfs, groups))
        files = VGroup(*[Square(.5, color=YELLOW, fill_opacity=.8) for _ in range(3)]).arrange(RIGHT, buff=0)
        self.play(FadeOut(groups[0][-1]), Create(files.next_to(groups[0][3], buff=0)))

        self.play(Succession(Indicate(VGroup(groups[0][2], groups[0][7]), color=YELLOW_E),
                             Indicate(VGroup(groups[0][3], groups[0][8]), color=GREEN), Indicate(files)))
        journal_icon = VGroup(Square(.5, color=ORANGE, fill_opacity=.8))
        journal_icon.add(Text('J').scale(.5).move_to(journal_icon))
        self.play(VGroup(groups[0][0], groups[0][5]).animate.shift(LEFT*.25),
                  VGroup(groups[0][1:5], groups[0][6:], groups[1:]).animate.shift(RIGHT*.25), FadeOut(files))
        self.play(Create(journal_icon.next_to(groups[0][0], RIGHT, buff=0)))
        journal = VGroup(Rectangle(width=.5, height=1, fill_opacity=.8).set(color=ORANGE),
                         Square(1, color=YELLOW_E, fill_opacity=.8), Square(1, color=GREEN, fill_opacity=.8),
                         Square(1, color=BLUE, fill_opacity=.8),
                         Rectangle(width=.5, height=1, fill_opacity=.8).set(color=ORANGE)).arrange(RIGHT, buff=0)
        journal.add(Text('头').scale(.5).move_to(journal[0]), Text('位图').scale(.5).move_to(journal[1]),
                    Text('inode').scale(.5).move_to(journal[2]), Text('数据').scale(.5).move_to(journal[3]),
                    Text('尾').scale(.5).move_to(journal[4])).next_to(groups, UP, buff=1)
        self.play(ReplacementTransform(journal_icon.copy(), VGroup(journal[1:4], journal[-4:-1])))
        self.play(Create(VGroup(journal[0], journal[4], journal[-1], journal[-5])))
        self.play(ReplacementTransform(journal.copy(), VGroup(groups[0][1:5], groups[0][6:])))
        self.play(FadeOut(journal[-2]))
        self.play(FadeIn(journal[-2]))
        self.play(FadeOut(journal[4], journal[-1]))
        self.play(Create(VGroup(journal[4], journal[-1])))
        self.play(ReplacementTransform(VGroup(journal[3], journal[-2]), VGroup(groups[0][4], groups[0][-1])))
        self.play(VGroup(journal[4], journal[-1]).animate.next_to(journal[2], buff=0))
        self.clear()

        mem = VGroup(Rectangle(width=2.5, height=4, fill_color=BLUE, fill_opacity=.8))
        mem.add(Text('内存').scale(.8).next_to(mem, UP))
        disk = VGroup(Circle(1.5, fill_color=BLUE, fill_opacity=.8, stroke_color=WHITE))
        disk.add(Text('磁盘').scale(.8).next_to(disk, UP))
        VGroup(mem, disk).arrange(RIGHT, buff=1)
        cache = VGroup(Rectangle(width=2.5, height=1, fill_color=YELLOW, fill_opacity=.8).next_to(mem[0], UP, buff=-1))
        cache.add(Text('缓存', color=BLACK).scale(.8).move_to(cache))
        self.play(Create(VGroup(mem, disk)))
        self.play(Create(cache))
        deep_dir = Text('/dir1/dir2/.../dir100', color=BLUE).next_to(VGroup(mem, disk), UP)
        self.play(Write(deep_dir))
        self.play(FadeOut(deep_dir))
        self.play(Transform(cache[1], Text('更新', color=BLACK).scale(.8).move_to(cache)))
        disk_block = Sector(inner_radius=1, outer_radius=1.5, fill_color=YELLOW, fill_opacity=.8, angle=PI/3
                            ).move_to(disk).shift(RIGHT, UP*.3)
        disk_blocks = VGroup(disk_block.copy().rotate(PI/3, about_point=disk[0].get_center()),
                             disk_block.copy().rotate(2*PI/3, about_point=disk[0].get_center()),
                             disk_block.copy().rotate(PI, about_point=disk[0].get_center()))
        self.remove(cache)
        self.play(ReplacementTransform(cache.copy(), disk_block))
        self.play(FadeIn(cache))
        self.play(FadeOut(cache))
        batch = VGroup(*[Rectangle(width=2.5, height=1, fill_color=YELLOW, fill_opacity=.8) for _ in range(3)]
                       ).arrange(DOWN, buff=0).move_to(mem[0]).shift(UP*.5)
        self.play(Create(batch))
        self.play(ReplacementTransform(batch, disk_blocks))
        self.play(FadeIn(cache))
        self.play(FadeOut(cache))
        self.wait()


class Patch(Scene):
    def construct(self):
        # group = VGroup(Square(.5, color=RED, fill_opacity=.8),
        #                *[Square(.5, color=YELLOW_E, fill_opacity=.8) for _ in range(2)],
        #                Rectangle(width=1, height=.5, fill_opacity=.8).set(color=GREEN),
        #                Rectangle(width=2, height=.5, fill_opacity=.8).set(color=BLUE)).arrange(RIGHT, buff=0)
        # group.add(Text('S').scale(.5).move_to(group[0]), Text('i').scale(.5).move_to(group[1]),
        #           Text('d').scale(.5).move_to(group[2]), Text('I').scale(.5).move_to(group[3]),
        #           Text('D').scale(.5).move_to(group[4]))
        # groups = VGroup(*[group.copy() for _ in range(3)]).arrange(RIGHT, buff=0)
        # self.play(Create(groups))
        # journal_icon = VGroup(Square(.5, color=ORANGE, fill_opacity=.8))
        # journal_icon.add(Text('J').scale(.5).move_to(journal_icon))
        # self.play(VGroup(groups[0][0], groups[0][5]).animate.shift(LEFT * .25),
        #           VGroup(groups[0][1:5], groups[0][6:], groups[1:]).animate.shift(RIGHT * .25))
        # self.play(Create(journal_icon.next_to(groups[0][0], RIGHT, buff=0)))
        # journal = VGroup(Rectangle(width=.5, height=1, fill_opacity=.8).set(color=ORANGE),
        #                  Square(1, color=YELLOW_E, fill_opacity=.8), Square(1, color=GREEN, fill_opacity=.8),
        #                  Square(1, color=BLUE, fill_opacity=.8),
        #                  Rectangle(width=.5, height=1, fill_opacity=.8).set(color=ORANGE)).arrange(RIGHT, buff=0)
        # journal.add(Text('头').scale(.5).move_to(journal[0]), Text('位图').scale(.5).move_to(journal[1]),
        #             Text('inode').scale(.5).move_to(journal[2]), Text('数据').scale(.5).move_to(journal[3]),
        #             Text('尾').scale(.5).move_to(journal[4])).next_to(groups, UP, buff=1)
        # self.play(Create(journal))
        # self.play(ReplacementTransform(journal.copy(), VGroup(groups[0][1:5], groups[0][6:])))
        # self.play(FadeOut(journal))
        # self.play(FadeIn(journal))
        # self.clear()

        mem = VGroup(Rectangle(width=2.5, height=4, fill_color=BLUE, fill_opacity=.8))
        mem.add(Text('内存').scale(.8).next_to(mem, UP))
        disk = VGroup(Circle(1.5, fill_color=BLUE, fill_opacity=.8, stroke_color=WHITE))
        disk.add(Text('磁盘').scale(.8).next_to(disk, UP))
        VGroup(mem, disk).arrange(RIGHT, buff=1)
        cache = VGroup(Rectangle(width=2.5, height=1, fill_color=YELLOW, fill_opacity=.8).next_to(mem[0], UP, buff=-1))
        cache.add(Text('缓存', color=BLACK).scale(.8).move_to(cache))
        self.play(Create(VGroup(mem, disk)))
        self.play(Create(cache))
        self.play(Transform(cache[1], Text('更新', color=BLACK).scale(.8).move_to(cache)))
        disk_block = Sector(inner_radius=1, outer_radius=1.5, fill_color=YELLOW, fill_opacity=.8, angle=PI/3
                            ).move_to(disk).shift(RIGHT, UP*.3)
        disk_blocks = VGroup(disk_block.copy().rotate(PI/3, about_point=disk[0].get_center()),
                             disk_block.copy().rotate(2*PI/3, about_point=disk[0].get_center()),
                             disk_block.copy().rotate(PI, about_point=disk[0].get_center()))
        self.remove(cache)
        self.play(ReplacementTransform(cache.copy(), disk_block))
        cache[1].become(Text('缓存', color=BLACK).scale(.8).move_to(cache))
        self.play(FadeIn(cache))
        self.play(FadeOut(cache))
        batch = VGroup(*[Rectangle(width=2.5, height=1, fill_color=YELLOW, fill_opacity=.8) for _ in range(3)]
                       ).arrange(DOWN, buff=0).move_to(mem[0]).shift(UP*.5)
        self.play(Create(batch))
        self.play(ReplacementTransform(batch, disk_blocks))
        self.play(FadeIn(cache))
        self.play(FadeOut(cache))
        self.wait()
