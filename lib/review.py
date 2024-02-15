class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self._rating = rating
        Review.all_reviews.append(self)

    def get_rating(self):
        return self._rating
    
    @classmethod
    def get_all_reviews(cls):
        return cls.all_reviews
    
    def set_customer(self, customer):
        if not hasattr(self, '_customer'):
            self._customer = customer
        else:
            print("Customer name cannot be changed.")

    def set_restaurant(self, restaurant):
        if not hasattr(self, '_restaurant'):
            self._restaurant = restaurant
        else:
            print("Restaurant name cannot be changed.")
# Usage
class Customer:
    def __init__(self, name):
        self.name = name

class Restaurant:
    def __init__(self, name):
        self.name = name

# Creating customer and restaurant instances
customer1 = Customer("Alpha Likembe")
customer2 = Customer("Jeff Sabatto")

restaurant1 = Restaurant("The Food Palace")
restaurant2 = Restaurant("Spicy Alleys")


# Creating a reviews
review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant2, 3)


# Accessing review attributes
print(f"Customer: {review1.customer.name}")
print(f"Restaurant: {review1.restaurant.name}")
print(f"Rating: {review1.get_rating()}")

#Access all reviews
all_reviews = Review.get_all_reviews()
for review in all_reviews:
    print(f"Customer: {review.customer.name}, Restaurant: {review.restaurant.name}, Rating: {review.get_rating()}")

#Attempt to chnage the customer object for review1
new_customer = Customer("Ray Daniel")
review1.set_customer(new_customer)

#Attempt to change restaurant object for review1
new_restaurant = Restaurant("Tin to ler")
review1.set_restaurant(new_restaurant)


#check if customer and restaurant objets have changed
print(f"Customer (After Attempt): {review1.customer.name}")
print(f"Restaurant (After Attempt): {review1.restaurant.name}")