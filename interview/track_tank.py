# -*- coding: utf-8 -*-
'''
   某次战役中，为便于信息交互，我军侦察部门将此次战役的关键高地坐标设定为（x=0，y=0）并规定，每向东增加100米，x加1，每向北增加100米，y加1。

   同时，我军情报部门也破译了敌军向坦克发送的指挥信号，其中有三种信号（L,R,M）用于控制坦克的运动，
L 和 R 分别表示使令坦克向左、向右转向，M 表示令坦克直线开进100米，其它信号如T用于时间同步，
P用于反转信号，既出现p，后面的信号向左变为向右，向右变为向左，向前变为向后，反之亦然。

   一日，我军侦察兵发现了敌军的一辆坦克，侦察兵立即将坦克所在坐标（P, Q）及坦克前进方向（W：西，E：东，N：北，S：南）发送给指挥部，
同时启动信号接收器，将坦克接收到的信号实时同步发往指挥部，指挥部根据这些信息得以实时掌控了该坦克的位置，并使用榴弹炮精准地击毁了该坦克。

   假设，侦察兵发送给指挥部的信息如下：坦克坐标：（11，39）坦克运行方向：W，坦克接收到的信号为：MTMPRPMTMLMRPRMTPLMMTLMRRMP，
请通过编程计算出坦克所在的位置（编程语言不限）。
'''
'''
输出结果如下

    ---- 初始化坦克数据 -----
    坦克id:4471322440, 正在向【W】方向行驶，当前坐标(x:11,y:39)
    ---- 初始化完成开始追踪 -----
    
指令:[M] 坦克id:4471322440, 正在向【W】方向行驶，当前坐标(x:10,y:39)
指令:[T] 坦克id:4471322440, 正在向【W】方向行驶，当前坐标(x:10,y:39)
指令:[M] 坦克id:4471322440, 正在向【W】方向行驶，当前坐标(x:9,y:39)
指令:[P] 坦克id:4471322440, 正在向【E】方向行驶，当前坐标(x:9,y:39)
指令:[R] 坦克id:4471322440, 正在向【S】方向行驶，当前坐标(x:9,y:39)
指令:[P] 坦克id:4471322440, 正在向【N】方向行驶，当前坐标(x:9,y:39)
指令:[M] 坦克id:4471322440, 正在向【N】方向行驶，当前坐标(x:9,y:40)
指令:[T] 坦克id:4471322440, 正在向【N】方向行驶，当前坐标(x:9,y:40)
指令:[M] 坦克id:4471322440, 正在向【N】方向行驶，当前坐标(x:9,y:41)
指令:[L] 坦克id:4471322440, 正在向【W】方向行驶，当前坐标(x:9,y:41)
指令:[M] 坦克id:4471322440, 正在向【W】方向行驶，当前坐标(x:8,y:41)
指令:[R] 坦克id:4471322440, 正在向【N】方向行驶，当前坐标(x:8,y:41)
指令:[P] 坦克id:4471322440, 正在向【S】方向行驶，当前坐标(x:8,y:41)
指令:[R] 坦克id:4471322440, 正在向【W】方向行驶，当前坐标(x:8,y:41)
指令:[M] 坦克id:4471322440, 正在向【W】方向行驶，当前坐标(x:7,y:41)
指令:[T] 坦克id:4471322440, 正在向【W】方向行驶，当前坐标(x:7,y:41)
指令:[P] 坦克id:4471322440, 正在向【E】方向行驶，当前坐标(x:7,y:41)
指令:[L] 坦克id:4471322440, 正在向【N】方向行驶，当前坐标(x:7,y:41)
指令:[M] 坦克id:4471322440, 正在向【N】方向行驶，当前坐标(x:7,y:42)
指令:[M] 坦克id:4471322440, 正在向【N】方向行驶，当前坐标(x:7,y:43)
指令:[T] 坦克id:4471322440, 正在向【N】方向行驶，当前坐标(x:7,y:43)
指令:[L] 坦克id:4471322440, 正在向【W】方向行驶，当前坐标(x:7,y:43)
指令:[M] 坦克id:4471322440, 正在向【W】方向行驶，当前坐标(x:6,y:43)
指令:[R] 坦克id:4471322440, 正在向【N】方向行驶，当前坐标(x:6,y:43)
指令:[R] 坦克id:4471322440, 正在向【E】方向行驶，当前坐标(x:6,y:43)
指令:[M] 坦克id:4471322440, 正在向【E】方向行驶，当前坐标(x:7,y:43)
指令:[P] 坦克id:4471322440, 正在向【W】方向行驶，当前坐标(x:7,y:43)

        ---- 发射榴弹 -----
        坦克id:4471322440, 正在向【W】方向行驶，当前坐标(x:7,y:43)
        ---- 目标已击毁 -----
'''

import time

DIRECTION = ['N', 'E', 'S', 'W']


def get_direction_index(direction: str):
    if direction not in DIRECTION:
        raise ('方向错误')
    for index, item in enumerate(DIRECTION):
        if item == direction:
            return index


class Tank(object):

    def __init__(self, direction: int, start_x: int = 0, start_y: int = 0):
        self.direction = direction
        self.x = start_x
        self.y = start_y

    def move(self):
        '''
        按步进单位移动坦克
        :param direction:
        :return:
        '''
        d = DIRECTION[self.direction % len(DIRECTION)]
        if d == 'N':
            self.y += 1
        elif d == 'S':
            self.y -= 1
        elif d == 'E':
            self.x += 1
        elif d == 'W':
            self.x -= 1
        else:
            pass

    def now(self):
        '''
        返回坦克当前位置
        :return:
        '''
        return "坦克id:{}, 正在向【{}】方向行驶，当前坐标({})".format(
            id(self), DIRECTION[self.direction], 'x:%d,y:%s' % (self.x, self.y)
        )


class Dispatch(object):
    '''
    解析指令, 实时处理最终坦克位置
    '''

    INSTRUCTION = 'LRMTP'

    def deal_instruction(self, instruction: str, tank: Tank):
        '''
        获取指令实时调整坦克位置
        :return:
        '''
        if instruction in self.INSTRUCTION:
            if instruction == 'T':
                time.sleep(1)
                print('指令:[%s]' % instruction, '正在时间同步')
            elif instruction == 'L':
                tank.direction -= 1
                tank.direction = (tank.direction) % len(DIRECTION)
                print('指令:[%s]' % instruction, '坦克向左转')
            elif instruction == 'R':
                tank.direction += 1
                tank.direction = (tank.direction) % len(DIRECTION)
                print('指令:[%s]' % instruction, '坦克向右转')
            elif instruction == 'P':
                tank.direction -= 2
                tank.direction = (tank.direction) % len(DIRECTION)
                print('指令:[%s]' % instruction, '坦克向后转')
            elif instruction == 'M':
                tank.move()
                print('指令:[%s]' % instruction, tank.now())
            else:
                print('非指令')
        else:
            print('非指令')
        return tank


if __name__ == '__main__':
    instructions = 'MTMPRPMTMLMRPRMTPLMMTLMRRMP'
    tank = Tank(direction=get_direction_index('W'), start_x=11, start_y=39)
    dispatch = Dispatch()
    print('''
    ---- 初始化坦克数据 -----
    坦克id:{}, 正在向【{}】方向行驶，当前坐标({})
    ---- 初始化完成开始追踪 -----
    '''.format(id(tank), DIRECTION[tank.direction], 'x:%d,y:%s' % (tank.x, tank.y)))
    for instruction in instructions:
        dispatch.deal_instruction(instruction, tank)

    print('''
        ---- 发射榴弹 -----
        坦克id:{}, 正在向【{}】方向行驶，当前坐标({})
        ---- 目标已击毁 -----
        '''.format(id(tank), DIRECTION[tank.direction], 'x:%d,y:%s' % (tank.x, tank.y)))
