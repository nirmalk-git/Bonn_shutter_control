import Bonn_shutter_class as shutter


# Intialize the shutter
Bonn_shutter1 = shutter("COM7")

# Verify the connection has established
Bonn_shutter1.start_interactive_session()

# Open the shutter
Bonn_shutter1.open_shutter()

# Close the shutter
Bonn_shutter1.close_shutter()

# Open the Bonn shutter for 10 ms
Bonn_shutter1.set_exposure_time(10)
