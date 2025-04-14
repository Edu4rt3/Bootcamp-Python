import random
pedra =    """   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)  """

papel =    """  _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________) """

tesoura =    """  _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) """

player = int(input("Bem vindo ao jogo de pedra, papel e tesoura! Escolha 1 para pedra, 2 para papel e 3 para tesoura \n"))
if player == 1:
    print(pedra)
if player == 2:
    print(papel)
if player == 3:
    print(tesoura)

cpu = random.randint(1,3)
if cpu == 1:
    print(f"Computer chose: \n{pedra}")
if cpu == 2:
    print(f"Computer chose: \n{papel}")
if cpu == 3:
    print(f"Computer chose: \n{tesoura}")

if player == 1 and cpu == 3:
    print("You win!")
elif cpu == 1 and player == 3:
    print("You lose!")
elif cpu > player:
    print("You lose!")
elif player> cpu:
    print("You win!")
elif cpu == player:
    print("It's a draw!")
elif player > 3:
    print("You type a invalid number!")