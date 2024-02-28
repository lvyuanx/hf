from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import UploadedFile
from django.db import transaction
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from hf_system import settings
from hf_system.settings import MEDIA_ROOT
from hf_system.utils.response_utils import LResponse
from hf_system.utils.utils import is_image
from staff.serializers.staff_serializer import StaffBaseSerializer
from staff.models import StaffBase


class StaffView(ModelViewSet):
    queryset = StaffBase.objects.all()
    serializer_class = StaffBaseSerializer

    @action(methods=["post"], detail=False, url_path="edit", url_name="edit")
    def edit(self, request):
        print(request)
        # 获取用户信息
        full_name = request.data.get("fullname")
        staff_code = request.data.get("staff_code")
        phone_number = request.data.get("phone_number")
        notes = request.data.get("notes")

        # 获取头像文件
        avatar = request.FILES.get("avatar")
        # 判断是否是图片
        if not is_image(avatar):
            return LResponse().error('文件类型错误，请上传图片类型！')
        # 校验文件大小
        max_size = 15 * 1024 * 1024  # 5M
        if isinstance(avatar, UploadedFile) and avatar.size > max_size:
            return LResponse().error('图片太大了！')
        # 将图片上传到media目录
        avatar_dir = f'/avatar/{staff_code}'
        base_dir = f'{MEDIA_ROOT}{avatar_dir}'

        # 创建 FileSystemStorage 对象，并指定保存路径
        fs = FileSystemStorage(location=base_dir)

        # 生成随机文件名，避免覆盖已有文件
        filename = fs.save(fs.get_available_name(avatar.name), avatar)

        # 获取文件 URL
        url = fs.url(f'{avatar_dir}/{filename}')

        # 创建系统用户
        default_pwd = settings.default_pwd.format(staff_code=staff_code)

        if User.objects.filter(username=staff_code).exists():
            return LResponse().error('员工编号重复！')

        # 开启事务
        with transaction.atomic():
            # 插入系统用户
            user = User.objects.create_user(username=staff_code, password=default_pwd)

            StaffBase(
                user=user,
                staff_code=staff_code,
                phone_number=phone_number,
                full_name=full_name,
                avatar=url,
                notes=notes
            ).save()

        # 创建系统用户
        return LResponse().ok()
