.. module:: sw03

****************
SW03 Module
****************

This is a module for the `SW03 <https://wiki.xinabox.cc/SW03_-_Weather_Sensor>`_ ambient temperature, altitude and pressure sensor.
The board is based off the MPL3115A2 manufactured by NXP Semiconductors.
The board uses I2C for communication.

Datasheets:

- `MPL3115A2 <http://www.nxp.com/assets/documents/data/en/data-sheets/MPL3115A2.pdf>`_
    
===============
SW03 class
===============

.. class:: SW03(i2cdrv, addr=0x60, clk=100000)

    Creates an intance of a new SW03.

    :param i2cdrv: I2C Bus used '( I2C0, ... )'
    :param addr: Slave address, default 0x60
    :param clk: Clock speed, default 100kHz

    Example: ::

        from xinabox.sw03 import sw03

        ...

        SW03 = sw03.SW03(I2C0)
        SW03.init()
        alt = SW03.getAltitude()
        pres = SW03.getPressure()

    
.. method:: init(osr=0)

        Initialize the MPL3115A2 setting the oversample rate value.

        :param osr: set the oversample rate value (from 0 to 7), default 0

========= ================ ==========
OSR Value Oversample Ratio Data Ready
========= ================ ==========
0         1                6 ms             
1         2                10 ms              
2         4                18 ms      
3         8                34 ms               
4         16               66 ms     
5         32               130 ms     
6         64               258 ms    
7         128              512 ms 
========= ================ ==========

        
.. method:: get_raw_alt()

        Retrieves the current altitude data from the sensor as raw value.

        Returns raw_a

        
.. method:: get_raw_pres()

        Retrieves the current pressure data from the sensor as raw value.

        Returns raw_p

        
.. method:: get_raw_temp()

        Retrieves the current temperature data from the sensor as raw value.

        Returns raw_t

        
.. method:: getAltitude()

        Calculates, from measured pressure, the current altitude data as value in meters.

        Returns altitude

        
.. method:: getPressure()

        Retrieves the current pressure data from the sensor as calibrate value in Pa.

        Returns pres

        
.. method:: getTempC()

        Retrieves the current temperature data from the sensor as calibrate value in °C.

        Returns temp

        
