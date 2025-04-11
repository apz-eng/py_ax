# py_ax v2.3.1

import jieba
import wordcloud as wordc
import matplotlib.pyplot as plt

def worldcloud_plt(text, map_width = 5, map_height = 5, save_png = False, output_file = "wordcloud", width = 800, height = 400): # 绘制matplotlib词云图
    # 检查输入文本是否为空，如果为空则直接返回0
    if text == " ":
        return 0

    # 使用jieba分词将输入文本切分成词列表
    word_list = jieba.lcut(text)
    # 将词列表转换为单个字符串，词之间用空格分隔，以便生成词云
    word_string = ' '.join(word_list)

    # 创建WordCloud对象，设置字体路径以支持中文显示，以及词云的基本属性
    wordcloud = wordc.WordCloud(font_path = 'simhei.ttf',
                                width = width,
                                height = height,
                                background_color = 'white').generate(word_string)

    # 创建一个新的图形，指定图形的大小
    plt.figure(figsize = (map_width, map_height))
    # 显示词云图，使用'bilinear'插值方法使图像看起来更平滑
    plt.imshow(wordcloud, interpolation = 'bilinear')
    # 关闭坐标轴显示，因为词云图不需要坐标轴
    plt.axis('off')
    # 如果save_png参数为True，则保存生成的词云图
    if save_png:
        plt.savefig(output_file, bbox_inches = 'tight', pad_inches = 0)

    # 显示生成的词云图
    plt.show()
    # 返回生成的词云对象
    return wordcloud

def worldcloud_pro(text, save_png = False, output_file = "wordcloud", width = 800, height = 400):
    # 检查输入文本是否为空，如果为空则直接返回0
    if text == " ":
        return 0

    # 使用jieba分词将输入文本切分成词列表
    word_list = jieba.lcut(text)
    # 将词列表转换为单个字符串，词之间用空格分隔，以便生成词云
    word_string = ' '.join(word_list)

    # 创建WordCloud对象，设置字体路径以支持中文显示，以及词云的基本属性
    wordcloud = wordc.WordCloud(font_path = 'simhei.ttf',
                                width = width,
                                height = height,
                                background_color = 'white').generate(word_string)

    # 将词云对象转换为图像对象
    image = wordcloud.to_image()
    # 如果save_png参数为True，则保存生成的词云图
    if save_png:
        image.save(output_file + ".png")

    # 显示生成的词云图
    image.show()
    # 返回生成的词云对象
    return wordcloud

def cut_wordC(text):
    # 使用jieba的lcut方法直接对输入的文本进行分词，返回结果为词语列表
    word_list = jieba.lcut(text)
    # 返回分词后的词语列表
    return word_list

