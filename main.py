# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。

# 访问 https:#www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助


"""
from tkinter import *



def run1():
    a = float(inp1.get())
    b = float(inp2.get())
    s = '%0.2f+%0.2f=%0.2f\n' % (a, b, a + b)
    txt.insert(END, s)  # 追加显示运算结果
    inp1.delete(0, END)  # 清空输入
    inp2.delete(0, END)  # 清空输入


def run2(x, y):
    a = float(x)
    b = float(y)
    s = '%0.2f+%0.2f=%0.2f\n' % (a, b, a + b)
    txt.insert(END, s)  # 追加显示运算结果
    inp1.delete(0, END)  # 清空输入
    inp2.delete(0, END)  # 清空输入


root = Tk()
root.geometry('460x240')
root.title('simple calc')

lb1 = Label(root, text='input two nums')
lb1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
inp1 = Entry(root)
inp1.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.1)
inp2 = Entry(root)
inp2.place(relx=0.6, rely=0.2, relwidth=0.3, relheight=0.1)

# 方法-直接调用 run1()
btn1 = Button(root, text='方法一', command=run1)
btn1.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.1)

# 方法二利用 lambda 传参数调用run2()
btn2 = Button(root, text='方法二', command=lambda: run2(inp1.get(), inp2.get()))
btn2.place(relx=0.6, rely=0.4, relwidth=0.3, relheight=0.1)

# 在窗体垂直自上而下位置60%处起，布局相对窗体高度40%高的文本框
txt = Text(root)
txt.place(rely=0.6, relheight=0.4)

root.mainloop()

"""
import random

"""
import tkinter

root = tkinter.Tk()  # 声明窗体
root.title("Wumpus World")
root.geometry("400x400+200+200")
LabelRed = tkinter.Label(root, text="Wumpus", fg="Red", relief="groove")
LabelRed.pack()

root.mainloop()
"""

"""
# tkinter实现菜单功能
from tkinter import *
from PIL import Image, ImageTk


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("第一个窗体")

        self.pack(fill=BOTH, expand=1)

        # 实例化一个Menu对象，这个在主窗体添加一个菜单
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # 创建File菜单，下面有Save和Exit两个子菜单
        file = Menu(menu)
        file.add_command(label='Save')
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        # 创建Edit菜单，下面有一个Undo菜单
        edit = Menu(menu)
        edit.add_command(label='Undo')
        edit.add_command(label='Show  Image', command=self.showImg)
        edit.add_command(label='Show  Text', command=self.showTxt)
        menu.add_cascade(label='Edit', menu=edit)

    def client_exit(self):
        exit()

    def showImg(self):
        load = Image.open('pic.jpg')  # 我图片放桌面上
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def showTxt(self):
        text = Label(self, text='GUI')
        text.pack()


root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()
"""
"""
QList<QLabel *> map_label    # 地图
    QLabel *score_get            # 分数显示
    QLabel *state                # 当前状态
int real_world[ROW_NUM][COL_NUM]	# 真实世界
    int agent_world[ROW_NUM][COL_NUM]	# 代理世界

    Point cave_position[CAVE_NUM]		# 陷阱坐标
    Point wumpus_position[WUMPUS_NUM]	# 怪兽坐标
    Point gold_position[GOLD_NUM]		# 金子坐标

    Point path_record[100]			# 路径记录
    Point start	# 起始点坐标

    bool find_gold	# 是否找到金子
    bool game_over	# 是否游戏结束
    int score		# 当前分数
    int step_cnt   # 步数
"""

import queue

ROW_NUM = 4  # 行数
COL_NUM = 4  # 列数
GOLD_NUM = 1  # 金子数
CAVE_NUM = 3  # 陷阱数
WUMPUS_NUM = 1  # 怪兽数
FLAG_NUM = 12  # 标记向量的比特位数量
CUR = 1  # 当前点
SAFE = 2  # 安全
VISITED = 4  # 已访问
GLITTER = 8  # 发光
STENCH = 16  # 臭气
BREEZE = 32  # 微风
GOLD_SUSPECT = 64  # 怀疑有金子
CAVE_SUSPECT = 128  # 怀疑有陷阱
WUMPUS_SUSPECT = 256  # 怀疑有怪兽
GOLD = 512  # 金子
CAVE = 1024  # 陷阱
WUMPUS = 2048  # 怪兽
GOLD_VALUE = 1000  # 金子价值
SHOOT_WUMPUS_COST = 10  # 怪兽消耗
DEATH_COST = 1000  # 死亡消耗
STEP_COST = 1  # 行动消耗
start = (0, 0)
real_world = [[0 for i in range(COL_NUM)] for j in range(ROW_NUM)]
agent_world = [[0 for k in range(COL_NUM)] for l in range(ROW_NUM)]
cave_position = [(0, 0) for j in range(CAVE_NUM)]
wumpus_position = [(0, 0) for j in range(WUMPUS_NUM)]
gold_position = [(0, 0) for j in range(GOLD_NUM)]


def find(x, y, un):
    if len(un) == 0:
        return False
    for i, j in un:
        if x == i and y == j:
            return True
    return False


def rand_point(l, r, un):
    x = 0
    y = 0
    while find(x, y, un):
        x = random.randint(l[0], r[0])
        y = random.randint(l[1], r[1])
    return x, y


def put_flag(world, pos, f):
    # 如果已访问则其他的传感器标志置零
    if pos[0] < 0 or pos[0] >= ROW_NUM or pos[1] < 0 or pos[1] >= COL_NUM:
        return
    if f == VISITED:
        world[pos[0]][pos[1]] &= ~SAFE
        world[pos[0]][pos[1]] &= ~CAVE_SUSPECT
        world[pos[0]][pos[1]] &= ~GOLD_SUSPECT
        world[pos[0]][pos[1]] &= ~WUMPUS_SUSPECT
    world[pos[0]][pos[1]] |= f  # 放标记


def get_neighbor_position(pos, neighbor):
    next = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for i in {0, 1, 2, 3}:
        next_x = pos[0] + next[i][0]  # 邻居点x坐标
        next_y = pos[1] + next[i][1]  # 邻居点y坐标
        if 0 <= next_x < ROW_NUM and 0 <= next_y < COL_NUM:  # 边界检查
            neighbor.append((next_x, next_y))


def init():
    unacceptable = []
    unacceptable.append(start)
    left = (1, 1)
    right = (ROW_NUM - 1, COL_NUM - 1)  # 边界点
    find_gold = False
    game_over = False
    step_cnt = 0
    for i in range(ROW_NUM):
        for j in range(COL_NUM):
            real_world[i][j] = 0
            agent_world[i][j] = 0
    # 生成陷阱位置
    for i in range(CAVE_NUM):
        cave_position[i] = rand_point(left, right, unacceptable)
        unacceptable.append(cave_position[i])
    # 生成怪兽位置
    for i in range(WUMPUS_NUM):
        wumpus_position[i] = rand_point(left, right, unacceptable)
        unacceptable.append(wumpus_position[i])
    # 生成金子位置
    for i in range(GOLD_NUM):
        gold_position[i] = rand_point(left, right, unacceptable)
        unacceptable.append(gold_position[i])

    neighbor = []  # 当前点的邻居坐标
    # 生成世界
    for i in range(ROW_NUM):
        for j in range(COL_NUM):
            # 陷阱检查
            for k in range(CAVE_NUM):
                if (i, j) == cave_position[k]:
                    put_flag(real_world, cave_position[k], CAVE)  # 放陷阱
                    get_neighbor_position(cave_position[k], neighbor)  # 获取邻居坐标
                    while len(neighbor) != 0:  # 陷阱的邻居点都打上微风标记
                        put_flag(real_world, neighbor[len(neighbor) - 1], BREEZE)
                        neighbor.pop()

            # 怪兽检查
            for k in range(WUMPUS_NUM):
                if i == wumpus_position[k][0] and j == wumpus_position[k][1]:
                    put_flag(real_world, wumpus_position[k], WUMPUS)  # 放怪兽
                    get_neighbor_position(wumpus_position[k], neighbor)  # 获取邻居坐标
                    while len(neighbor) != 0:  # 怪兽的邻居点都打上臭气标记
                        put_flag(real_world, neighbor[len(neighbor) - 1], STENCH)
                        neighbor.pop()
            # 金子检查
            for k in range(GOLD_NUM):
                if i == gold_position[k][0] and j == gold_position[k][1]:
                    put_flag(real_world, gold_position[k], GOLD)  # 放金子
                    # get_neighbor_position(gold_position[k], neighbor)  # 获取邻居坐标
                    # while len(neighbor) != 0:
                    put_flag(real_world, gold_position[k], GLITTER)
                    #    neighbor.pop()
    # 界面
    for i in range(CAVE_NUM):
        print("#%d cave cord: (%d, %d)" % (i, cave_position[i][0], cave_position[i][1]))
    for i in range(WUMPUS_NUM):
        print("#%d wumpus cord: (%d, %d)" % (i, wumpus_position[i][0], wumpus_position[i][1]))
    for i in range(GOLD_NUM):
        print("#%d gold cord: (%d, %d)" % (i, gold_position[i][0], gold_position[i][1]))

    # 显示世界
    for i in range(ROW_NUM):
        for j in range(COL_NUM):
            if real_world[i][j] & CAVE == CAVE:
                print("C", end=' ')
            elif real_world[i][j] & WUMPUS == WUMPUS:
                print("W", end=' ')
            elif real_world[i][j] & GOLD == GOLD:
                print("G", end=' ')
            else:
                print("O", end=' ')
        print('')


"""
    #图形界面
    int w = 140, h = 140, px = 0, py = 0
    for(int i = 0 i < ROW_NUM ++ i){
        for(int j = 0 j < COL_NUM ++ j){
            QLabel *label = new QLabel(this)
            map_label.push_back(label)
            px = i * w + 30, py = j * h + 30
            label->setGeometry(px, py, w, h)   # 设置坐标和大小
            if ((real_world[i][j] & CAVE) == CAVE) label->setStyleSheet("border-image:url(:/cave.png)")
            else if ((real_world[i][j] & WUMPUS) == WUMPUS) label->setStyleSheet("border-image:url(:/monster.png)")
            else if ((real_world[i][j] & GOLD) == GOLD) label->setStyleSheet("border-image:url(:/gold.png)")
            else label->setStyleSheet("border-image:url(:/grid.png)")
        }
    }
    map_label[0]->setStyleSheet("border-image:url(:/agent.png)")
    # 开始按钮
    QPushButton *startBut = new QPushButton(this)
    startBut->setGeometry(650, 30, 210, 70)
    startBut->setStyleSheet("border-image:url(:/start.png)")
    connect(startBut, SIGNAL(clicked(bool)), this, SLOT(ButtonClick()))#为每个按钮添加响应函数

    # 分数标签
    QLabel *score_label = new QLabel(this)
    score_label->setGeometry(startBut->pos().x(), startBut->pos().y() + 70, 210, 60)
    score_label->setStyleSheet("border-image:url(:/score.png)")

    # 分数
    score_get = new QLabel(this)
    score_get->setGeometry(score_label->pos().x(), score_label->pos().y() + 50, 210, 60)
    score_get->setStyleSheet("qproperty-alignment: 'AlignVCenter|AlignHCenter'font-size:50pxcolor:rgb(31, 93, 173)font-family:黑体")
    score_get->setText("0")

    # 当前状态
    QLabel *state_text = new QLabel(this)
    state_text->setGeometry(score_get->pos().x(), score_get->pos().y() + 70, 210, 60)
    state_text->setStyleSheet("border-image:url(:/state.png)")

    state = new QLabel(this)
    state->setGeometry(state_text->pos().x(), state_text->pos().y() + 50, 210, 50)
    state->setStyleSheet("border-image:url(:/waiting.png)")
}
CreatWorld()
"""


def upd_neighbor_info(cur):
    neighbors = []
    get_neighbor_position(cur, neighbors)
    cur_x = cur[0]
    cur_y = cur[1]
    for i in range(len(neighbors)):
        nx = neighbors[i][0]
        ny = neighbors[i][1]
        if (agent_world[nx][ny] & SAFE) == 0 and (agent_world[nx][ny] & VISITED) == 0:  # 不安全且未被访问
            if (agent_world[cur_x][cur_y] & BREEZE) == BREEZE:  # 有微风
                if (agent_world[nx][ny] & CAVE_SUSPECT) == CAVE_SUSPECT:
                    put_flag(agent_world, neighbors[i], CAVE)
                else:
                    put_flag(agent_world, neighbors[i], CAVE_SUSPECT)
            if (agent_world[cur_x][cur_y] & STENCH) == STENCH:  # 有臭气
                if (agent_world[nx][ny] & WUMPUS_SUSPECT) == WUMPUS_SUSPECT:
                    put_flag(agent_world, neighbors[i], WUMPUS)
                else:
                    put_flag(agent_world, neighbors[i], WUMPUS_SUSPECT)
            if (agent_world[cur_x][cur_y] & GLITTER) == GLITTER:  # 有闪光
                if (agent_world[nx][ny] & GOLD_SUSPECT) == GOLD_SUSPECT:
                    put_flag(agent_world, neighbors[i], GOLD)
                else:
                    put_flag(agent_world, neighbors[i], GOLD_SUSPECT)

            if ((agent_world[cur_x][cur_y] & BREEZE) == 0) and (
                    (agent_world[cur_x][cur_y] & STENCH) == 0):  # 没有微风和臭气则安全
                put_flag(agent_world, neighbors[i], SAFE)
                # 删除其他非必要标记
                agent_world[nx][ny] &= ~CAVE_SUSPECT
                agent_world[nx][ny] &= ~WUMPUS_SUSPECT
                agent_world[nx][ny] &= ~CAVE
                agent_world[nx][ny] &= ~WUMPUS


step_cnt = 0
find_gold = False
game_over = False
path_record = []


def dfs(cur):
    global find_gold
    global game_over
    global step_cnt
    neighbors = []
    path_record.append(cur)
    step_cnt += 1
    # path_record[step_cnt++] = cur

    agent_world[cur[0]][cur[1]] |= real_world[cur[0]][cur[1]]  # 获取当前点信息
    if (agent_world[cur[0]][cur[1]] & GOLD) == GOLD:  # 如果遇到了金子
        find_gold = True
        return
    if (agent_world[cur[0]][cur[1]] & CAVE) == CAVE:  # 掉进了洞穴
        game_over = True
        return
    put_flag(agent_world, cur, VISITED)  # 当前点已访问
    upd_neighbor_info(cur)  # 更新周围点的信息
    agent_world[cur[0]][cur[1]] &= ~CUR  # 不在当前点

    next = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 上，下，左，右
    for i, j in next:
        next_x = cur[0] + i  # 邻居点x坐标
        next_y = cur[1] + j  # 邻居点y坐标
        if 0 <= next_x < ROW_NUM and 0 <= next_y < COL_NUM:  # 边界检查
            neighbors.append((next_x, next_y))
    for i, j in neighbors:  # 周围可能有金子
        if (agent_world[i][j] & GOLD) == GOLD:
            put_flag(agent_world, neighbors[i], cur)
            dfs((i, j))  # 下一步
            if find_gold or game_over:
                return
    # 周围没有金子
    if not find_gold:
        safe_place = []
        for i, j in neighbors:
            if (agent_world[i][j] & SAFE) == SAFE and (agent_world[i][j] & VISITED) == 0:  # 安全 未访问
                safe_place.append((i, j))
        if len(safe_place) > 0:  # 存在安全区域
            rand_next_pos = random.randint(0, len(safe_place) - 1)  # 随机选择一个安全区域
            put_flag(agent_world, safe_place[rand_next_pos], CUR)

            dfs(safe_place[rand_next_pos])  # 下一步
            if find_gold or game_over:
                return
        else:  # 没有安全区域，寻找最近的安全地带
            nearest_safe_pos = (-1, -1)  # 最近的安全点初始化
            for i in range(ROW_NUM):
                for j in range(COL_NUM):
                    if (agent_world[i][j] & SAFE) == SAFE:
                        if nearest_safe_pos == (-1, -1):  # 第一个安全的点
                            nearest_safe_pos = (i, j)
                        else:
                            dismin = bfs(cur, nearest_safe_pos, False)  # 最近安全点距离
                            discur = bfs(cur, (i, j), False)  # 当前安全点距离
                            if discur < dismin:  # 当前安全点更近
                                nearest_safe_pos = (i, j)  # 更新最近安全点
            # 智能体地图上有安全点
            if nearest_safe_pos != (-1, -1):
                put_flag(agent_world, nearest_safe_pos, CUR)
                bfs(cur, nearest_safe_pos, True)  # 记录行动路线
                dfs(nearest_safe_pos)  # 下一步
                if find_gold or game_over:
                    return
            else:  # 没有安全点，选择一个相对安全的地点
                good_neighbor = []
                for i, j in neighbors:
                    if ((agent_world[i][j] & VISITED) == 0) and ((agent_world[i][j] & CAVE) == 0) and \
                            ((agent_world[i][j] & WUMPUS) == 0):  # 未被访问 没有陷阱 没有怪兽
                        good_neighbor.append((i, j))
                if len(good_neighbor) > 0:  # 有相对安全的点
                    rand_next_good_pos = random.randint(0, len(good_neighbor) - 1)  # 随机选取一个相对安全的点

                    dfs(good_neighbor[rand_next_good_pos])  # 下一步
                    if find_gold or game_over:
                        return
                else:  # 没有相对安全的点，选择杀死怪兽
                    kill_pos = []
                    cave_pos = []
                    for i, j in neighbors:
                        if (agent_world[i][j] & VISITED) == 0:  # 未被访问过
                            if (agent_world[i][j] & WUMPUS) == WUMPUS:  # 是怪兽
                                kill_pos.append((i, j))
                            else:
                                cave_pos.append((i, j))
                    if len(kill_pos) > 0:  # 存在怪兽则杀死怪兽
                        kill_wumpus = random.randint(0, len(kill_pos) - 1)
                        wumpus_neighbors = []
                        get_neighbor_position(kill_pos[kill_wumpus], wumpus_neighbors)
                        agent_world[kill_pos[kill_wumpus][0]][kill_pos[kill_wumpus][1]] &= ~WUMPUS  # 取消怪兽标记
                        # 将杀死的怪兽周围的臭气标记取消
                        for i, j in wumpus_neighbors:
                            agent_world[i][j] &= ~STENCH
                        put_flag(agent_world, kill_pos[kill_wumpus], cur)
                        dfs(kill_pos[kill_wumpus])  # 下一步
                        if find_gold or game_over:
                            return
                    elif len(cave_pos) > 0:  # 没有怪兽只有陷阱
                        jump_cave = random.randint(0, len(cave_pos) - 1)
                        put_flag(agent_world, cave_pos[jump_cave], CUR)
                        dfs(cave_pos[jump_cave])


# src, dest:point, record:sbool
def bfs(src, dest, record):
    next = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 上，下，左，右
    steps = 0
    bfs_path = {}
    flag = False
    if (agent_world[dest[0]][dest[1]] & VISITED) == 0:
        agent_world[dest[0]][dest[1]] |= VISITED
        flag = True

    Q = queue.Queue()
    Q.put(src)
    vis = [[False for i in range(COL_NUM)] for j in range(ROW_NUM)]  # 遍历标记
    vis[src[0]][src[1]] = True
    while not Q.empty():
        cur = Q.get()
        steps += 1
        if cur == dest:
            break
        for i, j in next:
            nx = cur[0] + i  # 下一个点的坐标
            ny = cur[1] + j
            if 0 <= nx < ROW_NUM and 0 <= ny < COL_NUM and ((agent_world[nx][ny] & VISITED) == VISITED) and not vis[nx][ny]:
                if record:  # 需要记录路径
                    bfs_path[(nx, ny)] = cur
                vis[nx][ny] = True
                Q.put((nx, ny))
    if record:  # 需要记录则根据搜索路径找到搜索结果
        get_bfs_path(dest, src, dest, bfs_path)

    if flag:
        agent_world[dest[0]][dest[1]] &= ~VISITED  # 取消访问标记
    return steps  # 返回最短路径长度


import sys

sys.setrecursionlimit(100000)


def get_bfs_path(cur, beg_pos, tar, bfs_path):
    global step_cnt
    if cur == beg_pos:
        return
    get_bfs_path(bfs_path.get(cur), beg_pos, tar, bfs_path)
    if cur != tar:
        path_record.append(cur)
        step_cnt += 1


def show_path():
    global step_cnt
    dfs(start)
    score = 0
    if find_gold:
        bfs(gold_position[0], start, True)
        path_record.append(start)
        step_cnt += 1
    for i in range(step_cnt):
        pos_index = path_record[i][0] * ROW_NUM + path_record[i][1]
        # map_label[pos_index]->setStyleSheet("border-image:url(:/agent.png)")
        # QTest::qWait(400)
        if (real_world[path_record[i][0]][path_record[i][1]] & CAVE) == CAVE:  # 当前点是陷阱
            # map_label[pos_index]->setStyleSheet("border-image:url(:/deathagent.png)")
            pass
        if i != step_cnt - 1:
            # map_label[pos_index]->setStyleSheet("border-image:url(:/grid.png)")
            score -= STEP_COST
            print("- STEP_COST ", STEP_COST, end=' ')
            if path_record[i + 1] == start:  # 下个点是起点
                # state->setStyleSheet("border-image:url(:/back.png)")
                pass
            elif (real_world[path_record[i + 1][0]][path_record[i + 1][1]] & WUMPUS) == WUMPUS:  # 下一个点是怪兽
                score -= SHOOT_WUMPUS_COST
                print("- SHOOT_WUMPUS_COST ", SHOOT_WUMPUS_COST, end=' ')
                real_world[path_record[i + 1][0]][path_record[i + 1][1]] &= ~WUMPUS
                # state->setStyleSheet("border-image:url(:/kill.png)")
            elif (real_world[path_record[i + 1][0]][path_record[i + 1][1]] & GOLD) == GOLD:  # 下一个点是金子
                score += GOLD_VALUE
                print("+ GOLD_VALUE ", GOLD_VALUE, end=' ')
                # state->setStyleSheet("border-image:url(:/findgold.png)")
            elif (real_world[path_record[i + 1][0]][path_record[i + 1][1]] & CAVE) == CAVE:  # 下一个点是陷阱
                score -= DEATH_COST
                print("- DEATH_COST ", DEATH_COST, end=' ')
                # state->setStyleSheet("border-image:url(:/death.png)")
            else:
                # state->setStyleSheet("border-image:url(:/move.png)")
                pass
            # score_get->setText(QString::number(score))
            print("score:", score)
        print("(%d, %d)\t" % (path_record[i][0], path_record[i][1]))


init()
show_path()
