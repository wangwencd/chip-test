# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/8/9 13:45
File: scpi.py
"""
import logging

L = logging.getLogger('Main')

class SCPI:
    """
    SCPI protocol command
    """

    def CLS(self):
        """
        Clear current state, IEEE-488 standard
        """
        self.control.write('*CLS')
        self.check_error()

    def ESR(self):
        """
        Enable bits in the Standard Event Enable register, IEEE-488 standard
        """
        self.control.write('*ESR')
        self.check_error()

    def ESR_query(self):
        """
        Return the decimal value of the binary-weighted sum of all bits in the Standard Event register,
        IEEE-488 standard
        """
        result = self.control.query('*ESR?')
        L.info('ESR result: ' + result)
        self.check_error()

    def IDN_query(self):
        """
        Return instrument's identification, IEEE-488 standard
        """
        result = self.control.query('*IDN?')
        L.info('IDN result: ' + result)
        self.check_error()

    def OPC(self):
        """
        Set the “Operation Complete” bit (bit 0) of the Standard Event register, IEEE-488 standard
        """
        self.control.write('*OPC')
        self.check_error()

    def OPC_query(self):
        """
        Return 1 to the output buffer, IEEE-488 standard
        """
        result = self.control.query('*OPC?')
        L.info('OPC result: ' + result)
        self.check_error()

    def RST(self):
        """
        Reset instrument to its power-on default state, don't clear any status register or error multiprocess,
        IEEE-488 standard
        """
        self.control.write('*RST')
        self.check_error()

    def PSC(self, value: str):
        """
        Clear or not the Status Byte and the Standard Event register enable masks when power is turned on,
        IEEE-488 standard

        Args:
            value: Command value, 0 / 1
        """
        self.control.write(str('*PSC ' + value))
        self.check_error()

    def PSC_query(self):
        """
        Return a 0 (*PSC 0) or a 1 (*PSC 1), IEEE-488 standard
        """
        result = self.control.query('*PSC?')
        L.info('PSC result: ' + result)
        self.check_error()

    def RCL(self, value: str):
        """
        Recall instrument's status, IEEE-488 standard

        Args:
            value: Number of status, 0 / 1 / 2 ...
        """
        self.control.write(str('*RCL ' + value))
        self.check_error()

    def SAV(self, value: str):
        """
        Save instrument's status, IEEE-488 standard

        Args:
            value: Number of status, 0 / 1 / 2 ...
        """
        self.control.write(str('*SAV ' + value))
        self.check_error()

    def SRE(self, value: str):
        """
        Enable the bits in the Status Byte Enable register, IEEE-488 standard

        Args:
            value: Bit number in the register, 0 / 1 / 01 / 012 ...
        """
        self.control.write(str('*SRE ' + value))
        self.check_error()

    def STB_query(self):
        """
        Query the Status Byte Summary register and return the same result as a serial poll, IEEE-488 standard
        """
        result = self.control.query('*STB?')
        L.info('STB result: ' + result)
        self.check_error()

    def TRG(self):
        """
        Generate an event trigger to the trigger system when the trigger system has a BUS trigger as its trigger source,
        IEEE-488 standard
        """
        self.control.write('*TRG')
        self.check_error()

    def TST_query(self):
        """
        Self-test, return 0 if passed, otherwise return non-zero value, IEEE-488 standard
        """
        result = self.control.query('*TST?')
        L.info('TST result: ' + result)
        self.check_error()

    def WAI(self):
        """
        Wait for all pending operations to complete, IEEE-488 standard
        """
        self.control.write('*WAI')
        self.check_error()

    def check_error(self):
        """
        Read the most recent error.
        """
        command = 'SYSTem:ERRor?'
        result = self.control.query(command)
        L.info('Error result: ' + result)

    def enable_remote(self):
        """
        Enter remote mode, commands are enabled
        """
        command = 'SYST:REM'
        self.control.write(command)
        self.check_error()

    def open_all(self):
        """
        Open serial com
        """
        self.control.open()
        self.check_error()

    def close_all(self):
        """
        Close serial com
        """
        self.control.close()
        self.check_error()

