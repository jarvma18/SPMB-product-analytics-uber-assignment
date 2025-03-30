from lib.csv_import import read_csv_file
import pandas as pd
from scipy.stats import ttest_ind

def run_t_test(first_sample: pd.Series, first_sample_title: str, second_sample: pd.Series, second_sample_title: str):
  t_stat, p_value = ttest_ind(first_sample, second_sample, equal_var=False)
  print(f"Mean {first_sample_title}: {first_sample.mean()}, Mean {second_sample_title}: {second_sample.mean()}")
  print(f"t = {t_stat:.3f}, p = {p_value:.3f}")
  print("Statistically significant at 5%" if p_value < 0.05 else "Not statistically significant")

df = read_csv_file("data/uber_dataset.csv")

control_df = df[df['treat'] == False]
commute_express = control_df[control_df['commute'] == True]['trips_express']
commute_pool = control_df[control_df['commute'] == True]['trips_pool']
commute_ridesharing = commute_express + commute_pool
non_commute_express = control_df[control_df['commute'] == False]['trips_express']
non_commute_pool = control_df[control_df['commute'] == False]['trips_pool']
non_commute_ridesharing = non_commute_express + non_commute_pool

print('1. Do commuting hours experience a higher number of ridesharing (Express + POOL) trips compared to non-commuting hours?')
commute_has_higher_number_ridesharing: bool = commute_ridesharing.sum() > non_commute_ridesharing.sum();
print('Commute: ', commute_ridesharing.sum(), ' vs Non-commute: ', non_commute_ridesharing.sum())
print('Commute hours experience a higher number of ridesharing\n' if\
      commute_has_higher_number_ridesharing else 'Non-commute hours win\n')

print('2. What is the difference in the number of ridesharing trips between commuting and noncommuting hours?')
difference_commute_vs_noncommute_ridesharing: float = abs(commute_ridesharing.sum() - non_commute_ridesharing.sum())
print('Difference: ', difference_commute_vs_noncommute_ridesharing, '\n')

print('3. Is the difference statistically significant at the 5% confidence level?')
run_t_test(commute_ridesharing, 'Commute', non_commute_ridesharing, 'Non-commute')
print('\n')

print('4. Do riders use Express at higher rates during commuting hours compared to non-commuting hours?')
commute_express_has_higher_rates: bool = commute_express.sum() > non_commute_express.sum()
print('Commute Express: ', commute_express.sum(), ' vs Non-commute Express: ', non_commute_express.sum())
print('Commute hours experience a higher number of Express\n' if\
      commute_has_higher_number_ridesharing else 'Non-commute hours win\n')

print('5. What is the difference in the share of Express trips between commuting and non-commuting hours?')
difference_commute_vs_noncommute_express: float = abs(commute_express.sum() - non_commute_express.sum())
print('Difference: ', difference_commute_vs_noncommute_express, '\n')

print('6. Is the difference statistically significant at the 5% confidence level?')
run_t_test(commute_express, 'Commute Express', non_commute_express, 'Non-commute Express')
print('\n')

print('7. Assume that riders pay $12.5 on average for a POOL ride, and $10 for an Express ride.')
print('What is the difference in revenues between commuting and non-commuting hours?')
pool_price: float = 12.5
express_price: float = 10
commute_ridesharing_revenue = (commute_pool * pool_price) + (commute_express * express_price)
non_commute_ridesharing_revenue = (non_commute_pool * pool_price) + (non_commute_express * express_price)
difference_commute_vs_noncommute_ridesharing_revenue = abs(commute_ridesharing_revenue.sum() - non_commute_ridesharing_revenue.sum())
print('Commute revenue: ', commute_ridesharing_revenue.sum(), '$ ', ' Non-commute revenue: ', non_commute_ridesharing_revenue.sum(), '$')
print('Difference: ', difference_commute_vs_noncommute_ridesharing_revenue, '$\n')

print('8. Is the difference statistically significant at the 5% confidence level?')
run_t_test(commute_ridesharing_revenue, 'Commute Revenue', non_commute_ridesharing_revenue, 'Non-commute Revenue')

print('9. Assume again that riders pay $12.5 on average for a POOL ride, and $10 for an Express ride.')
print('What is the difference in profits per trip between commuting and non-commuting hours?')
# Profit per trip = (Revenue - Total Driver Payout) / Total number of trips
commute_total_driver_payout = control_df[control_df['commute'] == True]['total_driver_payout'].str.replace(",", ".").astype(float)
non_commute_total_driver_payout = control_df[control_df['commute'] == False]['total_driver_payout'].str.replace(",", ".").astype(float)
commute_ridesharing_profit_per_trip = (commute_ridesharing_revenue - commute_total_driver_payout) / commute_ridesharing
non_commute_ridesharing_profit_per_trip = (non_commute_ridesharing_revenue - non_commute_total_driver_payout) / non_commute_ridesharing
difference_commute_vs_noncommute_ridesharing_profit_per_trip = abs(commute_ridesharing_profit_per_trip.sum() - non_commute_ridesharing_profit_per_trip.sum())
print('Commute profit per trip: ', commute_ridesharing_profit_per_trip.sum(), '$ ', ' Non-commute profit per trip: ', non_commute_ridesharing_profit_per_trip.sum(), '$')
print('Difference: ', difference_commute_vs_noncommute_ridesharing_profit_per_trip, '$\n')

print('10. Is the difference statistically significant at the 5% confidence level?')
run_t_test(commute_ridesharing_profit_per_trip, 'Commute Profit per Trip', non_commute_ridesharing_profit_per_trip, 'Non-commute Profit per Trip')