from machine import Pin, ADC, I2C
import ssd1306
from time import sleep

# -------------------------
# OLED I2C
# -------------------------
i2c = I2C(
    0,
    scl=Pin(22),
    sda=Pin(21),
    freq=400000
)

oled = ssd1306.SSD1306_I2C(
    128,
    64,
    i2c,
    addr=0x3C
)

# -------------------------
# LDR
# -------------------------
ldr = ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)
ldr.width(ADC.WIDTH_12BIT)

# -------------------------
# Startup screen
# -------------------------
oled.fill(0)
oled.text("LDR SENSOR", 25, 5)
oled.text("Light Level", 25, 25)
oled.text("Starting...", 25, 45)
oled.show()

sleep(2)

# -------------------------
# Main loop
# -------------------------
while True:

    # Read LDR value
    light = ldr.read()

    # Calculate percentage
    percentage = int((light / 4095) * 100)

    # Clear OLED
    oled.fill(0)

    # Display title
    oled.text("LIGHT LEVEL", 25, 0)

    # Display raw LDR value
    oled.text("LDR:", 10, 20)
    oled.text(str(light), 55, 20)

    # Display percentage
    oled.text("Light:", 10, 35)
    oled.text(str(percentage) + "%", 55, 35)

    # Display status
    if percentage < 30:
        status = "DARK"
    elif percentage < 70:
        status = "NORMAL"
    else:
        status = "BRIGHT"

    oled.text(status, 45, 52)

    # Update OLED
    oled.show()

    # Update every 0.5 second
    sleep(0.5)
