
class FarmerBaseView:
    """
    eita shudu farmer related view gulate use hobe.
    and sathe IsActiveFarmer permission use korte hobe.
    """
    def get_farmer(self):
        return self.request.user.farmer_profile