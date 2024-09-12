# 导入线程模块
import threading

# 导入时间模块
import time

# 定义任务1函数
def task1():
    for i in range(10):
        print("任务1：正在执行第{}次".format(i+1))
        time.sleep(1)

    print("任务1：执行完毕")

# 定义任务2函数
def task2():
    for i in range(10):
        print("任务2：正在执行第{}次".format(i+1))
        time.sleep(1)

    print("任务2：执行完毕")


# 主函数
if __name__ == '__main__':
    # 创建线程对象
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    # 启动线程
    t1.start()
    t2.start()

    # 等待线程结束
    t1.join()
    t2.join()

    # 输出结果
    print("主线程结束")