monthly_cost = 120
personal_training = 80 #6sessions
locker_rental , towel_service = 25 , 15
regis_fee = 50
total_first_month = float(monthly_cost + (personal_training) + locker_rental + towel_service + regis_fee)
monthly_cost_after = float(monthly_cost + locker_rental + towel_service + (personal_training * (5/12)))
anual_cost = float((monthly_cost_after * 11) + (personal_training * 5) + total_first_month)
print(f"Total cost for the first month: ${total_first_month:.2f}, Monthly cost after the first month: ${monthly_cost_after:.2f}, Annual cost: ${anual_cost:.2f}")
