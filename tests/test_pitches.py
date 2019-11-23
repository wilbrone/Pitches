import unittest

from app.models import User,Pitch,Comment
from app import db


class PitchModelTest(unittest.TestCase):
    '''
    this is a test case for the class comments. for adding and saving new comments and to check if they are saved
    '''
    def setUp(self):
        self.user_Trial = User(username = 'Baron',password = 'potato', email = 'baron@gmail.com')
        self.new_pitch = Pitch(id=1,title='Test',content='This is a test pitch',category="interview",user = self.user_Trial,likes=0,dislikes=0)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.title,'Test')
        self.assertEquals(self.new_pitch.content,'This is a test pitch')
        self.assertEquals(self.new_pitch.category,"interview")
        self.assertEquals(self.new_pitch.user,self.user_Trial)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch(self):
        self.new_pitch.save_pitch()
        saved_pitch = Pitch.get_pitches("interview")
        self.assertTrue(saved_pitch is not None)

    def test_get_pitch_by_id(self):
        self.new_pitch.save_pitch()
        pitch = Pitch.get_single_pitch(1)
        self.assertTrue(pitch is not None)
