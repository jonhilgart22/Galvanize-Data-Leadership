from math import sqrt
def two_sample_pooled_se(control_total_num,control_num_of_success,experiment_total_num,experiment_num_of_success,confidence_z=1.96):
    """Return the confidence interval for the difference in two sample proportions at 95% confidence level"""
    control_proportion = control_num_of_success/control_total_num
    experiment_proportion = experiment_num_of_success/experiment_total_num
    proportion_difference = experiment_proportion - control_proportion
    
    pooled_propotion = (experiment_num_of_success  + control_num_of_success) / \
    (experiment_total_num+control_total_num)
    
    pooled_standard_error = sqrt(pooled_propotion*(1-pooled_propotion)*\
                            (1/experiment_total_num + 1/control_total_num))
    
    print('The {} z-score confidence interval is:'.format(confidence_z),
          proportion_difference-confidence_z*pooled_standard_error,proportion_difference+confidence_z*pooled_standard_error)
    
    