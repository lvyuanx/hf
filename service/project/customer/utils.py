import os
import uuid


def get_upload_path(instance, filename, img_type='avatar'):
    return os.path.join(img_type, str(instance.company_name), f'{uuid.uuid4()}_{filename}')
