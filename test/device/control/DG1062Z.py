# -- coding:utf-8 --
"""
User: ww
Version: 3.8
Date: 2022/10/17 13:45
File: DG1062Z.py
"""
import logging

from test.device.control.scpi import SCPI

L = logging.getLogger('Main')

class DG1062Z(SCPI):
    """
    DG1062Z control
    """
    def __init__(self, cls):
        self.control = cls
        self.name = 'DG1062Z'
        super().__init__()

    def set_channel_impedance(self, impedance, channel=1):
        """
        Set channel's impedance

        Args:
            impedance: Output impedance value, string format, unit: ohm
            channel: Channel number, string format, 2 options: 1 / 2
        """
        command = ':OUTP' + str(channel) + ':IMP ' + str(impedance)   # format example: :OUTP1:IMP 100
        self.control.write(command)
        L.debug(self.name + ' set channel: ' + str(channel) + ', impendace: ' + str(impedance) + 'ohm')
        self.check_error()

    def channel_on(self, channel=1):
        """
        Set channel output on

        Args:
            channel: Channel number, string format, 2 options: 1 / 2
        """
        command = ':OUTP' + str(channel) + ' ON'
        self.control.write(command)
        L.debug(self.name + ' set channel: ' + str(channel) + ' ON')
        self.check_error()

    def channel_off(self, channel=1):
        """
        Set channel output off

        Args:
            channel: Channel number, string format, 2 options: 1 / 2
        """
        command = ':OUTP' + str(channel) + ' OFF'
        self.control.write(command)
        L.debug(self.name + ' set channel: ' + str(channel) + ' OFF')
        self.check_error()

    def query_channel_parameter(self, channel=1):
        """
        Return waveform type, frequency, amplitude, offset and phase values

        Args:
            channel: Channel number, string format, 2 options: 1 / 2
        """
        command = ':SOURce' + str(channel) + ':APPL?'
        result = self.control.query(command).replace('"', '')
        L.debug(self.name + ' channel: ' + str(channel)
                + ', waveform: ' + result.split(',')[0]
                + ', frequency: ' + str(eval(result.split(',')[1])) + 'Hz'
                + ', amplitude: ' + str(eval(result.split(',')[2])) + 'Vpp'
                + ', offset: ' + str(eval(result.split(',')[3])) + 'Vdc'
                + ', phase: ' + str(eval(result.split(',')[4])) + 'deg'
                )
        self.check_error()

    def set_channel_sinc_parameter(self, sample, amplitude, offset=0, channel=1):
        """
        Set channel to be SINC waveform, set sample rate, amplitude and offset

        Args:
            sample: Sample rate, string format, unit: Sa/s
            amplitude: Amplitude value of waveform, string format, unit: Vpp
            offset: Offset value of waveform, string format, unit: Vdc
            channel: Channel number, string format, 2 options: 1 / 2
        """
        command = ':SOURce' + str(channel) + ':APPL:ARB ' + str(sample) + ',' + str(amplitude) + ',' + str(offset)
        self.control.write(command)
        L.debug(self.name + 'set channel: ' + str(channel)
                + ', waveform: SINC'
                + ', sample: ' + str(sample) + 'Sa/s'
                + ', amplitude: ' + str(amplitude) + 'Vpp'
                + ', offset: ' + str(offset) + 'Vdc'
                )
        self.check_error()

    def set_channel_dc_parameter(self, offset, channel=1):
        """
        Set channel to be DC waveform, set offset

        Args:
            offset: Offset value of waveform, string format, unit: Vdc
            channel: Channel number, string format, 2 options: 1 / 2
        """
        command = ':SOURce' + str(channel) + ':APPL:DC 1,1,' + str(offset)
        self.control.write(command)
        L.debug(self.name + 'set channel: ' + str(channel)
                + ', waveform: DC'
                + ', offset: ' + str(offset) + 'Vdc'
                )
        self.check_error()

    def set_channel_harm_parameter(self, frequency, amplitude, offset=0, phase=0, channel=1):
        """
        Set channel to be HARM waveform, set frequency, amplitude, offset and phase.

        Args:
            frequency: Frequency value of waveform, string format, unit: Hz
            amplitude: Amplitude value of waveform, string format, unit: Vpp
            offset: Offset value of waveform, string format, unit: Vdc
            phase: Phase value of waveform, string format, unit: dge
            channel: Channel number, string format, 2 options: 1 / 2
        """
        command = ':SOURce' + str(channel) + ':APPL:HARM ' \
                  + str(frequency) + ',' + str(amplitude) + ',' + str(offset) + ',' + str(phase)
        self.control.write(command)
        L.debug(self.name + 'set channel: ' + str(channel)
                + ', waveform: HARM'
                + ', frequency: ' + str(frequency) + 'Hz'
                + ', amplitude: ' + str(amplitude) + 'Vpp'
                + ', offset: ' + str(offset) + 'Vdc'
                + ', phase: ' + str(phase) + 'dge'
                )
        self.check_error()

    def set_channel_noise_parameter(self, amplitude, offset=0, channel=1):
        """
        Set channel to have noise, set amplitude and offset

        Args:
            amplitude: Amplitude value of noise, string format, unit: Vpp
            offset: Offset value of noise, string format, unit: Vdc
            channel: Channel number, string format, 2 options: 1 / 2
        """
        command = ':SOURce' + str(channel) + ':APPL:NOIS ' + str(amplitude) + ',' + str(offset)
        self.control.write(command)
        L.debug(self.name + 'set channel: ' + str(channel)
                + ', waveform: NOISE'
                + ', amplitude: ' + str(amplitude) + 'Vpp'
                + ', offset: ' + str(offset) + 'Vdc'
                )
        self.check_error()

    def set_channel_pul_parameter(self, frequency, amplitude, offset=0, phase=0, channel=1):
        """
        Set channel to be PUL waveform, set frequency, amplitude, offset and phase.

        Args:
            frequency: Frequency value of waveform, string format, unit: Hz
            amplitude: Amplitude value of waveform, string format, unit: Vpp
            offset: Offset value of waveform, string format, unit: Vdc
            phase: Phase value of waveform, string format, unit: dge
            channel: Channel number, string format, 2 options: 1 / 2
        """
        command = ':SOURce' + str(channel) + ':APPL:PULS ' \
                  + str(frequency) + ',' + str(amplitude) + ',' + str(offset) + ',' + str(phase)
        self.control.write(command)
        L.debug(self.name + 'set channel: ' + str(channel)
                + ', waveform: PUL'
                + ', frequency: ' + str(frequency) + 'Hz'
                + ', amplitude: ' + str(amplitude) + 'Vpp'
                + ', offset: ' + str(offset) + 'Vdc'
                + ', phase: ' + str(phase) + 'dge'
                )
        self.check_error()

    def set_channel_ramp_parameter(self, frequency, amplitude, offset=0, phase=0, channel=1):
        """
        Set channel to be RAMP waveform, set frequency, amplitude, offset and phase.

        Args:
            frequency: Frequency value of waveform, string format, unit: Hz
            amplitude: Amplitude value of waveform, string format, unit: Vpp
            offset: Offset value of waveform, string format, unit: Vdc
            phase: Phase value of waveform, string format, unit: dge
            channel: Channel number, string format, 2 options: 1 / 2
        """
        command = ':SOURce' + str(channel) + ':APPL:RAMP ' \
                  + str(frequency) + ',' + str(amplitude) + ',' + str(offset) + ',' + str(phase)
        self.control.write(command)
        L.debug(self.name + 'set channel: ' + str(channel)
                + ', waveform: RAMP'
                + ', frequency: ' + str(frequency) + 'Hz'
                + ', amplitude: ' + str(amplitude) + 'Vpp'
                + ', offset: ' + str(offset) + 'Vdc'
                + ', phase: ' + str(phase) + 'dge'
                )
        self.check_error()

    def set_channel_sin_parameter(self, frequency, amplitude, offset=0, phase=0, channel=1):
        """
        Set channel to be SIN waveform, set frequency, amplitude, offset and phase.

        Args:
            frequency: Frequency value of waveform, string format, unit: Hz
            amplitude: Amplitude value of waveform, string format, unit: Vpp
            offset: Offset value of waveform, string format, unit: Vdc
            phase: Phase value of waveform, string format, unit: dge
            channel: Channel number, string format, 2 options: 1 / 2
        """
        command = ':SOURce' + str(channel) + ':APPL:SIN ' \
                  + str(frequency) + ',' + str(amplitude) + ',' + str(offset) + ',' + str(phase)
        self.control.write(command)
        L.debug(self.name + 'set channel: ' + str(channel)
                + ', waveform: SIN'
                + ', frequency: ' + str(frequency) + 'Hz'
                + ', amplitude: ' + str(amplitude) + 'Vpp'
                + ', offset: ' + str(offset) + 'Vdc'
                + ', phase: ' + str(phase) + 'dge'
                )
        self.check_error()

    def set_channel_squ_parameter(self, frequency, amplitude, offset=0, phase=0, channel=1):
        """
        Set channel to be SQU waveform, set frequency, amplitude, offset and phase.

        Args:
            frequency: Frequency value of waveform, string format, unit: Hz
            amplitude: Amplitude value of waveform, string format, unit: Vpp
            offset: Offset value of waveform, string format, unit: Vdc
            phase: Phase value of waveform, string format, unit: dge
            channel: Channel number, string format, 2 options: 1 / 2
        """
        command = ':SOURce' + str(channel) + ':APPL:SQU ' \
                  + str(frequency) + ',' + str(amplitude) + ',' + str(offset) + ',' + str(phase)
        self.control.write(command)
        L.debug(self.name + 'set channel: ' + str(channel)
                + ', waveform: SQU'
                + ', frequency: ' + str(frequency) + 'Hz'
                + ', amplitude: ' + str(amplitude) + 'Vpp'
                + ', offset: ' + str(offset) + 'Vdc'
                + ', phase: ' + str(phase) + 'dge'
                )
        self.check_error()

    def set_channel_tri_parameter(self, frequency, amplitude, offset=0, phase=0, channel=1):
        """
        Set channel to be TRI waveform, set frequency, amplitude, offset and phase.

        Args:
            frequency: Frequency value of waveform, string format, unit: Hz
            amplitude: Amplitude value of waveform, string format, unit: Vpp
            offset: Offset value of waveform, string format, unit: Vdc
            phase: Phase value of waveform, string format, unit: dge
            channel: Channel number, string format, 2 options: 1 / 2
        """
        command = ':SOURce' + str(channel) + ':APPL:TRI ' \
                  + str(frequency) + ',' + str(amplitude) + ',' + str(offset) + ',' + str(phase)
        self.control.write(command)
        L.debug(self.name + 'set channel: ' + str(channel)
                + ', waveform: TRI'
                + ', frequency: ' + str(frequency) + 'Hz'
                + ', amplitude: ' + str(amplitude) + 'Vpp'
                + ', offset: ' + str(offset) + 'Vdc'
                + ', phase: ' + str(phase) + 'dge'
                )
        self.check_error()

    def set_channel_user_parameter(self, frequency, amplitude, offset=0, phase=0, channel=1):
        """
        Set channel to be any waveform, set frequency, amplitude, offset and phase.

        Args:
            frequency: Frequency value of waveform, string format, unit: Hz
            amplitude: Amplitude value of waveform, string format, unit: Vpp
            offset: Offset value of waveform, string format, unit: Vdc
            phase: Phase value of waveform, string format, unit: dge
            channel: Channel number, string format, 2 options: 1 / 2
        """
        command = ':SOURce' + str(channel) + ':APPL:USER ' \
                  + str(frequency) + ',' + str(amplitude) + ',' + str(offset) + ',' + str(phase)
        self.control.write(command)
        L.debug(self.name + 'set channel: ' + str(channel)
                + ', waveform: USER'
                + ', frequency: ' + str(frequency) + 'Hz'
                + ', amplitude: ' + str(amplitude) + 'Vpp'
                + ', offset: ' + str(offset) + 'Vdc'
                + ', phase: ' + str(phase) + 'dge'
                )
        self.check_error()

    def set_channel_frequency(self, frequency, channel=1):
        """
        Set channel's frequency

        Args:
            frequency: Frequency value of waveform, string format, unit: Hz
            channel: Channel number, string format, 2 options: 1 / 2
        """
        command = ':SOURce' + str(channel) + ':FREQ ' + str(frequency)
        self.control.write(command)
        L.debug(self.name + 'set channel: ' + str(channel)
                + ', frequency: ' + str(frequency) + 'Hz'
                )
        self.check_error()

    def set_channel_mode_frequency(self, channel=1):
        """
        Set channel into frequency mode

        Args:
            channel: Channel number, string format, 2 options: 1 / 2
        """
        command = ':SOURce' + str(channel) + ':FUNC:ARB:MODE FREQ'
        self.control.write(command)
        L.debug(self.name + 'set channel: ' + str(channel)
                + ' into frequency mode'
                )
        self.check_error()

    def set_channel_mode_sample(self, channel=1):
        """
        Set channel into sample rate mode

        Args:
            channel: Channel number, string format, 2 options: 1 / 2
        """
        command = ':SOURce' + str(channel) + ':FUNC:ARB:MODE SRATE'
        self.control.write(command)
        L.debug(self.name + 'set channel: ' + str(channel)
                + ' into sample rate mode'
                )
        self.check_error()

    def set_channel_sample(self, sample, channel=1):
        """
        Set channel's sample rate

        Args:
            sample: Sample rate, string format, unit: Sa/s
            channel: Channel number, string format, 2 options: 1 / 2
        """
        command = ':SOURce' + str(channel) + ':FUNC:ARB:SRAT ' + str(sample)
        self.control.write(command)
        L.debug(self.name + 'set channel: ' + str(channel)
                + ', sample: ' + str(sample) + 'Sa/s'
                )
        self.check_error()

    def set_channel_type(self, type, channel=1):
        """
        Set channel's waveform type

        Type range:
            SINusoid|SQUare|RAMP| PULSe|NOISe|USER|HARMonic|DC|KAISER|ROUNDPM|SINC|NEGRAMP|
            ATTALT|AMPALT|STAIRDN|STAIRUP|STAIRUD|CPULSE|PPULSE|NPULSE|TRAPEZIA|
            ROUNDHALF|ABSSINE|ABSSINEHALF|SINETRA|SINEVER|EXPRISE|EXPFALL|TAN|COT|
            SQRT|X2DATA|GAUSS|HAVERSINE|LORENTZ|DIRICHLET|GAUSSPULSE|AIRY|
            CARDIAC|QUAKE|GAMMA|VOICE|TV|COMBIN|BANDLIMITED|STEPRESP|
            BUTTERWORTH|CHEBYSHEV1|CHEBYSHEV2|BOXCAR|BARLETT|TRIANG|BLACKMAN|
            HAMMING|HANNING|DUALTONE|ACOS|ACOSH|ACOTCON|ACOTPRO|ACOTHCON|
            ACOTHPRO|ACSCCON|ACSCPRO|ACSCHCON|ACSCHPRO|ASECCON|ASECPRO|ASECH|
            ASIN|ASINH|ATAN|ATANH|BESSELJ|BESSELY|CAUCHY|COSH|COSINT|COTHCON|
            COTHPRO|CSCCON|CSCPRO|CSCHCON|CSCHPRO|CUBIC|ERF|ERFC|ERFCINV|ERFINV|
            LAGUERRE|LAPLACE|LEGEND|LOG|LOGNORMAL|MAXWELL|RAYLEIGH|RECIPCON|
            RECIPPRO|SECCON|SECPRO|SECH|SINH|SININT|TANH|VERSIERA|WEIBULL|
            BARTHANN|BLACKMANH|BOHMANWIN|CHEBWIN|FLATTOPWIN|NUTTALLWIN|
            PARZENWIN|TAYLORWIN|TUKEYWIN|CWPUSLE|LFPULSE|LFMPULSE|EOG|EEG|EMG|
            PULSILOGRAM|TENS1|TENS2|TENS3|SURGE|DAMPEDOSC|SWINGOSC|RADAR|
            THREEAM|THREEFM|THREEPM|THREEPWM|THREEPFM|RESSPEED|MCNOSIE|
            PAHCUR|RIPPLE|ISO76372TP1|ISO76372TP2A|ISO76372TP2B|ISO76372TP3A|
            ISO76372TP3B|ISO76372TP4|ISO76372TP5A|ISO76372TP5B|ISO167502SP|
            ISO167502VR|SCR|IGNITION|NIMHDISCHARGE|GATEVIBR

        Args:
            type: Type of waveform, string format, see above type range.
            channel: Channel number, string format, 2 options: 1 / 2
        """
        command = ':SOURce' + str(channel) + ':FUNC ' + str(type)
        self.control.write(command)
        L.debug(self.name + 'set channel: ' + str(channel)
                + ' to be ' + str(type) + ' waveform'
                )
        self.check_error()
