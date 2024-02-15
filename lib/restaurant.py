class Restaurant:
    def __init__(self, name):
        self._name = name
        self._reviews = {}

    @property
    def name(self):
        return self._name
    
    def add_review(self, customer_name, review, rating):
        if customer_name not in self._reviews:
            self._reviews[customer_name] = (review, rating)
        else:
            existing_review, existing_rating = self._reviews[customer_name]
            # Update the review and rating if the customer has reviewed before
            self._reviews[customer_name] = (existing_review + "\n" + review, (existing_rating + rating) / 2)



    def reviews(self):
        return [review[0] for review in self._reviews.values()]
    
    def customers(self):
        return list(self._reviews.keys())
    
    def average_star_rating(self):
        total_rating = sum(review[1] for review in self._reviews.values())
        if not self._reviews:
            return 0  # Return 0 if there are no reviews to avoid division by zero
        return total_rating / len(self._reviews)

    
#Usage
restaurant1 = Restaurant("Urban Bites")

#Get the restaurant name
print("Restaurant Name:", restaurant1.name)

#Trying to change restautant name
restaurant1.name = "New Restaurant"

print("Restaurant Name:", restaurant1.name)

#Add reviews with star ratings
restaurant1.add_review("Customer1", "Great food and service!", 5)
restaurant1.add_review("Customer2", "Loved the ambiance.", 4)
restaurant1.add_review("Customer1", "I'll definitely come back.", 5)

#Get restaurant name
print("Restaurant Name:", restaurant1.name)

#Get reviews for the restaurant
print("Reviews:", restaurant1.reviews())

#Get unique customers who have reviewed the restaurant
print("Customers:", restaurant1.customers())

# Get the restaurant's average star rating
print("Average Star Rating:", restaurant1.average_star_rating())