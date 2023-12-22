import os
say=input("Enter your path ")
if 'open' in say:
    ispath=say.removeprefix("open ")
    os.chdir()
    ispath_check=os.path.exists(ispath)
    print(ispath,
          ispath_check)