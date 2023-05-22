import os
import uuid


def get_upload_path(instance, filename, img_type='model_image'):
    return os.path.join(img_type, str(instance.name), f'{uuid.uuid4()}_{filename}')
