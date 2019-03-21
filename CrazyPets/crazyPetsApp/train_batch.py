import subprocess

try:
    subprocess.check_output(["python3.6 ./scripts/train.py"],shell=True)
except:
    print("エラー")
    exit()

print("学習完了!!")