# Image manipulation
Tungsten RPA Connector is specific add-on to RPA, which can be used to implement missing features.
This specific connector adds Image resize function for PNGs.

# How to add connector to RPA
Here is an explanation directly from Tungsten Automation, how to upload and use finished connector: https://docshield.tungstenautomation.com/RPA/en_US/11.5.0-nlfihq5gwr/help/rpa_help/help_main/designstudio/c_das_customactionstep.html

Here is my explanation:
1) Copy the connector file to any folder in your project (via File explorer) and synchronize the project with Management Console.
2) Open your robot and via Desktop Automation add new step called "Integration" → "Custom Action".
3) When everything is ok, you'll be able to select "Image manipulation (python)" connector from the drop-down list with one Action "Resize Image".
4) It has three inputs, "input_png" Base-64 PNG, "max_width" and "max_height" to which size the source PNG should be resized.
5) It has three outputs, "status" (ok/error), "message" (Error message) and "output_png" Base-64 resized PNG.
