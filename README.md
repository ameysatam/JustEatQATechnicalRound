# Detailed instructions to run the program

Please find prerequisites below with each details. After the prerequisites are satisfied, see the instructions to run the file:

**_Prerequisites_**

1. Windows 10 laptop/desktop
   
   This program was developed on Windows 10 laptop. It will run on any windows machine irrespective whether it is 32 bit or 64 bit. If using Mac or Linux, the format of location of Chrome webdriver will differ. Also, if needed the Chrome webdriver needs to be included in PATH, the way of doing the same is way different in Mac and Linux as compared to Windows 10 and little different in lower versions of Windows as compared to Windows 10.
   

2. Chrome browser
   
   Please use Chrome Browser Version 88.0.4324.104 or below in Windows 10 machine.
   

3. Python 3.8x installed on your computer.
   
   Please download and install Python 3.8x on your Windows 10 laptop or PC. The most important step is to add the location to python.exe in your windows environment variables. Follow [this link](https://www.youtube.com/watch?v=7brx8mjCgEU) to install Python and add it to environment variable.
   

4. Selenium module installed in python
   
   In your Windows 10 laptop or PC command prompt enter the following command after above steps were followed, to install Selenium:
   `python -m pip install selenium`
   
   
**_Running the file_**

1. In your Windows 10 laptop or PC, go to the directory which contains the python file and the chromedriver given with the file. If chromedriver is not provided, please download the same appropriately for your Chrome browser version from [this link](https://chromedriver.chromium.org/downloads) and extract the chromedriver.exe in the folder containing the python file "test_restaurantNearby.py".

2. Open command prompt then go to the directory containing the file "test_restaurantNearby.py" in the command prompt and run the following command:
    
    `python test_restaurantNearby.py`
