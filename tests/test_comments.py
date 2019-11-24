import unittest

from app.models import User,Pitch,Comment
from app import db


class CommentModelTest(unittest.TestCase):
    '''
    this is a test case for the class comments. for adding and saving new comments and to check if they are saved
    '''
    def setUp(self):
        self.user_Trial = User(username = 'Baron',password = 'potato', email = 'baron@gmail.com')
        self.new_pitch = Pitch(id=1,title='Test',content='This is a test pitch',category="interview",user = self.user_Trial,likes=0,dislikes=0)
        self.new_comment = Comment(id=1,comment='Test comment',user_id=self.user_Trial,pitch_id=self.new_pitch)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user_id,self.user_Trial)
        self.assertEquals(self.new_comment.pitch_id,self.new_pitch)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment(self):
        self.new_comment.save_comment()
        comment = Comment.get_comments(1)
        self.assertTrue(comment is not None)
