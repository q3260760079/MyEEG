from pylsl import StreamInlet, resolve_stream,resolve_byprop
import time
import numpy as np
from pyedflib import highlevel
try:
    # first resolve an EEG stream on the lab network
    print("looking for all stream...")
    EEG_streams = resolve_stream('type', 'EEG')
    IMU_streams = resolve_byprop("type", "IMU", timeout=1)
    print("EEG:", EEG_streams, "IMU:", IMU_streams)
    # create a new inlet to read from the stream
    EEG_inlet = StreamInlet(EEG_streams[0])
    IMU_inlet = StreamInlet(IMU_streams[0])
    while True:
        # get a new sample (you can also omit the timestamp part if you're not interested in it)
        EEG_sample, EEG_timestamp = EEG_inlet.pull_sample()
        IMU_sample, IMU_timestamp = IMU_inlet.pull_sample()
        print("EEGdata:", EEG_sample,"IMUdata:", IMU_sample)
except KeyboardInterrupt as e:
    print("Ending program")
    raise e