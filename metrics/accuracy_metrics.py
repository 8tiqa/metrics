import maths
#TODO: functions to load + store modelMetricsCalculation to json

modelMetrics = {
	    "absoluteError": 0,
	    "squaredError": 0,
	    "MAPE": 0,
	    "sMAPE": 0,
	    "MASE": 0
	}

modelMetricsCalculation = {
	    "numberOfEvaluations": 0,
	    "forecast_Sum": 0,
	    "forecastError_Sum": 0,
	    "absoluteError_Sum": 0,
	    "squaredError_Sum": 0,
	    "MAPE_Sum": 0,
	    "sMAPE_Sum": 0,
	    "MASE_Sum": 0,
	    "standardDeviation_Sum": 0,
        "naive_forecastError_Sum": 0
	}

# Residual Forecast Error
def __error(forcast, observation): 
    return (observation - forcast)

# Mean absolute error (MAE)
def __MAE(forecastError):   
    n = modelMetricsCalculation.numberOfEvaluations
    modelMetricsCalculation.absoluteError_Sum = modelMetricsCalculation.absoluteError_Sum + abs(forecastError)
    modelMetrics.absoluteError = modelMetricsCalculation.absoluteError_Sum / n
	

# Root mean squared error (RMSE)
def __RMSE(forecastError):  
    n = modelMetricsCalculation.numberOfEvaluations
    modelMetricsCalculation.squaredError_Sum = modelMetricsCalculation.squaredError_Sum + (forecastError ** 2)
    modelMetrics.squaredError = sqrt(modelMetricsCalculation.squaredError_Sum / n)
	

# Mean absolute percentage error (MAPE)
def __MAPE(observation, forecastError):
    n = modelMetricsCalculation.numberOfEvaluations
    modelMetricsCalculation.MAPE_Sum = modelMetricsCalculation.MAPE_Sum + abs(100 * (forecastError / observation))
	modelMetrics.autoregression_MAPE = modelMetricsCalculation.MAPE_Sum / n

# Symmetric MAPE (sMAPE)
def __sMAPE(observation, forecastError, forecast):
    n = modelMetricsCalculation.numberOfEvaluations
    modelMetricsCalculation.sMAPE_Sum = modelMetricsCalculation.sMAPE_Sum + 200 * (abs(forecastError) / (observation + forecast))
	modelMetrics.sMAPE = modelMetricsCalculation.sMAPE_Sum / n
	
        
# Mean absolute scaled error (MASE)
def __MASE(observation, forecastError, forecastErrorNaive):
    n = modelMetricsCalculation.numberOfEvaluations
    modelMetricsCalculation.naive_forecastError_Sum = modelMetricsCalculation.naive_forecastError_Sum + abs(forecastErrorNaive)
	denominator = 1 / (n - 1)
	q = forecastError / (denominator * modelMetricsCalculation.naive_forecastError_Sum)
	modelMetricsCalculation.sMASE_Sum = modelMetricsCalculation.sMASE_Sum + abs(q)	
    modelMetrics.sMAPE = abs(sMASE_Sum) / n



def compute_accuracy_metrics(observation, forecast, forecastNaive):
    	modelMetricsCalculation.numberOfEvaluations = modelMetricsCalculation.numberOfEvaluations + 1

        forecastError = __error(forcast, observation)
        
        modelMetricsCalculation.lstm_forecast_Sum = modelMetricsCalculation.forecast_Sum + forecast
        modelMetricsCalculation.forecastError_Sum = modelMetricsCalculation.forecastError_Sum + forecastError
        
        __MAE(forecastError)
        __RMSE(forecastError)
        __MAPE(observation, forecastError)
        __sMAPE(observation, forecastError, forecast)

        forecastErrorNaive = __error(forecastNaive, observation)
        __MASE(observation, forecastError, forecastErrorNaive)




