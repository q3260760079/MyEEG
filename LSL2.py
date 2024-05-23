import time
import numpy as np
from pyedflib import highlevel
from pylsl import resolve_byprop, StreamInlet

save_time_interval = 30


def sampling_data():
    global running, data
    start_time = time.time()
    while time.time() - start_time < save_time_interval:
        try:
            print(time.time())
            sample, timestamp = stream_inlet.pull_sample()
            print(sample)
            for i, d in enumerate(sample):
                data[i].append(d * 1e6)
        except Exception as e:
            print(e)
    stream_inlet.close_stream()


if __name__ == '__main__':
    running = True
    # ch_names = [str(_) for _ in list(range(64))]
    ch_names = ['Fp1', 'Fp2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4']
    streams = resolve_byprop("type", "IMU", timeout=1)
    if streams:
        print(streams)
        stream_inlet = StreamInlet(streams[0])
        save_path = "./test.edf"
        data = [[] for _ in ch_names]
        sampling_data()
        signal_headers = highlevel.make_signal_headers(ch_names, dimension='uV', sample_frequency=500,
                                                       physical_min=-250000, physical_max=250000)
        header = highlevel.make_header(patientname="", gender="")
        highlevel.write_edf(save_path, np.array(data), signal_headers, header)
        print("保存edf文件结束：{}".format(save_path))
    else:
        print("未找到lsl流")