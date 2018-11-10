from .models import Menu


def common(request):
    """テンプレートに毎回渡すデータ"""

    context = {
        'menu_list': Menu.objects.all(),
    }
    return context