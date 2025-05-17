import time

def countdown_timer(t):
    while t : 
        mins , secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Time's up!")

if __name__ == "__main__":
    t = input("Enter the time in seconds: ")
    countdown_timer(int(t))

