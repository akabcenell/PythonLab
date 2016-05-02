from src.instruments import microwave_generator
from src.core.scripts import Script
from PySide.QtCore import Signal, QThread

# import standard libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import time
import pandas as pd
from PyQt4 import QtGui
from src.core import Parameter
from src.instruments import MicrowaveGenerator, DAQ

class StanfordResearch_ESR(Script):
    # NOTE THAT THE ORDER OF Script and QThread IS IMPORTANT!!
    _DEFAULT_SETTINGS = Parameter([
        Parameter('path', 'Z:/Lab/Cantilever/Measurements/----data_tmp_default----', str, 'path for data'),
        Parameter('tag', 'dummy_tag', str, 'tag for data'),
        Parameter('save', True, bool, 'save data on/off'),
        Parameter('power_out', -45.0, float, 'output power (dBm)'),
        Parameter('esr_avg', 50, int, 'number of esr averages'),
        Parameter('freq_start', 2.82e9, float, 'start frequency of scan'),
        Parameter('freq_stop', 2.92e9, float, 'end frequency of scan'),
        Parameter('freq_points', 100, int, 'number of frequencies in scan'),
        Parameter('integration_time', 0.01, float, 'measurement time of fluorescent counts'),
        Parameter('settle_time', .0002, float, 'time to allow system to equilibrate after changing microwave powers')
        # Parameter('runs_between_focusing', 10, int, 'runs after which we refocus - not implemented yet!!!')
    ])

    _INSTRUMENTS = {
        'microwave_generator': MicrowaveGenerator,
        'daq' : DAQ
    }

    _SCRIPTS = {

    }
    updateProgress = Signal(int)

    def __init__(self, instruments, scripts = None, name=None, settings=None, log_output=None):
        """
        Example of a script that emits a QT signal for the gui
        Args:
            name (optional): name of script, if empty same as class name
            settings (optional): settings for this script, if empty same as default settings
        """
        self._abort = False
        Script.__init__(self, name, settings=settings, scripts=scripts, instruments=instruments, log_output=log_output)
        QThread.__init__(self)

    def _function(self):
        """
        This is the actual function that will be executed. It uses only information that is provided in the settings property
        will be overwritten in the __init__
        """
        self.freq_values = np.linspace(self.settings['freq_start'], self.settings['freq_stop'], self.settings['freq_points'])
        freq_range = max(self.freq_values) - min(self.freq_values)
        num_freq_sections = int(freq_range) / int(self.instruments['microwave_generator'].settings['dev_width']*2) + 1
        clock_adjust = int((self.settings['integration_time'] + self.settings['settle_time']) / self.settings['settle_time'])
        freq_array = np.repeat(self.freq_values, clock_adjust)
        (self.settings['integration_time'] + self.settings['settle_time']) / clock_adjust
        self.instruments['microwave_generator'].update({'amplitude': self.settings['power_out']})

        # move to NV point if given
        # if not (nv_x is None):
        #     move_to_NV((nv_x, nv_y))

        esr_data = np.zeros((self.settings['esr_avg'], len(self.freq_values)))
        converge_data = []

        # run sweeps
        for scan_num in xrange(0, self.settings['esr_avg']):
            if self._abort:
                break
            print("Scan Number: " + str(scan_num))
            esr_data_pos = 0
            self.instruments['microwave_generator'].update({'enable_output': True})
            for sec_num in xrange(0, num_freq_sections):
                # initialize APD thread

                # calculate the minimum ad and max frequency of current section
                sec_min = min(self.freq_values) + self.settings['dev_width']*2 * sec_num
                sec_max = sec_min + self.settings['dev_width']*2

                # make freq. array for current section
                freq_section_array = freq_array[np.where(np.logical_and(freq_array >= sec_min,
                                                                        freq_array < sec_max))]
                # if section is empty skip
                if len(freq_section_array) == 0:
                    continue
                center_freq = (sec_max + sec_min) / 2.0
                freq_voltage_array = ((
                                      freq_section_array - sec_min) / (self.settings['dev_width']*2)) * 2 - 1  # normalize voltages to +-1 range

                self.instruments['microwave_generator'].update({'frequency': center_freq})

                self.instruments['daq'].DI_init(["ctr0"],  len(freq_voltage_array) + 1, sample_rate_multiplier=(clock_adjust- 1))
                self.instruments['daq'].AO_init(["ao2"], freq_voltage_array)

                # start counter and scanning sequence
                self.instruments['daq'].DI_run()
                self.instruments['daq'].AO_run()
                self.instruments['daq'].AO_waitToFinish()
                self.instruments['daq'].AO_stop()

                raw_data, _ = self.instruments['daq'].DI_read()

                # raw_data = sweep_mw_and_count_APD(freq_voltage_array, dt)
                # counter counts continiously so we take the difference to get the counts per time interval
                diff_data = np.diff(raw_data)
                summed_data = np.zeros(len(freq_voltage_array) / clock_adjust)
                for i in range(0, int((len(freq_voltage_array) / clock_adjust))):
                    summed_data[i] = np.sum(diff_data[(i * clock_adjust + 1):(i * clock_adjust + clock_adjust - 1)])
                # also normalizing to kcounts/sec
                esr_data[scan_num, esr_data_pos:(esr_data_pos + len(summed_data))] = summed_data * (.001 / int_time)
                esr_data_pos += len(summed_data)

                # clean up APD tasks
                self.instruments['daq'].DI_stop()

            self.esr_avg = np.mean(esr_data[0:(scan_num + 1)], axis=0)
            self.fit_params, _ = self.fit_esr(self.freq_values, self.esr_avg)

            self.plot()
            self.updateProgress.emit(self.calc_progress)


        if self.settings['save']:
            self.save()

        self.instruments['microwave_generator'].update({'enable_output': False})
        print('finished')
        # plt.show()
        return self.esr_avg, self.fit_params

        def calc_progress():
            return np.round(scan_num/self.settings['esr_avg'])

        # send 100 to signal that script is finished
        self.updateProgress.emit(100)

    def plot(self, axes):
        if not self.fit_params[0] == -1:  # check if fit failed
            fit_data = self.lorentzian(self.freq_values, self.fit_params[0], self.fit_params[1], self.fit_params[2], self.fit_params[3])
        else:
            fit_data = None
        fig = axes.get_figure()
        fig.clf()
        if fit_data: # plot esr and fit data
            axes.plot(self.freq_values, self.esr_data, 'b', self.freq_values, fit_data, 'r')
            axes.set_title('ESR')
            axes.set_xlabel('Frequency (Hz)')
            axes.set_ylabel('Kcounts/s')
        else: #plot just esr data
            axes.plot(self.freq_values, self.esr_data, 'b')
            axes.set_title('ESR')
            axes.set_xlabel('Frequency (Hz)')
            axes.set_ylabel('Kcounts/s')

    def stop(self):
        self._abort = True

    # fit ESR curve to lorentzian and return fit parameters. If initial guess known, put in fit_start_params, otherwise
    # guesses reasonable initial values.
    def fit_esr(self, freq_values, esr_data, fit_start_params=None):
        if (fit_start_params is None):
            offset = np.mean(esr_data)
            amplitude = np.max(esr_data) - np.min(esr_data)
            center = freq_values[esr_data.argmin()]
            width = 10000000  # 10 MHz arbitrarily chosen as reasonable
            fit_start_params = [amplitude, width, center, offset]
        try:
            return opt.curve_fit(self.lorentzian, freq_values, esr_data, fit_start_params)
        except RuntimeError:
            print('Lorentzian fit failed')
            return (-1, -1, -1, -1), 'Ignore'

    # defines a lorentzian with some amplitude, width, center, and offset to use with opt.curve_fit
    def lorentzian(self, x, amplitude, width, center, offset):
        return (-(amplitude*(.5*width)**2)/((x-center)**2+(.5*width)**2))+offset