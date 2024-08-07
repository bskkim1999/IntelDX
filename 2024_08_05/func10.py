def factorial(n):
    # 재귀함수를 이용하여 팩토리얼을 계산합니다.
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    while True:
        try:
            # 사용자로부터 입력을 받습니다.
            num = int(input("팩토리얼을 계산할 숫자를 입력하세요: "))
            if num < 0:
                print("음수에 대한 팩토리얼은 정의되지 않습니다. 다시 입력해 주세요.")
            else:
                # 팩토리얼 계산 함수 호출 및 결과 출력
                result = factorial(num)
                print(f"{num}의 팩토리얼은 {result}입니다.")
                break
        except ValueError:
            print("유효한 숫자를 입력해 주세요.")

if __name__ == "__main__":
    main()
