import io

def crash_test():
    file_handle = io.StringIO()
    counter = 0
    while True:
        file_handle.write('1')
        counter += 1
        print(counter)

if __name__ == "__main__":
    crash_test()
    
# At what count did your computer crash?
# Count made it to 28261650 before I forced it to stop.
# 
# What kind of error did you get?
# 
# 
# Did your program crash earlier or later than expected? Why do you think?
