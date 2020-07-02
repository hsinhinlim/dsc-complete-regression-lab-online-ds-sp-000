def sq_err(y_real, y_predicted):
    return round(np.sum((y_predicted - y_real)**2),2)

def r_squared(y_real, y_predicted):
    RES = sq_err(y_real,y_predicted)
    y_mean = y_real.mean()
    TOT =  round(np.sum((y_real - y_mean)**2),2)
    cod = 1 - (RES/TOT)
    return cod
