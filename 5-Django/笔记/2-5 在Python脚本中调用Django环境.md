在Python脚本中调用Django环境
import os

if __name__ == '__main__':
    # 加载Django项目的配置信息
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BMS.settings")
    import django     # 导入Django，并启动Django项目
    django.setup()

    from app01 import models

    books = models.Book.objects.all()
    print(books)