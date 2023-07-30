from django.contrib.auth.models import User


def add_role(user_id, role_ids):
    """
    给用户添加角色
    :param user_id: 用户id
    :param role_ids: 角色id列表
    :return:
    """
    user = User.objects.get(id=user_id)
    user.roles.add(*role_ids)


def has_role(user_id, role_id):
    """
    判断用户是否有某个角色
    :param user_id: 用户id
    :param role_id: 角色id
    :return:
    """
    user = User.objects.get(id=user_id)
    return user.roles.filter(id=role_id).exists()



