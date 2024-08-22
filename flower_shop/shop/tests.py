from django.test import TestCase
from django.contrib.auth.models import User
from .models import Flower, Order

class FlowerModelTest(TestCase):
    def test_flower_creation(self):
        flower = Flower.objects.create(name="Rose", price=10.0)
        self.assertEqual(flower.name, "Rose")
        self.assertEqual(flower.price, 10.0)

class OrderModelTest(TestCase):
    def test_order_creation(self):
        user = User.objects.create_user(username="testuser", password="testpass")
        flower = Flower.objects.create(name="Rose", price=10.0)
        order = Order.objects.create(user=user)
        order.flowers.add(flower)
        self.assertEqual(order.user.username, "testuser")
        self.assertIn(flower, order.flowers.all())
