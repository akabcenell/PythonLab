from src.core import Script, Parameter
from PySide.QtCore import Signal, QThread
from collections import deque
import numpy as np
from src.instruments import NI7845RPidSimpleLoop
import time
from copy import deepcopy

class LabviewFpgaTimetrace(Script, QThread):
    updateProgress = Signal(int)

    _DEFAULT_SETTINGS = Parameter([
        Parameter('path',  'C:\\Users\\Experiment\\Desktop\\tmp_data', str, 'path to folder where data is saved'),
        Parameter('tag', 'some_name'),
        Parameter('save', True, bool,'check to automatically save data'),
        Parameter('dt', 200, int, 'sample period of acquisition loop in ticks (40 MHz)'),
        Parameter('N', 2000, int, 'numer of samples'),
        Parameter('TimeoutBuffer', 0, int, 'time after which buffer times out in clock ticks (40MHz)'),
        Parameter('BlockSize', 1000, int, 'block size of chunks that are read from FPGA'),
    ])

    _INSTRUMENTS = {'fpga' : NI7845RPidSimpleLoop}

    _SCRIPTS = {}

    def __init__(self, instruments, name = None, settings = None, log_output = None):

        self._recording = False

        Script.__init__(self, name, settings, instruments, log_output = log_output)
        QThread.__init__(self)

        self.data = deque()



    def _function(self):
        """
        This is the actual function that will be executed. It uses only information that is provided in the settings property
        will be overwritten in the __init__
        """

        def calculate_progress(loop_index):
            progress = int(100.0 * loop_index / number_of_reads)

        self._recording = True
        self.data.clear() # clear data queue

        # reset FIFO
        block_size = self.settings['BlockSize']
        self.instruments['fpga'].update({'fifo_size' :block_size * 2})
        time.sleep(0.1)
        self.instruments['fpga'].start_fifo()
        time.sleep(0.1)
        number_of_reads = int(np.ceil(1.0 * self.settings['N'] / self.settings['BlockSize']))
        print('number_of_reads', number_of_reads)
        N_actual = number_of_reads * block_size
        if N_actual!=self.settings['N']:
            self.log('warning blocksize not comensurate with number of datapoints, set N = {:d}'.format(N_actual))
            self.settings.update({'N' : N_actual})
            time.sleep(0.1)

        # apply settings to instrument
        instr_settings = {
            'SamplePeriodsAcq' : self.settings['dt'],
            'ElementsToWrite' : self.settings['N'],
            'TimeoutBuffer' : self.settings['TimeoutBuffer']

        }
        self.instruments['fpga'].update(instr_settings)
        time.sleep(0.1)
        self.instruments['fpga'].update({'Acquire' : True})

        time.sleep(1)

        print('ElementsWritten: ', self.instruments['fpga'].ElementsWritten)

        ai1 = np.zeros(N_actual)
        for i in range(number_of_reads):
            data = self.instruments['fpga'].read_fifo(block_size)
            print(i, 'ddd', data)
            print('block_size', block_size)
            ai1[i* block_size:(i+1)*block_size] = deepcopy(data['AI1'])
            # append data to queue
            self.data.append({
                'AI1' : ai1
            })


            progress = calculate_progress(i)

            self.updateProgress.emit(progress)

        self._recording = False
        progress = 100 # make sure that progess is set 1o 100 because we check that in the old_gui

        if self.settings['save']:
            self.save()


    def plot(self, axes):

        r = self.data[-1]['AI1']
        axes.plot(r)



if __name__ == '__main__':

    fpga = NI7845RPidSimpleLoop()

        # reset FIFO
    block_size = 100

    N= 400
    dt = 2000


    fpga.update({'fifo_size': block_size * 2})
    time.sleep(0.1)
    fpga.start_fifo()
    time.sleep(0.1)
    number_of_reads = int(np.ceil(1.0 * N / block_size))
    print('number_of_reads', number_of_reads)
    N_actual = number_of_reads * block_size

    # apply settings to instrument
    instr_settings = {
        'SamplePeriodsAcq': dt,
        'ElementsToWrite': N,
        'TimeoutBuffer': 100

    }
    fpga.update(instr_settings)
    time.sleep(0.1)

    print('----------')
    print(fpga.settings)
    print('----------')

    print('ElementsWritten: ', fpga.ElementsWritten)
    fpga.update({'Acquire': True})

    # time.sleep(1)
    print(fpga.settings)




    ai1 = np.zeros(N_actual)
    i = 0
    while i < number_of_reads:
        elem_written = fpga.ElementsWritten
        if elem_written>=block_size:
            data = fpga.read_fifo(block_size)
            # print(i, 'AI1', data['AI1'])
            print(i, 'elements_remaining', data['elements_remaining'])
            ai1[i * block_size:(i + 1) * block_size] = deepcopy(data['AI1'])
            i += 1

        print('-----', i, '------', 'elem_written', elem_written)

