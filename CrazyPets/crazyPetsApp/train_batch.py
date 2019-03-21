import subprocess

try:
    subprocess.check_output(["python ./scripts/train.py"],shell=True)
except:
    print("エラー")
    exit()

print("学習完了!!")