import uuid
import os
import bleach

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('sportNews/images/article/', filename)

def clean_html(content):
    allowed_tags = ['b', 'i', 'u', 'a', 'p', 'br', 'strong', 'em', 'ul', 'li', 'ol', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']  # Các thẻ HTML được phép
    allowed_attributes = {'a': ['href', 'title'], 'img': ['src', 'alt', 'title']}
    return bleach.clean(content, tags=allowed_tags, attributes=allowed_attributes, strip=True)
