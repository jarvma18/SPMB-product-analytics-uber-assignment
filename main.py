import pandas as pd
from lib.csv_import import read_csv_file
from lib.shared import run_t_test, print_difference, print_higher_number_choice, print_labeled_amount

POOL_PRICE: float = 12.5
EXPRESS_PRICE: float = 10.0

df: pd.DataFrame = read_csv_file("data/uber_dataset.csv")
control_df: pd.DataFrame = df[df['treat'] == False]
treat_df: pd.DataFrame = df[df['treat'] == True]
control_commute_express: pd.Series = control_df[control_df['commute'] == True]['trips_express']
control_commute_pool: pd.Series = control_df[control_df['commute'] == True]['trips_pool']
control_commute_ridesharing: pd.Series = control_commute_express + control_commute_pool
treat_commute_express: pd.Series = treat_df[treat_df['commute'] == True]['trips_express']
treat_commute_pool: pd.Series = treat_df[treat_df['commute'] == True]['trips_pool']
treat_commute_ridesharing: pd.Series = treat_commute_express + treat_commute_pool
control_non_commute_express: pd.Series = control_df[control_df['commute'] == False]['trips_express']
control_non_commute_pool: pd.Series = control_df[control_df['commute'] == False]['trips_pool']
control_non_commute_ridesharing: pd.Series = control_non_commute_express + control_non_commute_pool
treat_non_commute_express: pd.Series = treat_df[treat_df['commute'] == False]['trips_express']
treat_non_commute_pool: pd.Series = treat_df[treat_df['commute'] == False]['trips_pool']
treat_non_commute_ridesharing: pd.Series = treat_non_commute_express + treat_non_commute_pool
control_commute_rider_cancellations: pd.Series = control_df[control_df['commute'] == True]['rider_cancellations']
treat_commute_rider_cancellations: pd.Series = treat_df[treat_df['commute'] == True]['rider_cancellations']
control_commute_total_driver_payout = control_df[control_df['commute'] == True]['total_driver_payout']
treat_commute_total_driver_payout = treat_df[treat_df['commute'] == True]['total_driver_payout']
control_commute_total_matches: pd.Series = control_df[control_df['commute'] == True]['total_matches']
treat_commute_total_matches: pd.Series = treat_df[treat_df['commute'] == True]['total_matches']
control_commute_total_double_matches: pd.Series = control_df[control_df['commute'] == True]['total_double_matches']
treat_commute_total_double_matches: pd.Series = treat_df[treat_df['commute'] == True]['total_double_matches']
control_non_commute_rider_cancellations: pd.Series = control_df[control_df['commute'] == False]['rider_cancellations']
treat_non_commute_rider_cancellations: pd.Series = treat_df[treat_df['commute'] == False]['rider_cancellations']
control_non_commute_total_driver_payout = control_df[control_df['commute'] == False]['total_driver_payout']
treat_non_commute_total_driver_payout = treat_df[treat_df['commute'] == False]['total_driver_payout']
control_non_commute_total_matches: pd.Series = control_df[control_df['commute'] == False]['total_matches']
treat_non_commute_total_matches: pd.Series = treat_df[treat_df['commute'] == False]['total_matches']
control_non_commute_total_double_matches: pd.Series = control_df[control_df['commute'] == False]['total_double_matches']
treat_non_commute_total_double_matches: pd.Series = treat_df[treat_df['commute'] == False]['total_double_matches']

# Problem 1 questions
print('1. Do commuting hours experience a higher number of ridesharing (Express + POOL) trips compared to non-commuting hours?')
print_higher_number_choice('Commute', control_commute_ridesharing.sum(), 'Non-commute', control_non_commute_ridesharing.sum());

print('2. What is the difference in the number of ridesharing trips between commuting and noncommuting hours?')
print_difference(
  control_commute_ridesharing.sum(),
  control_non_commute_ridesharing.sum(),
  'Commute Ridesharing',
  'Non-commute Ridesharing',
  False
)

print('3. Is the difference statistically significant at the 5% confidence level?')
run_t_test(control_commute_ridesharing, 'Commute', control_non_commute_ridesharing, 'Non-commute')

print('4. Do riders use Express at higher rates during commuting hours compared to non-commuting hours?')
print_higher_number_choice('Commute Express', control_commute_express.sum(), 'Non-commute Express', control_non_commute_express.sum())

print('5. What is the difference in the share of Express trips between commuting and non-commuting hours?')
print_difference(
  control_commute_express.sum(),
  control_non_commute_express.sum(),
  'Commute Express',
  'Non-commute Express',
  False
)

print('6. Is the difference statistically significant at the 5% confidence level?')
run_t_test(control_commute_express, 'Commute Express', control_non_commute_express, 'Non-commute Express')

print('7. Assume that riders pay $12.5 on average for a POOL ride, and $10 for an Express ride.')
print('What is the difference in revenues between commuting and non-commuting hours?')
commute_ridesharing_revenue = (control_commute_pool * POOL_PRICE) + (control_commute_express * EXPRESS_PRICE)
non_commute_ridesharing_revenue = (control_non_commute_pool * POOL_PRICE) + (control_non_commute_express * EXPRESS_PRICE)
print_difference(
  commute_ridesharing_revenue.sum(),
  non_commute_ridesharing_revenue.sum(),
  'Commute Revenue',
  'Non-commute Revenue',
  True
)

print('8. Is the difference statistically significant at the 5% confidence level?')
run_t_test(commute_ridesharing_revenue, 'Commute Revenue', non_commute_ridesharing_revenue, 'Non-commute Revenue')

print('9. Assume again that riders pay $12.5 on average for a POOL ride, and $10 for an Express ride.')
print('What is the difference in profits per trip between commuting and non-commuting hours?')
# Profit per trip = (Revenue - Total Driver Payout) / Total number of trips
commute_ridesharing_profit_per_trip = (commute_ridesharing_revenue - control_commute_total_driver_payout) / control_commute_ridesharing
non_commute_ridesharing_profit_per_trip = (non_commute_ridesharing_revenue - control_non_commute_total_driver_payout) / control_non_commute_ridesharing
print_difference(
  commute_ridesharing_profit_per_trip.mean(),
  non_commute_ridesharing_profit_per_trip.mean(),
  'Aver. Commute Profit per Trip',
  'Aver. Non-commute Profit per Trip',
  True
)

print('10. Is the difference statistically significant at the 5% confidence level?')
run_t_test(commute_ridesharing_profit_per_trip, 'Commute Profit per Trip', non_commute_ridesharing_profit_per_trip, 'Non-commute Profit per Trip')

# Problem 2 questions

print('1. What is the difference in the number of ridesharing trips between the treatment and control groups during commuting hours?')
print_difference(
  treat_commute_ridesharing.sum(),
  control_commute_ridesharing.sum(),
  'Treatment Commute Ridesharing',
  'Control Commute Ridesharing',
  False
)

print('2. Is the difference statistically significant at the 5% confidence level?')
run_t_test(treat_commute_ridesharing, 'Treatment Commute Ridesharing', control_commute_ridesharing, 'Control Commute Ridesharing')

print('3. What is the difference in the number of rider cancellations between the treatment and control groups during commuting hours?')
print_difference(
  treat_commute_rider_cancellations.sum(),
  control_commute_rider_cancellations.sum(),
  'Treatment Commute Rider Cancellations',
  'Control Commute Rider Cancellations',
  False
)

print('4. Is the difference statistically significant at the 5% confidence level?')
run_t_test(treat_commute_rider_cancellations, 'Treatment Commute Rider Cancellations', control_commute_rider_cancellations, 'Control Commute Rider Cancellations')

print('5. What is the difference in driver payout per trip between the treatment and control groups during commuting hours?')
print_difference(
  treat_commute_total_driver_payout.sum(),
  control_commute_total_driver_payout.sum(),
  'Treatment Commute Total Driver Payout',
  'Control Commute Total Driver Payout',
  False
)

print('6. Is the difference statistically significant at the 5% confidence level?')
run_t_test(treat_commute_total_driver_payout, 'Treatment Commute Total Driver Payout', control_commute_total_driver_payout, 'Control Commute Total Driver Payout')

print('7. What is the difference in overall match rate between the treatment and control groups during commuting hours?')
print_difference(
  treat_commute_total_matches.sum(),
  control_commute_total_matches.sum(),
  'Treatment Commute Total Matches',
  'Control Commute Total Matches',
  False
)

print('8. Is the difference statistically significant at the 5% confidence level?')
run_t_test(treat_commute_total_matches, 'Treatment Commute Total Matches', control_commute_total_matches, 'Control Commute Total Matches')

print('9. What is the difference in double match rate between the treatment and control groups during commuting hours?')
print_difference(
  treat_commute_total_double_matches.sum(),
  control_commute_total_double_matches.sum(),
  'Treatment Commute Double Matches',
  'Control Commute Double Matches',
  False
)

print('10. Is the difference statistically significant at the 5% confidence level?')
run_t_test(treat_commute_total_double_matches, 'Treatment Commute Double Matches', control_commute_total_double_matches, 'Control Commute Double Matches')

print('11. Does the analysis support extending waiting times to 5 minutes for commuting hours?')
print('No, the data provides clear evidence against extending waiting times.\n')

print('12. What is the difference in the number of ridesharing trips between the treatment and control groups during non-commuting hours?')
print_difference(
  treat_non_commute_ridesharing.sum(),
  control_non_commute_ridesharing.sum(),
  'Treatment Non-commute Ridesharing',
  'Control Non-commute Ridesharing',
  False
)

print('13. Is the difference statistically significant at the 5% confidence level?')
run_t_test(treat_non_commute_ridesharing, 'Treatment Non-commute Ridesharing', control_non_commute_ridesharing, 'Control Non-commute Ridesharing')

print('14. What is the difference in the number of rider cancellations between the treatment and control groups during non-commuting hours?')
print_difference(
  treat_non_commute_rider_cancellations.sum(),
  control_non_commute_rider_cancellations.sum(),
  'Treatment Non-commute Rider Cancellations',
  'Control Non-commute Rider Cancellations',
  False
)

print('15. Is the difference statistically significant at the 5% confidence level?')
run_t_test(treat_non_commute_rider_cancellations, 'Treatment Non-commute Rider Cancellations', control_non_commute_rider_cancellations, 'Control Non-commute Rider Cancellations')

print('16. What is the difference in driver payout per trip between the treatment and control groups during non-commuting hours?')
print_difference(
  treat_non_commute_total_driver_payout.sum(),
  control_non_commute_total_driver_payout.sum(),
  'Treatment Non-commute Total Driver Payout',
  'Control Non-commute Total Driver Payout',
  False
)

print('17. Is the difference statistically significant at the 5% confidence level?')
run_t_test(treat_non_commute_total_driver_payout, 'Treatment Non-commute Total Driver Payout', control_non_commute_total_driver_payout, 'Control Non-commute Total Driver Payout')

print('18. What is the difference in overall match rate between the treatment and control groups during non-commuting hours?')
print_difference(
  treat_non_commute_total_matches.sum(),
  control_non_commute_total_matches.sum(),
  'Treatment Non-commute Total Matches',
  'Control Non-commute Total Matches',
  False
)

print('19. Is the difference statistically significant at the 5% confidence level?')
run_t_test(treat_non_commute_total_matches, 'Treatment Non-commute Total Matches', control_non_commute_total_matches, 'Control Non-commute Total Matches')

print('20. What is the difference in double match rate between the treatment and control groups during non-commuting hours?')
print_difference(
  treat_non_commute_total_double_matches.sum(),
  control_non_commute_total_double_matches.sum(),
  'Treatment Non-commute Double Matches',
  'Control Non-commute Double Matches',
  False
)

print('21. Is the difference statistically significant at the 5% confidence level?')
run_t_test(treat_non_commute_total_double_matches, 'Treatment Non-commute Double Matches', control_non_commute_total_double_matches, 'Control Non-commute Double Matches')

print('22. Does the analysis support extending waiting times to 5 minutes for non-commuting hours?')
print('No, the data provides clear evidence against extending waiting times.\n')