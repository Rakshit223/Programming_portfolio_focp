def bpp_pizza_calculator():
    print("Beckett Pizza Plaza 4-for-3 Offer")
    print("=================================")

    prices = []
    
    # Loop until we have 4 valid pizza prices
    while len(prices) < 4:
        current_num = len(prices) + 1
        raw_input = input(f"Enter Price of Pizza #{current_num}: ")
        
        try:
            # Convert to float for decimal prices
            price = float(raw_input)
            
            # Check if price is positive
            if price <= 0:
                print("Please enter a valid price!")
            else:
                prices.append(price)
                
        except ValueError:
            # This triggers if user enters text like "pepperoni"
            print("Please enter a valid price!")

    # 1. Find the total sum of all pizzas
    full_price = sum(prices)
    
    # 2. Find the cheapest one (the discount amount)
    discount_amount = min(prices)
    
    # 3. Calculate final charge
    final_total = full_price - discount_amount
    
    # 4. Calculate discount percentage
    # Formula: (Cheapest / Total sum of all 4) * 100
    discount_percentage = (discount_amount / full_price) * 100

    # Final Output - formatted to 2 decimal places for currency
    print(f"\nOrder Total is £{final_total:.2f}, a fabulous discount of {int(discount_percentage)}%!")

if __name__ == "__main__":
    bpp_pizza_calculator()