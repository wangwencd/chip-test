import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'framework'))
import PBCore

spi_configured:bool = False

def SPI_config(**kwargs):
    spi_cfg = {'cfg': 1, 'fstb':'MSB', 'cpol': 'HIGHLEVEL', 'cpha': 'SECOND', 'size': 'HALF_WD', 'cspol': 'LOWEN', 'freq': 'SPI_187P5Khz', 'bus_num': 1, 'data_buf': [], 'rx_size': 0, 'proto_type': 'SPI_Proto'}
    tx_buf = []
    global spi_configured
    spi_configured = True

    if 'fstb' in kwargs:
        spi_cfg['fstb'] = kwargs.get('fstb')
    
    if 'cpol' in kwargs:
        spi_cfg['cpol'] = kwargs.get('cpol')

    if 'cpha' in kwargs:
        spi_cfg['cpha'] = kwargs.get('cpha')

    if 'size' in kwargs:
        spi_cfg['size'] = kwargs.get('size')

    if 'cspol' in kwargs:
        spi_cfg['cspol'] = kwargs.get('cspol')

    if 'freq' in kwargs:
        spi_cfg['freq'] = kwargs.get('freq')

    if 'tx_data' in kwargs:
        tx_data = kwargs.get('tx_data')
        tx_buf = tx_buf + tx_data
        spi_cfg['data_buf'] = tx_buf

    if 'rx_size' in kwargs:
        spi_cfg['rx_size'] = kwargs.get('rx_size')

    return PBCore.com_transimit_read(**spi_cfg)
    
def SPI_trans(**kwargs):
    spi_info = {'bus_num': 1, 'data_buf': [], 'rx_size': 0, 'proto_type': 'SPI_Proto'}
    tx_buf = []
    global spi_configured

    if spi_configured == False:
        # raise Exception('SPI has none initialed!')
        print('SPI has not initialized yet, and will use the default configure:')
        print('MSB, CPOL=1, CPHA=1, 16bit, CSPOL=0, FREQ=SPI_187.5Khz')
        return SPI_config(**kwargs)

    if 'tx_data' in kwargs:
        tx_data = kwargs.get('tx_data')
        tx_buf = tx_buf + tx_data
        spi_info['data_buf'] = tx_buf

    if 'rx_size' in kwargs:
        spi_info['rx_size'] = kwargs.get('rx_size')

    return PBCore.com_transimit_read(**spi_info)
