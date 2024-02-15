class Customer:
    all_customers = []  #class attribute to store all customers instances

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.reviewed_restaurants = set()
        self.reviews = [] #List to store reviews associated with customer
        Customer.all_customers.append(self)   #Adds the current instance to the list

    def given_name(self):
        return self.first_name
    
    def set_given_name(self, new_given_name):
        self.first_name = new_given_name
    
    def family_name(self):
        return self.last_name
    
    def set_family_name(self, new_family_name):
        self.last_name = new_family_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def review_restaurant(self, restaurant_name):
        self.reviewed_restaurants.add(restaurant_name)

    def get_reviewed_restaurants(self):
        return list(self.reviewed_restaurants)
    
    def add_review(self, restaurant, rating):
        review = (restaurant, rating)
        self.reviews.append(review)

    @classmethod
    def all(cls):
        return cls.all_customers

# Usage for printing first name of customer
customer = Customer("Wasaa", "Abdalla")
print(customer.given_name())

#Usage for changing customer when name is changed
customer.set_given_name("Jaffar")
print(customer.given_name())

# Usage for printing family name of customer
print(customer.family_name())
customer.set_family_name("Nassoro")
print(customer.family_name())

#Usage for printing full customer name
print(customer.full_name())


customer1 = Customer("Wasaa", "Abdalla")
customer2 = Customer("Jaffar", "Nassoro")
customer3 = Customer("Tony", "Cruise")

#Simulate restaurant reviews for customers
customer1.review_restaurant("Restaurant A")
customer1.review_restaurant("Restaurant B")
customer2.review_restaurant("Restaurant B")
customer2.review_restaurant("Restaurant C")
customer3.review_restaurant("Restaurant A")


#Retrieve all customer instances
all_customers = Customer.all()
for customer in all_customers:
    print(f"{customer.full_name()} has reviewed: {customer.get_reviewed_restaurants()}")

#for addreview method to associate customer with a restaurant
#create customer instance
customer = Customer("Wasaa", "Abdalla")

#Add review for a restaurant
restaurant = "Restaurant A"
rating = 5


customer.add_review(restaurant,rating)
