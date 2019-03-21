import subprocess

try:
    subprocess.check_output(["python3.6 /home/crazy_pets/CrazyPets/CrazyPets/crazyPetsApp/scripts/train.py"],shell=True)
except:
    print("エラー")
    exit()

print("学習完了!!")