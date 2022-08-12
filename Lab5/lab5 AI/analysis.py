# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2a():
    #Living reward will be some negative quantity so it will exit as soon as possible
    #and noise will be very less so that it will defect less from its path
    answerDiscount = 0.5
    answerNoise = 0.001
    answerLivingReward = -1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question2b():
    #Living reward should be very less so that it will choose longer path and noise should also be 
    #less and discount also be less so that it will exit from +1 state
    answerDiscount = 0.03
    answerNoise = 0.05
    answerLivingReward = 0.01
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question2c():
    #Living reward will be some negative quantity but less than in que 2a so that it will exit 
    #from terminal state with payoff +10 and noise can be very very less or may be zero so that
    #it will not defect from its path and discount may be 1
    answerDiscount = 1
    answerNoise = 0.0001
    answerLivingReward = -0.4
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question2d():
    #Here living reward should be greater than que 2c but in negative quantity so that it will 
    #choose longer path
    answerDiscount = 1
    answerNoise = 0.01
    answerLivingReward = -0.01
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question2e():
    #In this case living reward will be very large so that it will never terminate
    answerDiscount = 1
    answerNoise = 0
    answerLivingReward = 100
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
