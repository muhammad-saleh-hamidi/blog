from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse


class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='saleh')
        cls.post1 = Post.objects.create(
            title='post1',
            text='this is the description of post1',
            status=Post.CHOICES_STATUS[0][0],
            auther=user,
        )
        cls.post2 = Post.objects.create(
            title='post2',
            text='this is the description of post2',
            status=Post.CHOICES_STATUS[1][0],
            # status='drf',
            auther=user,
        )
        #? tafavotesh to ine k to setup baray har test yek bar setup anjam mishe va agar niaz be naghir bash to ye test emkanesh hast
        #? ama dar setUpTestData yek bar baray hame ejra mishe

    # def setUp(self):
    #     self.user = User.objects.create(username='saleh')
    #     self.post1 = Post.objects.create(
    #         title='post1',
    #         text='this is the description of post1',
    #         status=Post.CHOICES_STATUS[0][0],
    #         auther=self.user,
    #     )
    #     self.post2 = Post.objects.create(
    #         title='post2',
    #         text='this is the description of post2',
    #         status=Post.CHOICES_STATUS[1][0],
    #         # status='drf',
    #         auther=self.user,
    #     )

    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code,200)

    def test_post_list_url_by_name(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_title_on_blog_list_page(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response,self.post1.title)

    def test_post_details_on_blog_post_detail_page(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_post_detail_url_by_name(self):
        response = self.client.get(reverse('post_detail',args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_status_404_if_post_not_found(self):
        response = self.client.get(reverse('post_detail',args=[1111]))
        self.assertEqual(response.status_code, 404)

    def test_draft_post_not_show_in_post_list(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response,self.post1.title)
        self.assertNotContains(response,self.post2.title)

