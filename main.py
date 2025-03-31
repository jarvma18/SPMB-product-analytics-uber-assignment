import pandas as pd
from scipy.stats import ttest_ind
from lib.csv_import import read_csv_file
from lib.shared import run_t_test, print_difference, print_higher_number_choice

POOL_PRICE: float = 12.5
EXPRESS_PRICE: float = 10.0

df: pd.DataFrame = read_csv_file("data/uber_dataset.csv")
control_df: pd.DataFrame = df[df['treat'] == False]
commute_express: pd.Series = control_df[control_df['commute'] == True]['trips_express']
commute_pool: pd.Series = control_df[control_df['commute'] == True]['trips_pool']
commute_ridesharing: pd.Series = commute_express + commute_pool
non_commute_express: pd.Series = control_df[control_df['commute'] == False]['trips_express']
non_commute_pool: pd.Series = control_df[control_df['commute'] == False]['trips_pool']
non_commute_ridesharing: pd.Series = non_commute_express + non_commute_pool

print('1. Do commuting hours experience a higher number of ridesharing (Express + POOL) trips compared to non-commuting hours?')
print_higher_number_choice('Commute', commute_ridesharing.sum(), 'Non-commute', non_commute_ridesharing.sum());

print('2. What is the difference in the number of ridesharing trips between commuting and noncommuting hours?')
difference_commute_vs_noncommute_ridesharing: float = abs(commute_ridesharing.sum() - non_commute_ridesharing.sum())
print_difference(difference_commute_vs_noncommute_ridesharing)

print('3. Is the difference statistically significant at the 5% confidence level?')
run_t_test(commute_ridesharing, 'Commute', non_commute_ridesharing, 'Non-commute')

print('4. Do riders use Express at higher rates during commuting hours compared to non-commuting hours?')
print_higher_number_choice('Commute Express', commute_express.sum(), 'Non-commute Express', non_commute_express.sum())

print('5. What is the difference in the share of Express trips between commuting and non-commuting hours?')
difference_commute_vs_noncommute_express: float = abs(commute_express.sum() - non_commute_express.sum())
print_difference(difference_commute_vs_noncommute_express)

print('6. Is the difference statistically significant at the 5% confidence level?')
run_t_test(commute_express, 'Commute Express', non_commute_express, 'Non-commute Express')

print('7. Assume that riders pay $12.5 on average for a POOL ride, and $10 for an Express ride.')
print('What is the difference in revenues between commuting and non-commuting hours?')
commute_ridesharing_revenue = (commute_pool * POOL_PRICE) + (commute_express * EXPRESS_PRICE)
non_commute_ridesharing_revenue = (non_commute_pool * POOL_PRICE) + (non_commute_express * EXPRESS_PRICE)
difference_commute_vs_noncommute_ridesharing_revenue = abs(commute_ridesharing_revenue.sum() - non_commute_ridesharing_revenue.sum())
print('Commute revenue: ', commute_ridesharing_revenue.sum(), '$ ', ' Non-commute revenue: ', non_commute_ridesharing_revenue.sum(), '$')
print_difference(difference_commute_vs_noncommute_ridesharing_revenue)

print('8. Is the difference statistically significant at the 5% confidence level?')
run_t_test(commute_ridesharing_revenue, 'Commute Revenue', non_commute_ridesharing_revenue, 'Non-commute Revenue')

print('9. Assume again that riders pay $12.5 on average for a POOL ride, and $10 for an Express ride.')
print('What is the difference in profits per trip between commuting and non-commuting hours?')
# Profit per trip = (Revenue - Total Driver Payout) / Total number of trips
commute_total_driver_payout = control_df[control_df['commute'] == True]['total_driver_payout'].str.replace(",", ".").astype(float)
non_commute_total_driver_payout = control_df[control_df['commute'] == False]['total_driver_payout'].str.replace(",", ".").astype(float)
commute_ridesharing_profit_per_trip = (commute_ridesharing_revenue - commute_total_driver_payout) / commute_ridesharing
non_commute_ridesharing_profit_per_trip = (non_commute_ridesharing_revenue - non_commute_total_driver_payout) / non_commute_ridesharing
difference_commute_vs_noncommute_ridesharing_profit_per_trip = abs(commute_ridesharing_profit_per_trip.mean() - non_commute_ridesharing_profit_per_trip.mean())
print('Average commute profit per trip: ', commute_ridesharing_profit_per_trip.mean(), '$ ', ' Average non-commute profit per trip: ', non_commute_ridesharing_profit_per_trip.mean(), '$')
print_difference(difference_commute_vs_noncommute_ridesharing_profit_per_trip)

print('10. Is the difference statistically significant at the 5% confidence level?')
run_t_test(commute_ridesharing_profit_per_trip, 'Commute Profit per Trip', non_commute_ridesharing_profit_per_trip, 'Non-commute Profit per Trip')