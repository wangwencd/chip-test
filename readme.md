AutoTest Version

20220705-initial commit
1.Initial version

20220804-add visa command, add exceptions, add logging, add file_operation
1.Add visa protocol class
2.Add exception class
3.Add logging class
4.Add file operation function

20220810-add serial protocol and 2400 control command
1.Add serial protocol class
2.Add 2400 instrument code

20220815-add multiprocess and flow
1.Add message multiprocess class
2.Add control flow 
3.Add E36312A instrument code
4.Add IT8811 instrument code

20220822-modify control interface
1.Modify file operation code error
2.Modify 2400 instrument exception
3.Modify message multiprocess class
4.Modify queue class
5.Modify condition class

20220829-add instrument 2450
1.Add 2450 instrument code
2.Modify 2400 instrument code

20220901-add rtu and DL11B
1.Add modbus-RTU protocol class
2.Add DL11B instrument code
3.Modify file operation code error

20220908-add whole sop of battery lab
1.Add battery lab sop code
2.Add battery lab parse, output code
3.Modify condition class code

20220930-modify sop and add main ui
1.Modify battery lab sop code error
2.Add mainwindow UI

20221024-add DG1062Z
1.Add DG1062Z instrument code

20221107-add DHT260
1.Add DHT260 instrument code
2.Modify battery lab sop code, including temperature control.
3.Modify project structure for installering.
4.Modify some code error

20221107-add instrument ui
1.Add instrumentwindow UI
2.Add 5 instruments control function on instrumentwindow UI

20221127-add custom test, finish total battery lab sop, add threadpool
1.Modify project name as AutoTest
2.Add custom test sop code
3.Finish battery lab sop
4.Modify multiprocess method, using threadpool.

20230109-add MAX32670 control code, add MCU control UI
1.Add MAX32670 instrument code
2.Add mcuwindow UI
3.Modify some code error

20230201-add lithium test flow, add lithium test UI
1.Add lithium test sop, including GPADC, CCADC, ADS1115 auto-test flow.
2.Add lithium test interface on mainwindow UI.
3.Add list of third-party libraries python needed.
4.Modify some code error

20230207-add 2450 control UI
1.Add 2450 control UI
2.Add add lithium test measurement period
3.Add code version log

20230303-modify lithium test
1.Modify lithium test gpadc/ ccadc accuracy test flow.
2.Add lithium test adc deviation, external clk, otp, uv/od delay test and so on.
3.Add tool function, could generate ADC fitting result and deviation result.
4.Add lithium test UI function

20230314-add code density method
1.Add lithium test code density test flow.
2.Add plot_dnl function in tool, could calculate dnl from original data and generate figure.
3.Add many comments of python code, enhance code readability.
4.Add DNL test function at lithium test UI.

20230410-modify DNL algorithm
1.Modify DNL algorithm.
2.Modify code density test method.
3.Add max counts of displayed log on mainwindow.
4.Add size limit of log file(every file 50M max).

20230412-redesign main UI
1.Redesign mainwindow UI(v2.00.00).
2.Add function of generating and reading old config.
3.Add sending results into .ini function.
4.Optimize lithium test flow code.
5.Optimize DNL algorithm.

20230428-add lithium otp bgr test
1.Add lithium OTP BGR test method.
2.Modify battery lab test method.
3.Add 2450 instrument 4-wire sense mode function.
4.Modify mainwindow control error.

20230529-add DMM7510 instrument control code
1.Add DMM7510 instrument control code.
2.Modify DL11B instrument funciton error.
3.Modify output process function error.
4.Add venus test.

20230629-add venus control UI
1.Add venus test control UI.
2.Add DMM7510 new functions.
3.Supply venus test flow code.
4.Modify 2450 code error.

20230726-add jupiter test
1.Add jupiter test flow and UI.
2.Add B2912A instrument control code and UI.
3.Add B2910BL instrument control code.
4.Add F413CH CMU control code and UI.
5.Add ramp and best-fit calculation method.

20230822-add jupiter test option
1.Add jupiter test option.
2.Add DMM7510 auto impedence funciton.

20230926-modify jupiter test flow
1.Modify jupiter ramp test flow, which is checked.

20231031-add natrium test flow
1.Add natrium test flow, which is checked.
2.Add B2912B instrument control code.

20231110-update i2c probo
1.Update I2C probobuf, increase i2c communication success rate.
2.Modify natrium test flow, increase test stability.
3.Modify mcu control UI, make it more convenient.

20231120-Modify instrument UI
1.Modify instrument control UI, make it more convenient.
2.Add DP832 instrument control code.

20231205-add tcp/ip protocol
1.Add tcp/ip control protocol, add tcp/ip protocol on instrument UI
2.Add DHT260 control method by tcp/ip.
3.Add natrium temperature test flow.

20231218-modify MAX32670 i2c error
1.Modify MAX32670 i2c frequency not working error.
2.Modify average_flag causing output info error in natrium test flow. # chip-test
