@contextmanager
def subplots(nrows, ncols, **kwargs):
    """
    cf. 0020_explore_data.ipynb for an example
    """
    from itertools import chain
    from matplotlib import pyplot

    fig, axes = pyplot.subplots(nrows, ncols, **kwargs)
    axes = chain(*axes)

    yield fig, axes
    
    for remaining in axes:
        remaining.axis("off")