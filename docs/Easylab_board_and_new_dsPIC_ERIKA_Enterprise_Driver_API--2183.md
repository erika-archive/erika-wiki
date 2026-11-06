# Easylab board and new dsPIC ERIKA Enterprise Driver API

<a id="Introduction"></a>

## Introduction

During the development of Erika support for easylab some new API have created and other ones have been updated.
Follow an overview of these changes, but to be sure that the information of this page are updated double check the code.

<a id="Easylab_Board_API"></a>

## Easylab Board API

The [EasyLab board](http://www.evidence.eu.com/products/easy-lab.html) is fully supported by [Erika Rtos](http://erika.tuxfamily.org/).
This chapter describes the API support done in Erika Enterprise for the Evidence EasyLab Board.
To configure the usage of the EasyLab Board, the user has to specify an appropriate **BOARD\_DATA** in *OIL* file , as in the following example:

```
...
BOARD_DATA = EE_EASYLAB {
...
}
...
```

this *OIL* element enable the inclusion of *pkg/board/ee\_easylab/inc/ee\_board.h* as board header.

<a id="System_LED"></a>

### **System LED**

The [Microstic](http://www.microchip.com/stellent/idcplg?IdcService=SS_GET_PAGE&nodeId=1406&dDocName=en548414) Guest board has a system LED attached to a GPIO pin of the microcontroller. To use the system LED, the developer should specify the **USELEDS** attribute as **TRUE**, as in the following example:

```
...
BOARD_DATA = EE_EASYLAB {
  USELEDS = TRUE;
  ...
}
...
```

The following paragraphs will describe the functions available to control the easyLab System LED.

- *void EE\_sys\_led\_init(void);*

  Description: Initialize the system LED (the one on microstick). The LED starts turned off.
- *void EE\_sys\_led\_on(void);*

  Description: The function turns on the system LED (the one on microstick).
- *void EE\_led\_sys\_off(void);*

  Description: The function turns off the system LED (the one on microstick).

<a id="Board_LEDs"></a>

### **Board LEDs**

The EasyLab includes 8 red LEDs. To use the board LEDs the developer have to specify the **USELEDS** attribute as **TRUE**, as in the following example (same *OIL* configuration of the **System LED**):

```
...
BOARD_DATA = EE_EASYLAB {
  USELEDS = TRUE;
  ...
}
...
```

The *API* for board LEDS control are the follow:

- *void EE\_leds\_init(void);*

  Description: Initialize all LEDS present on the board. The LEDs starts turned off.
- *void EE\_leds\_enable(void);*

  Description: Turn on all the LEDs present on the board (system LED too).
- *void EE\_leds\_disable(void);*

  Description: Turn off all the LEDs present on the board (system LED too).
- *void EE\_ledx\_init(void); (x=1,...,8)*

  Description: Initialize the LED**x** present on the board (x=1,...,8). The LED starts turned off.
- *void EE\_ledx\_on(void); (x=1,...,8)*

  Description: Turn on the LED**x** present on the board (x=1,...,8).
- *void EE\_led1\_off(void); (x=1,...,8)*

  Description: Turn off the LED**x** present on the board (x=1,...,8).
- *void EE\_led1\_toggle(void); (x=1,...,8)*

  Description: Toggle the LED**x** present on the board (x=1,...,8).

<a id="Digital_Pin_I.2FO"></a>

### **Digital Pin I/O**

The same pins connected to board LEDS can be used how general *Digital Pin I/O*. These pins are exported on board connectors.

For their use on the board the developer have to specify the **USE\_DIO** attribute as **TRUE**, as in the following example (same *OIL* configuration of the **DIO**):

```
...
BOARD_DATA = EE_EASYLAB {
  USEDIO = TRUE;
  ...
}
...
```

The *API* than uses the digital pins I/O (DIO) are the follow:

- *void EE\_diox\_configure(EE\_BIT in); (x=1,...,8)*

  Description: Initialize the pin**x** (x=1,...,8). If the **in** parameter is **0** (zero) the pin is output while **1** is input.
- *void EE\_diox\_write(EE\_BIT bit); (x=1,...,8)*

  Description: If the parameter **in=1** the output pin is **1** logic, while if the parameter **in=0** the output pin is **0** logic.
- *int EE\_BIT EE\_diox\_read(void); (x=1,...,8)*

  Description: The API return the logic value on pin**x** when it is configured as input.

<a id="Buzzer"></a>

### **Buzzer**

On the EasyLab board is present a simple piezo buzzer. When the users wants use it in a his project, he has to write, in the OIL file, something like this:

```
...
BOARD_DATA = EE_EASYLAB {
  USEBUZZER = TRUE;
  ...
}
...
```

The API are the follow:

- *void EE\_buzzer\_start(EE\_UINT16 freq);*

  Description: Start on the buzzer. The parameter **freq** is the frequency value and it's value is from 100 to 48000 Hz.
- *void EE\_buzzer\_stop(void);*

  Description: Turn off the buzzer sound.

<a id="ADC_Channels"></a>

### **ADC Channels**

The EasyLab board has 4 input analog to digital converter (ADCx). If an application uses the ADC functionality in necessary modified the OIL file adding the option USEADC:

```
...
BOARD_DATA = EE_EASYLAB {
  USEADC = TRUE;
  ...
}
...
```

The ADC's API are the follow:

- *EE\_INT8 EE\_easylab\_adc\_init\_ch(EE\_AdcChId adc\_ch\_id, EE\_Adc\_VoltageRef volt\_ref, EE\_Adc\_BitResolution bit\_res);*

  Description: Initialize an specific ADC channel. The parameter can be used are the follow:

  - **adc\_ch\_id**: Is the ADC channel, the value can be:
    - EE\_ADC\_AN1
    - EE\_ADC\_AN2
    - EE\_ADC\_AN3
    - EE\_ADC\_AN4
  - **volt\_ref** : Is the Ref for ADC conversion. At this parameter can be assigned the follow value:
    - *EE\_ADC\_VDD\_VSS*
    - *EE\_ADC\_VREFh\_VSS*
    - *EE\_ADC\_VDD\_VREFl*
    - *EE\_ADC\_VREFh\_VREFl*
  - **bit\_res** : Is the resolution of the ADC.
    - EE\_ADC\_10\_BIT
    - EE\_ADC\_12\_BIT
  - return value: 0 if no errors happened. Otherwise appropriate error value (negative value).
- *EE\_INT8 EE\_easylab\_adc\_get\_ch\_uint(EE\_AdcChId adc\_ch\_id, EE\_UINT16 \* value );*

  Description: Acquire analog value on specific input.

  - **adc\_ch\_id**: Channel's ID to acquire.
    - EE\_ADC\_AN1
    - EE\_ADC\_AN2
    - EE\_ADC\_AN3
    - EE\_ADC\_AN4
  - **\*value**: return value conversion pointer.
  - return value: 0 if no errors happened. Otherwise appropriate error value (negative value).
- *EE\_INT8 EE\_INT8 EE\_easylab\_adc\_start(void):*

  Description: Start ADC sampling.

  - return value: 0 if no errors happened. Otherwise appropriate error value (negative value).
- *EE\_INT8 EE\_easylab\_adc\_stop(void):*

  Description: Stop ADC sampling.

  - return value: 0 if no errors happened. Otherwise appropriate error value (negative value).

<a id="PWM_Channels"></a>

### **PWM Channels**

The EasyLab board has 4 independent and configurable pwm output (*PWM1*, *PWM2*, *PWM3* and *PWM4*).
These outputs can work also how two both pwm configuration (*PWM12*, *PWM1* together *PWM2* and *PWM34*, *PWM3* with *PWM4*).
In the OIL file need to use the flag **USEPWM**:

```
...
BOARD_DATA = EE_EASYLAB {
  USEPWM = TRUE;
  ...
}
...
```

The PWM's API are the follow:

- *EE\_INT16 EE\_easylab\_pwm\_init(EE\_UINT8 pwm\_pin, EE\_UINT32 pwm\_freq);*

  Description: Initialize an specific PWM channel. The parameter can be used are the follow:

  - **pwm\_pin**: Is the PWM channel, its values can be:
    - EE\_EASYLAB\_PWM1
    - EE\_EASYLAB\_PWM2
    - EE\_EASYLAB\_PWM3
    - EE\_EASYLAB\_PWM4
    - EE\_EASYLAB\_PWM12
    - EE\_EASYLAB\_PWM34
  - **pwm\_freq**: pwm frequency
  - return value: 0 if no errors happened. Otherwise appropriate error value (negative value).
- *EE\_INT16 EE\_easylab\_pwm\_close(EE\_UINT8 pwm\_pin);*

  Description: Close the specific PWM channel passed as parameter.

  - **pwm\_pin**: Is the PWM channel, its values can be:
    - EE\_EASYLAB\_PWM1
    - EE\_EASYLAB\_PWM2
    - EE\_EASYLAB\_PWM3
    - EE\_EASYLAB\_PWM4
    - EE\_EASYLAB\_PWM12
    - EE\_EASYLAB\_PWM34
  - return value: 0 if no errors happened. Otherwise appropriate error value (negative value).
- *EE\_INT16 EE\_easylab\_pwm\_set\_duty(EE\_UINT8 pwm\_pin, EE\_UINT16 duty);*

  Description: Set the duty-cycle at specific PWM channel passed as parameter.

  - **pwm\_pin**: Is the PWM channel, its values can be:
    - EE\_EASYLAB\_PWM1
    - EE\_EASYLAB\_PWM2
    - EE\_EASYLAB\_PWM3
    - EE\_EASYLAB\_PWM4
    - EE\_EASYLAB\_PWM12
    - EE\_EASYLAB\_PWM34
  - **duty**: duty-cycle
  - return value: 0 if no errors happened. Otherwise appropriate error value (negative value).

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Easylab_board_and_new_dsPIC_ERIKA_Enterprise_Driver_API) · [Archived source revision 4565](http://erika.tuxfamily.org/wiki/index.php?oldid=4565)
- Last source edit: 2012-01-31T16:53:07Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Eguidieri, Salva.
- [Original MediaWiki source](../source/wikitext/2183.mediawiki) · [Original editing history](../source/history/batch-003.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
