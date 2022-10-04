
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    return EXPECTED_BAKE_TIME - elapsed_bake_time     

def preparation_time_in_minutes(layers):
    return layers * PREPARATION_TIME
        
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    print( preparation_time_in_minutes(number_of_layers),bake_time_remaining(elapsed_bake_time)
    )
    return preparation_time_in_minutes(number_of_layers) + bake_time_remaining(elapsed_bake_time)
    
elapsed_time_in_minutes(1,3)