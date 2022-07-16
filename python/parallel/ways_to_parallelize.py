"""Using DASK"""

from dask import compute, delayed

def function_to_parallelize(arguments):
    #do something
    return # something

delayed_results = [delayed(function_to_parallelize)(some_arguments) for s in list]
mean_squared_errors = compute(*delayed_results, scheduler="processes")