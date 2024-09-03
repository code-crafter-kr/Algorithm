import pyautogui
import keyboard
import time
import win32gui
import win32con

def rapid_click():
    # 현재 마우스 위치 저장
    x, y = pyautogui.position()
    # 해당 위치의 윈도우 핸들 가져오기
    window = win32gui.WindowFromPoint((x, y))
    # 윈도우를 전경으로 가져오기
    win32gui.SetForegroundWindow(window)
    # 클릭 수행
    pyautogui.click(x, y, clicks=10, interval=0.01)

def main():
    print("빠른 클릭 오토마우스 시작. 'q'를 눌러 종료하세요.")
    running = False

    while True:
        if keyboard.is_pressed('f2'):  # F2 키로 on/off 전환
            running = not running
            print("오토마우스:", "실행 중" if running else "정지")
            time.sleep(0.1)  # 키 눌림 중복 방지

        if running:
            rapid_click()

        if keyboard.is_pressed('q'):  # q 키로 프로그램 종료
            print("프로그램을 종료합니다.")
            break

        time.sleep(0.01)  # CPU 사용량 줄이기

if __name__ == "__main__":
    main()