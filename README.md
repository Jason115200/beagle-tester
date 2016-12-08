# beagle-tester

## Supported boards

* [BeagleBone Black](#beaglebone-black)
* [BeagleBone Black Wireless](#beaglebone-black-wireless)
* [BeagleBone Blue](#beaglebone-blue)
* [BeagleBoard-xM](#beagleboard-xm)

## Supported scanners

* [Datalogic QuickScan L](http://www.datalogic.com/eng/products/automatic-data-capture/general-duty-handheld-scanners/quickscan-l-qd2300-pd-166.html) - VID:05f9 "PSC Scanning, Inc." PID:2204 
* [Intermec SG20 General Duty 1D/2D Handheld Scanner](http://www.intermec.com/products/scansg20t/) - VID:067E PID: 0801

## Software setup

If not already setup, on a recent [BeagleBoard.org Debian image](https://beagleboard.org/latest-images), perform:

    cd /opt/source
    git clone https://github.com/jadonk/beagle-tester
    cd beagle-tester
    make && make install
    
## Serial number barcode format

Each board that has an on-board EEPROM should have an associated 16 digit serial number placed onto a barcode on the board.

The first 4 ASCII characters indicate the board type:

* BeagleBone Black - 00C0
* BeagleBone Black Wireless - BWA5
* BeagleBone Blue - BLA2

The second 4 characters should indicate the manufacturing week in the format YYWW, where YY is currently 16 and WW is currently 30.

The next 4 characters should be a manufacturer-specific product code. If you are a new manufacturer, please choose something unique you can use to identify your boards.

Allocations include, but are not limited to: 

* BBGW for GHI manufactured BeagleBone Black Wireless

The final 4 characters are a sequential decimal number. If more than 10,000 boards are manufactured that week, roll over the top digit to an ASCII hex character.

# BeagleBone Black

## Required equipment

* HDMI TV capable of 1280x720p60 (720p) (HDMI monitor if no audio testing)
* Ethernet router (configured to answer DHCP requests and answer pings on the provided gateway)
* BeagleBone Black or other computer (configured to make DHCP requests over USB RNDIS interface and answer pings)
* A supported barcode scanner (listed above) (along with a suitable 16 character barcode on the device under test)
* Approved 5V power brick

## Test steps

1. Connect HDMI from board under test to TV to see output and hear audio
2. Connect an Ethernet device (router) with a DHCP server that has a gateway that will respond to pings
3. (optional) connect a wire from TP4 to ground to enable EEPROM writing of board revision and serial number
4. Power the board under test
5. Connect to the board under test USB client port from a USB host with RNDIS client support that will perform a DHCP request that will respond to pings
6. Wait for the BeagleBoard.org desktop to show (should be under 2 minutes)
7. Connect one of the supported barcode scanners
8. Wait for the CISPR test animation and audio playback (should be under 15 seconds) ![CISPR image][cispr]
9. Scan the 16 character barcode (4 character board revision and 12 character serial number) (will be programmed if step 3 completed and other tests pass)
10. Pass or fail will be indicated by a respectively green or red box on the TV
11. Disconnect the barcode scanner
12. Disconnect USB client
13. Remove power
14. Disconnect remaining devices

# BeagleBone Black Wireless

## Required equipment

* HDMI TV capable of 1280x720p60 (720p) (HDMI monitor if no audio testing)
* BeagleBone Black Wireless running 'connman tether' to act as a WiFi access point (should be default on production image)
* BeagleBone Black Wireless or other computer (configured to make DHCP requests over USB RNDIS interface and answer pings)
* A supported barcode scanner (listed above) (along with a suitable 16 character barcode on the device under test)
* Approved 5V power brick

## Test steps

1. Have BeagleBone Black Wireless running as WiFi access point (SSID: BeagleBone-XXXX, PSK: BeagleBone)
2. Connect HDMI from board under test to TV to see output and hear audio
3. (optional) connect a wire from TP1 to ground to enable EEPROM writing of board revision and serial number
4. Power the board under test
5. Connect to the board under test USB client port from a USB host with RNDIS client support that will perform a DHCP request that will respond to pings
6. Wait for the BeagleBoard.org desktop to show (should be under 2 minutes)
7. Connect one of the supported barcode scanners
8. Wait for the CISPR test animation and audio playback (should be under 15 seconds) ![CISPR image][cispr]
9. Scan the 16 character barcode (4 character board revision and 12 character serial number) (will be programmed if step 3 completed and other tests pass)
10. Pass or fail will be indicated by a respectively green or red box on the TV
11. Disconnect the barcode scanner
12. Disconnect USB client
13. Remove power
14. Disconnect remaining devices

# BeagleBone Blue

## Required equipment

* Adafruit 2.4" TFT LCD subassembly (See https://gist.github.com/jadonk/0e4a190fc01dc5723d1f183737af1d83)
* BeagleBone Blue acting as a WiFi access point (should be default on production image)
* BeagleBone Blue or other computer (configured to make DHCP requests over USB RNDIS interface and answer pings)
* A supported barcode scanner (listed above) (along with a suitable 16 character barcode on the device under test)
* Approved 12V power brick
* Approved 2S LiPo battery

## Test steps

1. Have BeagleBone Blue running as WiFi access point (SSID: BeagleBone-XXXX, PSK: BeagleBone)
2. Connect S1.1/GP0 from board under test to Adafruit 2.4" TFT LCD subassembly to see display output
3. (optional) connect a wire from WP to GND to enable EEPROM writing of board revision and serial number
4. Power the board under test using the 2S LiPo battery
5. Connect the 12V power brick
6. Connect to the board under test USB client port from a USB host with RNDIS client support that will perform a DHCP request that will respond to pings
7. Connect one of the supported barcode scanners
8. Wait for the CISPR test animation (should be under 2 minutes) ![CISPR image][cispr]
9. Scan the 16 character barcode (will be programmed if step 3 completed and other tests pass)
10. Pass or fail will be indicated by a respectively green or red box on the display
11. Disconnect the barcode scanner
12. Disconnect USB client
13. Disconnect 12V power brick
14. Disconnect 2S LiPo battery
14. Disconnect display

# BeagleBoard-xM

## Required equipment

* HDMI TV capable of 1280x1024 (HDMI monitor if no audio testing)
* Ethernet router (configured to answer DHCP requests and answer pings on the provided gateway)
* BeagleBone Black or other computer (configured to make DHCP requests over USB RNDIS interface and answer pings)
* A supported barcode scanner (listed above) (along with a suitable 16 character barcode on the device under test)
* Three (3) USB 2.0 HS capable flash drives
* 1/8" audio patch cable
* DB9 serial loopback cable
* Approved 5V power brick

## Test steps

1. Connect HDMI from board under test to TV to see output
2. Connect an Ethernet device (router) with a DHCP server that has a gateway that will respond to pings
3. Connect the 3 USB flash drives
4. Connect the audio patch cable
5. Power the board under test
6. Connect to the board under test USB client port from a USB host with RNDIS client support that will perform a DHCP request that will respond to pings
7. Wait for the BeagleBoard.org desktop to show (should be under 2 minutes)
8. Connect one of the supported barcode scanners
9. Wait for the CISPR test animation and audio playback (should be under 15 seconds) ![CISPR image][cispr]
10. Scan a barcode to begin the test
11. Pass or fail will be indicated by a respectively green or red box on the TV ![xM pass image][xm-pass]
12. Disconnect the barcode scanner
13. Disconnect USB client
14. Remove power
15. Disconnect remaining devices

[cispr]: https://raw.githubusercontent.com/jadonk/beagle-tester/master/images/itu-r-bt1729-colorbar-3200x1800.png
[xm-pass]: https://raw.githubusercontent.com/jadonk/beagle-tester/master/images/beagleboard-xm-pass.png
