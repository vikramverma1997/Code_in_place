"""
File: moon_weight.py
--------------------
Add your comments here.
"""

import random


def main():
    eight_ball_answers = ['As I see it, yes.', 'Ask again later', 'Better not tell you know', 'Cannot predict now.',
                          'Concentrate and ask again.', 'Don’t count on it.', 'It is certain.', 'It is decidedly so.',
                          'Most likely', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Reply hazy.',
                          'try again.', 'Signs point to yes.', 'Very doubtful.', 'Without a doubt.', 'Yes – definitely.',
                          'You may rely on it.']
    user_question = str(input("Ask a yes or no question: "))
    print(random.sample(eight_ball_answers, 1))
    end_question = "No question"
    while user_question != end_question:
        main()





# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
