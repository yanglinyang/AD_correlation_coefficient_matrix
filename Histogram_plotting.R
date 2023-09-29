
# 安装openxlsx包
install.packages("openxlsx")

# 加载openxlsx包
library(openxlsx)
library(read)
install.packages("gplots")
install.packages("readxl")
# 读入数据
data <- read_xlsx("D:/rwork/AD病标准化数据.xlsx",9)
data2 = read_xlsx('D:/rwork/GPL96基因对照表.xlsx')
id = data[,1]
d1 = data$`inc-con`
d2 = data$`mod-con`
d3 = data$`sev-con`

ids = data2$ID
gen_name = data2$NAME
# 绘制直方图，并自定义外观
extra_1 = id[which(abs(d1)>2*sd(d1)),]
extra_2 = id[which(abs(d2)>2*sd(d2)),]
extra_3 = id[which(abs(d3)>2*sd(d3)),]
m1 = intersect(extra_2$gens,extra_3$gens)
m2 = intersect(extra_1$gens,m1)

for (i in 1:length(m2)) {
  print(i)
  for (j in 1:19813) {
    if (m2[i] == data2[j,1]){
      a <- data2[j,]
    }
  }
  if(i == 1){
    all <- a
  }
  else{
    all<-rbind(all,a)
  }
}
write.xlsx(all,'D:/rwork/Spea_extra_gens.xlsx')
# 绘制直方图
hist(d1,
     main = "Incipient-Control",     # 图的标题
     xlab = "",              # x轴标签
     ylab = "",           # y轴标签
     col = "steelblue",            # 柱子的颜色
     border = "white",             # 柱子边框颜色
     breaks = "Sturges"            # 使用Sturges公式选择分组数量（柱子的个数）
)
hist(d2,
     main = "Moderate-Control",     # 图的标题
     xlab = "",              # x轴标签
     ylab = "",           # y轴标签
     col = "steelblue",            # 柱子的颜色
     border = "white",             # 柱子边框颜色
     breaks = "Sturges"            # 使用Sturges公式选择分组数量（柱子的个数）
)
hist(d3,
     main = "Severe-Control",     # 图的标题
     xlab = "",              # x轴标签
     ylab = "",           # y轴标签
     col = "steelblue",            # 柱子的颜色
     border = "white",             # 柱子边框颜色
     breaks = "Sturges"            # 使用Sturges公式选择分组数量（柱子的个数）
)

