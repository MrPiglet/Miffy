import jieba
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

f = open('JD.txt', 'r', encoding='utf-8')
text = f.read()
font = r'C:\Windows\Fonts\STZHONGS.TTF'
cut = ''.join(jieba.cut(text))
img = Image.open('itachi.jpg')
background_image = np.array(img)
stopword = []
print('加载图片成功！')
wc = WordCloud(
	background_color = 'white', #PIG 背景颜色
	width = 1000,
	height = 800,
	mask = background_image, #PIG 背景图片
	font_path = font, #PIG 中文一定要设置字体，不然会出现方框 
	max_font_size = 150, #PIG 设置字体最大值
	random_state = 30, #PIG 有多少种随机生成方案，即多少种配色
	stopwords = stopword #PIG 设置停用词
	)

wc.generate_from_text(text)
print('开始加载文本！')
#PIG 改变字体颜色
#img_colors = ImageColorGenerator(background_image)
#PIG 字体颜色为背景图片的颜色
#wc.recolor(color_func=img_colors)

#PIG 显示词云图
plt.imshow(wc)
#PIG 是否显示x轴，y轴下表
plt.axis('off')
plt.show()

wc.to_file('new.png')

