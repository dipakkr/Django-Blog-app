from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User

from blog.models import Post


class UnitTestPost(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='testuser', password='12345')
        cls.One = Post.objects.create(title='one', author=user)
        cls.One.save()

    def test_Post_publish_method(self):
        post_date = self.One.publish()
        self.assertTrue(post_date)
