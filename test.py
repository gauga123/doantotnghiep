from appium import webdriver
from appium.options.android import UiAutomator2Options  # Import UiAutomator2Options
import time

# Cấu hình thiết bị với UiAutomator2Options
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "emulator-5555"  # Kiểm tra adb devices để lấy ID thiết bị
options.app_package = "com.android.calculator2"  # Tên package ứng dụng cần mở
options.app_activity = ".Calculator"  # Activity chính của ứng dụng

# Kết nối với Appium Server
driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(5)  # Chờ 5 giây trước khi đóng ứng dụng

driver.quit()  # Đóng ứng dụng
