import matplotlib.pyplot as plt
import numpy as np

# data = np.arange(10)
# plt.plot(data)
# plt.show()

# fig = plt.figure()
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# plt.plot(np.random.randn(50).cumsum(), 'k--')   # plot表示绘制的是折线图
# ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3) # hist表示绘制的是直方图
# ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30)) # scatter表示绘制的是散点图
# plt.show()

# fig, axes = plt.subplots(2, 3)
# plt.show()

# 隐式创建 => 前方无图，但是此时又得在有图的条件下才能使用，才会偷偷创建
# 显式创建 => plt.figure() => 创建一个空白的图
#            plt.subplots() => 创建一个空白的图，并且创建子图
#            fig, ax = plt.subplots() => 创建一个空白的图，并且创建一个子图

# 共享x轴和y轴
# 参数顺序决定了最好写上xx=yy
# fig, axes = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(8, 6))
# plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9, wspace=0, hspace=0)   # 调整间距，matplotlib不会检查标签是否重叠
# plt.show()

# fig = plt.figure()
# x = [1, 2, 3, 4]
# y = [1, 2, 3, 4]
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(x, y, 'bo--')   # o表示粗点标记
# plt.show()

# 自动挡 / 手动挡
# 只涉及一张图可以直接把工作全部交给plt(本质还是先figure再add_subplot)
# data = np.random.randn(30).cumsum()
# plt.plot(data, 'k--', label='Default')
# plt.plot(data, 'k-', drawstyle='steps-post', label='steps-post')
# plt.legend(loc='best')      # 显示标签，best表示显示到不挡标签的最佳位置
# plt.show()

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(np.random.randn(1000).cumsum(), 'ko-')
# ticks = ax.set_xticks([0, 250, 500, 750, 1000])    # => 没写label才显示，本质决定的是label的位置
# # rotation表示标签旋转30度，fontsize表示字体为小
# labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='small')
# ax.set_title('My first matplotlib plot')
# ax.set_xlabel('Stages')
# plt.legend(loc='best')
# plt.show()