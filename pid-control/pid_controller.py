from robot import Robot, show
import numpy as np


def run(robot, k_p, k_d, k_i, n=100, speed=1.0):
    """
    运行多次运动并记录轨迹
    :param robot:   小车
    :param k_p:     p系数
    :param k_d:     d系数
    :param n:       循环次数
    :param speed:   小车速度
    """
    x_trajectory = []
    y_trajectory = []
    p_arr = []  # 记录每一次的p
    d_arr = []  # 记录每一次的d
    i_arr = []  # 记录每一次的i

    prev_cte = 0 - robot.y
    sum_cte = 0
    for i in range(n):
        # ---------------------------- start
        cte = 0 - robot.y
        p = k_p * cte               # p

        d = k_d * (cte - prev_cte)  # d
        prev_cte = cte

        sum_cte += cte
        i = k_i * sum_cte           # i

        steer = p + d + i           # sum

        p_arr.append(p)
        d_arr.append(d)
        i_arr.append(i)
        # ---------------------------- end

        robot.move(steer, speed)

        x_trajectory.append(robot.x)
        y_trajectory.append(robot.y)
        print(robot)
    return x_trajectory, y_trajectory, p_arr, d_arr, i_arr


if __name__ == '__main__':
    robot = Robot()
    # 初始位置 x=0, y=-1, orient=0
    robot.set(0, -1, 0)
    robot.set_steering_drift(5. / 180. * np.pi)  # 10 degrees of steer drift

    # 运行并收集所有的x，y，以及 p值
    x_trajectory, y_trajectory, p_arr, d_arr, i_arr = run(robot, k_p=0.2, k_d=0.0, k_i=0.0)
    # 可视化运行结果
    show(x_trajectory, y_trajectory, p_array=p_arr, d_array=d_arr, i_array=i_arr, label = 'P')
    # 重置小车位置
    robot.reset()

    # 运行并收集所有的x，y，以及 p值
    x_trajectory, y_trajectory, p_arr, d_arr, i_arr = run(robot, k_p=0.2, k_d=3.0, k_i=0.0)
    # 可视化运行结果
    show(x_trajectory, y_trajectory, p_array=p_arr, d_array=d_arr, i_array=i_arr, label = 'PD')
    # 重置小车位置
    robot.reset()

    # 运行并收集所有的x，y，以及 p值
    x_trajectory, y_trajectory, p_arr, d_arr, i_arr = run(robot, k_p=0.2, k_d=3.0, k_i=0.005)
    # 可视化运行结果
    show(x_trajectory, y_trajectory, p_array=p_arr, d_array=d_arr, i_array=i_arr, label = 'PID')