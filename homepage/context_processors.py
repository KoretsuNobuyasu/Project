from .models import Category,Menu


def common(request):
    """テンプレートに毎回渡すデータ"""

    context = {
        'category_list': Category.objects.all(),
        'menu_list': Menu.objects.all(),
    }
    return context