import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rcParams

path1 = '0.1_256_acc.csv'
path2 = '0.3_256_acc.csv'
path3 = '0.5_256_dt_acc.csv'
path4 = '0.7_256_acc.csv'
path5 = '0.9_256_acc.csv'

data1 = np.array(pd.read_csv(path1,header=0,sep=','))
data2 = np.array(pd.read_csv(path2,header=0,sep=','))
data3 = np.array(pd.read_csv(path3,header=0,sep=','))
data4 = np.array(pd.read_csv(path4,header=0,sep=','))
data5 = np.array(pd.read_csv(path5,header=0,sep=','))

x = np.arange(1,len(data1)+1)
colors = ['r','g','b','m','y']


# 设置中文字体支持（如果需要显示中文）
plt.rcParams["font.family"] = ["Times New Roman", "SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
# 设置全局字体为Times New Roman
rcParams['font.serif'] = ['Times New Roman']
rcParams['font.family'] = 'serif'

# 全局设置字体大小
rcParams['font.size'] = 10  # 基础字体大小
rcParams['axes.titlesize'] = 8  # 子图标题大小
rcParams['axes.labelsize'] = 10  # 坐标轴标签大小
rcParams['legend.fontsize'] = 8  # 图例大小
rcParams['xtick.labelsize'] = 8  # x轴刻度字体大小
rcParams['ytick.labelsize'] = 8  # y轴刻度字体大小

# 创建大图，宽度7英寸，高度按比例设置
fig, axes = plt.subplots(2, 3, figsize=(7, 4.2))  # 2行3列共6个子图

# 全局设置子图之间的距离和留白
plt.subplots_adjust(
    left=0.05,  # 左边留白
    right=0.98,  # 右边留白
    bottom=0.05,  # 底部留白
    top=0.9,  # 顶部留白
    wspace=0.2,  # 子图之间的水平距离
    hspace=0.25  # 子图之间的垂直距离
)

#acc
axes[0,0].plot(x,data1[:,1], label= r'$\tau=0.1$',color=colors[0], linewidth=0.5)
axes[0,0].plot(x,data2[:,1], label= r'$\tau=0.3$',color=colors[1], linewidth=0.5)
# axes[0,0].plot(x,data3[:,1], label= r'$\tau=0.5$',color=colors[2], linewidth=0.5)
axes[0,0].plot(x,data4[:,1], label= r'$\tau=0.7$',color=colors[3], linewidth=0.5)
axes[0,0].plot(x,data5[:,1], label= r'$\tau=0.9$',color=colors[4], linewidth=0.5)
axes[0,0].legend()
axes[0,0].set_ylim([60,90])
axes[0,0].set_title('(a) Acc')



#loss
axes[1,0].plot(x,data1[:,3], label= r'$\tau=0.1$',color=colors[0], linewidth=0.5)
axes[1,0].plot(x,data2[:,3], label= r'$\tau=0.3$',color=colors[1], linewidth=0.5)
# axes[1,0].plot(x,data3[:,3], label= r'$\tau=0.5$',color=colors[2], linewidth=0.5)
axes[1,0].plot(x,data4[:,3], label= r'$\tau=0.7$',color=colors[3], linewidth=0.5)
axes[1,0].plot(x,data5[:,3], label= r'$\tau=0.9$',color=colors[4], linewidth=0.5)
axes[1,0].legend()
# axes[1,0].set_ylim([5,0.5])
axes[1,0].set_title('(d) Loss value')


#pos mean
axes[0,1].plot(x,data1[:,4], label= r'$\tau=0.1$',color=colors[0], linewidth=0.5)
axes[0,1].plot(x,data2[:,4], label= r'$\tau=0.3$',color=colors[1], linewidth=0.5)
# axes[0,1].plot(x,data3[:,4], label= r'$\tau=0.5$',color=colors[2], linewidth=0.5)
axes[0,1].plot(x,data4[:,4], label= r'$\tau=0.7$',color=colors[3], linewidth=0.5)
axes[0,1].plot(x,data5[:,4], label= r'$\tau=0.9$',color=colors[4], linewidth=0.5)
axes[0,1].legend()
axes[0,1].set_ylim([0.6,0.9])
axes[0,1].set_title('(b) Pos Mean')

#neg mean
axes[0,2].plot(x,data1[:,6], label= r'$\tau=0.1$',color=colors[0], linewidth=0.5)
axes[0,2].plot(x,data2[:,6], label= r'$\tau=0.3$',color=colors[1], linewidth=0.5)
# axes[0,2].plot(x,data3[:,6], label= r'$\tau=0.5$',color=colors[2], linewidth=0.5)
axes[0,2].plot(x,data4[:,6], label= r'$\tau=0.7$',color=colors[3], linewidth=0.5)
axes[0,2].plot(x,data5[:,6], label= r'$\tau=0.9$',color=colors[4], linewidth=0.5)
axes[0,2].legend()
# axes[0,2].set_ylim([-0.0035,-0.002])
axes[0,2].set_ylim([-0.005,0.005])
axes[0,2].set_title('(c) Neg Mean')


#pos var
axes[1,1].plot(x,data1[:,5], label= r'$\tau=0.1$',color=colors[0], linewidth=0.5)
axes[1,1].plot(x,data2[:,5], label= r'$\tau=0.3$',color=colors[1], linewidth=0.5)
# axes[1,1].plot(x,data3[:,5], label= r'$\tau=0.5$',color=colors[2], linewidth=0.5)
axes[1,1].plot(x,data4[:,5], label= r'$\tau=0.7$',color=colors[3], linewidth=0.5)
axes[1,1].plot(x,data5[:,5], label= r'$\tau=0.9$',color=colors[4], linewidth=0.5)
axes[1,1].legend()
axes[1,1].set_ylim([0.01,0.10])
axes[1,1].set_title('(e) Pos Var')

#neg Var
axes[1,2].plot(x,data1[:,7], label= r'$\tau=0.1$',color=colors[0], linewidth=0.5)
axes[1,2].plot(x,data2[:,7], label= r'$\tau=0.3$',color=colors[1], linewidth=0.5)
# axes[1,2].plot(x,data3[:,7], label= r'$\tau=0.5$',color=colors[2], linewidth=0.5)
axes[1,2].plot(x,data4[:,7], label= r'$\tau=0.7$',color=colors[3], linewidth=0.5)
axes[1,2].plot(x,data5[:,7], label= r'$\tau=0.9$',color=colors[4], linewidth=0.5)
axes[1,2].legend()
axes[1,2].set_ylim([0,0.2])
axes[1,2].set_title('(f) Neg Var')

plt.savefig('1.png', dpi=600, bbox_inches='tight')
plt.show()
