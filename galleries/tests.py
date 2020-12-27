from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Photographer,Location,Image,Category
import datetime as dt

class ImageTestClass(TestCase):
    '''
    image test
    '''
    def setUp(self):
        self.landscape=Category(photo_category='Landscape')
        self.landscape.save_category()

        self.deborah=Photographer(first_name='Deborah',last_name="Ingabire M.")
        self.deborah.save_photographer()

        self.africa=Location(photo_location='Africa')
        self.africa.save_location()

        self.image=Image(title='hills',description='beautiful',photographer=self.deborah,location=self.africa,category=self.lanLandscape)
        self.image.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
    def test_save_method(self):
        '''
        test image and saved
        '''
        self.image.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_method(self):
        '''
        test of delete image
        '''
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_update(self):
        '''
        test to update image's
        '''
        self.image.save_image()
        img=self.image.get_image_by_id(self.image.id)
        image=Image.objects.get(id=self.image.id)
        self.assertTrue(img,image)

    def test_filter_by_location(self):
        '''
        test of filter image by location
        '''
        self.image.save_image()
        img=self.image.filter_by_location(self.image.location_id)
        image=Image.objects.filter(location=self.image.location_id)
        self.assertTrue(img,image)

    def test_filter_by_category(self):
        '''
        test image by category
        '''
        self.image.save_image()
        images=Image.search_by_category('this')
        self.assertFalse(len(images)>0)


class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.rwanda= Location(photo_location = 'Rwanda')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.rwanda,Location))
    #Testing to update
    def test_update(self):
        '''
        test to update image
        '''
        self.rwanda.save_location()
        img=self.rwanda.get_location_id(self.rwanda.id)
        location=Location.objects.get(id=self.rwanda.id)
        self.assertTrue(img,location)

    #test delete
    def tearDown(self):

        Location.objects.all().delete()
        Image.objects.all().delete()

    # Testing Save Method
    def test_save_method(self):
        self.rwanda.save_location()
        locations= Location.objects.all()
        self.assertTrue(len(locations) > 0)

class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.landscape= Category(photo_category = 'Landscape')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.landscape,Category))
    #Testing to update
    def test_update(self):
        '''
        test to update image
        '''
        self.landscape.save_category()
        img=self.landscape.get_category_id(self.landscape.id)
        category=Category.objects.get(id=self.landscape.id)
        self.assertTrue(img,category)

    #test delete
    def tearDown(self):

        Category.objects.all().delete()
        Image.objects.all().delete()

    # Testing Save Method
    def test_save_method(self):
        self.nature.save_category()
        categories= Category.objects.all()
        self.assertTrue(len(categories) > 0)
