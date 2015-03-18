
SA_MAX_DEVICES = 8

saDeviceTypeNone = 0
saDeviceTypeSA44 = 1
saDeviceTypeSA44B = 2
saDeviceTypeSA124A= 3
saDeviceTypeSA124B = 4


sa44_MIN_FREQ = 1.0
sa124_MIN_FREQ = 100.0e3
sa44_MAX_FREQ = 4.4e9
sa124_MAX_FREQ = 13.0e9
sa_MIN_SPAN = 1.0
sa_MAX_REF = 20
sa_MAX_ATTEN = 3
sa_MAX_GAIN = 2
sa_MIN_RBW = 0.1
sa_MAX_RBW = 6.0e6
sa_MIN_RT_RBW = 100.0
sa_MAX_RT_RBW = 10000.0
sa_MIN_IQ_BANDWIDTH = 100.0
sa_MAX_IQ_DECIMATION = 128

sa_IQ_SAMPLE_RATE = 486111.111

sa_IDLE      = -1
sa_SWEEPING  = 0x0
sa_REAL_TIME = 0x1
sa_IQ        = 0x2
sa_AUDIO     = 0x3
sa_TG_SWEEP  = 0x4

sa_MIN_MAX = 0x0
sa_AVERAGE = 0x1

sa_LOG_SCALE      = 0x0
sa_LIN_SCALE      = 0x1
sa_LOG_FULL_SCALE = 0x2
sa_LIN_FULL_SCALE = 0x3

sa_AUTO_ATTEN = -1
sa_AUTO_GAIN  = -1

sa_LOG_UNITS   = 0x0
sa_VOLT_UNITS  = 0x1
sa_POWER_UNITS = 0x2 
sa_BYPASS      = 0x3

sa_AUDIO_AM  = 0x0
sa_AUDIO_FM  = 0x1
sa_AUDIO_USB = 0x2
sa_AUDIO_LSB = 0x3
sa_AUDIO_CW  = 0x4

TG_THRU_0DB  = 0x1
TG_THRU_20DB  = 0x2

saUnknownErr = -666

saFrequencyRangeErr = -99
saInvalidDetectorErr = -95
saInvalidScaleErr = -94
saBandwidthErr = -91
saExternalReferenceNotFound = -89
	
saOvenColdErr = -20

saInternetErr = -12
saUSBCommErr = -11

saTrackingGeneratorNotFound = -10
saDeviceNotIdleErr = -9
saDeviceNotFoundErr = -8
saInvalidModeErr = -7
saNotConfiguredErr = -6
saTooManyDevicesErr = -5
saInvalidParameterErr = -4
saDeviceNotOpenErr = -3
saInvalidDeviceErr = -2
saNullPtrErr = -1

saNoError = 0

saNoCorrections = 1
saCompressionWarning = 2
saParameterClamped = 3
saBandwidthClamped = 4


# SA_API saStatus saGetSerialNumberList(int serialNumbers[8], int *deviceCount);
# SA_API saStatus saOpenDeviceBySerialNumber(int *device, int serialNumber);
# SA_API saStatus saOpenDevice(int *device);
# SA_API saStatus saCloseDevice(int device);
# SA_API saStatus saPreset(int device);

# SA_API saStatus saGetSerialNumber(int device, int *serial);
# SA_API saStatus saGetFirmwareString(int device, char firmwareString[16]);
# SA_API saStatus saGetDeviceType(int device, saDeviceType *device_type);
# SA_API saStatus saConfigAcquisition(int device, int detector, int scale);
# SA_API saStatus saConfigCenterSpan(int device, double center, double span);
# SA_API saStatus saConfigLevel(int device, double ref);
# SA_API saStatus saConfigGainAtten(int device, int atten, int gain, bool preAmp);
# SA_API saStatus saConfigSweepCoupling(int device, double rbw, double vbw, bool reject);
# SA_API saStatus saConfigProcUnits(int device, int units);
# SA_API saStatus saConfigIQ(int device, int decimation, double bandwidth);
# SA_API saStatus saConfigAudio(int device, int audioType, double centerFreq,
#                               double bandwidth, double audioLowPassFreq, 
#                               double audioHighPassFreq, double fmDeemphasis);
# SA_API saStatus saEnableExternalReference(int device);

# SA_API saStatus saInitiate(int device, int mode, int flag);
# SA_API saStatus saAbort(int device);

# SA_API saStatus saQuerySweepInfo(int device, int *sweepLength, double *startFreq, double *binSize);
# SA_API saStatus saQueryStreamInfo(int device, int *returnLen, double *bandwidth, double *samplesPerSecond);
# SA_API saStatus saGetSweep_32f(int device, float *min, float *max);
# SA_API saStatus saGetSweep_64f(int device, double *min, double *max);
# SA_API saStatus saGetPartialSweep_32f(int device, float *min, float *max, int *start, int *stop);
# SA_API saStatus saGetPartialSweep_64f(int device, double *min, double *max, int *start, int *stop);
# SA_API saStatus saGetIQ_32f(int device, float *iq);
# SA_API saStatus saGetIQ_64f(int device, double *iq);
# SA_API saStatus saGetAudio(int device, float *audio);
# SA_API saStatus saQueryTemperature(int device, float *temp);
# SA_API saStatus saQueryDiagnostics(int device, float *voltage);

# SA_API saStatus saAttachTg(int device);
# SA_API saStatus saIsTgAttached(int device, bool *attached);
# SA_API saStatus saConfigTgSweep(int device, int sweepSize, bool highDynamicRange, bool passiveDevice);
# SA_API saStatus saStoreTgThru(int device, int flag);
# SA_API saStatus saSetTg(int device, double frequency, double amplitude);

# SA_API saStatus saConfigIFOutput(int device, double inputFreq, double outputFreq,
#                                  int inputAtten, int outputGain);
# SA_API saStatus saSelfTest(int device, saSelfTestResults *results);

# SA_API const char* saGetAPIVersion();
# SA_API const char* saGetErrorString(saStatus code);
'''
SA_API saStatus saOpenDevice(int *device);
SA_API saStatus saCloseDevice(int device);

SA_API saStatus saConfigureAcquisition(int device, unsigned int detector, unsigned int scale);
SA_API saStatus saConfigureCenterSpan(int device, double center, double span);
SA_API saStatus saConfigureLevel(int device, double ref, double atten);
SA_API saStatus saConfigureGain(int device, int gain);
SA_API saStatus saConfigureSweepCoupling(int device, double rbw, double vbw, double sweepTime, unsigned int rbwType, unsigned int rejection);
SA_API saStatus saConfigureWindow(int device, unsigned int window);
SA_API saStatus saConfigureProcUnits(int device, unsigned int units);
SA_API saStatus saConfigureTrigger(int device, unsigned int type, unsigned int edge, double level, double timeout);
SA_API saStatus saConfigureTimeGate(int device, double delay, double length, double timeout);
SA_API saStatus saConfigureRawSweep(int device, int start, int ppf, int steps, int stepsize);
SA_API saStatus saConfigureIO(int device, unsigned int port1, unsigned int port2);
SA_API saStatus saConfigureDemod(int device, int modulationType, double freq, float IFBW, float audioLowPassFreq, float audioHighPassFreq, float FMDeemphasis);

SA_API saStatus saInitiate(int device, unsigned int mode, unsigned int flag);

SA_API saStatus saFetchTrace(int device, int arraySize, double *min, double *max);
SA_API saStatus saFetchAudio(int device, float *audio);
SA_API saStatus saFetchRawCorrections(int device, float *corrections, int *index, double *startFreq);
SA_API saStatus saFetchRaw(int device, float *buffer, int *triggers);
SA_API saStatus saFetchRaw_s(int device, short *buffer, int *triggers);
SA_API saStatus saFetchRawSweep(int device, short *buffer);
SA_API saStatus saStartRawSweepLoop(int device, void(*sweep_callback)(short *buffer, int len));

SA_API saStatus saQueryTraceInfo(int device, unsigned int *traceLen, double *binSize, double *start);
sa_API saStatus saQueryStreamingCenter(int device, double *center);
sa_API saStatus saQueryTimestamp(int device, unsigned int *seconds, unsigned int *nanoseconds);
sa_API saStatus saQueryDiagnostics(int device, float *temperature, float *voltage1_8, float *voltage1_2, float *voltageUSB, float *currentUSB);

sa_API saStatus saAbort(int device);
sa_API saStatus saPreset(int device);
sa_API saStatus saSelfCal(int device);
sa_API saStatus saSyncCPUtoGPS(int comPort, int baudRate);

sa_API saStatus saGetDeviceType(int device, int *type);
sa_API saStatus saGetSerialNumber(int device, unsigned int *sid);
sa_API saStatus saGetFirmwareVersion(int device, int *version);

sa_API const char* saGetAPIVersion();
sa_API const char* saGetErrorString(saStatus status);
'''