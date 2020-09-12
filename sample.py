

employee = spark.sql("select * from employee")

employee_part_time, employee_permanent, employee_contract_based = employee.split(employee['employee_type'])

employee_pt_morning_shift = employee_part_time.where(employee_part_time['shift']=="morning")

employee_pt_evening_shift = employee_part_time.where(employee_part_time['shift']=="evening")

employee_perms_ind, employee_perms_usuk = employee_permanent.split(employee_permanent['location'])

employee_perms_ind = employee_perms_ind_technologist

employee_perms_usuk_bueiness = employee_perms_usuk.filter(filter_condition(), employee_perms_usuk['business_level'])