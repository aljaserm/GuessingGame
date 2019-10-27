# from random import randint, randrange
# import sys
#
# # answer= randint(1,10)
# answer = randint(int(sys.argv[1]), int(sys.argv[2]))
#
# while True:
#     try:
#         guess = int(input(f'guess a number {sys.argv[1]}~{sys.argv[2]}:  '))
#         if  0 < guess < 11:
#             if guess == answer:
#                 print('you are a genius!')
#                 break
#         else:
#             print('hey bozo, I said 1~10')
#     except ValueError:
#         print('please enter a number')
#         continue
#


from random import randint
import sys

def checkResult(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, I said 1~10')
        return False


if __name__=='__main__':
    # generate a number 1~10
    answer = randint(1, 10)

    # input from user?

    # check that input is a number 1~10
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            # result= checkResult(guess, answer)
            if(checkResult(guess, answer)):
                break
            # if result==1:
            #    print('you are a genius!')
            #    break
            # else:
            #    print('hey bozo, I said 1~10')
        except ValueError:
            print('please enter a number')
            continue

