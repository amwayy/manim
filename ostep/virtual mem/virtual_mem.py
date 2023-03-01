from manim import *
import math

coord_reference = NumberPlane()


class Slot(Scene):
    def construct(self):
        disk = VGroup(Circle(1.5, stroke_color=WHITE, fill_color=BLUE_A, fill_opacity=.8))
        code = VGroup(Rectangle(width=2.5, height=.5, fill_color=BLUE, fill_opacity=.8),
                      Text('代码').scale(.5))
        disk.add(Text('磁盘', color=BLUE_E).scale(.6).move_to(disk.get_top()+DOWN*.5), code.move_to(disk),)
        mem = VGroup(Rectangle(width=2.5, height=4, fill_color=BLUE_A, fill_opacity=.8))
        cpu = mem.copy()
        mem.add(Text('内存', color=BLUE_E).scale(.6).move_to(mem.get_top()+DOWN*.5))
        cpu.add(Text('CPU', color=BLUE_E).scale(.6).move_to(cpu.get_top()+DOWN*.5))
        self.play(Create(VGroup(VGroup(cpu, mem).arrange(RIGHT, buff=1), disk).arrange(DOWN)))
        self.play(code.animate.move_to(mem.get_center()+UP*.8))
        ins = VGroup(Rectangle(width=2.5, height=.5, fill_color=BLUE, fill_opacity=.8),
                     Text('指令').scale(.5)).move_to(cpu)
        self.play(ReplacementTransform(code.copy(), ins))
        stack = VGroup(Rectangle(width=2.5, height=.5, fill_color=YELLOW_E, fill_opacity=.8),
                       Text('栈').scale(.5)).move_to(mem.get_center()+DOWN*1.5)
        heap = VGroup(Rectangle(width=2.5, height=.5, fill_color=GREEN, fill_opacity=.8),
                      Text('堆').scale(.5)).next_to(code, DOWN, buff=0)
        self.play(Create(stack))
        self.play(Create(heap))
        self.clear()

        mem = VGroup(Rectangle(width=2.5, height=8, fill_color=BLUE_A, fill_opacity=.8))
        mem.add(Line(LEFT*1.25, RIGHT*1.25))
        mem.add(mem[1].copy().shift(UP*2), mem[1].copy().shift(DOWN*2))
        self.play(Create(mem[0]))
        self.play(Create(mem[1:]))
        address_space = VGroup(code, heap, stack.next_to(heap, DOWN, buff=.5)).move_to(mem.get_center()+DOWN)
        address_space_c = address_space.copy()
        self.play(Create(address_space))
        os_space = VGroup(Rectangle(width=2.5, height=2, fill_color=BLUE_E, fill_opacity=.8))
        os_space.add(Text('OS').scale(.6).move_to(os_space))
        self.play(Create(os_space.move_to(mem.get_center()+UP*3)))
        grown_heap = VGroup(Rectangle(width=2.5, height=.75, fill_color=GREEN, fill_opacity=.8),
                            Text('堆').scale(.5)).next_to(code, DOWN, buff=0)
        grown_stack = VGroup(Rectangle(width=2.5, height=.75, fill_color=YELLOW_E, fill_opacity=.8),
                             Text('栈').scale(.5)).next_to(grown_heap, DOWN, buff=0)
        self.play(Succession(Transform(stack, grown_stack), Transform(heap, grown_heap)))
        pointer = Triangle(color=ORANGE, fill_color=ORANGE, fill_opacity=1
                           ).rotate(PI*(3/2)).scale(0.1).next_to(code, LEFT).shift(UP*.25)
        offset = Brace(Line(code.get_left()+UP*.25, grown_stack.get_left()), LEFT)
        offset_txt = Text('+偏移值').scale(.8).next_to(offset, LEFT)
        self.play(Create(pointer), Write(Text('起始地址').scale(.8).next_to(pointer, LEFT)))
        self.play(pointer.animate.next_to(grown_stack, LEFT))
        self.play(FadeOut(pointer), Create(offset), Write(offset_txt))
        self.play(FadeOut(offset), Write(Text('=物理地址').scale(.8).next_to(offset_txt, DOWN)))
        self.clear()

        print_addr = Code('print_addr.c', style=Code.styles_list[9])
        addr = Code('addr.txt', insert_line_no=False)
        self.play(Create(VGroup(print_addr, addr).arrange(DOWN)))
        physical_addr = Text('物理地址=起始地址+偏移值').scale(.8).next_to(addr, DOWN)
        self.play(Succession(Write(physical_addr), Circumscribe(physical_addr[10:])))
        self.play(Write(Text('内存虚拟化').scale(.8).set_color_by_gradient(BLUE_A, BLUE_E).next_to(addr, RIGHT)))
        virtual_addr = Text('虚拟地址').set_color_by_gradient(BLUE_A, BLUE_E
                                                          ).scale(.8).next_to(physical_addr[:10], RIGHT, buff=.1)
        self.play(ReplacementTransform(physical_addr[10:], virtual_addr))
        self.clear()

        self.play(Create(VGroup(mem, os_space, address_space_c)))
        self.play(Circumscribe(address_space_c))
        unused = Rectangle(width=2.5, height=.5, stroke_width=0, fill_color=BLUE_A, fill_opacity=.8
                           ).next_to(address_space_c[1], DOWN, buff=0)
        self.play(Indicate(unused, color=BLUE_A))
        self.play(FadeOut(address_space_c, mem[1:4], unused))
        self.wait()


mem_space = VGroup(Rectangle(width=2.5, height=8, fill_color=BLUE_A, fill_opacity=.8))
mem_space.add(Rectangle(width=2.5, height=2, fill_color=BLUE_E, fill_opacity=.8).move_to(mem_space.get_center()+UP*3))
mem_space.add(Text('OS').scale(.6).move_to(mem_space[1]))


class Segment(Scene):
    def construct(self):
        self.add(mem_space)
        code = VGroup(Rectangle(width=2.5, height=.5, fill_color=BLUE, fill_opacity=.8), Text('代码').scale(.5))
        stack = VGroup(Rectangle(width=2.5, height=.5, fill_color=YELLOW_E, fill_opacity=.8), Text('栈').scale(.5))
        heap = VGroup(Rectangle(width=2.5, height=.5, fill_color=GREEN, fill_opacity=.8), Text('堆').scale(.5))
        self.play(Create(VGroup(code.move_to(mem_space.get_center()+DOWN), stack.move_to(mem_space.get_center()+UP),
                                heap.move_to(mem_space.get_center()+DOWN*2)), run_time=3))
        seg_hardware = Table([['40KB', '4K', '1', '读-执行'], ['48KB', '4K', '1', '读-写'], ['24KB', '4K', '0', '读-写']],
                             row_labels=[Text('代码', color=BLUE), Text('堆', color=GREEN), Text('栈', color=YELLOW_E)],
                             col_labels=[Text('基址', color=ORANGE), Text('大小', color=ORANGE),
                                         Text('正向延伸？', color=ORANGE), Text('保护', color=ORANGE)],
                             top_left_entry=Text('段')).scale(.6).shift(RIGHT*4)
        self.play(Create(seg_hardware.get_columns()[:3]),
                  VGroup(mem_space, code, heap, stack).animate.shift(LEFT*2))
        self.clear()

        seg_virtual_addr = VGroup(VGroup(*[Square(.5, fill_color=BLUE_E, fill_opacity=1) for _ in range(2)]
                                         ).arrange(RIGHT, buff=0),
                                  VGroup(*[Square(.5, fill_color=BLUE_C, fill_opacity=1) for _ in range(12)]
                                         ).arrange(RIGHT, buff=0)).arrange(RIGHT, buff=0)
        self.play(Create(seg_virtual_addr))
        seg_num_label = VGroup(Brace(seg_virtual_addr[0], DOWN))
        seg_num_label.add(Text('段号').scale(.6).next_to(seg_num_label, DOWN))
        self.play(Create(seg_num_label))
        self.play(FadeOut(seg_num_label))
        seg_num = VGroup(Text('0').move_to(seg_virtual_addr[0][0]), Text('0').move_to(seg_virtual_addr[0][1]),
                         Text('未使用', color=BLUE_A).scale(.8).next_to(seg_virtual_addr[0], DOWN))
        self.play(Create(seg_num))
        self.play(Transform(seg_num[1], Text('1').move_to(seg_num[1])),
                  Transform(seg_num[2], Text('代码', color=BLUE).scale(.8).move_to(seg_num[2])))
        self.play(Transform(seg_num[0], Text('1').move_to(seg_num[0])),
                  Transform(seg_num[1], Text('0').move_to(seg_num[1])),
                  Transform(seg_num[2], Text('堆', color=GREEN).scale(.8).move_to(seg_num[2])))
        self.play(Transform(seg_num[1], Text('1').move_to(seg_num[1])),
                  Transform(seg_num[2], Text('栈', color=YELLOW_E).scale(.8).move_to(seg_num[2])))
        self.play(FadeOut(seg_num))
        offset_label = VGroup(Brace(seg_virtual_addr[1], DOWN))
        offset_label.add(Text('偏移值').scale(.6).next_to(offset_label, DOWN))
        self.play(Create(offset_label))
        self.clear()

        seg_physical_addr = Code('segmentation.c', style=Code.styles_list[9])
        self.play(Write(seg_physical_addr))
        stack_offset = Text('栈偏移值=偏移值-段大小'
                            ).set_color_by_gradient(BLUE_A, BLUE_E).scale(.8).next_to(seg_physical_addr, DOWN)
        self.play(Write(stack_offset))
        self.play(Create(seg_hardware.get_columns()[:4].move_to(ORIGIN)),
                  FadeOut(seg_physical_addr))
        self.play(FadeOut(stack_offset))
        self.play(Create(seg_hardware.get_columns()[4].next_to(seg_hardware.get_columns()[3], RIGHT)))
        self.clear()

        code = VGroup(Rectangle(width=2.5, height=.5, fill_color=BLUE, fill_opacity=.8), Text('代码').scale(.5)
                      ).move_to(mem_space.get_center()+DOWN)
        stack = VGroup(Rectangle(width=2.5, height=.5, fill_color=YELLOW_E, fill_opacity=.8), Text('栈').scale(.5)
                       ).move_to(mem_space.get_center()+UP)
        heap = VGroup(Rectangle(width=2.5, height=1, fill_color=GREEN, fill_opacity=.8), Text('堆').scale(.5)
                      ).next_to(code, DOWN, buff=.2)
        self.play(Create(VGroup(mem_space, code, stack, heap).move_to(ORIGIN)))
        self.play(Indicate(Rectangle(width=2.5, height=.2, fill_color=BLUE_A, fill_opacity=.8
                                     ).next_to(code, DOWN, buff=0), color=BLUE_A))
        heap_local = VGroup(Rectangle(width=2.5, height=1.5, fill_color=GREEN_A, fill_opacity=.8),
                            Rectangle(width=2.5, height=.5, fill_color=GREEN_E, fill_opacity=.8)
                            ).arrange(DOWN, buff=0).next_to(heap, RIGHT)
        heap_local.add(Text('未使用').move_to(heap_local[0]), Text('堆').scale(.5).move_to(heap_local[1]))
        self.play(ReplacementTransform(heap.copy(), heap_local))
        self.clear()
        self.wait()


class Paging(Scene):
    def construct(self):
        self.play(Create(mem_space))
        self.play(Create(VGroup(Line(LEFT*1.25, RIGHT*1.25), Line([-1.25, -2, 0], [1.25, -2, 0]))))
        page_bound = VGroup(Line(LEFT*1.25, RIGHT*1.25))
        for page in range(-7, 16):
            page_bound.add(page_bound[0].copy().shift(DOWN*page*.25))
        self.play(Create(page_bound))
        self.play(ReplacementTransform(Rectangle(width=2.5, height=.25, fill_color=BLUE_A, fill_opacity=.8
                                                 ).shift(UP*.125),
                                       Text('页', color=BLUE_A).next_to(mem_space, RIGHT, buff=.5)))
        self.clear()

        virtual_pages = VGroup(*[Rectangle(width=2.5, height=.5, fill_color=BLUE, fill_opacity=.8) for _ in range(4)]
                               ).arrange(DOWN, buff=0)
        for page in range(4):
            virtual_pages.add(Text(str(page)).scale(.8).next_to(virtual_pages[page], LEFT))
        physical_pages = VGroup(*[Rectangle(width=2.5, height=.5) for _ in range(8)]).arrange(DOWN, buff=0)
        for page in range(8):
            physical_pages.add(Text(str(page)).scale(.8).next_to(physical_pages[page], LEFT))
        self.play(Create(VGroup(virtual_pages, physical_pages).arrange(RIGHT, buff=1)))
        self.play(Succession(virtual_pages[0].copy().animate.move_to(physical_pages[2]),
                             virtual_pages[1].copy().animate.move_to(physical_pages[6]),
                             virtual_pages[2].copy().animate.move_to(physical_pages[4]),
                             virtual_pages[3].copy().animate.move_to(physical_pages[1])))
        self.clear()

        page_table = VGroup(Rectangle(width=2.5, height=.5, fill_color=BLUE_C, fill_opacity=.5))
        page_table.add(Text('页表').scale(.5).move_to(page_table))
        mem_space.add(page_table.copy().move_to(mem_space[1].get_bottom()+UP*.25))
        self.play(Create(page_table))
        self.play(Create(mem_space[:3]), ReplacementTransform(page_table, mem_space[3]))
        self.wait()
        self.clear()

        pt_array = VGroup(*[Square(.5) for _ in range(4)]).arrange(RIGHT, buff=0)
        for page in range(4):
            pt_array.add(Text(str(page)).scale(.8).next_to(pt_array[page], UP))
        self.play(Create(pt_array[:4]))
        self.play(Create(pt_array[4:]))
        entry = VGroup(Rectangle(width=4, height=.5, fill_color=BLUE, fill_opacity=.8),
                       Square(.5, fill_color=GREEN, fill_opacity=.8), Square(.5, fill_color=YELLOW_E, fill_opacity=.8),
                       Rectangle(width=1.5, height=.5)).arrange(RIGHT, buff=0).next_to(pt_array, DOWN, buff=1)
        entry.add(Text('物理页号').scale(.5).move_to(entry[0]), Text('...').move_to(entry[3]),
                  Rectangle(width=6.5, height=.5).move_to(entry))
        self.play(ReplacementTransform(pt_array[0].copy(), VGroup(entry[0], entry[4], entry[6])))
        valid = VGroup(Text('有效位').scale(.5).next_to(entry[1], DOWN, buff=.5))
        valid.add(Arrow(entry[1].get_bottom(), valid.get_top(), buff=0))
        self.play(Create(VGroup(entry[1], valid)))
        self.play(FadeOut(valid))
        protection = VGroup(Text('保护位').scale(.5).next_to(entry[2], DOWN, buff=.5))
        protection.add(Arrow(entry[2].get_bottom(), protection.get_top(), buff=0))
        self.play(Create(VGroup(entry[2], entry[5], protection)))
        self.play(FadeOut(protection))
        self.clear()

        page_virtual_addr = VGroup(Rectangle(width=2, height=.5, fill_color=BLUE_E, fill_opacity=.8),
                                   Rectangle(width=2, height=.5, fill_color=BLUE_C, fill_opacity=.8)
                                   ).arrange(RIGHT, buff=0)
        page_virtual_addr.add(Text('虚拟页号').scale(.5).move_to(page_virtual_addr[0]),
                              Text('偏移值').scale(.5).move_to(page_virtual_addr[1]))
        self.play(Create(page_virtual_addr[:2]))
        self.play(Write(page_virtual_addr[2]))
        self.play(Write(page_virtual_addr[3]))
        physical_page = VGroup(Rectangle(width=2, height=.5, fill_color=BLUE_E, fill_opacity=.8
                                         ).next_to(page_virtual_addr[0], DOWN, buff=.5))
        physical_page.add(Text('物理页号').scale(.5).move_to(physical_page))
        map_arrow = Arrow(page_virtual_addr[0].get_bottom(), physical_page.get_top(), buff=0)
        self.play(Create(VGroup(map_arrow, physical_page)))
        self.play(FadeOut(map_arrow, VGroup(page_virtual_addr[0], page_virtual_addr[2])),
                  physical_page.animate.next_to(page_virtual_addr[1], LEFT, buff=0))
        physical_addr = VGroup(Brace(page_virtual_addr, DOWN))
        physical_addr.add(Text('物理地址').scale(.7).next_to(physical_addr, DOWN))
        self.play(Create(physical_addr))
        self.clear()
        self.wait()


class TLB(Scene):
    def construct(self):
        page_table = VGroup(Rectangle(width=2, height=1, fill_color=BLUE, fill_opacity=.8).shift(UP*.5))
        mem = page_table.copy().shift(DOWN*1.5)
        page_table.add(Text('页表').scale(.8).move_to(page_table))
        mem.add(Text('内存').scale(.8).move_to(mem))
        self.play(Create(VGroup(Arrow(page_table.get_left()+LEFT, page_table.get_left(), buff=0), page_table,
                                CurvedArrow(page_table.get_left(), mem.get_left()), mem)), run_time=3)
        self.clear()

        self.play(Write(Text('快表(TLB)').set_color_by_gradient(BLUE_A, BLUE_E)))
        tlb_entry = VGroup(Rectangle(width=2.5, height=.5, fill_color=BLUE, fill_opacity=.8),
                           Rectangle(width=2.5, height=.5, fill_color=RED_A, fill_opacity=.8),
                           Square(.5, fill_color=GREEN, fill_opacity=.8),
                           Square(.5, fill_color=YELLOW_E, fill_opacity=.8), Rectangle(width=1.5, height=.5)
                           ).arrange(RIGHT, buff=0).shift(DOWN)
        tlb_entry.add(Text('虚拟页号').scale(.5).move_to(tlb_entry[0]), Text('物理页号').scale(.5).move_to(tlb_entry[1]),
                      Text('...').move_to(tlb_entry[4]))
        valid = VGroup(Text('有效位').scale(.5).next_to(tlb_entry[2], DOWN, buff=.5))
        valid.add(Arrow(tlb_entry[2].get_bottom(), valid.get_top(), buff=0))
        protection = VGroup(Text('保护位').scale(.5).next_to(tlb_entry[3], DOWN, buff=.5))
        protection.add(Arrow(tlb_entry[3].get_bottom(), protection.get_top(), buff=0))
        self.play(Create(tlb_entry))
        self.play(Create(valid))
        self.play(FadeOut(valid))
        self.play(Create(protection))
        self.play(FadeOut(protection))
        self.clear()

        tlb = VGroup(page_table[0].copy()).shift(UP*1.5)
        tlb.add(Text('TLB').move_to(tlb))
        access = Arrow(tlb.get_left()+LEFT*.5, tlb.get_left(), buff=0)
        self.play(Create(VGroup(access, tlb, page_table, mem)))
        tlb_hit = Text('TLB命中√', color=GREEN).scale(.8).next_to(tlb, RIGHT)
        self.play(Write(tlb_hit))
        self.play(FadeOut(tlb_hit))
        empty_tlb = VGroup(*[Rectangle(width=2.5, height=.5) for _ in range(4)]
                           ).arrange(DOWN, buff=0).next_to(tlb, RIGHT)
        self.play(Create(empty_tlb))
        access_pt = CurvedArrow(tlb.get_left(), page_table.get_left())
        self.play(Create(access_pt))
        self.play(ReplacementTransform(page_table.copy(),
                                       Rectangle(width=2.5, height=.5, fill_color=BLUE_A, fill_opacity=.8
                                                 ).move_to(empty_tlb[0])), FadeOut(access_pt))
        self.play(Create(access))
        self.play(Write(tlb_hit.next_to(empty_tlb, RIGHT)))
        self.clear()

        full_tlb = VGroup(*[Rectangle(width=2.5, height=.5, fill_color=BLUE_A, fill_opacity=.8) for _ in range(4)]
                          ).arrange(DOWN, buff=0)
        full_tlb.add(Text('TLB').scale(.8).next_to(full_tlb, UP))
        full_tlb_c = full_tlb.copy()
        self.play(Create(full_tlb))
        self.play(Transform(full_tlb[:4], empty_tlb.move_to(full_tlb[:4])))
        self.clear()

        self.play(Create(tlb_entry.move_to(ORIGIN)))
        asid = VGroup(Rectangle(width=1, height=.5, fill_color=BLUE_A, fill_opacity=.8)
                      ).next_to(tlb_entry[3], RIGHT, buff=0)
        asid.add(Text('ID').scale(.5).move_to(asid))
        tlb_entry.add(asid)
        self.play(Create(asid), VGroup(tlb_entry[4], tlb_entry[-2]).animate.shift(RIGHT))
        self.clear()

        self.play(Create(VGroup(full_tlb_c, empty_tlb.move_to(full_tlb_c[:4]))))
        new_entry = full_tlb_c[0].copy().next_to(full_tlb_c, DOWN, buff=1)
        self.play(Create(new_entry))
        self.play(new_entry.animate.move_to(empty_tlb[-1]), full_tlb_c[-2].animate.shift(RIGHT*10))
        self.clear()

        self.play(FadeIn(tlb_entry.move_to(ORIGIN)))
        time = VGroup(Rectangle(width=1, height=.5, fill_color=RED, fill_opacity=.8)).next_to(asid, RIGHT, buff=0)
        time.add(Text('时间').scale(.5).move_to(time))
        self.play(Create(time), VGroup(tlb_entry[4], tlb_entry[-2]).animate.shift(RIGHT))
        self.clear()
        self.wait()


class MultiLevel(Scene):
    def construct(self):
        pt_size_calc = VGroup(Text('物理地址32位', color=BLUE_E), Text('页大小=4KB', color=BLUE_D),
                              VGroup(Text('页数=', color=BLUE_C), Tex(r'$\frac{2^{32}}{2^{12}}=2^{20}$', color=BLUE_C)
                                     ).arrange(RIGHT), Text('页表项大小=4Byte', color=BLUE_B),
                              VGroup(Text('页表项大小=', color=BLUE_A), Tex(r'$2^{20}*4Byte\approx$', '4MB', color=BLUE_A)
                                     ).arrange(RIGHT)).arrange(DOWN)
        for formula in pt_size_calc:
            self.play(Create(formula))
        self.play(Create(SurroundingRectangle(pt_size_calc[-1][1][1])))
        self.clear()

        page_table = Table([['12', '1', 'r-x'], ['13', '1', 'r-x'], ['-', '0', '-'], ['100', '1', 'r-w'],
                            ['-', '0', '-'], ['-', '0', '-'], ['-', '0', '-'], ['-', '0', '-'], ['-', '0', '-'],
                            ['-', '0', '-'], ['-', '0', '-'], ['-', '0', '-'], ['-', '0', '-'], ['-', '0', '-'],
                            ['86', '1', 'r-w'], ['15', '1', 'r-w']],
                           col_labels=[Text('物理页号', color=BLUE), Text('有效位', color=GREEN),
                                       Text('保护位', color=YELLOW_E)]).scale(.35)
        self.play(Create(page_table))
        self.play(Circumscribe(page_table.get_rows()[5:-2]))
        page_dir = Table([['201', '1'], ['-', '0'], ['-', '0'], ['204', '1']],
                         col_labels=[Text('物理页号', color=BLUE), Text('有效位', color=GREEN)]
                         ).scale(.5).next_to(page_table, RIGHT)
        self.play(ReplacementTransform(page_table.get_rows()[5:9].copy(), page_dir.get_rows()[2]),
                  ReplacementTransform(page_table.get_rows()[9:13].copy(), page_dir.get_rows()[3]))
        self.play(ReplacementTransform(page_table.get_rows()[:5].copy(), page_dir.get_rows()[:2]),
                  ReplacementTransform(page_table.get_rows()[13:].copy(), page_dir.get_rows()[4]))
        pfn1 = VGroup(Brace(page_table.get_rows()[1:5], LEFT).shift(LEFT*.5))
        pfn1.add(Text('物理页201').scale(.5).next_to(pfn1, LEFT)).set(color=BLUE)
        pfn2 = VGroup(Brace(page_table.get_rows()[13:], LEFT).shift(LEFT*.5))
        pfn2.add(Text('物理页204').scale(.5).next_to(pfn2, LEFT)).set(color=BLUE)
        self.play(Create(VGroup(pfn1, pfn2)))
        self.clear()

        virtual_addr = VGroup(Rectangle(width=2, height=.5, fill_color=BLUE_E, fill_opacity=.8),
                              Rectangle(width=2, height=.5, fill_color=BLUE_C, fill_opacity=.8),
                              Rectangle(width=3, height=.5, fill_color=BLUE_A, fill_opacity=.8)).arrange(RIGHT, buff=0)
        virtual_addr.add(Text('偏移值').scale(.5).move_to(virtual_addr[2]),
                         Brace(virtual_addr[:2], UP))
        virtual_addr.add(Text('虚拟页号').scale(.5).next_to(virtual_addr[-1], UP))
        self.play(Create(virtual_addr))
        page_dir_index = Text('二级页表索引').scale(.4).move_to(virtual_addr[0])
        pt_index = Text('一级页表索引').scale(.4).move_to(virtual_addr[1])
        self.play(Write(page_dir_index))
        self.play(Write(pt_index))
        self.clear()

        page_table_eg = VGroup(Rectangle(width=2.5, height=8))
        page_table_eg.add(VGroup(Rectangle(width=2.5, height=.5, stroke_width=0, fill_color=BLUE_A, fill_opacity=.8),
                                 Rectangle(width=2.5, height=7, stroke_width=0, fill_color=BLUE_A, fill_opacity=.8),
                                 Rectangle(width=2.5, height=.5, stroke_width=0, fill_color=BLUE_A, fill_opacity=.8)
                                 ).arrange(DOWN, buff=0))
        size = Text('256项').scale(.8).move_to(page_table_eg)
        self.play(Create(VGroup(page_table_eg, size)))
        page_line = VGroup(Line(LEFT*1.25, RIGHT*1.25))
        for page in range(-7, 8):
            page_line.add(page_line[0].copy().shift(UP*.5*page))
        self.play(FadeOut(size), Create(page_line))
        self.play(page_table_eg[1][1].animate.set(color=BLACK))
        page_dir_eg = VGroup(Rectangle(width=1.5, height=2, fill_color=BLUE_C, fill_opacity=.8))
        page_dir_eg.add(Text('二级页表').scale(.5).move_to(page_dir_eg))
        page1 = Rectangle(width=1.5, height=2, fill_color=BLUE_A, fill_opacity=.8)
        page2 = page1.copy()
        stored = VGroup(page_dir_eg, VGroup(page1, page2).arrange(RIGHT, buff=2)).arrange(DOWN, buff=1).shift(RIGHT*3)
        stored.add(Line(page_dir_eg.get_bottom(), page_dir_eg.get_bottom()+DOWN*.5),
                   Line(page1.get_top()+UP*.5, page2.get_top()+UP*.5),
                   Line(page1.get_top(), page1.get_top()+UP*.5), Line(page2.get_top(), page2.get_top()+UP*.5))
        self.play(VGroup(page_table_eg, page_line).animate.shift(LEFT*3), Create(stored))
        self.clear()

        pt1 = VGroup(Rectangle(width=.75, height=1, fill_color=BLUE_A, fill_opacity=.8), Text('...'),
                     Rectangle(width=.75, height=1, fill_color=BLUE_A, fill_opacity=.8)).arrange(RIGHT)
        pt2 = pt1.copy()
        pt = VGroup(pt1[:3], Text('...'), pt2[:3]).arrange(RIGHT).shift(DOWN)
        pt_dir1 = VGroup(Rectangle(width=.75, height=1, fill_color=BLUE_C, fill_opacity=.8).next_to(pt1, UP, buff=1),
                         Text('...').next_to(pt[1], UP, buff=1.7),
                         Rectangle(width=.75, height=1, fill_color=BLUE_C, fill_opacity=.8).next_to(pt2, UP, buff=1))
        pt1.add(VGroup(Line(pt_dir1[0].get_bottom(), pt_dir1[0].get_bottom()+DOWN*.5),
                       Line(pt1[0].get_top()+UP*.5, pt1[2].get_top()+UP*.5),
                       Line(pt1[0].get_top(), pt1[0].get_top()+UP*.5), Line(pt1[2].get_top(), pt1[2].get_top()+UP*.5)))
        pt2.add(pt1[-1].copy().next_to(pt2, UP, buff=0))
        pt_size = VGroup(Brace(pt, DOWN))
        pt_size.add(Tex('$2^{14}pages$').next_to(pt_size, DOWN))
        pt_dir1_size = VGroup(DoubleArrow(pt_dir1[0].get_right(), pt_dir1[2].get_left(), buff=0))
        pt_dir1_size.add(Text('128页').scale(.5).next_to(pt_dir1_size, UP, buff=.1))
        self.play(Create(pt))
        self.play(Create(pt_size))
        self.play(Create(VGroup(pt1[-1], pt2[-1], pt_dir1, pt_dir1_size)))
        pt_dir0 = Rectangle(width=.75, height=1, fill_color=BLUE_E, fill_opacity=.8).next_to(pt_dir1, UP, buff=1)
        pt_dir1.add(VGroup(Line(pt_dir0.get_bottom(), pt_dir0.get_bottom()+DOWN*.5),
                           Line(pt_dir1[0].get_top()+UP*.5, pt_dir1[2].get_top()+UP*.5),
                           Line(pt_dir1[0].get_top(), pt_dir1[0].get_top()+UP*.5),
                           Line(pt_dir1[2].get_top(), pt_dir1[2].get_top()+UP*.5)))
        self.play(Create(VGroup(pt_dir1[-1], pt_dir0)))
        virtual_addr = VGroup(Rectangle(width=2, height=.5, fill_color=BLUE_E, fill_opacity=.8),
                              Rectangle(width=2, height=.5, fill_color=BLUE_C, fill_opacity=.8),
                              Rectangle(width=2, height=.5, fill_color=BLUE_A, fill_opacity=.8),
                              Rectangle(width=3, height=.5, fill_color=BLUE, fill_opacity=.8)
                              ).arrange(RIGHT, buff=0).next_to(pt_size, DOWN)
        virtual_addr.add(Text('三级页表索引').scale(.4).move_to(virtual_addr[0]),
                         Text('二级页表索引').scale(.4).move_to(virtual_addr[1]),
                         Text('一级页表索引').scale(.4).move_to(virtual_addr[2]),
                         Text('偏移值').scale(.5).move_to(virtual_addr[3]))
        pfn = VGroup(Rectangle(width=6, height=.5, fill_color=BLUE_E, fill_opacity=.8)).move_to(virtual_addr[:3])
        pfn.add(Text('物理页号').scale(.5).move_to(pfn))
        self.play(Create(virtual_addr))
        self.play(Create(CurvedArrow(pt_dir0.get_left(), pt_dir1[0].get_left())))
        self.play(Create(CurvedArrow(pt_dir1[0].get_left(), pt1[0].get_left())))
        self.play(Create(CurvedArrow(pt1[0].get_left(), virtual_addr.get_left())),
                  ReplacementTransform(VGroup(virtual_addr[:3], virtual_addr[4:7]), pfn))
        self.clear()


class Disk(Scene):
    def construct(self):
        # tlb = VGroup(Rectangle(width=3, height=1, fill_color=BLUE, fill_opacity=.8))
        # pt_lv2 = tlb.copy()
        # pt_lv1 = tlb.copy()
        # mem = tlb.copy()
        # tlb.add(Text('TLB').scale(.8).move_to(tlb))
        # pt_lv2.add(Text('二级页表').scale(.8).move_to(pt_lv2))
        # mem.add(Text('内存').scale(.8).move_to(mem))
        # VGroup(tlb, pt_lv2, mem).arrange(DOWN)
        # pt_lv1.add(Text('一级页表').scale(.8).move_to(pt_lv1)).next_to(pt_lv2, RIGHT, buff=1)
        # self.play(Create(VGroup(tlb, pt_lv2, pt_lv1, mem).move_to(ORIGIN)))
        # tlb_miss = VGroup(Arrow(tlb.get_left()+LEFT, tlb.get_left(), buff=0),
        #                   CurvedArrow(tlb.get_left(), pt_lv2.get_left()))
        # tlb_miss.add(Text('TLB miss', color=RED).scale(.5).next_to(tlb_miss[1], LEFT),
        #              Arrow(pt_lv2.get_right(), pt_lv1.get_left(), buff=0))
        # self.play(Create(tlb_miss), run_time=2)
        # self.play(ReplacementTransform(pt_lv1.copy(), tlb))
        # tlb_hit = VGroup(Arrow(tlb.get_left()+LEFT, tlb.get_left(), buff=0),
        #                  Text('TLB命中！', color=GREEN).scale(.8).next_to(tlb, RIGHT))
        # self.play(FadeOut(tlb_miss), Create(tlb_hit))
        # self.play(FadeOut(tlb_hit))
        # disk = VGroup(Circle(1.5, stroke_color=WHITE, fill_color=BLUE, fill_opacity=.8).next_to(pt_lv1, DOWN))
        # disk.add(Text('磁盘').scale(.8).move_to(disk.get_center()+UP))
        # self.play(Create(VGroup(disk, CurvedArrow(mem.get_bottom(), disk.get_left()))))
        # swap = VGroup(Rectangle(width=2, height=1, fill_color=BLUE_E, fill_opacity=.8).move_to(disk))
        # swap.add(Text('交换区').scale(.8).move_to(swap))
        # disk.add(swap)
        # self.play(Create(swap))
        # self.play(ReplacementTransform(mem.copy(), swap))
        # self.play(ReplacementTransform(swap.copy(), mem))
        # self.clear()
        #
        pte = VGroup(Rectangle(width=4, height=.5, fill_color=BLUE, fill_opacity=.8),
                     Square(.5, fill_color=GREEN, fill_opacity=.8), Square(.5, fill_color=YELLOW_E, fill_opacity=.8),
                     Square(.5, fill_color=RED_A, fill_opacity=.8), Rectangle(width=1.5, height=.5)).arrange(RIGHT, buff=0)
        pte.add(Text('物理页号').scale(.5).move_to(pte[0]), Text('...').move_to(pte[-1]))
        # self.play(Create(pte))
        # present = VGroup(Text('存在位').scale(.5).next_to(pte[3], DOWN, buff=.5))
        # present.add(Arrow(pte[3].get_bottom(), present.get_top(), buff=0))
        # self.play(Create(present))
        # self.play(FadeOut(present))
        # self.play(Write(Text('缺页中断').set_color_by_gradient(BLUE_A, BLUE_E).next_to(pte, DOWN)))
        # self.clear()
        #
        # empty_mem = VGroup(*[Rectangle(width=2.5, height=.5) for _ in range(4)]).arrange(DOWN, buff=0)
        # full_mem = VGroup(*[Rectangle(width=2.5, height=.5, fill_color=BLUE, fill_opacity=.8) for _ in range(4)]
        #                   ).arrange(DOWN, buff=0)
        # VGroup(VGroup(empty_mem, full_mem), disk).arrange(DOWN)
        # self.play(Create(VGroup(empty_mem, full_mem[:3], disk)))
        # self.play(ReplacementTransform(swap.copy(), full_mem[3]))
        # self.play(ReplacementTransform(swap.copy(), full_mem[0].copy()),
        #           full_mem[0].animate.shift(RIGHT*10))
        # self.clear()
        #
        VGroup(pte[-1], pte[4]).shift(RIGHT*.5)
        pte.add(Square(.5, fill_color=BLUE_A, fill_opacity=.8).next_to(pte[3], RIGHT, buff=0))
        use_bit = VGroup(Text('使用位').scale(.5).next_to(pte[-1], DOWN, buff=.5))
        use_bit.add(Arrow(pte[-1].get_bottom(), use_bit.get_top(), buff=0))
        self.play(FadeIn(pte), Create(use_bit))
        self.clear()

        round_list = VGroup()
        for page in range(12):
            round_list.add(Square(.5, fill_color=BLUE, fill_opacity=.8
                                  ).move_to([2*math.sin(page*PI/6), 2*math.cos(page*PI/6), 0]))
        for page in range(12):
            round_list.add(Arrow(round_list[page], round_list[(page+1) % 12], buff=0))
        self.play(Create(round_list))
        pointer = Arrow(ORIGIN, UP*1.5, buff=0, color=BLUE_A)
        rotate_ref = VGroup(pointer, Line(ORIGIN, DOWN*1.5, stroke_width=0))
        self.play(Create(pointer))
        use_bit1 = Text('使用位=1').scale(.5).next_to(round_list[0], UP)
        self.play(Indicate(round_list[0], color=BLUE), Write(use_bit1))
        use_bit0 = Text('使用位=0').scale(.5).next_to(round_list[0], UP)
        self.play(ReplacementTransform(use_bit1, use_bit0))
        self.play(FadeOut(use_bit0))
        self.play(rotate_ref.animate.rotate(-PI/6), Indicate(round_list[1], color=BLUE),
                  Create(use_bit0.next_to(round_list[1], UR)))
        empty_page2 = Square(.5).move_to(round_list[1].copy())
        self.add(empty_page2)
        self.play(round_list[1].animate.shift(RIGHT*10))
        self.play(FadeOut(use_bit0))
        self.play(FadeIn(round_list[1].move_to(empty_page2)), rotate_ref.animate.rotate(PI/6))

        VGroup(pte[6], pte[4]).shift(RIGHT*.5)
        pte.add(Square(.5, fill_color=RED, fill_opacity=.8).next_to(pte[-1], RIGHT, buff=0))
        dirty = VGroup(Text('修改位').scale(.5).next_to(pte[-1], DOWN, buff=.5))
        dirty.add(Arrow(pte[-1].get_bottom(), dirty.get_top(), buff=0))
        self.play(FadeIn(VGroup(pte, dirty).next_to(round_list, DOWN)))
        self.play(FadeOut(VGroup(pte, dirty)))

        replace1 = Text('修改位=0，\n使用位=0').scale(.5).next_to(round_list[1], UR)
        replace2 = Text('修改位=1，\n使用位=0').scale(.5).next_to(round_list[1], UR)
        self.play(rotate_ref.animate.rotate(-PI/6))
        self.play(Indicate(round_list[1], color=BLUE), Write(replace1))
        self.play(round_list[1].animate.shift(RIGHT*10))
        self.play(FadeOut(replace1), FadeIn(round_list[1].move_to(empty_page2)))
        self.play(Rotate(rotate_ref, -2*PI))
        self.play(Indicate(round_list[1], color=BLUE), Write(replace2))
        self.play(round_list[1].animate.shift(RIGHT*10))
        self.wait()


class Example(Scene):
    def construct(self):
        eg = Code(code='65 movl\t1089, %eax', language='asm', style=Code.styles_list[9])[2][0].scale(1.5)
        self.play(Write(eg))
        self.play(Write(Text('虚拟地址14位，页大小64字节').scale(.7).next_to(eg, UP, buff=1)))
        virtual_addr = VGroup(VGroup(*[Square(.5, fill_color=BLUE_E, fill_opacity=.8) for _ in range(8)]
                                     ).arrange(RIGHT, buff=0),
                              VGroup(*[Square(.5, fill_color=BLUE_C, fill_opacity=.8) for _ in range(6)]
                                     ).arrange(RIGHT, buff=0)).arrange(RIGHT, buff=0).next_to(eg, DOWN, buff=1)
        self.play(Create(virtual_addr))
        vpn = VGroup(Brace(virtual_addr[0], DOWN))
        vpn.add(Text('虚拟页号').scale(.5).next_to(vpn, DOWN))
        offset = VGroup(Brace(virtual_addr[1], DOWN))
        offset.add(Text('偏移值').scale(.5).next_to(offset, DOWN))
        self.play(Create(vpn))
        self.play(FadeOut(vpn), Create(offset))
        self.play(FadeOut(offset))
        self.play(Circumscribe(eg[:2].copy(), shape=Circle))
        binary_addr = VGroup()
        binary = '00000001000001'
        for bit in range(14):
            if bit < 8:
                binary_addr.add(Text(binary[bit]).scale(.5).move_to(virtual_addr[0][bit]))
            else:
                binary_addr.add(Text(binary[bit]).scale(.5).move_to(virtual_addr[1][bit-8]))
        self.play(ReplacementTransform(eg[:2].copy(), binary_addr))
        self.wait()
