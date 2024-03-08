"""
 Program purpose: Sales and customer satisfaction
 Programmer: NURULAIN BINTI ROSDI
 Date: 8 March 2024
"""

# Lists of flower names, unit sold, and customer reviews
flower_names = ["Lily", "Iris", "Rose", "Tulip", "Jasmine", "Dahlia", "Daisy", "Orchid", "Peony", "Marigold", "Sunflower",
                "Lotus", "Lavender", "Dandelion", "Baby-breath", "Cornflower", "Kale", "Lilac", "Hibiscus", "Angelica"]
units_sold = [100, 200, 150, 300, 250, 180, 220, 190, 280, 240,
              150, 200, 100, 75, 60, 45, 170, 110, 200, 80]
customer_reviews = [4.5, 1.8, 4.2, 3.6, 4.0, 2.1, 3.9, 2.2, 3.0, 2.8,
                    4.3, 3.7, 4.4, 2.9, 4.5, 5.0, 2.9, 3.1, 1.9, 4.9]

# Calculate the total number of units sold for all flowers based on the given flower sales data.
total_units_sold = sum(units_sold)
print("Total units sold for all flowers:", total_units_sold)

# Determine the flower with the highest sales among the provided flower sales data.
max_sales_index = units_sold.index(max(units_sold))
highest_sales = flower_names[max_sales_index]
print("Flowers with the highest sales:", highest_sales)

# Identify flowers with average customer reviews above 3 from the given flower sales data.
above_3_reviews = [flower_names[i] for i in range(len(customer_reviews)) if customer_reviews[i] > 3]
print("Flowers with average customer reviews above 3:", above_3_reviews)

# Calculate the average customer review score for all flowers based on the provided flower sales data.
average_review = sum(customer_reviews)/len(customer_reviews)
print("The average customer review score for all flowers:", average_review)

# Calculate the average sales for below-average sales
average_sold = total_units_sold / len(units_sold)

# Identify flowers names with below-average sales from the given flower sales
below_names = [flower_names[i] for i in range(len(units_sold)) if units_sold[i] < average_sold]
print("\nFlower with below-average sales from the average units sold:", below_names)
# Identify the below-average sales from the average units sold
below_average = [units_sold[i] for i in range(len(units_sold)) if units_sold[i] < average_sold]
print("Below-average sales from the average units sold:", below_average)
# Identify the below-average for customer review
below_review = [customer_reviews[i] for i in range(len(customer_reviews)) if customer_reviews[i] < average_review]
print("Below-average sales from the average customer review:", below_review)



