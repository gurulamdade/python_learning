ratings = (1,2,3,4,5,6,7,8,9,10)
print("number of 10 ratings:", ratings.count(10))
print("first 5 star ratings index:", ratings.index(5))  # Find index of first occurrence of 5
print("Total Ratings:", len(ratings))

print("Highest Rating:", max(ratings))
print("Lowest Rating:", min(ratings))
print("Total Score:", sum(ratings))

# Find index of rating 2
index_of_2 = ratings.index(2)
print("Index of rating 2:", index_of_2)

# Count how many 4-star ratings
count_4_star = ratings.count(4)
print("Count of 4-star ratings:", count_4_star)

# Calculate average rating (hint: sum/len)
average_rating = sum(ratings) / len(ratings)
print("Average rating:", average_rating)




