import statistics

# mean
def mean(input):
    return sum(input) / len(input)

# median
def median(input):
    return statistics.median(input)

# mode
def mode(input):
    return statistics.mode(input)

# standard deviation
def stdev(input):
    return statistics.stdev(input)

