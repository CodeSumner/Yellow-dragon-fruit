#https://replit.com/@CodeSumner/boilerplate-probability-calculator#prob_calculator.py
from collections import Counter
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = [] # create contents list.
        for key, val in kwargs.items():
            for i in range(val):
                self.contents.append(key)

    def draw(self, number):
        draw_list = []
        if number == len(self.contents):
            return self.contents
        else:
            for i in range(number):
                ball = random.choice(self.contents)
                draw_list.append(ball)
                self.contents.remove(ball) # remove the ball drawn from contents. 
            # give the draw_ist balls back for next turn drawing.
        self.contents += draw_list 
        #print(draw_list)
        return draw_list
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0 # count the times expected balls choosen
    j = 0
    i = 0
    while i < num_experiments:
        # create random drawn  balls' color and the number dictionary.
        draw_list_dic = Counter(hat.draw(num_balls_drawn))
        # find the intersection keys.
        intersection = [k for k in expected_balls if k in draw_list_dic]
        # check if the expected balls colors in randon drawn balls.
        if intersection & expected_balls.keys() == expected_balls.keys():
            # when colors match, then check if the numbers are right.  
            for key , val in expected_balls.items():
                if draw_list_dic[key] >= val:
                    j += 1
                if j == len(expected_balls):  # if the number is good, then count.
                    m += 1     
            j = 0
                
        i += 1
    # calculate the probability.      
    probability = m/num_experiments
    return probability

hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
print(probability)
"""
hat = Hat(red=5, blue=2)
print(hat.draw(2))
#expected = ['blue', 'red']
#self.assertEqual(actual, expected, 'Expected hat draw to return two random items from hat contents.')
print(len(hat.contents))
#expected = 5
"""
"""
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
hat = Hat(black=6, red=4, green=3)
random.seed(95)
hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=5,
    num_experiments=3000)
print("Probability:", probability)


random.seed(95)
hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2, "red": 1},
    num_balls_drawn=4,
    num_experiments=4000)
print("Probability:", probability)
"""