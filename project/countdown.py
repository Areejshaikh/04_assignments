import time
import sys

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = f"{mins:02d}:{secs:02d}"
        sys.stdout.write(f"\r⏳ Timer: {timer} ")
        sys.stdout.flush()
        time.sleep(1)
        t -= 1

    print("\n🎉 Timer Completed!")

t = int(input("Enter the time in seconds: "))



countdown(t)