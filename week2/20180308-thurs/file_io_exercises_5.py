import io

def crash_test():
    file_handle = io.StringIO()
    counter = 0
    while True:
        file_handle.write('1' * 1024 * 1024)
        counter += 1
        print(counter)

if __name__ == "__main__":
    crash_test()
    
# At what count did your computer crash?
# ~670 when 1MB is added during each cycle
# 
# What kind of error did you get?
# Just the word "Killed"
# 
# Did your program crash earlier or later than expected? Why do you think?
