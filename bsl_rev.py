from bsl import StreamReceiver

# Connects to all available streams
sr = StreamReceiver()
# Update each stream buffer with new data
sr.acquire()
# Retrieve buffer/window for the stream named 'StreamPlayer'
