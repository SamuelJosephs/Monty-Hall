from result import result

results = []


num_trials = 10000
tracking = 0
while tracking < num_trials:
    f = 0
    while f < 100:
        outcome = result()
        if outcome:
            results.append("win")
            f += 1
        else:
            results.append("loss")
            f += 1
    tracking += 1

wins = results.count("win")
mean = wins / num_trials
print("The mean of the percentage of wins is: " + str(mean) + "%")

