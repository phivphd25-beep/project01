secret_word="Python"
hint="Gợi ý đây là tên một ngôn ngữ lập trình"
guess=""
guess_count=0
guess_limit=2
while guess != secret_word:
    if guess_count < guess_limit:
        guess=input("Bạn đoán đây là từ gì?")
        guess_count+=1
    else:
        break
if guess == secret_word:
    print(f"bạn đã đoán đúng, ngôn ngữ đó là {guess}")
else:
    print("Bạn đã đoán quá số lần")