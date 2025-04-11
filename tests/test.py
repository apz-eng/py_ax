from src.py_ax.main import *

text_t = open("test.txt", encoding ="utf-8").read()

def worldcloud_plt_test(text):
    return worldcloud_plt(text, 5, 5, False, "wordcloud", 800, 400)
def worldcloud_pro_test(text):
    return worldcloud_pro(text, False, "wordcloud", 800, 400)
def cut_wordC_test(text):
    return cut_wordC(text)

result = worldcloud_pro_test(text_t)
# print(result)
