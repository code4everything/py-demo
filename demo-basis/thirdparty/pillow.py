# coding:utf-8

from PIL import Image

# 打开图片
im = Image.open('jingronghui.jpg')
# 获取图像尺寸
w, h = im.size
print('image size: %sx%s' % (w, h))
# 缩放（压缩）
im.thumbnail((w // 2, h // 2))
print('resize image: %sx%s' % (w // 2, h // 2))
# 保存
im.save('thumbnail.jpg', 'jpeg')

# 更多用法，参考官方文档：
# https://github.com/python-pillow/Pillow
