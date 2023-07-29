import uuid
import random
import string

from django.db import models


class Image(models.Model):
	identifier = models.UUIDField(default=uuid.uuid4, editable=False)
	slug = models.SlugField(max_length=20, unique=True)
	image = models.ImageField()
	created_at = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = self._generate_slug()
		super().save(*args, **kwargs)

	def _generate_slug(self):
		return ''.join(random.choices(string.ascii_letters + string.digits, k=20))


class UploadRecord(models.Model):
    ip_address = models.GenericIPAddressField()
    upload_datetime = models.DateTimeField(auto_now_add=True)

