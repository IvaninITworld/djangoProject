import os
from PIL import Image
from django.db.models.fields import ImageField, ImageFieldFile


class ThumbnailImageFieldFile(ImageFieldFile):
    # def _add_thumb(s):
    #     parts = s.split(".")
    #     parts.insert(-1, "thumb")
    #     if parts[-1].lower() not in ['jpeg', 'jpg']:
    #         parts[-1] = 'jpg'
    #     return "."
    #     join(parts)
    #
    # @property
    #     def thumb_path(self):
    #     return self._add_thumb(self.path)
    pass


class ThumbnailImageField(ImageField):
    attr_class = ThumbnailImageFieldFile

    def __init__(self, verbose_name=None, thumb_width=128, thumb_height=128, **kwargs):
        self.thumb_width, self.thumb_height = thumb_width, thumb_height
        super().__init__(verbose_name, **kwargs)