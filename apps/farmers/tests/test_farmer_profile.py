from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.farmers.models import FarmerProfile

User = get_user_model()

class FarmerProfileTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            phone_number="1234567890",
            full_name="Test User",
            password="testpassword",
        )
        self.client.force_authenticate(user=self.user)
        self.create_url = reverse("farmers:profile-create")
        self.profile_url = reverse("farmers:profile-retrieve-update")


    def test_user_can_create_farmer_profile(self):
        data = {
            "union": "Union A",
            "upazila": "Upazila B",
            "village": "Village E"
        }
        response = self.client.post(self.create_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(
            FarmerProfile.objects.filter(user=self.user).exists()
        )

    def test_user_cannot_create_duplicate_farmer_profile(self):
        FarmerProfile.objects.create(user=self.user)

        data = {
            "district": "Dhaka",
            "upazila": "Rampura",
            "village": "Test Village",
        }

        response = self.client.post(self.create_url, data)
        
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )


    def test_user_can_retrieve_own_farmer_profile(self):
        profile = FarmerProfile.objects.create(
            user=self.user,
            district="Dhaka",
        )

        response = self.client.get(self.profile_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], profile.id)
        self.assertEqual(response.data["district"], "Dhaka")


    def test_user_can_update_own_farmer_profile(self):
        profile = FarmerProfile.objects.create(
            user=self.user,
            district="Dhaka",
        )

        data = {
            "district": "Chittagong",
        }

        response = self.client.patch(self.profile_url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        profile.refresh_from_db()

        self.assertEqual(profile.district, "Chittagong")