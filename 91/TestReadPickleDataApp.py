from FileUtil import FileUtil
dataset=FileUtil.loadmodel("mydataset.data")
for cate in dataset:
    print(cate)
    cate.printProducts()