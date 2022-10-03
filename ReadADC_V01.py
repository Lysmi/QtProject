import smbus
import time
import numpy as np
import matplotlib.pyplot as plt
import pickle


##########################################################################
# Initialize ADC
# ADS1115 address, 0x48(72)
# Select configuration register, 0x01(01)
#		0x8483(33923)	AINP = AIN0 and AINN = AIN1, +/- 2.048V
#				Continuous conversion mode, 128SPS
##########################################################################

def ADCSignale(freq, duration):
    bus = smbus.SMBus(1)  # Get I2C bus
    data = [0xC4, 0x83]
    bus.write_i2c_block_data(0x48, 0x01, data)

    listACD = []  # Array with Sampled Values
    SamplingPeriod = 1/freq  # Sampling Period in seconds
    Samples = duration/SamplingPeriod  # Number of Samples to Acquire
    NoBits = 12  # Number of Bits ADC
    AmplitudeScaling = 0.1875  # From ADC

    print("started")

    for x in range(Samples):
        ActualTime = time.time()  # Get actual time to start acquisition

        # ADS1115 address, 0x48(72)
        # Read data back from 0x00(00), 2 bytes
        # raw_adc MSB, raw_adc LSB
        data = bus.read_i2c_block_data(0x48, 0x00, 2)
        raw_adc = data[0] * 256 + data[1]  # Convert the data

        if raw_adc > 32767:
            raw_adc -= 65535
        raw_adc = raw_adc / 2**NoBits * AmplitudeScaling / 2.0 * np.sqrt(2.0)
        listACD.append(raw_adc)
        # wait for next sampling period
        time.sleep(SamplingPeriod - (time.time() - ActualTime))
    return listACD
##########################################################################
# Show Data
##########################################################################
#fig, ax = plt.subplots(2, 1)
