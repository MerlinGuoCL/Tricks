import pandas as pd
import os
import glob
import requests
import aiohttp
from sd import api_key
import numpy as np
import time
import random

def title_doi(foldpath):
    excel_files = glob.glob(os.path.join(foldpath, '*.xls'))
    # print(excel_files)
    data = []
    # 遍历找到的Excel文件
    for file in excel_files:
        # 使用pandas读取Excel文件
        df = pd.read_excel(file, usecols=[11,32], header = None, skiprows=1)
        data.append(df)
        # 打印文件名和数据框的前几行

    # 将列表中的所有数据框合并成一个大的数据框
    combined_data = pd.concat(data, ignore_index=True)

    # 将数据框转换为矩阵A
    datalist = combined_data.values
    return datalist
def sci_dir_download_paper(doi, api, title, foldpath):
    # ScienceDirect API的基础URL
    base_url = "https://api.elsevier.com/content/article/doi/"
    # 设置请求的headers
    headers = {
        'X-ELS-APIKey': api_key,
        'Accept': 'application/pdf'
    }
    # 发送请求
    response = requests.get(base_url + doi, headers=headers)
    if response.status_code == 200:
        # directory = os.path.join(foldpath)
        # if not os.path.exists(directory):
        #     os.makedirs(directory)
        try:
            with open(title + '.pdf', 'wb') as f:
                f.write(response.content)
            print(f"成功下载论文：{doi}")
        except FileNotFoundError:
            print(f"文件不存在: 跳过处理。")
        except Exception as e:
            print(f"处理文件时发生错误: {e}")
    else:
        print("请求失败")

def detect(foldpath, datalist):
    df = []
    for root, dirs, files in os.walk(foldpath):
        for i in files:
            if '.pdf' + ' ' in i + ' ':  # 这里后面不加一个字母可能会出问题，加上一个（不一定是空格）可以解决99.99%的情况
                df.append(i)
    df = np.array(df)
    datalist = np.hstack((datalist, np.zeros((datalist.shape[0], 1))))
    # 遍历datalist的第一列
    for i in range(len(datalist)):
        # 检查datalist的第一列中的元素是否在B中
        A = datalist[i, 0] + '.pdf'
        if A in df:
            datalist[i, 2] = 1
    return datalist






codefoldpath = ''# 代码存储的路径
foldpath = ''# doi存储的文件夹
datalist = title_doi(foldpath)
# 你的API密钥
api_key = ''# 替换为自己的api
# 文献的DOI
outputfoldpath = ''# 文件存储的位置
datalist = detect(codefoldpath,datalist)
sum1 = np.sum(datalist[:, 2])
for row in datalist:
    atitle = row[0]
    doi = row[1]
    if row[2] == 0:
        sci_dir_download_paper(doi, api_key, atitle, outputfoldpath)
        sleep_time = random.randint(0, 20)
        time.sleep(sleep_time)




