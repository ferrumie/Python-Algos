first = ['aatarget_class', 'updated_bank_statement_woe',
        'title_woe',
       'frobenius_dist_adj_woe',
       'request_repayment_periodicity_woe', 'product_was_changed_woe',
       'df1_woe', 'df3_woe', 'df2_woe', 'position_woe',
       'collection_division_woe', 'request_tenor_days_woe',
       'years_in_business_woe', 'df4_woe', 'POSRate_woe', 'lead_woe',
       'number_employees_woman_woe', 'number_of_dependents_woe', 'df5_woe',
       'frobenius_dist_lap_woe', 'tenor_days_woe', 'state_woe',
       'interest_rate_woe', 'request_amount_woe', 'gender_woe', 'cf1_woe',
       'residence_woe', 'device_info_validated_woe', 'cf2_woe', 'amount_woe',
       'average_monthly_sales_woe', 'LOANRate_woe', 'security_deposit_woe',
       'business_activities_woe', 'incomplete_provider_statements_woe',
       'is_registered_woe', 'debitMonthweekSeasonality_woe',
       'business_sector_woe', 'creditWeekdaySeasonality_woe', 'cf5_woe',
       'business_type_woe', 'incomplete_bank_statement_woe']

second = ['balanceWeekdaySeasonality',
       'frobenius_dist_adj_woe',
       'request_repayment_periodicity_woe', 'product_was_changed_woe',
       'df1_woe', 'df3_woe', 'df2_woe', 'incomplete_bank_statement_woe',
       'position_woe', 'collection_division_woe', 'request_tenor_days_woe',
       'years_in_business_woe', 'df4_woe', 'POSRate_woe', 'lead_woe',
       'number_employees_woman_woe', 'number_of_dependents_woe', 'df5_woe',
       'frobenius_dist_lap_woe', 'tenor_days_woe', 'state_woe',
       'request_amount_woe', 'cf1_woe', 'residence_woe',
       'device_info_validated_woe', 'cf2_woe', 'amount_woe',
       'average_monthly_sales_woe', 'LOANRate_woe', 'security_deposit_woe',
       'business_activities_woe', 'incomplete_provider_statements_woe',
       'is_registered_woe', 'business_sector_woe',
       'debitMonthweekSeasonality_woe', 'creditWeekdaySeasonality_woe',
       'cf5_woe', 'business_type_woe', 'interest_rate_woe']

for i in second:
    if i not in first:
        print(i)